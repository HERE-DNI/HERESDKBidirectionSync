---
title: "isManeuverDetectionEnabled property - AutomotiveCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-ismaneuverdetectionenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isManeuverDetectionEnabled.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isManeuverDetectionEnabled</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isManeuverDetectionEnabled</span>

</div>

<div class="section desc markdown">

Enables or disables automatic camera adjustments during upcoming maneuvers. When enabled, the tracking camera automatically adjusts zoom and framing to provide better visibility of upcoming turns and maneuvers during navigation. The specific adjustments and their timing are defined in the camera configuration.

If tracking is currently active when this property is changed, the setting takes effect immediately. Otherwise, it will apply the next time tracking is activated. The initial state is determined by the camera configuration provided during construction. Gets whether maneuver-based camera adjustments are enabled.

</div>

## Implementation

``` dart
bool get isManeuverDetectionEnabled;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isManeuverDetectionEnabled=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isManeuverDetectionEnabled-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Enables or disables automatic camera adjustments during upcoming maneuvers. When enabled, the tracking camera automatically adjusts zoom and framing to provide better visibility of upcoming turns and maneuvers during navigation. The specific adjustments and their timing are defined in the camera configuration.

If tracking is currently active when this property is changed, the setting takes effect immediately. Otherwise, it will apply the next time tracking is activated. The initial state is determined by the camera configuration provided during construction. Sets whether maneuver-based camera adjustments are enabled.

</div>

## Implementation

``` dart
set isManeuverDetectionEnabled(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
