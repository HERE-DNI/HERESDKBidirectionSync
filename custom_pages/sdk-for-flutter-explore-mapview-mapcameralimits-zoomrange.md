---
title: "zoomRange property - MapCameraLimits class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-zoomrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomRange.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraLimits-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">zoomRange</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a></span> <span class="name">zoomRange</span>

</div>

<div class="section desc markdown">

The zoom range that can be applied to the camera. Gets the currently set camera zoom range.

By default, a <a href="sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxzoomlevel">MapCameraLimits.maxZoomLevel</a> zoom range is set during initialization.

</div>

## Implementation

``` dart
MapMeasureRange get zoomRange;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">zoomRange=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-zoomRange-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The zoom range that can be applied to the camera. Sets a new camera zoom range.

The supported values fall inside <a href="sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxzoomlevel">MapCameraLimits.maxZoomLevel</a> range. Values outside the supported zoom range are ignored.

If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.

This new limit range becomes active during the next rendering loop.

</div>

## Implementation

``` dart
set zoomRange(MapMeasureRange value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
