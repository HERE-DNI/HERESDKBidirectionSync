---
title: "DangerZoneWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-dangerzonewarning-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/DangerZoneWarning-class-sidebar.html">

<div>

# <span class="kind-class">DangerZoneWarning</span> class

</div>

<div class="section desc markdown">

Represents danger zones.

A danger zone refers to areas where there is an increased risk of traffic incidents. These zones are designated to alert drivers to potential hazards and encourage safer driving behaviors. Legally, certain devices can alert you to being in a danger zone, typically indicating the presence of a speed camera. In line with applicable law and industry standard, these alerts are usually provided along a road within a range of 4 km on a motorway, 2 km outside built-up areas, and 300 m in built-up areas​​. The HERE SDK warns when approaching the danger zone, as well as when leaving such a zone. A danger zone may or may not have one or more speed cameras in it. The exact location of such speed cameras is not provided. Note that danger zones are only available in selected countries, such as France.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-dangerzonewarning">DangerZoneWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-isZoneStart" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isZoneStart</span>, </span><span id="sdk-for-flutter-navigate-param-distanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-distanceinmeters">distanceInMeters</a></span> <span class="signature">↔ double</span>  
The distance from the current location to the Danger zone.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
Indicates if the specified zone is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-distanceinmeters">DangerZoneWarning.distanceInMeters</a> is greater than 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific danger zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-iszonestart">isZoneStart</a></span> <span class="signature">↔ bool</span>  
A flag indicating whether the Danger Zone officially start in the location the user is entering it.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

