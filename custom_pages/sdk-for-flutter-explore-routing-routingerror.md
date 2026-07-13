---
title: "RoutingError enum - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routingerror"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutingError.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutingError-enum-sidebar.html">

<div>

# <span class="kind-enum">RoutingError</span> enum

</div>

<div class="section desc markdown">

Specifies possible errors that may result from the calculation of a route.

</div>

## Values

<span class="name">internalError</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Generic internal error.

<span class="name">invalidParameter</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
An invalid input parameter.

<span class="name">serverUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Routing server is unreachable.

<span class="name">httpError</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
A general network request error.

<span class="name">authenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Routing operation is not authenticated. Check your credentials.

<span class="name">forbidden</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
The provided credentials don't give access to the requested resource.

<span class="name">exceededUsageLimit</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Credentials exceeded the allowed requests limit.

<span class="name">parsingError</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Error while parsing route data. This is not expected to happen. Try updating to the newest version of the SDK. If the problem persists, please report a bug in the SDK.

<span class="name">noRouteFound</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
No route can be calculated for the given input.

<span class="name">timedOut</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
The request timed out.

<span class="name">offline</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
The device has no internet connection.

<span class="name">noIsolineFound</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
No isoline can be calculated for the given input.

<span class="name">noRouteHandle</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
The route has no <a href="sdk-for-flutter-explore-routing-route-routehandle">Route.routeHandle</a>, but it was used for a feature that requires one. Consider to recalculate the route with a route handle. See <a href="sdk-for-flutter-explore-routing-routeoptions-enableroutehandle">RouteOptions.enableRouteHandle</a>.

<span class="name">operationCancelled</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Operation cancelled.

<span class="name">couldNotMatchDestination</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Destination waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.

<span class="name">couldNotMatchOrigin</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Origin waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.

<span class="name">failedRouteHandleCreation</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
No RouteHandle was created.

<span class="name">importFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
No route section was found for imported waypoints.

<span class="name">noReachableChargingStationFound</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Initial charge is not enough to reach any known charging stations.

<span class="name">routeCalculationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Calculation did not succeed.

<span class="name">routeLengthLimitExceeded</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Distance between waypoints is too large for current options.

<span class="name">violatedTransportModeInRouteHandleDecoding</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Route handle decoding failed due to forbidden segments for the specified transport mode.

<span class="name">proxyAuthenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Proxy is not authenticated. Check your proxy credentials.

<span class="name">proxyServerUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Proxy server unreachable.

<span class="name">activeMapUpdate</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>  
Route cannot be calculated due to active map update. Please, repeat the request after map update is finished successfully.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-routingerror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingerror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingerror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-routingerror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingerror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-routingerror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-routing-routingerror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
