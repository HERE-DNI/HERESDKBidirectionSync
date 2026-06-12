---
title: "startWithWaypointsAndRoutingOptions abstract method"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypointsandroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithWaypointsAndRoutingOptions.html -->


<div>
<h1>startWithWaypointsAndRoutingOptions abstract method</h1></div>

void
startWithWaypointsAndRoutingOptions(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> routeHandle, </li>
<li>List&lt;<a href="/sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a>&gt; waypoints, </li>
<li><a href="/sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a> routingOptions, </li>
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
<p><code>routingOptions</code> The options for the route calculation.</p>
</li>
<li>
<p><code>listener</code> The listener to receive the events.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class">DynamicRoutingEngineStartException</a>. when the passed parameter are invalid.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startWithWaypointsAndRoutingOptions(RouteHandle routeHandle, List&lt;Waypoint&gt; waypoints, RoutingOptions routingOptions, DynamicRoutingListener listener);</code></pre>

 



</div>
`
}</HTMLBlock>
