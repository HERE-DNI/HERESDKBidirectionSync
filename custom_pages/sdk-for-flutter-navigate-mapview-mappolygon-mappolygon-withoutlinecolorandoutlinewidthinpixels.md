---
title: "MapPolygon.withOutlineColorAndOutlineWidthInPixels constructor - MapPolygon - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolygon-mappolygon-withoutlinecolorandoutlinewidthinpixels"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolygon-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolygon.withOutlineColorAndOutlineWidthInPixels</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolygon.withOutlineColorAndOutlineWidthInPixels</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geometry</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-outlineColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">outlineColor</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-outlineWidthInPixels" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">outlineWidthInPixels</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.

Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque by interpreting the alpha value as 1.

The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

Note:

- The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.

- Polygons which are self-intersecting are not supported and may lead to render artifacts.

- The inner boundaries (holes) specified in the GeoPolygon are ignored.

- `geometry` The list of vertices representing the outer boundary of polygon.

- `color` The fill color for the polygon.

- `outlineColor` The color of the polygon outline, alpha channel is ignored and treated as 1.

- `outlineWidthInPixels` The width of the polygon outline (in pixels). Negative values are clamped to 0.

</div>

## Implementation

``` dart
factory MapPolygon.withOutlineColorAndOutlineWidthInPixels(GeoPolygon geometry, ui.Color color, ui.Color outlineColor, double outlineWidthInPixels) => $prototype.withOutlineColorAndOutlineWidthInPixels(geometry, color, outlineColor, outlineWidthInPixels);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

