---
title: "TollStop class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-tollstop-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TollStop-class-sidebar.html">

<div>

# <span class="kind-class">TollStop</span> class

</div>

<div class="section desc markdown">

A class that provides information for a toll stop with multiple toll booths.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-tollstop">TollStop</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span>, </span><span id="sdk-for-flutter-navigate-param-distanceToTollStopInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToTollStopInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-lanes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-tollboothlane-class">TollBoothLane</a></span>\></span></span> <span class="parameter-name">lanes</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-distancetotollstopinmeters">distanceToTollStopInMeters</a></span> <span class="signature">↔ double</span>  
Distance to the toll stop in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
Indicates if the specified toll stop is ahead of the vehicle or has just passed by.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific toll stop warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-lanes">lanes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-tollboothlane-class">TollBoothLane</a></span>\></span></span>  
Describes the features of the booth for the lane. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

