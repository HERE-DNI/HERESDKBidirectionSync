---
title: "version property - CatalogIdentifier class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-catalogidentifier-version"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/CatalogIdentifier-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">version</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">version</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A version number for a catalog. When accessing a catalog, this version must be specified. Set `null` to automatically get the latest version for a catalog. The field defaults to `null`. Since the data inside a catalog can be updated, each published modification needs to correlate to a specific version number. Note: when `CatalogIdentifier` created with <a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-class">DesiredCatalog</a> then:

- numerical `-1` corresponds to <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-latestwithignoringcacheddata">CatalogVersionHint.latestWithIgnoringCachedData</a> with `ignoreCachedData` set to `true`;
- `null` corresponds to <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-latestwithignoringcacheddata">CatalogVersionHint.latestWithIgnoringCachedData</a> with `ignoreCachedData` set to `false`;
- other numerical values correspond to `version` passed to <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-specific">CatalogVersionHint.specific</a>.

</div>

## Implementation

``` dart
int? version;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

