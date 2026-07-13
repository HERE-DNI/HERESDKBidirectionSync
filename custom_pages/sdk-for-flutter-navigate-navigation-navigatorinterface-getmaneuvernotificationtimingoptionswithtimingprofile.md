---
title: "getManeuverNotificationTimingOptionsWithTimingProfile method - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getManeuverNotificationTimingOptionsWithTimingProfile</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> <span class="name">getManeuverNotificationTimingOptionsWithTimingProfile</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getManeuverNotificationTimingOptionsWithTimingProfile-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span>
2.  <span id="sdk-for-flutter-navigate-getManeuverNotificationTimingOptionsWithTimingProfile-param-timingProfile" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="parameter-name">timingProfile</span></span>

)

</div>

<div class="section desc markdown">

Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.

The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.

- `transportMode` The transport mode of the timing options.

- `timingProfile` The timing profile of the timing options.

Returns <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a>. The timing options with default values.

</div>

## Implementation

``` dart
ManeuverNotificationTimingOptions getManeuverNotificationTimingOptionsWithTimingProfile(TransportMode transportMode, TimingProfile timingProfile);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

