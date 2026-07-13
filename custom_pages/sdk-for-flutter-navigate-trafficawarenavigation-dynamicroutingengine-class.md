---
title: "DynamicRoutingEngine class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DynamicRoutingEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/trafficawarenavigation-library-sidebar.html" data-below-sidebar="trafficawarenavigation/DynamicRoutingEngine-class-sidebar.html">

<div>

# <span class="kind-class">DynamicRoutingEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This class queries the HERE routing backend to find routes with less traffic and therefore an earlier remaining estimated time of arrival.

<a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a> polls the HERE routing backend periodically to find the best new route out of a given initial route. For initial route calculation it is recommended to use the <a href="sdk-for-flutter-navigate-routing-routingengine-class">RoutingEngine</a> as it already requests traffic-optimized routes.

When a better route is found, it is recommended to follow these steps to set the new route:

1.  Stop the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>.

2.  Update the currently active `Navigator`instance with the newly found route.

3.  Restart the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>. This should be done outside of the

        onBetterRouteFound()

    callback.

For both <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a> and <a href="sdk-for-flutter-navigate-routing-routingengine-class">RoutingEngine</a>, the resulting routes are optimized based on speed flow changes such as traffic jams, street closures or road accidents. To get the best result, it is recommended to not specify the <a href="sdk-for-flutter-navigate-routing-routeoptions-departuretime">RouteOptions.departureTime</a> as then the current time is used by default.

The poll interval is defined by <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval">DynamicRoutingEngineOptions.pollInterval</a> and triggered by <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation">DynamicRoutingEngine.updateCurrentLocation</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-dynamicroutingengine">DynamicRoutingEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>?</span> <span class="parameter-name">options</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-dynamicroutingengine-withsdkengine">DynamicRoutingEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-withSdkEngine-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>?</span> <span class="parameter-name">options</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-start">start</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-start-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">route</span>, </span><span id="sdk-for-flutter-navigate-start-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypoints" class="deprecated">startWithWaypoints</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startWithWaypoints-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span><span id="sdk-for-flutter-navigate-startWithWaypoints-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-startWithWaypoints-param-refreshRouteOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-class" class="deprecated">RefreshRouteOptions</a></span> <span class="parameter-name">refreshRouteOptions</span>, </span><span id="sdk-for-flutter-navigate-startWithWaypoints-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts polling the HERE backend services to find a better route, as defined by the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypointsandroutingoptions">startWithWaypointsAndRoutingOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startWithWaypointsAndRoutingOptions-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span><span id="sdk-for-flutter-navigate-startWithWaypointsAndRoutingOptions-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-startWithWaypointsAndRoutingOptions-param-routingOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">routingOptions</span>, </span><span id="sdk-for-flutter-navigate-startWithWaypointsAndRoutingOptions-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts polling the HERE backend services to find a better route, as defined by the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-stop">stop</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops polling the HERE backend services.

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation">updateCurrentLocation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateCurrentLocation-param-mapMatchedLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a></span> <span class="parameter-name">mapMatchedLocation</span>, </span><span id="sdk-for-flutter-navigate-updateCurrentLocation-param-sectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">sectionIndex</span></span>) <span class="returntype parameter">→ void</span> </span>  
Updates the current location.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
