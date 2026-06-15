---
title: "calculateEVTruckRoute abstract method"
slug: "sdk-for-flutter-explore-routing-routinginterface-calculateevtruckroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateEVTruckRoute.html -->


<div>
<h1>calculateEVTruckRoute abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the calculate_route() methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
calculateEVTruckRoute(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt; waypoints, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-evtruckoptions-class">EVTruckOptions</a> evTruckOptions, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously calculates an electic truck route from one point to another,
passing through the given waypoints in the given order.</p>
<ul>
<li><code>waypoints</code> The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</li>
</ul>
<p>An <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the waypoint list
contains less than two elements or when the first and the last waypoints are not of type
<a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType.stopover</a>.</p>
<ul>
<li>
<p><code>evTruckOptions</code> Options specific for an electric truck route calculation, along with
common route options.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the calculate_route() methods with RoutingOptions parameter instead.")

TaskHandle calculateEVTruckRoute(List&lt;Waypoint&gt; waypoints, EVTruckOptions evTruckOptions, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
