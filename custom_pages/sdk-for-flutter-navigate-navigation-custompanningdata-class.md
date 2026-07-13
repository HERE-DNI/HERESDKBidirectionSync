---
title: "CustomPanningData class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/CustomPanningData-class-sidebar.html">

<div>

# <span class="kind-class">CustomPanningData</span> class

</div>

<div class="section desc markdown">

This class contains all the information regarding the next angular panning element, including a new estimated audio cue duration, and a new set of initial and sweep angular angle, allowing the customization of the spatial audio trajectories for any type of notification, such as speed or merge warners, maneuvers or even roundabouts notifications.

The orientation in space for <a href="sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees">CustomPanningData.initialAzimuthInDegrees</a> and <a href="sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees">CustomPanningData.sweepAzimuthInDegrees</a> can be represented by the following angular values:

| Front | Right |  Rear  | Left |
|:-----:|:-----:|:------:|:----:|
|  0°   | +90°  | +- 180 | -90° |

When any of the members of <a href="sdk-for-flutter-navigate-navigation-custompanningdata-class">CustomPanningData</a> are initialized as null, the default value provided by HERE SDK will be used instead. The audio cue is spatialized considering the action of both maneuvers, for example, the audio cue 'Now turn right and then turn left' will be spatialized as following: 'Now turn right' will be heard as coming from the right. 'and then turn left' will be heard as coming from the left. Note: The estimation for playing both audio cues could be not fully accurate and therefore a mismatch between the audio source and the audio cue message could be perceived.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-custompanningdata">CustomPanningData</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-estimatedAudioCueDuration" class="parameter"><span class="type-annotation">Duration?</span> <span class="parameter-name">estimatedAudioCueDuration</span>, </span><span id="sdk-for-flutter-navigate-param-initialAzimuthInDegrees" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">initialAzimuthInDegrees</span>, </span><span id="sdk-for-flutter-navigate-param-sweepAzimuthInDegrees" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">sweepAzimuthInDegrees</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-estimatedaudiocueduration">estimatedAudioCueDuration</a></span> <span class="signature">↔ Duration?</span>  
Customized estimated duration for playing the audio cue on the selected TTS Engine. When not used, HERE SDK's estimation will be used instead.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees">initialAzimuthInDegrees</a></span> <span class="signature">↔ double?</span>  
Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (`ManeuverAction.RightTurn`) we want to create a spatial audio arc from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is slightly located on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees">sweepAzimuthInDegrees</a></span> <span class="signature">↔ double?</span>  
Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (i.e. `ManeuverAction.RightTurn`), within an `initial_azimuth_in_degrees` of -5 degrees, we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of +95 degrees would be required. On the other hand, when the desired spatialization is to the left side (i.e. `ManeuverAction.LeftTurn`), the `initial_azimuth_in_degrees` could be set to +5 degrees and the `sweep_azimuth_in_degrees` to -95 degrees

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

