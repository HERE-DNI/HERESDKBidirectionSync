---
title: "lookAtAreaWithGeoOrientationAndViewRectangle method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-lookatareawithgeoorientationandviewrectangle"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtAreaWithGeoOrientationAndViewRectangle</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">lookAtAreaWithGeoOrientationAndViewRectangle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-lookAtAreaWithGeoOrientationAndViewRectangle-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-navigate-lookAtAreaWithGeoOrientationAndViewRectangle-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span>
3.  <span id="sdk-for-flutter-navigate-lookAtAreaWithGeoOrientationAndViewRectangle-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span></span>

)

</div>

<div class="section desc markdown">

Makes the camera look at the specified geodetic area and pass a rectangle which specifies where the area should appear inside of the map view.

The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method. Please note that the resulting orientation might deviate from the provided orientation. This is particularly the case if a large geobox on world level and a view rectangle which is relatively small was passed to the method.

The altitude of the target points is ignored.

- `target` Geodetic area which will be shown in the viewRectangle.

- `orientation` Desired orientation of the camera.

- `viewRectangle` The view rectangle in viewport pixel coordinates inside which the geographical target area is displayed.

</div>

## Implementation

``` dart
void lookAtAreaWithGeoOrientationAndViewRectangle(GeoBox target, GeoOrientationUpdate orientation, Rectangle2D viewRectangle);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

