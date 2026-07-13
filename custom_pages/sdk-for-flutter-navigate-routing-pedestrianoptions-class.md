---
title: "PedestrianOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-pedestrianoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/PedestrianOptions-class-sidebar.html">

<div>

# <span class="kind-class">PedestrianOptions</span> class

</div>

<div class="section desc markdown">

All the options to specify how a pedestrian route should be calculated.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`RoutingOptions\` class instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-pedestrianoptions">PedestrianOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-avoidanceoptions">avoidanceOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
Options to specify restrictions for route calculations. By default no restrictions are applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-routeoptions">routeOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a></span>  
Specifies the common route calculation options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-walkspeedinmeterspersecond">walkSpeedInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
Specifies the speed that will be used by the service as the walking speed for pedestrian routing in meters per second. It influences the duration of walking segments along the route. The provided value must be in the range \[0.5, 2.0\]. When the value is outside this range, an invalid parameter error is raised. Refer to <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a> for details. The default speed is 1 meter per second.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-fromdefaultparameterconfiguration">fromDefaultParameterConfiguration</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-routing-pedestrianoptions-class" class="deprecated">PedestrianOptions</a></span> </span>  
Returns PedestrianOptions instance with default values used in SDK.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

