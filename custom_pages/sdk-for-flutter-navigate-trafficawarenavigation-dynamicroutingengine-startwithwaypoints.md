---
title: "startWithWaypoints abstract method"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithWaypoints.html -->


<div>
<h1>startWithWaypoints abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the start() method with RoutingOptions parameter instead.")</li>
</ol>
</div>
void
startWithWaypoints(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> routeHandle, </li>
<li>List&lt;<a href="/sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a>&gt; waypoints, </li>
<li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-refreshrouteoptions-class">RefreshRouteOptions</a> refreshRouteOptions, </li>
<li><a href="/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a> listener, </li>
</ol>)

      

    

<p>Starts polling the HERE backend services to find a better route,
as defined by the <a href="/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle from the HERE routing backend.</p>
</li>
<li>
<p><code>waypoints</code> Allows to specify detailed information on the waypoints of the route.
This parameter can be useful, when additional information needs to be
specified besides the coordinates - as the coordinates can be retrieved
from the contained <a href="/sdk-for-flutter-navigate-routing-routeplace-class">RoutePlace</a> that are already contained in
the <a href="/sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> parameter.</p>
</li>
<li>
<p><code>refreshRouteOptions</code> The options for the route calculation.</p>
</li>
<li>
<p><code>listener</code> The listener to receive the events.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class">DynamicRoutingEngineStartException</a>. when the passed parameter are invalid.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the start() method with RoutingOptions parameter instead.")

void startWithWaypoints(RouteHandle routeHandle, List&lt;Waypoint&gt; waypoints, RefreshRouteOptions refreshRouteOptions, DynamicRoutingListener listener);</code></pre>

 



</div>
`
}</HTMLBlock>
