---
title: "TransitRouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-transitrouteoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TransitRouteOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TransitRouteOptions-class-sidebar.html">

<div>

# <span class="kind-class">TransitRouteOptions</span> class

</div>

<div class="section desc markdown">

All the options to specify how a public transit route should be calculated.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-transitrouteoptions">TransitRouteOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-alternatives">alternatives</a></span> <span class="signature">↔ int</span>  
Number of alternative routes to return aside from the optimal route. The provided value must be in the range \[0, 6\]. By default, it is 0 and only one route is calculated.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-arrivaltime">arrivalTime</a></span> <span class="signature">↔ DateTime?</span>  
Optional time when travel is expected to end.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-changes">changes</a></span> <span class="signature">↔ int?</span>  
Maximum number of changes or transfers allowed in a route. When it is not set, unlimited number of changes is permitted. The provided value must be in the range \[0, 6\].

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-departuretime">departureTime</a></span> <span class="signature">↔ DateTime?</span>  
Optional time when travel is expected to start. If it is not specified, it is set to the current time.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-modefilter">modeFilter</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-transitmodefilter">TransitModeFilter</a></span>  
Defines inclusion or exclusion of transit modes for route calculation. By default, the inclusion mode is used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-modes">modes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-transitmode">TransitMode</a></span>\></span></span>  
This list is used to determine which transit modes should be used for route calculation, <a href="sdk-for-flutter-navigate-routing-transitrouteoptions-modefilter">TransitRouteOptions.modeFilter</a> specifies whether this list is an inclusion or an exclusion. For example, specifying subway and bus transit modes with the include filter, returns only subway and bus transit modes, and with the exclude filter, returns all the transit modes except subway and bus. When not set, all the supported transit modes are permitted. By default, this list is empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-pedestrianmaxdistanceinmeters">pedestrianMaxDistanceInMeters</a></span> <span class="signature">↔ int</span>  
Maximum allowed walking distance in meters (e.g. when looking for nearest stations). The provided value must be in the range \[0, 6000\]. The default value is 2000 meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-pedestrianspeedinmeterspersecond">pedestrianSpeedInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
Walking speed in meters per second. Influences the duration of walking segments from origin to a station, from a station to destination and in-between the stations (e.g. if transfer is needed). The provided value must be in the range \[0.5, 2.0\]. The default value is 1.0 mps.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-fromdefaultparameterconfiguration">fromDefaultParameterConfiguration</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-routing-transitrouteoptions-class">TransitRouteOptions</a></span> </span>  
Returns TransitRouteOptions instance with default values used in SDK.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
