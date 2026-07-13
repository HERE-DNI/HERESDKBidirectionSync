---
title: "toStringShort method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremap-tostringshort"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">toStringShort</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @override

</div>

<span class="returntype">String</span> <span class="name">toStringShort</span>(<wbr></wbr>)

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

A short, textual description of this widget.

</div>

## Implementation

``` dart
@override
String toStringShort() {
  final String type = objectRuntimeType(this, 'Widget');
  return key == null ? type : '$type-$key';
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

