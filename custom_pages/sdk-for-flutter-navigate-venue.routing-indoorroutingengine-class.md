---
title: "IndoorRoutingEngine class - venue.routing library - Dart API"
slug: "sdk-for-flutter-navigate-venue.routing-indoorroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IndoorRoutingEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.routing/venue.routing-library-sidebar.html" data-below-sidebar="venue.routing/IndoorRoutingEngine-class-sidebar.html">

<div>

# <span class="kind-class">IndoorRoutingEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use the IndoorRoutingEngine to calculate a route inside a venue.

\
Route calculation is done asynchronously and requires an internet connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.\
Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. Currently, the indoor route calculation may not be accurate so that e.g. a pedestrian end user might be routed via a vehicle access and route or similar. Therefore end users must use this feature with caution and always be aware of the surroundings. The signs and instructions given at the premises must be observed. You are required to inform the end user about this in an appropriate manner, whether in the UI of your application, your end user terms or similar.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingengine-indoorroutingengine">IndoorRoutingEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-venueService" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a></span> <span class="parameter-name">venueService</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingengine-calculateroute">calculateRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateRoute-param-from" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class">IndoorWaypoint</a></span> <span class="parameter-name">from</span>, </span><span id="sdk-for-flutter-navigate-calculateRoute-param-to" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class">IndoorWaypoint</a></span> <span class="parameter-name">to</span>, </span><span id="sdk-for-flutter-navigate-calculateRoute-param-routeOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-indoorrouteoptions-class">IndoorRouteOptions</a></span> <span class="parameter-name">routeOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-calculateindoorroutecallback">CalculateIndoorRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Asynchronously calculates a route inside a venue.

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
