---
title: "setManeuverModeConfiguration method - TrackingCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehavior-setmaneuvermodeconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setManeuverModeConfiguration.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TrackingCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setManeuverModeConfiguration</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setManeuverModeConfiguration</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setManeuverModeConfiguration-param-maneuverModeConfiguration" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>?</span> <span class="parameter-name">maneuverModeConfiguration</span></span>

)

</div>

<div class="section desc markdown">

Sets the configuration for camera behavior near maneuvers.

Defines how the camera reacts to nearby maneuvers when <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-ismaneuverdetectionenabled">TrackingCameraBehavior.isManeuverDetectionEnabled</a> is `true`. When set to `null`, the camera does not react to maneuvers. The configuration must contain at least one rule to be valid. Defaults to `null`.

- `maneuverModeConfiguration` The maneuver mode configuration. Invalid configurations are rejected.

</div>

## Implementation

``` dart
void setManeuverModeConfiguration(TrackingCameraBehaviorManeuverModeConfiguration? maneuverModeConfiguration);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
