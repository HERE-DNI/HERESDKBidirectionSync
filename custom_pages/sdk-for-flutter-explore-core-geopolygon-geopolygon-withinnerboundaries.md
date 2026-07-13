---
title: "GeoPolygon.withInnerBoundaries constructor - GeoPolygon - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geopolygon-geopolygon-withinnerboundaries"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoPolygon-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">GeoPolygon.withInnerBoundaries</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">GeoPolygon.withInnerBoundaries</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withInnerBoundaries-param-vertices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">vertices</span>, </span>
2.  <span id="sdk-for-flutter-explore-withInnerBoundaries-param-innerBoundaries" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span>\></span></span> <span class="parameter-name">innerBoundaries</span></span>

)

</div>

<div class="section desc markdown">

Constructs an instance of this class from the provided vertices and inner boundaries (holes).

Throws InstantiationError if the number of vertices is less than three.

- `vertices` List of vertices representing the polygon outer boundary in clockwise order.

- `innerBoundaries` List of polygon inner boundaries (holes), each in counterclockwise order.

Throws <a href="sdk-for-flutter-explore-core-errors-instantiationexception-class">InstantiationException</a>. Instantiation error.

</div>

## Implementation

``` dart
factory GeoPolygon.withInnerBoundaries(List<GeoCoordinates> vertices, List<List<GeoCoordinates>> innerBoundaries) => $prototype.withInnerBoundaries(vertices, innerBoundaries);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

