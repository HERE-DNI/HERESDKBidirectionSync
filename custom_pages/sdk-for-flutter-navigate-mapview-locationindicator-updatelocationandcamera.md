---
title: "updateLocationAndCamera method - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-updatelocationandcamera"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateLocationAndCamera.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">updateLocationAndCamera</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">updateLocationAndCamera</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-updateLocationAndCamera-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span>, </span>
2.  <span id="sdk-for-flutter-navigate-updateLocationAndCamera-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span></span>

)

</div>

<div class="section desc markdown">

Updates the indicator to a new location and applies a camera update at the same time.

Does nothing if the indicator instance is not enabled. If accuracy visualized is set to `true` the field <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> determines the size of the accuracy indicator halo.

The altitude of the location is ignored.

- `location` The updated location of the user.

- `cameraUpdate` The update to apply to the camera.

</div>

## Implementation

``` dart
void updateLocationAndCamera(Location location, MapCameraUpdate cameraUpdate);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
