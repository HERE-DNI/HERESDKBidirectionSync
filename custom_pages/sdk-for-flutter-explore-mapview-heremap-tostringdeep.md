---
title: "toStringDeep method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremap-tostringdeep"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toStringDeep.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">toStringDeep</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">String</span> <span class="name">toStringDeep</span>(<wbr></wbr>{

1.  <span id="sdk-for-flutter-explore-toStringDeep-param-prefixLineOne" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">prefixLineOne</span> = <span class="default-value">''</span>, </span>
2.  <span id="sdk-for-flutter-explore-toStringDeep-param-prefixOtherLines" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">prefixOtherLines</span>, </span>
3.  <span id="sdk-for-flutter-explore-toStringDeep-param-minLevel" class="parameter"><span class="type-annotation">DiagnosticLevel</span> <span class="parameter-name">minLevel</span> = <span class="default-value">DiagnosticLevel.debug</span>, </span>
4.  <span id="sdk-for-flutter-explore-toStringDeep-param-wrapWidth" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">wrapWidth</span> = <span class="default-value">65</span>, </span>

})

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

Returns a string representation of this node and its descendants.

`prefixLineOne` will be added to the front of the first line of the output. `prefixOtherLines` will be added to the front of each other line. If `prefixOtherLines` is null, the `prefixLineOne` is used for every line. By default, there is no prefix.

`minLevel` specifies the minimum `DiagnosticLevel` for properties included in the output.

`wrapWidth` specifies the column number where word wrapping will be applied.

The `toStringDeep` method takes other arguments, but those are intended for internal use when recursing to the descendants, and so can be ignored.

See also:

- `toString`, for a brief description of the object but not its children.
- `toStringShallow`, for a detailed description of the object but not its children.

</div>

## Implementation

``` dart
String toStringDeep({
  String prefixLineOne = '',
  String? prefixOtherLines,
  DiagnosticLevel minLevel = DiagnosticLevel.debug,
  int wrapWidth = 65,
}) {
  return toDiagnosticsNode().toStringDeep(
    prefixLineOne: prefixLineOne,
    prefixOtherLines: prefixOtherLines,
    minLevel: minLevel,
    wrapWidth: wrapWidth,
  );
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
