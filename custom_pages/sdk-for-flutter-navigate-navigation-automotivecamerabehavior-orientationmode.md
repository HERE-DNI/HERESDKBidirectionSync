---
title: "orientationMode property - AutomotiveCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-orientationmode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- orientationMode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">orientationMode</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode</a></span> <span class="name">orientationMode</span>

</div>

<div class="section desc markdown">

The current orientation mode of the camera. Defines the camera's viewing angle and orientation for tracking mode. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode2d</a>, the camera looks straight down and rotates with the vehicle heading. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode3d</a>, the camera is tilted for a perspective view. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.modeNorthUp</a>, the camera maintains north-up orientation regardless of vehicle heading.

Changes to this property take effect immediately on the tracking camera and are preserved when switching between tracking and area modes. Gets the current orientation mode.

</div>

## Implementation

``` dart
AutomotiveCameraBehaviorOrientationMode get orientationMode;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">orientationMode=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-orientationMode-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The current orientation mode of the camera. Defines the camera's viewing angle and orientation for tracking mode. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode2d</a>, the camera looks straight down and rotates with the vehicle heading. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode3d</a>, the camera is tilted for a perspective view. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.modeNorthUp</a>, the camera maintains north-up orientation regardless of vehicle heading.

Changes to this property take effect immediately on the tracking camera and are preserved when switching between tracking and area modes. Sets the orientation mode for the tracking camera.

</div>

## Implementation

``` dart
set orientationMode(AutomotiveCameraBehaviorOrientationMode value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
