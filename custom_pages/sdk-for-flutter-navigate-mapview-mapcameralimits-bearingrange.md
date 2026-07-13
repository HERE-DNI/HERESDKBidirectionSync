---
title: "bearingRange property - MapCameraLimits class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameralimits-bearingrange"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraLimits-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">bearingRange</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a></span> <span class="name">bearingRange</span>

</div>

<div class="section desc markdown">

The bearing range within which the camera can be rotated. Gets the currently set bearing range.

This may not be active now if no rendering loop has been executed since the last call to set the range.

By default, range for a full circle is set during initialization.

</div>

## Implementation

``` dart
AngleRange get bearingRange;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">bearingRange=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-bearingRange-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The bearing range within which the camera can be rotated. Sets a new bearing range.

It will be updated during the next rendering loop. All previously set bearing ranges are cleared and the new bearing range is applied for all zoom values.

If the current camera bearing exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.

</div>

## Implementation

``` dart
set bearingRange(AngleRange value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

