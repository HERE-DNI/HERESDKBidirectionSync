---
title: "setManeuverNotificationTimingOptionsWithTimingProfile method - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setManeuverNotificationTimingOptionsWithTimingProfile</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">setManeuverNotificationTimingOptionsWithTimingProfile</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-timingProfile" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="parameter-name">timingProfile</span>, </span>
3.  <span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> <span class="parameter-name">options</span></span>

)

</div>

<div class="section desc markdown">

Set timing option values for the combination of transport mode and timing profile.

- `transportMode` The transport mode of the timing options.

- `timingProfile` The timing profile of the timing options.

- `options` The timing options.

Returns `bool`. `True` if set successfully, `false` when options has invalid value, see <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a> for more details about options.

</div>

## Implementation

``` dart
bool setManeuverNotificationTimingOptionsWithTimingProfile(TransportMode transportMode, TimingProfile timingProfile, ManeuverNotificationTimingOptions options);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

