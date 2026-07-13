---
title: "debugDescribeChildren method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremap-debugdescribechildren"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- debugDescribeChildren.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">debugDescribeChildren</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @<a href="https://pub.dev/documentation/meta/1.17.0/meta/protected-constant.html">protected</a>

</div>

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter">DiagnosticsNode</span>\></span></span> <span class="name">debugDescribeChildren</span>(<wbr></wbr>)

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

Returns a list of `DiagnosticsNode` objects describing this node's children.

Children that are offstage should be added with `style` set to `DiagnosticsTreeStyle.offstage` to indicate that they are offstage.

The list must not contain any null entries. If there are explicit null children to report, consider `DiagnosticsNode.message` or `DiagnosticsProperty<Object>` as possible `DiagnosticsNode` objects to provide.

Used by `toStringDeep`, `toDiagnosticsNode` and `toStringShallow`.

See also:

- `RenderTable.debugDescribeChildren`, which provides high quality custom descriptions for its child nodes.

</div>

## Implementation

``` dart
@protected
List<DiagnosticsNode> debugDescribeChildren() => const <DiagnosticsNode>[];
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
