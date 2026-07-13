---
title: "SchoolZoneWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-schoolzonewarning-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SchoolZoneWarning-class-sidebar.html">

<div>

# <span class="kind-class">SchoolZoneWarning</span> class

</div>

<div class="section desc markdown">

A school zone warning which notifies about a school zone presence on road with a speed limit different than the default speed limit applicable for cars.

Use `SchoolZoneWarningListener` to get notifications about school zones.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-schoolzonewarning">SchoolZoneWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceToSchoolZoneInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToSchoolZoneInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-speedLimitInMetersPerSecond" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">speedLimitInMetersPerSecond</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-distancetoschoolzoneinmeters">distanceToSchoolZoneInMeters</a></span> <span class="signature">↔ double</span>  
The distance from the current location to the school zone in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The distance type for the warning, e.g. a warning for a new school zone ahead or a warning for passing a school zone.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific school zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-speedlimitinmeterspersecond">speedLimitInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
Speed limit meters/second, which applies to current school zone.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-timerule">timeRule</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-timerule-class">TimeRule</a>?</span>  
Time rule indicating the time periods for which the warning applies. If the field is 'null' then the warning is applicable at anytime.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

