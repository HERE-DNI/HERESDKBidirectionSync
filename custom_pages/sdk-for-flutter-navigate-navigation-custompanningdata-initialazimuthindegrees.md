---
title: "initialAzimuthInDegrees property - CustomPanningData class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/CustomPanningData-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">initialAzimuthInDegrees</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">initialAzimuthInDegrees</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (`ManeuverAction.RightTurn`) we want to create a spatial audio arc from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is slightly located on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps".

</div>

## Implementation

``` dart
double? initialAzimuthInDegrees;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

