---
title: "lookToMatchGeoPointToViewPoint method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpoint"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookToMatchGeoPointToViewPoint</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookToMatchGeoPointToViewPoint</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookToMatchGeoPointToViewPoint-param-geoPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">geoPoint</span>, </span>
2.  <span id="sdk-for-flutter-explore-lookToMatchGeoPointToViewPoint-param-viewPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewPoint</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to position the map camera to look at the map with the given geo point located at the given view point.

Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `geoPoint` The geo point that will be matched to the given view point. Note: the geo point will differ from the look at target of the camera. After this update the camera will still look at the principal point and therefore the look at target will be different from the geo point, since the geo point will correspond to the given view point and the look at target will correspond to the principal point. Look at target and the geo point will be identical only if the given view point is identical to the principal point.

- `viewPoint` View point coordinates in pixels.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookToMatchGeoPointToViewPoint(GeoCoordinates geoPoint, Point2D viewPoint) => $prototype.lookToMatchGeoPointToViewPoint(geoPoint, viewPoint);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

