---
title: "geometry property - MapPolygon class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolygon-geometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- geometry.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolygon-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">geometry</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="name">geometry</span>

</div>

<div class="section desc markdown">

The geometry of the polygon. Setting a new geometry will update the appearance. Gets the current geometry of the polygon.

</div>

## Implementation

``` dart
GeoPolygon get geometry;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">geometry=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-geometry-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The geometry of the polygon. Setting a new geometry will update the appearance. Sets a new geometry to update the appearance.

The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

Note:

- The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
- Polygons which are self-intersecting are not supported and may lead to render artifacts.
- The inner boundaries (holes) specified in the GeoPolygon are ignored.

</div>

## Implementation

``` dart
set geometry(GeoPolygon value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
