---
title: "optimizeWaypointsOrder property"
slug: "sdk-for-flutter-navigate-routing-routeoptions-optimizewaypointsorder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- optimizeWaypointsOrder.html -->


<div>
<h1>optimizeWaypointsOrder property</h1></div>

        
        bool
        optimizeWaypointsOrder
<div class="features">getter/setter pair</div>


<p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="/sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a>.
The starting and destination <a href="/sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a> are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see <a href="/sdk-for-flutter-navigate-routing-route-sections">Route.sections</a>, <a href="/sdk-for-flutter-navigate-routing-section-departureplace">Section.departurePlace</a>, <a href="/sdk-for-flutter-navigate-routing-section-arrivalplace">Section.arrivalPlace</a>, <a href="/sdk-for-flutter-navigate-routing-routeplace-waypointindex">RoutePlace.waypointIndex</a>).
Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
Defaults to <code>false</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool optimizeWaypointsOrder;</code></pre>

 



</div>
`
}</HTMLBlock>
