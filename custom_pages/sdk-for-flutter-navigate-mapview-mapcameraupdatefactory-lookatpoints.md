---
title: "lookAtPoints method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPoints.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtPoints</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookAtPoints</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-lookAtPoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">points</span>, </span>
2.  <span id="sdk-for-flutter-navigate-lookAtPoints-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span>, </span>
3.  <span id="sdk-for-flutter-navigate-lookAtPoints-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span>
4.  <span id="sdk-for-flutter-navigate-lookAtPoints-param-measureLimit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">measureLimit</span>, </span>

)

</div>

<div class="section desc markdown">

Create an update to look at the given geo locations and fit them inside the given rectangle, in accordance with a map measure limit.

If the provided `MapCameraUpdateFactory.lookAtPoints.points` list is empty, no update will be applied to the camera.

If the `MapCameraUpdateFactory.lookAtPoints.viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `MapCameraUpdateFactory.lookAtPoints.viewRectangle`. Thus, no padding will be applied. A `MapCameraUpdateFactory.lookAtPoints.viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

All `MapCameraUpdateFactory.lookAtPoints.viewRectangle` values need to be finite to be considered as valid. If measure limit is not valid, no update will be applied to the map camera.

The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `points` Array of points in geodetic space that should be visible inside the given view rectangle.

- `viewRectangle` View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.

- `orientation` Geodetic orientation at the new calculated target point.

- `measureLimit` Map measure limit:

- as distance: the minimum distance from map camera to earth surface at the center of the view rectangle in meters. The map camera should not be positioned closer to the center of view rectangle than this.

- as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the center of view rectangle in meters. This is not the zoom level for the calculated lookAt target point. Can be used to not zoom closer than a given level.

- as scale: the minimum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the center of view rectangle in meters. This is not the scale for the calculated lookAt target point.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookAtPoints(List<GeoCoordinates> points, Rectangle2D viewRectangle, GeoOrientationUpdate orientation, MapMeasure measureLimit) => $prototype.lookAtPoints(points, viewRectangle, orientation, measureLimit);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
