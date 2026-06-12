---
title: "start abstract method"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->


<div>
<h1>start abstract method</h1></div>

void
start(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-routing-route-class">Route</a> route, </li>
<li><a href="/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a> listener</li>
</ol>)

      

    

<p>Starts polling the HERE backend services to find a better route,
as defined by the DynamicRoutingEngineOptions.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<ul>
<li>
<p><code>route</code> The route to be refreshed. The route must contain a <a href="/sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>,
therefore the route must have been requested with
<a href="/sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle">RouteOptions.enableRouteHandle</a> set to <code>true</code>.
The information to calculate new routes will be extracted from the provided route parameter.
If more information from the original waypoints is important besides their location,
consider to use one of the overloaded methods instead.</p>
</li>
<li>
<p><code>listener</code> The listener to receive the events.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class">DynamicRoutingEngineStartException</a>. when the passed parameter are invalid.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void start(Route route, DynamicRoutingListener listener);</code></pre>

 



</div>
`
}</HTMLBlock>
