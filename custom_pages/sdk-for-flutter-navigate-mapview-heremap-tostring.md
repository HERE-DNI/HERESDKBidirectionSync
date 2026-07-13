---
title: "toString method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremap-tostring"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toString.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">toString</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @override

</div>

<span class="returntype">String</span> <span class="name">toString</span>(<wbr></wbr>{

1.  <span id="sdk-for-flutter-navigate-toString-param-minLevel" class="parameter"><span class="type-annotation">DiagnosticLevel</span> <span class="parameter-name">minLevel</span> = <span class="default-value">DiagnosticLevel.info</span>, </span>

})

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

A string representation of this object.

Some classes have a default textual representation, often paired with a static `parse` function (like `int.parse`). These classes will provide the textual representation as their string representation.

Other classes have no meaningful textual representation that a program will care about. Such classes will typically override `toString` to provide useful information when inspecting the object, mainly for debugging or logging.

</div>

## Implementation

``` dart
@override
String toString({DiagnosticLevel minLevel = DiagnosticLevel.info}) {
  String? fullString;
  assert(() {
    fullString = toDiagnosticsNode(
      style: DiagnosticsTreeStyle.singleLine,
    ).toString(minLevel: minLevel);
    return true;
  }());
  return fullString ?? toStringShort();
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
