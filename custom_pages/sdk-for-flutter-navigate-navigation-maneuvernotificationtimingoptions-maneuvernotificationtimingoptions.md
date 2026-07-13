---
title: "ManeuverNotificationTimingOptions constructor - ManeuverNotificationTimingOptions - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-maneuvernotificationtimingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationTimingOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationTimingOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ManeuverNotificationTimingOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ManeuverNotificationTimingOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-rangeNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">rangeNotificationDistanceInMeters</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-rangeNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">rangeNotificationTimeInSeconds</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-reminderNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">reminderNotificationDistanceInMeters</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-reminderNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">reminderNotificationTimeInSeconds</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-distanceNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">distanceNotificationDistanceInMeters</span>, </span>
6.  <span id="sdk-for-flutter-navigate-param-distanceNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">distanceNotificationTimeInSeconds</span>, </span>
7.  <span id="sdk-for-flutter-navigate-param-actionNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">actionNotificationDistanceInMeters</span>, </span>
8.  <span id="sdk-for-flutter-navigate-param-actionNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">actionNotificationTimeInSeconds</span>, </span>
9.  <span id="sdk-for-flutter-navigate-param-doubleNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">doubleNotificationDistanceInMeters</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `rangeNotificationDistanceInMeters` The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 0 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 0 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 0 |

- `rangeNotificationTimeInSeconds` The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 0 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 0 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 0 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 0 |

- `reminderNotificationDistanceInMeters` The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a> notification.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 500 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 500 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 500 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 2300 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 800 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 600 |

- `reminderNotificationTimeInSeconds` The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a> notification.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 40 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 40 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 40 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 40 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 40 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 40 |

- `distanceNotificationDistanceInMeters` The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a> notification.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 100 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 100 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 100 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 1300 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 300 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 300 |

- `distanceNotificationTimeInSeconds` The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a> notification.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 18 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 18 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 18 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 18 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 18 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 18 |

- `actionNotificationDistanceInMeters` The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a> notification.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 10 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 10 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 10 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 400 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 100 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 50 |

- `actionNotificationTimeInSeconds` The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a> notification.

| Transport Mode | Timing Profile | Default value |
|----|----|----|
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 5 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 5 |
| <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 5 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> | 5 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> | 5 |
| Others | <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> | 5 |

- `doubleNotificationDistanceInMeters` The default distance setting for double notification.

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
ManeuverNotificationTimingOptions(this.rangeNotificationDistanceInMeters, this.rangeNotificationTimeInSeconds, this.reminderNotificationDistanceInMeters, this.reminderNotificationTimeInSeconds, this.distanceNotificationDistanceInMeters, this.distanceNotificationTimeInSeconds, this.actionNotificationDistanceInMeters, this.actionNotificationTimeInSeconds, this.doubleNotificationDistanceInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
