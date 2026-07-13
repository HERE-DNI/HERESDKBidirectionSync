---
title: "LocationAccuracy enum - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationaccuracy"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationAccuracy-enum-sidebar.html">

<div>

# <span class="kind-enum">LocationAccuracy</span> enum

</div>

<div class="section desc markdown">

Indicates the desired location accuracy, however the actual accuracy is not guaranteed.

When requesting high-accuracy locations, the initial update delivered by the LocationEngine may not have the requested accuracy. Requesting higher accuracy location updates usually means higher power consumption, therefore you should use the lowest accuracy suitable for your use case to preserve the device battery.

</div>

## Values

<span class="name">bestAvailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span>  

<span class="name">subMeterNavigation</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span>  
Decimeter accurate navigation using satellite and WiFi positioning. Additional sensor data may be used for improving positioning accuracy. Update frequency is as close to once per second as possible. This feature requires Android 12 or later and dual frequency GNSS receiver and raw GNSS measurements. This feature is disabled by default: <a href="https://www.here.com/platform/positioning">Contact us</a> to enable it. If it is not enabled or the OS/device requirements are not met, fallback to other positioning technologies may occur and desired accuracy level may not be reached.

Not supported in iOS.

<span class="name">navigation</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span>  

<span class="name">tensOfMeters</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span>  
Accurate to within tens of meters of the desired target.

<span class="name">hundredsOfMeters</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span>  
Accurate to within hundreds of meters of the desired target.

<span class="name">kilometers</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span>  
Accurate to within kilometers of the desired target.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-locationaccuracy-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationaccuracy-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationaccuracy-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationaccuracy-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationaccuracy-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-locationaccuracy-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-location-locationaccuracy-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

