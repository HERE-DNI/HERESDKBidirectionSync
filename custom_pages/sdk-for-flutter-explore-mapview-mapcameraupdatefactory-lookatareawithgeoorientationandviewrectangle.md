---
title: "lookAtAreaWithGeoOrientationAndViewRectangle method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatareawithgeoorientationandviewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtAreaWithGeoOrientationAndViewRectangle.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtAreaWithGeoOrientationAndViewRectangle</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookAtAreaWithGeoOrientationAndViewRectangle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientationAndViewRectangle-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientationAndViewRectangle-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span>
3.  <span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientationAndViewRectangle-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span></span>

)

</div>

<div class="section desc markdown">

Create an update to look at the given geo-box and fit it inside the given rectangle.

If geoBox is not valid, no update will be applied to the map camera.

If the `MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle`. Thus, no padding will be applied. A `MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

All `MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle` values need to be finite to be considered as valid.

In cases where it is not possible to find a solution for the given parameters, the resulting MapCameraUpdate will not change the map camera.

The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` Geodetic box that should be visible inside the given view rectangle.

- `orientation` Geodetic orientation at the target point.

- `viewRectangle` View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookAtAreaWithGeoOrientationAndViewRectangle(GeoBox target, GeoOrientationUpdate orientation, Rectangle2D viewRectangle) => $prototype.lookAtAreaWithGeoOrientationAndViewRectangle(target, orientation, viewRectangle);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
