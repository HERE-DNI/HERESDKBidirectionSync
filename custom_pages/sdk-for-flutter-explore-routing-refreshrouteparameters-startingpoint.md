---
title: "startingPoint property"
slug: "sdk-for-flutter-explore-routing-refreshrouteparameters-startingpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startingPoint.html -->


<div>
<h1>startingPoint property</h1></div>

<a href="/sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>?
        startingPoint
<div class="features">getter/setter pair</div>


<p>Identify the new starting point of the route. It should be of type <a href="/sdk-for-flutter-explore-routing-waypointtype">WaypointType.stopover</a>.
Otherwise, an <a href="/sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated. Moreover, it should be very close to the
original route specified with the <a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. The location of this waypoint may by provided,
for example, by a <code>RouteProgress</code> event. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <a href="/sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a> items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, <a href="/sdk-for-flutter-explore-routing-route-lengthinmeters">Route.lengthInMeters</a>, <a href="/sdk-for-flutter-explore-routing-route-duration">Route.duration</a>, and similar
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <a href="/sdk-for-flutter-explore-routing-routingerror">RoutingError.couldNotMatchOrigin</a> error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Waypoint? startingPoint;</code></pre>

 



</div>
`
}</HTMLBlock>
