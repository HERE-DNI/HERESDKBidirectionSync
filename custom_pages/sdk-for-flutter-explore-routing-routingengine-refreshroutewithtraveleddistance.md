---
title: "refreshRouteWithTraveledDistance abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-refreshroutewithtraveleddistance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- refreshRouteWithTraveledDistance.html -->


<div>
<h1>refreshRouteWithTraveledDistance abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the refresh_route() methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
refreshRouteWithTraveledDistance(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> routeHandle, </li>
<li><a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>? startingPoint, </li>
<li>int? lastTraveledSectionIndex, </li>
<li>int? traveledDistanceOnLastSectionInMeters, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-refreshrouteoptions-class">RefreshRouteOptions</a> refreshRouteOptions, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback, </li>
</ol>)

      

    

<p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>, updating
the starting point and route metadata based on <a class="deprecated" href="sdk-for-flutter-explore-routing-refreshrouteoptions-class">RefreshRouteOptions</a>.</p>
<p>The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated. If you only want to refresh the contained traffic information, consider to use
<a href="sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroutewithcurrentcharge">RoutingEngine.calculateTrafficOnRouteWithCurrentCharge</a> instead.</p>
<p>Calling this method will trigger a new "HERE Routing" transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle holding the route to be refreshed.</p>
</li>
<li>
<p><code>startingPoint</code> Updates the starting point of the route. It should be of type <a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType.stopover</a>. Otherwise,
an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated. Moreover, it should be very close to the
original route specified with the <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a> items that lie behind the new starting point (i.e. the path that
was already travelled). Plus, <a href="sdk-for-flutter-explore-routing-route-lengthinmeters">Route.lengthInMeters</a> and <a href="sdk-for-flutter-explore-routing-route-duration">Route.duration</a>
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.couldNotMatchOrigin</a> error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
</li>
<li>
<p><code>refreshRouteOptions</code> Options to refresh the route.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after refreshing the route.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the refresh_route() methods with RoutingOptions parameter instead.")

TaskHandle refreshRouteWithTraveledDistance(RouteHandle routeHandle, Waypoint? startingPoint, int? lastTraveledSectionIndex, int? traveledDistanceOnLastSectionInMeters, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
