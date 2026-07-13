---
title: "withGeometry method - PolygonDataBuilder class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-polygondatabuilder-withgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withGeometry.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/PolygonDataBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">withGeometry</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-class">PolygonDataBuilder</a></span> <span class="name">withGeometry</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withGeometry-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geometry</span></span>

)

</div>

<div class="section desc markdown">

Configures the builder with geometry for the polygon to be created.

- `geometry` Geometry of the polygon. The outer boundary has to be ordered clockwise and closed. Any inner boundary has to be ordered counterclockwise and closed. Altitude of boundary vertices is ignored. The visual behaviour for self-intersecting outer boundary is undefined.

Returns <a href="sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-class">PolygonDataBuilder</a>. The builder.

</div>

## Implementation

``` dart
PolygonDataBuilder withGeometry(GeoPolygon geometry);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
