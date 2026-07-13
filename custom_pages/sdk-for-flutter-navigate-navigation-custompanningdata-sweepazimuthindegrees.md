---
title: "sweepAzimuthInDegrees property - CustomPanningData class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- sweepAzimuthInDegrees.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/CustomPanningData-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">sweepAzimuthInDegrees</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">sweepAzimuthInDegrees</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (i.e. `ManeuverAction.RightTurn`), within an `initial_azimuth_in_degrees` of -5 degrees, we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of +95 degrees would be required. On the other hand, when the desired spatialization is to the left side (i.e. `ManeuverAction.LeftTurn`), the `initial_azimuth_in_degrees` could be set to +5 degrees and the `sweep_azimuth_in_degrees` to -95 degrees

</div>

## Implementation

``` dart
double? sweepAzimuthInDegrees;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
