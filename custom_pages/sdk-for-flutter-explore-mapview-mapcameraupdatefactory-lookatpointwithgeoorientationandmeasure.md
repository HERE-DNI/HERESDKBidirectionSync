---
title: "lookAtPointWithGeoOrientationAndMeasure method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithgeoorientationandmeasure"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPointWithGeoOrientationAndMeasure.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtPointWithGeoOrientationAndMeasure</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookAtPointWithGeoOrientationAndMeasure</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span>
3.  <span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-measure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">measure</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to position the map camera to look at the given target with the given orientation and map measure.

Any target or orientation sub-element value that is not finite will be excluded from the update. If the map measure is not valid, the current map camera distance to the target point is preserved.

The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` The look-at target position in geodetic coordinates.

- `orientation` Geodetic orientation at look-at target.

- `measure` The desired map measure.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookAtPointWithGeoOrientationAndMeasure(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, MapMeasure measure) => $prototype.lookAtPointWithGeoOrientationAndMeasure(target, orientation, measure);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
