---
title: "lookAtTargetAndPoints method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookattargetandpoints"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtTargetAndPoints</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookAtTargetAndPoints</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span>
3.  <span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">points</span>, </span>
4.  <span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span>, </span>
5.  <span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-minMeasure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">minMeasure</span>, </span>
6.  <span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-maxMeasure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">maxMeasure</span>, </span>

)

</div>

<div class="section desc markdown">

Creates an update to position the camera to look at the given target with the given orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.

Such position update can possibly not be found.

Any target or orientation sub-element value that is not finite will be excluded from the update.

If the provided `MapCameraUpdateFactory.lookAtTargetAndPoints.points` list is empty, no update will be applied to the map camera.

If the `MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle`. Thus, no padding will be applied. A `MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

If map measures are not valid, no update will be applied to the map camera.

The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` The look-at target position in geodetic coordinates.

- `orientation` Geodetic orientation at look-at target.

- `points` Array of points in geodetic space that should be visible inside the given view rectangle.

- `viewRectangle` View rectangle in viewport pixel coordinates inside which the geographical points are displayed.

- `minMeasure` Minimum map measure:

- as distance: the minimum distance from map camera to earth surface at the look-at target in meters. The map camera should not be positioned closer to target than this.

- as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters. Can be used to not zoom closer than a given level.

- as scale: the minimum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters.

- `maxMeasure` Maximum map measure:

- as distance: the maximum distance from map camera to earth surface at the look-at target in meters. The map camera should not be positioned further from target than this.

- as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters. Can be used to not zoom further than a given level.

- as scale: the maximum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookAtTargetAndPoints(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, List<GeoCoordinates> points, Rectangle2D viewRectangle, MapMeasure minMeasure, MapMeasure maxMeasure) => $prototype.lookAtTargetAndPoints(target, orientation, points, viewRectangle, minMeasure, maxMeasure);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

