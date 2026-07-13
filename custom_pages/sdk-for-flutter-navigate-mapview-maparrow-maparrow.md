---
title: "MapArrow constructor - MapArrow - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maparrow-maparrow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapArrow.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapArrow-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapArrow</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapArrow</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span> <span class="parameter-name">geometry</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-widthInPixels" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">widthInPixels</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>

)

</div>

<div class="section desc markdown">

Creates a new `MapArrow` instance.

Altitude component of `GeoPolyline`'s vertices is ignored.

- `geometry` The geometry of the arrow tail. The last coordinate in the list defines the position where the head of the arrow is located.

- `widthInPixels` The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.

- `color` The color of the arrow. The alpha channel is ignored, the color is interpreted as fully opaque.

</div>

## Implementation

``` dart
factory MapArrow(GeoPolyline geometry, double widthInPixels, ui.Color color) => $prototype.$init(geometry, widthInPixels, color);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
