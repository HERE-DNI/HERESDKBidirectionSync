---
title: "coordinatesAtOffsetInMeters method - GeoPolyline class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geopolyline-coordinatesatoffsetinmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">coordinatesAtOffsetInMeters</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="name">coordinatesAtOffsetInMeters</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-coordinatesAtOffsetInMeters-param-offsetInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetInMeters</span>, </span>
2.  <span id="sdk-for-flutter-navigate-coordinatesAtOffsetInMeters-param-direction" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolylinedirection">GeoPolylineDirection</a></span> <span class="parameter-name">direction</span></span>

)

</div>

<div class="section desc markdown">

Returns the coordinates at the given distance along the polyline.

When the polyline is traversed from the beginning, the distance is calculated from the start of the polyline; while a direction from the end indicates a distance from the last vertex.

The offset is expected to be non-negative and smaller than the length of the polyline. When the offset is negative, the function returns the starting end point of the polyline, i.e. the first vertex in positive direction and the last vertex in the negative direction. Similarly, when the offset is larger than the length of the polyline, then the function returns the opposite end point of the polyline.

The distance between two consecutive vertices is calculated using the <a href="sdk-for-flutter-navigate-core-geocoordinates-distanceto">GeoCoordinates.distanceTo</a> function. Therefore, it computes the distance (in meters) along the great circle between the two vertices. Similarly, the full length of the polyline is the sum of the distances between its vertices. The interpolation coordinates between two vertices is calculated using the <a href="sdk-for-flutter-navigate-core-geocoordinates-interpolate">GeoCoordinates.interpolate</a> function.

Note: the result may different from the analogue result from other matching components since they may adapt the result to the length of the underlying object described by the polyline.

- `offsetInMeters` The distance along the polyline in meters

- `direction` The direction in which the polyline is traversed.

Returns <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>. The coordinates of the point at the given distance

</div>

## Implementation

``` dart
GeoCoordinates coordinatesAtOffsetInMeters(double offsetInMeters, GeoPolylineDirection direction) => $prototype.coordinatesAtOffsetInMeters(this, offsetInMeters, direction);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

