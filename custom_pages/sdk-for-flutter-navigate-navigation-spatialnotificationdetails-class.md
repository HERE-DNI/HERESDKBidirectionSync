---
title: "SpatialNotificationDetails class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpatialNotificationDetails-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SpatialNotificationDetails-class-sidebar.html">

<div>

# <span class="kind-class">SpatialNotificationDetails</span> class

</div>

<div class="section desc markdown">

This class provides all the information for a spatial text notification, including the maneuver data and extra data which is required to set the direction of spatialization of the audio cue.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-spatialnotificationdetails">SpatialNotificationDetails</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-initialAzimuthInDegrees" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">initialAzimuthInDegrees</span>, </span><span id="sdk-for-flutter-navigate-param-audioCuePanning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class">SpatialAudioCuePanning</a></span> <span class="parameter-name">audioCuePanning</span>, </span><span id="sdk-for-flutter-navigate-param-estimatedAudioCueDuration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">estimatedAudioCueDuration</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-audiocuepanning">audioCuePanning</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class">SpatialAudioCuePanning</a></span>  
Object to start the angular panning when spatialization of the text notification is desired

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-estimatedaudiocueduration">estimatedAudioCueDuration</a></span> <span class="signature">↔ Duration</span>  
Estimation of the required time to play an audio cue at speech rate 1.0. For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds. Therefore, an estimation of this audio cue duration is needed to correctly sync the movement of sound to the cue (so that audio movement and audio duration match).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees">initialAzimuthInDegrees</a></span> <span class="signature">↔ double</span>  
Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (`ManeuverAction.RightTurn`) we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is located slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps". The orientation in space for <a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees">SpatialNotificationDetails.initialAzimuthInDegrees</a> can be represented by the following angular values:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
