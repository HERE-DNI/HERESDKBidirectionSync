---
title: "calculateCarRoute abstract method"
slug: "sdk-for-flutter-navigate-routing-routinginterface-calculatecarroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateCarRoute.html -->


<div>
<h1>calculateCarRoute abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the calculate_route() methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
calculateCarRoute(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a>&gt; waypoints, </li>
<li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-caroptions-class">CarOptions</a> carOptions, </li>
<li><a href="/sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously calculates a car route from one point to another,
passing through the given waypoints in the given order.</p>
<ul>
<li><code>waypoints</code> The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</li>
</ul>
<p>An <a href="/sdk-for-flutter-navigate-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the waypoint list
contains less than two elements or when the first and the last waypoints are not of type
<a href="/sdk-for-flutter-navigate-routing-waypointtype">WaypointType.stopover</a>.</p>
<ul>
<li>
<p><code>carOptions</code> Options specific for car route calculation, along with
common route options.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the calculate_route() methods with RoutingOptions parameter instead.")

TaskHandle calculateCarRoute(List&lt;Waypoint&gt; waypoints, CarOptions carOptions, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
