---
title: "hdEnabled property - SatellitePositioningOptions class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-satellitepositioningoptions-hdenabled"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/SatellitePositioningOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">hdEnabled</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">hdEnabled</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Controls HD GNSS positioning. If false, HD GNSS positioning is disabled. VDR (Vehicle Dead Reckoning) is used if HD GNSS is enabled and sensors are used for positioning. This feature requires Android 12 or later and dual frequency GNSS receiver and raw GNSS measurements. This feature is disabled by default: <a href="https://www.here.com/platform/positioning">Contact us</a> to enable it. If it is not enabled or the OS/device requirements are not met, fallback to other positioning technologies may occur and desired accuracy level may not be reached. Defaults to `false`.

</div>

## Implementation

``` dart
bool hdEnabled;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

