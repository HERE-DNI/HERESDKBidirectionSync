---
title: "lookAtAreaWithViewRectangle method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatareawithviewrectangle"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtAreaWithViewRectangle</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookAtAreaWithViewRectangle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-lookAtAreaWithViewRectangle-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-navigate-lookAtAreaWithViewRectangle-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to look at the given geo-box and fit it inside the given rectangle, preserving current orientation and zooming at the center of view rectangle.

If geoBox is not valid, no update will be applied to the map camera.

If the `MapCameraUpdateFactory.lookAtAreaWithViewRectangle.viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `MapCameraUpdateFactory.lookAtAreaWithViewRectangle.viewRectangle`. Thus, no padding will be applied. A `MapCameraUpdateFactory.lookAtAreaWithViewRectangle.viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

In cases where it is not possible to find a solution for the given parameters, the resulting MapCameraUpdate will not change the map camera.

The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` Geodetic box that should be visible inside the given view rectangle.

- `viewRectangle` View rectangle in viewport pixel coordinates.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookAtAreaWithViewRectangle(GeoBox target, Rectangle2D viewRectangle) => $prototype.lookAtAreaWithViewRectangle(target, viewRectangle);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

