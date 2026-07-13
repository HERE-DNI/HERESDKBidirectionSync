---
title: "tiltRange property - MapCameraLimits class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- tiltRange.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraLimits-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">tiltRange</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span> <span class="name">tiltRange</span>

</div>

<div class="section desc markdown">

The tilt range that can be applied to the camera. Gets the current tilt range.

By default, a <a href="sdk-for-flutter-explore-mapview-mapcameralimits-mintilt">MapCameraLimits.minTilt</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt">MapCameraLimits.maxTilt</a> tilt range is set during initialization.

This range might not be yet active if no rendering loop has been executed since the last call to set the range.

</div>

## Implementation

``` dart
AngleRange get tiltRange;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">tiltRange=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-tiltRange-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The tilt range that can be applied to the camera. Sets a new tilt limit range.

The supported values fall inside <a href="sdk-for-flutter-explore-mapview-mapcameralimits-mintilt">MapCameraLimits.minTilt</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt">MapCameraLimits.maxTilt</a> range. Values outside the supported range are ignored.

If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum, depending on which is closest.

This new limit range becomes active during the next rendering loop.

All previously set tilt ranges are cleared and the new tilt range is applied for all zoom values.

</div>

## Implementation

``` dart
set tiltRange(AngleRange value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
