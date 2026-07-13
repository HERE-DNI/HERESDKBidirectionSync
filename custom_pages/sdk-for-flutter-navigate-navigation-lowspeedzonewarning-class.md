---
title: "LowSpeedZoneWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LowSpeedZoneWarning-class-sidebar.html">

<div>

# <span class="kind-class">LowSpeedZoneWarning</span> class

</div>

<div class="section desc markdown">

A class that provides low speed zone.

The main field describing the low speed zone is `LowSpeedZoneWarning.speed_limit_in_meters_per_second` specifying the speed limit of the low speed zone. Use `LowSpeedZoneWarningListener` to get notifications about upcoming low speed zones.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-lowspeedzonewarning">LowSpeedZoneWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceToLowSpeedZoneInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToLowSpeedZoneInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-speedLimitInMetersPerSecond" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">speedLimitInMetersPerSecond</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span>, </span><span id="sdk-for-flutter-navigate-param-segmentReference" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span> <span class="parameter-name">segmentReference</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-distancetolowspeedzoneinmeters">distanceToLowSpeedZoneInMeters</a></span> <span class="signature">↔ double</span>  
Distance to the low speed warning in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The distance type for the warning, e.g. a warning for a new low speed zone ahead or a warning for passing a low speed zone.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific low speed zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-segmentreference">segmentReference</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span>  
The reference to the segment where the low speed zone is located. It can be used to identify the location.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-speedlimitinmeterspersecond">speedLimitInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
Speed limit of the low speed zone.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

