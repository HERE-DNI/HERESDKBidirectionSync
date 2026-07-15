#!/usr/bin/env python3
"""Detect mismatched href targets versus page slugs in custom_pages markdown."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import signal
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

HREF_RE = re.compile(r'href="([^"]+)"')
SLUG_RE = re.compile(r'^slug:\s*"([^"]+)"', re.MULTILINE)


@dataclass
class HrefIssue:
    source_path: pathlib.Path
    line_number: int
    href: str
    matched_slug: Optional[str]
    slug_path: Optional[pathlib.Path]
    is_dot_hyphen_mismatch: bool = False


def find_slugs(page_paths: Iterable[pathlib.Path]) -> Dict[str, pathlib.Path]:
    slugs: Dict[str, pathlib.Path] = {}
    for page_path in page_paths:
        text = page_path.read_text(encoding='utf-8')
        match = SLUG_RE.search(text)
        if not match:
            continue
        slug = match.group(1)
        slugs[slug] = page_path
    return slugs


def iter_hrefs(page_path: pathlib.Path) -> Iterable[tuple[int, str]]:
    for lineno, line in enumerate(page_path.read_text(encoding='utf-8').splitlines(), start=1):
        for match in HREF_RE.finditer(line):
            href = match.group(1).strip()
            yield lineno, href


def normalize_slug_variant(value: str) -> str:
    return value.replace('.', '-')


def find_dot_hyphen_mismatch(href: str, slug_map: Dict[str, pathlib.Path]) -> Optional[str]:
    normalized = normalize_slug_variant(href)
    if normalized in slug_map and normalized != href:
        return normalized

    for slug in slug_map:
        if normalize_slug_variant(slug) == normalized and slug != href:
            return slug

    return None


def scan_custom_pages(root: pathlib.Path) -> List[HrefIssue]:
    page_paths = sorted(root.glob('*.md'))
    slug_map = find_slugs(page_paths)
    issues: List[HrefIssue] = []

    for page_path in page_paths:
        for lineno, href in iter_hrefs(page_path):
            if not href or href.startswith(('http://', 'https://', '#')):
                continue

            base_href = href.split('#', 1)[0]
            if base_href in slug_map:
                continue

            matched_slug = None
            is_dot_hyphen_mismatch = False
            normalized_match = find_dot_hyphen_mismatch(base_href, slug_map)
            if normalized_match:
                matched_slug = normalized_match
                is_dot_hyphen_mismatch = True

            issues.append(
                HrefIssue(
                    source_path=page_path,
                    line_number=lineno,
                    href=href,
                    matched_slug=matched_slug,
                    slug_path=slug_map[matched_slug] if matched_slug else None,
                    is_dot_hyphen_mismatch=is_dot_hyphen_mismatch,
                )
            )
    return issues


def print_issues(issues: List[HrefIssue]) -> None:
    if not issues:
        print('No broken page hrefs detected.')
        return

    dot_hyphen = [i for i in issues if i.is_dot_hyphen_mismatch]
    other = [i for i in issues if not i.is_dot_hyphen_mismatch]

    print(f'Detected {len(issues)} broken hrefs:')
    if dot_hyphen:
        print(f'  {len(dot_hyphen)} match only after dot/hyphen normalization:')
        for issue in dot_hyphen:
            print(
                f'    {issue.source_path}: line {issue.line_number}: href="{issue.href}"',
                f'matches slug="{issue.matched_slug}"',
            )
            print(f'      target file: {issue.slug_path}')

    if other:
        print(f'  {len(other)} broken hrefs with no matching slug:')
        for issue in other:
            print(f'    {issue.source_path}: line {issue.line_number}: href="{issue.href}"')


def write_report(issues: List[HrefIssue], path: pathlib.Path) -> None:
    payload = [
        {
            'source_path': str(issue.source_path),
            'line_number': issue.line_number,
            'href': issue.href,
            'matched_slug': issue.matched_slug,
            'slug_path': str(issue.slug_path) if issue.slug_path else None,
            'is_dot_hyphen_mismatch': issue.is_dot_hyphen_mismatch,
        }
        for issue in issues
    ]
    path.write_text(json.dumps({'broken_links': payload}, indent=2), encoding='utf-8')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Find href values in custom_pages that mismatch slugs because of dot vs hyphen conversions.'
    )
    parser.add_argument(
        '--folder',
        '-f',
        default='custom_pages',
        help='Folder containing markdown pages to scan (default: custom_pages)',
    )
    return parser.parse_args()


def main() -> int:
    if hasattr(signal, 'SIGPIPE'):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    args = parse_args()
    root = pathlib.Path(args.folder)
    if not root.exists() or not root.is_dir():
        print(f'Error: folder not found: {root}', file=sys.stderr)
        return 2

    issues = scan_custom_pages(root)
    report_path = pathlib.Path('broken-links-report.json')
    write_report(issues, report_path)
    try:
        print_issues(issues)
        print(f'Wrote report to {report_path}')
    except BrokenPipeError:
        return 0
    return 1 if issues else 0


if __name__ == '__main__':
    raise SystemExit(main())
