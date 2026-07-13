---
title: "doubleNotificationDistanceInMeters property - ManeuverNotificationTimingOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-doublenotificationdistanceinmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationTimingOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">doubleNotificationDistanceInMeters</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">doubleNotificationDistanceInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The default distance setting for double notification.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 20 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 20 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 20 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 750 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 250 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 150 |

</div>

## Implementation

``` dart
int doubleNotificationDistanceInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

