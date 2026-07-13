---
title: "lookAtPointWithGeoOrientationAndMeasure method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithgeoorientationandmeasure"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPointWithGeoOrientationAndMeasure.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtPointWithGeoOrientationAndMeasure</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">lookAtPointWithGeoOrientationAndMeasure</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span>
3.  <span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span></span>

)

</div>

<div class="section desc markdown">

Makes the camera look at the geodetic target with the given zoom and orientation.

The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method.

The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` Geodetic coordinates at which the camera will point.

- `orientation` Desired orientation of the camera.

- `zoom` The zoom level which can be provided as distance to the target point, scale or zoom level.

</div>

## Implementation

``` dart
void lookAtPointWithGeoOrientationAndMeasure(GeoCoordinates target, GeoOrientationUpdate orientation, MapMeasure zoom);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
