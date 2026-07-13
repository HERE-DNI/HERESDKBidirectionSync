---
title: "setBearingRangeAtZoom method - MapCameraLimits class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameralimits-setbearingrangeatzoom"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBearingRangeAtZoom.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraLimits-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setBearingRangeAtZoom</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setBearingRangeAtZoom</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setBearingRangeAtZoom-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setBearingRangeAtZoom-param-bearingRange" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a></span> <span class="parameter-name">bearingRange</span></span>

)

</div>

<div class="section desc markdown">

Sets the bearing range within which the camera can rotate at a given zoom.

The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no bearing range is specified for <a href="sdk-for-flutter-navigate-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>, the bearing range set through <a href="sdk-for-flutter-navigate-mapview-mapcameralimits-bearingrange">MapCameraLimits.bearingRange</a> is used for interpolation.

Zoom values outside the supported zoom range are ignored. By default, the maximum bearing range for all zoom values is set during initialization.

- `zoom` Zoom at which the range is set.

- `bearingRange` Bearing range.

</div>

## Implementation

``` dart
void setBearingRangeAtZoom(MapMeasure zoom, AngleRange bearingRange);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
