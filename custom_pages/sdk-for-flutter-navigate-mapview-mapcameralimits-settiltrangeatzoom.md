---
title: "setTiltRangeAtZoom method - MapCameraLimits class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameralimits-settiltrangeatzoom"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraLimits-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setTiltRangeAtZoom</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setTiltRangeAtZoom</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setTiltRangeAtZoom-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setTiltRangeAtZoom-param-tiltRange" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a></span> <span class="parameter-name">tiltRange</span></span>

)

</div>

<div class="section desc markdown">

Sets tilt ranges that can be set on the camera at given zoom.

The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no tilt range is specified for <a href="sdk-for-flutter-navigate-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>, the tilt range set through <a href="sdk-for-flutter-navigate-mapview-mapcameralimits-tiltrange">MapCameraLimits.tiltRange</a> is used for interpolation.

Zoom or tilt values outside the supported zoom and tilt range are ignored. By default, the maximum tilt range for all zoom values is set during initialization.

- `zoom` Zoom at which the range is set.

- `tiltRange` Tilt range.

</div>

## Implementation

``` dart
void setTiltRangeAtZoom(MapMeasure zoom, AngleRange tiltRange);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

