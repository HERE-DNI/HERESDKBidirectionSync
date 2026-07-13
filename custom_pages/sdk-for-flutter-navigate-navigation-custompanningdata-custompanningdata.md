---
title: "CustomPanningData constructor - CustomPanningData - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-custompanningdata"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomPanningData.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/CustomPanningData-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">CustomPanningData</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">CustomPanningData</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-estimatedAudioCueDuration" class="parameter"><span class="type-annotation">Duration?</span> <span class="parameter-name">estimatedAudioCueDuration</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-initialAzimuthInDegrees" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">initialAzimuthInDegrees</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-sweepAzimuthInDegrees" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">sweepAzimuthInDegrees</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `estimatedAudioCueDuration` Customized estimated duration for playing the audio cue on the selected TTS Engine. When not used, HERE SDK's estimation will be used instead.
- `initialAzimuthInDegrees` Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (`ManeuverAction.RightTurn`) we want to create a spatial audio arc from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is slightly located on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps".
- `sweepAzimuthInDegrees` Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (i.e. `ManeuverAction.RightTurn`), within an `initial_azimuth_in_degrees` of -5 degrees, we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of +95 degrees would be required. On the other hand, when the desired spatialization is to the left side (i.e. `ManeuverAction.LeftTurn`), the `initial_azimuth_in_degrees` could be set to +5 degrees and the `sweep_azimuth_in_degrees` to -95 degrees

</div>

## Implementation

``` dart
CustomPanningData(this.estimatedAudioCueDuration, this.initialAzimuthInDegrees, this.sweepAzimuthInDegrees);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
