---
title: "TrafficOptimizationMode enum - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-trafficoptimizationmode"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TrafficOptimizationMode-enum-sidebar.html">

<div>

# <span class="kind-enum">TrafficOptimizationMode</span> enum

</div>

<div class="section desc markdown">

Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.

</div>

## Values

<span class="name">timeDependent</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span>  
Traffic optimization is enabled, the shape of the route will be adjusted according to the traffic situation that depends on the <a href="sdk-for-flutter-navigate-routing-routeoptions-departuretime">RouteOptions.departureTime</a> or <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a>. As a result, streets with heavy traffic will be avoided whenever possible. Note that this mode enables traffic-aware routing.

<span class="name">longTermClosuresOnly</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span>  
Only long-term road closures are taken into account. Both <a href="sdk-for-flutter-navigate-routing-routeoptions-departuretime">RouteOptions.departureTime</a> and <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a> are ignored, and the route will be shaped disregarding all the available current and historical traffic information, except long-term road closures. Note that this mode disables traffic-aware routing regardless of other settings.

<span class="name">disabled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span>  
Traffic optimization is completely disabled, including long-term road closures. Both <a href="sdk-for-flutter-navigate-routing-routeoptions-departuretime">RouteOptions.departureTime</a> and <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a> are ignored, and the route will be shaped disregarding all the available current and historical traffic information. Note that seasonal closures are not excluded. To exclude seasonal closures, use <a href="sdk-for-flutter-navigate-routing-roadfeatures">RoadFeatures.seasonalClosure</a>. Note that this mode disables traffic-aware routing regardless of other settings.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

