---
title: "Route class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-route-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Route-class-sidebar.html">

<div>

# <span class="kind-class">Route</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A route is a path through a road network over which someone travels.

**Note:** Each <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> of a route contains a list of <a href="sdk-for-flutter-navigate-routing-sectionnotice-class">SectionNotice</a> objects that describe *potential issues* after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-route">Route</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>  
The closest rectangular area where this route fits in. Gets the closest rectangular area where this route fits in.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-consumptioninkilowatthours">consumptionInKilowattHours</a></span> <span class="signature">→ double?</span>  
Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation. Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-duration">duration</a></span> <span class="signature">→ Duration</span>  
The estimated time in seconds needed to travel along this route, including real-time traffic delays if available. Gets the estimated time in seconds needed to travel along this route, including real-time traffic delays if available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-geometry">geometry</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span>  
The <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route. Gets the <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-language">language</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a></span>  
Indicates the language requested for all textual information related to this route. Gets the language requested for all textual information related to this route.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-lengthinmeters">lengthInMeters</a></span> <span class="signature">→ int</span>  
The length of this route in meters. Gets the length of this route in meters.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-optimizationmode">optimizationMode</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a></span>  
The optimization mode requested for route calculation. Gets the optimization mode requested for route calculation.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-railwaycrossings">railwayCrossings</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-routerailwaycrossing-class">RouteRailwayCrossing</a></span>\></span></span>  
Collection of railway crossings along the route. Railway crossing information is only available for routes created with the online `RoutingEngine`. Gets railway crossings.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-requestedtransportmode">requestedTransportMode</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
The transport mode requested for route calculation. Gets the transport mode requested for route calculation.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-routehandle">routeHandle</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>?</span>  
The route handle of this route. Note that it is provided only if <a href="sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle">RouteOptions.enableRouteHandle</a> is set before route calculation. Gets the route handle of this route. Note that it is provided only if <a href="sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle">RouteOptions.enableRouteHandle</a> is set before route calculation.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-routelabels">routeLabels</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-routelabel-class">RouteLabel</a></span>\></span></span>  
A collection containing a maximum of 2 `RouteLabel` instances for the route. It will return an empty list if no labels are available. The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes. The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives when alternative routes have been quested via `RouteOptions`. Gets route labels.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-routingoptions">routingOptions</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a>?</span>  
The set of options used to calculate the route. Gets the options used to calculate this route.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-sections">sections</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-section-class">Section</a></span>\></span></span>  
The sections that make up this route. Gets the sections that make up this route.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-trafficdelay">trafficDelay</a></span> <span class="signature">→ Duration</span>  
The estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual. Gets the estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-deserialize">deserialize</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-deserialize-param-routeData" class="parameter"><span class="type-annotation">Uint8List</span> <span class="parameter-name">routeData</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span> </span>  
Creates route from the given binary data.

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-serialize">serialize</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-serialize-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">route</span></span>) <span class="returntype parameter">→ Uint8List?</span> </span>  
Serializes given route to a binary data.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

