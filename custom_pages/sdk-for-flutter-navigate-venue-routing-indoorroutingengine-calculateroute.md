---
title: "calculateRoute abstract method"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutingengine-calculateroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateRoute.html -->


<div>
<h1>calculateRoute abstract method</h1></div>

void
calculateRoute(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class">IndoorWaypoint</a> from, </li>
<li><a href="sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class">IndoorWaypoint</a> to, </li>
<li><a href="sdk-for-flutter-navigate-venue-routing-indoorrouteoptions-class">IndoorRouteOptions</a> routeOptions, </li>
<li><a href="sdk-for-flutter-navigate-venue-routing-calculateindoorroutecallback">CalculateIndoorRouteCallback</a> callback, </li>
</ol>)

      

    

<p>Asynchronously calculates a route inside a venue.</p>
<ul>
<li>
<p><code>from</code> A starting position of the route to calculate.</p>
</li>
<li>
<p><code>to</code> A destination position of the route to calculate.</p>
</li>
<li>
<p><code>routeOptions</code> Options specific for indoor route calculation, along with
common route options.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void calculateRoute(IndoorWaypoint from, IndoorWaypoint to, IndoorRouteOptions routeOptions, CalculateIndoorRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
