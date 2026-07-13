---
title: "earlyPreManeuverActivationThresholdInMeters property - TrackingCameraBehaviorManeuverRuleOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-earlypremaneuveractivationthresholdinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- earlyPreManeuverActivationThresholdInMeters.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TrackingCameraBehaviorManeuverRuleOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">earlyPreManeuverActivationThresholdInMeters</span> property

</div>

<div class="section multi-line-signature">

double <span class="name">earlyPreManeuverActivationThresholdInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Distance in meters for early activation. If the current position enters this threshold of the upcoming maneuver while still within <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-postmaneuveractivationthresholdinmeters">TrackingCameraBehaviorManeuverRuleOptions.postManeuverActivationThresholdInMeters</a> of the previous maneuver, the camera behaves as though it were already in the upcoming maneuver's pre-activation zone. Must be non-negative. Defaults to 0.0.

</div>

## Implementation

``` dart
double earlyPreManeuverActivationThresholdInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
