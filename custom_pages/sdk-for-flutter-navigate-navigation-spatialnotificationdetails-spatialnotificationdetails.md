---
title: "SpatialNotificationDetails constructor - SpatialNotificationDetails - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-spatialnotificationdetails-spatialnotificationdetails"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SpatialNotificationDetails-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SpatialNotificationDetails</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SpatialNotificationDetails</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-initialAzimuthInDegrees" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">initialAzimuthInDegrees</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-audioCuePanning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class">SpatialAudioCuePanning</a></span> <span class="parameter-name">audioCuePanning</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-estimatedAudioCueDuration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">estimatedAudioCueDuration</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `initialAzimuthInDegrees` Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (`ManeuverAction.RightTurn`) we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is located slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps". The orientation in space for <a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees">SpatialNotificationDetails.initialAzimuthInDegrees</a> can be represented by the following angular values:

| Front | Right |  Rear  | Left |
|:-----:|:-----:|:------:|:----:|
|  0°   | +90°  | +- 180 | -90° |

- `audioCuePanning` Object to start the angular panning when spatialization of the text notification is desired
- `estimatedAudioCueDuration` Estimation of the required time to play an audio cue at speech rate 1.0. For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds. Therefore, an estimation of this audio cue duration is needed to correctly sync the movement of sound to the cue (so that audio movement and audio duration match).

</div>

## Implementation

``` dart
SpatialNotificationDetails(this.initialAzimuthInDegrees, this.audioCuePanning, this.estimatedAudioCueDuration);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

