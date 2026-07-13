---
title: "MapPolyline.withRepresentation constructor - MapPolyline - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-mappolyline-withrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolyline.withRepresentation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolyline.withRepresentation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolyline.withRepresentation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withRepresentation-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span> <span class="parameter-name">geometry</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withRepresentation-param-representation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a></span> <span class="parameter-name">representation</span></span>

)

</div>

<div class="section desc markdown">

Creates a new `MapPolyline` instance with a specified visual representation.

Altitude component of `GeoPolyline`'s vertices is ignored.

After creating a `MapPolyline` with this representation, the deprecated `MapPolyline` properties do not work and any change to them will be ignored. Any modifications to polyline's appearance must be done with <a href="sdk-for-flutter-navigate-mapview-mappolyline-setrepresentation">MapPolyline.setRepresentation</a>.

- `geometry` The list of vertices representing the polyline.

- `representation` The styling properties of the polyline.

</div>

## Implementation

``` dart
factory MapPolyline.withRepresentation(GeoPolyline geometry, MapPolylineRepresentation representation) => $prototype.withRepresentation(geometry, representation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
