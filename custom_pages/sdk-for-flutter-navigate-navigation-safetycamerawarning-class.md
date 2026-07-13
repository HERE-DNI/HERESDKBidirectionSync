---
title: "SafetyCameraWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SafetyCameraWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SafetyCameraWarning-class-sidebar.html">

<div>

# <span class="kind-class">SafetyCameraWarning</span> class

</div>

<div class="section desc markdown">

A class that provides safety camera warning information.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-safetycamerawarning">SafetyCameraWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceToCameraInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToCameraInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-speedLimitInMetersPerSecond" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">speedLimitInMetersPerSecond</span>, </span><span id="sdk-for-flutter-navigate-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycameratype">SafetyCameraType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-distancetocamerainmeters">distanceToCameraInMeters</a></span> <span class="signature">↔ double</span>  
Distance to the safety camera in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The distance type of the warning (e.g.: warning for a new safety camera ahead, warning for passing a safety camera). Since the safety camera warning is given relative to a single position on the route, <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> will never be given for this warning.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific safety camera warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-speedlimitinmeterspersecond">speedLimitInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
The speed limit observed by the safety camera.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-safetycameratype">SafetyCameraType</a></span>  
The type of the safety camera element.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
