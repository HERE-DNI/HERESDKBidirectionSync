---
title: "setGeometry method - PolygonDataAccessor class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-polygondataaccessor-setgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setGeometry.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/PolygonDataAccessor-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setGeometry</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setGeometry</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setGeometry-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geometry</span></span>

)

</div>

<div class="section desc markdown">

Replaces polygon geometry.

The outer boundary has to be ordered clockwise and closed.

Altitude of the vertices is ignored.

The visual behaviour for self-intersecting outer boundary is undefined.

- `geometry` Geometry of the polygon. The outer boundary has to be ordered clockwise and closed. Altitude of the vertices is ignored. The visual behaviour for self-intersecting outer boundary is undefined.

</div>

## Implementation

``` dart
void setGeometry(GeoPolygon geometry);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
