---
title: "returnToRouteWithTraveledDistance abstract method"
slug: "sdk-for-flutter-explore-routing-routinginterface-returntoroutewithtraveleddistance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- returnToRouteWithTraveledDistance.html -->


<div>
<h1>returnToRouteWithTraveledDistance abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
returnToRouteWithTraveledDistance(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-routing-route-class">Route</a> route, </li>
<li><a href="/sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a> startingPoint, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li><a href="/sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback, </li>
</ol>)

      

    

<p>Asynchronously calculates a new route that leads back to the original route.</p>
<p>The part of
the original route which was already traveled by the user is ignored.</p>
<p><strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will
be ignored.
Additionally, the following route options are ignored:
<a href="/sdk-for-flutter-explore-routing-routeoptions-alternatives">RouteOptions.alternatives</a>, <a href="/sdk-for-flutter-explore-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a>, and
<a href="/sdk-for-flutter-explore-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a>.
Most route options are only applied to the newly calculated part back to the route.</p>
<p>An application may use this method to submit a new
starting point for a previously calculated route. This method tries to avoid a costly
route re-calculation as much as possible. In case returning to the route without
re-calculation is not possible, a new route is calculated, while trying to salvage
the previous route as much as possible. However, a completely new route
containing no part of the previous route is possible, too.</p>
<p>Note that this function uses only a limited amount of map data around the new origin.
Therefore, it may also work fine with temporarily cached map data. It may also copy some of the
original route data into the new route.</p>
<p>A typical use case is to await at least 3 <code>RouteDeviation</code> events before calling this method.</p>
<ul>
<li>Or alternatively, wait at least 10 seconds after getting the first deviation event.</li>
<li>On top, the user experience can be improved by checking if the vehicle has moved at least
50 meters since calling this method for the last time.</li>
<li>Optionally, it may make sense to verify if the vehicle was ever following the route by checking if
<code>RouteDeviation.lastLocationOnRoute</code> is set.</li>
</ul>
<p>Note that deviation events are sent each time a deviation is detected, i.e. for each new location
update, regardless if the location has changed or not.
More information can be found in the Developer Guide in the "Handle route deviations" section.</p>
<ul>
<li>
<p><code>route</code> A <a href="/sdk-for-flutter-explore-routing-route-class">Route</a> calculated using the online or offline route engine. For the offline case, It
should not contain an indoor <a href="/sdk-for-flutter-explore-routing-section-class">Section</a> as such routes will fail. For the online case, it
should have <a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>.</p>
</li>
<li>
<p><code>startingPoint</code> The current location, for example, provided by a <code>RouteDeviation</code> event. The waypoint needs to be of
type <a href="/sdk-for-flutter-explore-routing-waypointtype">WaypointType.stopover</a>. Otherwise, an <a href="/sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a>
error is generated.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle returnToRouteWithTraveledDistance(Route route, Waypoint startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
