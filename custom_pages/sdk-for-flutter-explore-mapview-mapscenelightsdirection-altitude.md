---
title: "altitude property - MapSceneLightsDirection class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsdirection-altitude"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLightsDirection-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">altitude</span> property

</div>

<div class="section multi-line-signature">

double <span class="name">altitude</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Direction altitude value in degrees in the range \[0, 90\]. The default value is 0.0. The altitude value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90. Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly. For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90. When both azimuth and altitude values are provided, they are adjusted independently: For instance, (0, -10) is changed to (0, 0) rather than (180, 10).

</div>

## Implementation

``` dart
double altitude;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

