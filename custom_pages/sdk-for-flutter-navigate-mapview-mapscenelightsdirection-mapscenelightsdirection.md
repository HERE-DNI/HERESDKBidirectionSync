---
title: "MapSceneLightsDirection constructor - MapSceneLightsDirection - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscenelightsdirection-mapscenelightsdirection"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLightsDirection-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapSceneLightsDirection</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapSceneLightsDirection</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-azimuth" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">azimuth</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-altitude" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">altitude</span></span>

)

</div>

<div class="section desc markdown">

Constructs a Direction from the values.

- `azimuth` Direction azimuth value in degrees in the range \[0, 360). The default value is 0.0. The azimuth range is half-open, meaning the maximum value is not included in the range. If the azimuth value falls outside the range, it is wrapped to stay within \[0, 360). Specifically, values less than 0 will be increased by 360 until they fall within the range, and values greater than or equal to 360 will be reduced by 360 until they fall within the range. By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise. Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.
- `altitude` Direction altitude value in degrees in the range \[0, 90\]. The default value is 0.0. The altitude value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90. Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly. For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90. When both azimuth and altitude values are provided, they are adjusted independently: For instance, (0, -10) is changed to (0, 0) rather than (180, 10).

</div>

## Implementation

``` dart
MapSceneLightsDirection(this.azimuth, this.altitude);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

