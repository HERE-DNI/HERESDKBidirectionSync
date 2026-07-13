---
title: "RefreshRouteParameters class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-refreshrouteparameters-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteParameters-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RefreshRouteParameters-class-sidebar.html">

<div>

# <span class="kind-class">RefreshRouteParameters</span> class

</div>

<div class="section desc markdown">

This class provides the necessary information for refreshing a route from a specific location on it.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandsectionposition">RefreshRouteParameters.withRouteHandleAndSectionPosition</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withRouteHandleAndSectionPosition-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span><span id="sdk-for-flutter-explore-withRouteHandleAndSectionPosition-param-startingSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">startingSectionIndex</span>, </span><span id="sdk-for-flutter-explore-withRouteHandleAndSectionPosition-param-traveledDistanceOnStartingSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnStartingSectionInMeters</span></span>)</span>  
Create a new instance of <a href="sdk-for-flutter-explore-routing-refreshrouteparameters-class">RefreshRouteParameters</a> with the point on the section of the route as a new starting point.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypoint">RefreshRouteParameters.withRouteHandleAndWaypoint</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withRouteHandleAndWaypoint-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span><span id="sdk-for-flutter-explore-withRouteHandleAndWaypoint-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">startingPoint</span></span>)</span>  
Create a new instance of <a href="sdk-for-flutter-explore-routing-refreshrouteparameters-class">RefreshRouteParameters</a> with the new starting point on the route.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypointandsectionposition">RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withRouteHandleAndWaypointAndSectionPosition-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span><span id="sdk-for-flutter-explore-withRouteHandleAndWaypointAndSectionPosition-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">startingPoint</span>, </span><span id="sdk-for-flutter-explore-withRouteHandleAndWaypointAndSectionPosition-param-startingSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">startingSectionIndex</span>, </span><span id="sdk-for-flutter-explore-withRouteHandleAndWaypointAndSectionPosition-param-traveledDistanceOnStartingSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnStartingSectionInMeters</span></span>)</span>  
Create a new instance of <a href="sdk-for-flutter-explore-routing-refreshrouteparameters-class">RefreshRouteParameters</a> with the new starting point and the section position on the route.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-routehandle">routeHandle</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a></span>  
The route handle holding the route to be refreshed.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-startingpoint">startingPoint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>?</span>  
Identify the new starting point of the route. It should be of type <a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType.stopover</a>. Otherwise, an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. The location of this waypoint may by provided, for example, by a `RouteProgress` event. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a> items that lie behind the new starting point (i.e. the path that was already traveled). Plus, <a href="sdk-for-flutter-explore-routing-route-lengthinmeters">Route.lengthInMeters</a>, <a href="sdk-for-flutter-explore-routing-route-duration">Route.duration</a>, and similar values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.couldNotMatchOrigin</a> error is triggered. In that case, an application may decide to calculate a new route from scratch.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-startingsectionindex">startingSectionIndex</a></span> <span class="signature">↔ int?</span>  
Indicates the index of the last traveled route section. When it is provided, the previous sections are discarded from the refreshed route and the starting point is searched in the provided section. If the starting point is not found in that section an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.couldNotMatchOrigin</a> error is triggered.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-traveleddistanceonstartingsectioninmeters">traveledDistanceOnStartingSectionInMeters</a></span> <span class="signature">↔ int?</span>  
Provides an indication on how much of the starting section is already traveled. The refresh route function would ignore the first part of the section. If it is provided with an invalid starting section index, an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
