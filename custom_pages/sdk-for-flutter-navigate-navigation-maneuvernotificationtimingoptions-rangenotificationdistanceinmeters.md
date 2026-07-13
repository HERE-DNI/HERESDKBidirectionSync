---
title: "rangeNotificationDistanceInMeters property - ManeuverNotificationTimingOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationTimingOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">rangeNotificationDistanceInMeters</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">rangeNotificationDistanceInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 0 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 0 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 0 |

</div>

## Implementation

``` dart
int rangeNotificationDistanceInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

