---
title: "NotificationOptions class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-notificationoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NotificationOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/NotificationOptions-class-sidebar.html">

<div>

# <span class="kind-class">NotificationOptions</span> class

</div>

<div class="section desc markdown">

Positioning notification options.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-notificationoptions">NotificationOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-desiredintervalmilliseconds">desiredIntervalMilliseconds</a></span> <span class="signature">↔ int</span>  
Desired interval for position updates in milliseconds. This interval is not guaranteed. Default interval is 30 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-smallestintervalmilliseconds">smallestIntervalMilliseconds</a></span> <span class="signature">↔ int</span>  
Smallest allowed interval for position updates in milliseconds. It is guaranteed that positions are not provided more often than this value. Smallest interval could be used for throttling position updates, e.g. when each position update triggers CPU intensive calculations in the client application. This value is used as a minimum update interval when requesting GNSS location updates from the operating system. When hdEnabled is set to `true` in SatellitePositioningOptions, the smallest_interval_milliseconds value has a limited range. The SDK will adjust the value to allow location updates with a frequency of 1Hz to 10Hz (1000 ms to 100 ms, respectively). Default interval is 900 milliseconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-notificationoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
