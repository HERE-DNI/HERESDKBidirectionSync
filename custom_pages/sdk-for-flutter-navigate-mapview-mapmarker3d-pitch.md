---
title: "pitch property - MapMarker3D class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-pitch"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">pitch</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double</span> <span class="name">pitch</span>

</div>

<div class="section desc markdown">

The pitch of the 3D model in degrees. The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis. Gets the pitch of the 3D model in degrees.

</div>

## Implementation

``` dart
double get pitch;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">pitch=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-pitch-param-value" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The pitch of the 3D model in degrees. The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis. Sets the pitch of the 3D model in degrees.

</div>

## Implementation

``` dart
set pitch(double value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

