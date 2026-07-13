---
title: "toStringShallow method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremap-tostringshallow"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">toStringShallow</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">String</span> <span class="name">toStringShallow</span>(<wbr></wbr>{

1.  <span id="sdk-for-flutter-navigate-toStringShallow-param-joiner" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">joiner</span> = <span class="default-value">', '</span>, </span>
2.  <span id="sdk-for-flutter-navigate-toStringShallow-param-minLevel" class="parameter"><span class="type-annotation">DiagnosticLevel</span> <span class="parameter-name">minLevel</span> = <span class="default-value">DiagnosticLevel.debug</span>, </span>

})

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

Returns a one-line detailed description of the object.

This description is often somewhat long. This includes the same information given by `toStringDeep`, but does not recurse to any children.

`joiner` specifies the string which is place between each part obtained from `debugFillProperties`. Passing a string such as `'\n '` will result in a multiline string that indents the properties of the object below its name (as per `toString`).

`minLevel` specifies the minimum `DiagnosticLevel` for properties included in the output.

See also:

- `toString`, for a brief description of the object.
- `toStringDeep`, for a description of the subtree rooted at this object.

</div>

## Implementation

``` dart
String toStringShallow({String joiner = ', ', DiagnosticLevel minLevel = DiagnosticLevel.debug}) {
  String? shallowString;
  assert(() {
    final StringBuffer result = StringBuffer();
    result.write(toString());
    result.write(joiner);
    final DiagnosticPropertiesBuilder builder = DiagnosticPropertiesBuilder();
    debugFillProperties(builder);
    result.write(
      builder.properties.where((DiagnosticsNode n) => !n.isFiltered(minLevel)).join(joiner),
    );
    shallowString = result.toString();
    return true;
  }());
  return shallowString ?? toString();
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

