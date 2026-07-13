---
title: "MapCameraState constructor - MapCameraState - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamerastate-mapcamerastate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraState.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraState-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapCameraState</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapCameraState</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-targetCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">targetCoordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-orientationAtTarget" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientation-class">GeoOrientation</a></span> <span class="parameter-name">orientationAtTarget</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-distanceToTargetInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToTargetInMeters</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-zoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">zoomLevel</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `targetCoordinates` Camera's 'LookAt' target position in geodetic space.

Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `orientationAtTarget` Camera's orientation at target point.
- `distanceToTargetInMeters` Distance from the camera to the target point in meters.
- `zoomLevel` Zoom level corresponding to the current distance to target.

</div>

## Implementation

``` dart
MapCameraState(this.targetCoordinates, this.orientationAtTarget, this.distanceToTargetInMeters, this.zoomLevel);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
