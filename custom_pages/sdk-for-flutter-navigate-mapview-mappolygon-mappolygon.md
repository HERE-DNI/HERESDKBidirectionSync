---
title: "MapPolygon constructor - MapPolygon - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolygon-mappolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolygon.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolygon-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolygon</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolygon</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geometry</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>

)

</div>

<div class="section desc markdown">

Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.

The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

Note:

- The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.

- Polygons which are self-intersecting are not supported and may lead to render artifacts.

- The inner boundaries (holes) specified in the GeoPolygon are ignored.

- `geometry` The list of vertices representing the outer boundary of polygon.

- `color` The fill color for the polygon

</div>

## Implementation

``` dart
factory MapPolygon(GeoPolygon geometry, ui.Color color) => $prototype.$init(geometry, color);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
