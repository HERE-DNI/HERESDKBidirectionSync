---
title: "maneuverRules property - TrackingCameraBehaviorManeuverModeConfiguration class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-maneuverrules"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TrackingCameraBehaviorManeuverModeConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">maneuverRules</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class">TrackingCameraBehaviorManeuverRule</a></span>\></span> <span class="name">maneuverRules</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Ordered list of maneuver rules. Rules are evaluated in order; the first matching rule determines the camera behavior. If empty, this configuration is not valid and the camera does not react to maneuvers. If <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration">TrackingCameraBehavior.defaultManeuverModeConfiguration</a> is not used for <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>, it will be an empty list.

</div>

## Implementation

``` dart
List<TrackingCameraBehaviorManeuverRule> maneuverRules;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

