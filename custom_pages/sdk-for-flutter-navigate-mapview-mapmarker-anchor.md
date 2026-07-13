---
title: "anchor property - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-anchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- anchor.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">anchor</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="name">anchor</span>

</div>

<div class="section desc markdown">

The anchor point for the marker image which specifies the position offset relative to the marker's coordinates. Gets current anchor point for the marker image.

</div>

## Implementation

``` dart
Anchor2D get anchor;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">anchor=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-anchor-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The anchor point for the marker image which specifies the position offset relative to the marker's coordinates. Sets anchor point of the marker image which specifies the position offset relative to the marker's coordinates.

For example, (0, 0) places the top-left corner of the image at the marker's coordinates. (1, 1) would place the bottom-right corner of the image at the marker's coordinates. (0.5, 0.5) which is the default value would center the image at the marker's coordinates. Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the marker's coordinates at the distance in pixels that is equal to the height of the image.

</div>

## Implementation

``` dart
set anchor(Anchor2D value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
