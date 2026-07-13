---
title: "zoomBy method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-zoomby"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">zoomBy</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">zoomBy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-zoomBy-param-factor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">factor</span>, </span>
2.  <span id="sdk-for-flutter-navigate-zoomBy-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>

)

</div>

<div class="section desc markdown">

Zooms in or out by a specified factor.

This effectively changes the distance from the camera to the <a href="sdk-for-flutter-navigate-mapview-mapcamerastate-targetcoordinates">MapCameraState.targetCoordinates</a> by the specified factor, which changes <a href="sdk-for-flutter-navigate-mapview-mapcamerastate-zoomlevel">MapCameraState.zoomLevel</a> as well.

Values above 1.0 will zoom in and values below will zoom out.

The relation with <a href="sdk-for-flutter-navigate-mapview-mapcamerastate-distancetotargetinmeters">MapCameraState.distanceToTargetInMeters</a> is inversely linear, meaning that zooming by 4 will decrease distance to target by 4 while zooming by 0.5 will increase distance to target by 2.

The relation with zoom level is logarithmic. Meaning that zooming by a factor of 4 will increase zoom level by 2 (because log2(4) == 2). So to zoom in by X zoom levels, the zoom factor needs to be 2^X. To zoom out by X zoom levels, zoom factor needs to be 1/(2^X).

The zooming occurs around the specified origin inside the view.

- `factor` The zoom factor. Values above 1.0 will zoom in and values below will zoom out.

- `origin` Pixel point in view coordinates around which zooming occurs.

</div>

## Implementation

``` dart
void zoomBy(double factor, Point2D origin);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

