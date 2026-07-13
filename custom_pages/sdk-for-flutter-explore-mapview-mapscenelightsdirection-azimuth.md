---
title: "azimuth property - MapSceneLightsDirection class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsdirection-azimuth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- azimuth.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLightsDirection-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">azimuth</span> property

</div>

<div class="section multi-line-signature">

double <span class="name">azimuth</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Direction azimuth value in degrees in the range \[0, 360). The default value is 0.0. The azimuth range is half-open, meaning the maximum value is not included in the range. If the azimuth value falls outside the range, it is wrapped to stay within \[0, 360). Specifically, values less than 0 will be increased by 360 until they fall within the range, and values greater than or equal to 360 will be reduced by 360 until they fall within the range. By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise. Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.

</div>

## Implementation

``` dart
double azimuth;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
