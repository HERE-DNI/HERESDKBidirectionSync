---
title: "calculateRoute abstract method"
slug: "sdk-for-flutter-explore-routing-transitroutingengine-calculateroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateRoute.html -->


<div>
<h1>calculateRoute abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
calculateRoute(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-routing-transitwaypoint-class">TransitWaypoint</a> startingPoint, </li>
<li><a href="/sdk-for-flutter-explore-routing-transitwaypoint-class">TransitWaypoint</a> destination, </li>
<li><a href="/sdk-for-flutter-explore-routing-transitrouteoptions-class">TransitRouteOptions</a> routeOptions, </li>
<li><a href="/sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback, </li>
</ol>)

      

    

<p>Asynchronously calculates a public transit route from the origin to the destination.</p>
<ul>
<li>
<p><code>startingPoint</code> Position of starting point.</p>
</li>
<li>
<p><code>destination</code> Position of destination.</p>
</li>
<li>
<p><code>routeOptions</code> Options for public transit route calculation.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateRoute(TransitWaypoint startingPoint, TransitWaypoint destination, TransitRouteOptions routeOptions, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
