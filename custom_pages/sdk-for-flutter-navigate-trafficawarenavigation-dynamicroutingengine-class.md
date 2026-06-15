---
title: "DynamicRoutingEngine class abstract"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DynamicRoutingEngine-class.html -->


<div>
<h1>DynamicRoutingEngine class abstract</h1></div>

<p>This class queries the HERE routing backend
to find routes with less traffic and therefore an earlier remaining estimated time of arrival.</p>
<p><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a> polls the HERE routing backend periodically to find the best new route out
of a given initial route.
For initial route calculation it is recommended to use the <a href="sdk-for-flutter-navigate-routing-routingengine-class">RoutingEngine</a>
as it already requests traffic-optimized routes.</p>
<p>When a better route is found, it is recommended to follow these steps to set the new route:</p>
<ol>
<li>Stop the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>.</li>
<li>Update the currently active <code>Navigator</code>instance with the newly found route.</li>
<li>Restart the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>. This should be done outside of the <code>onBetterRouteFound()</code> callback.</li>
</ol>
<p>For both <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a> and <a href="sdk-for-flutter-navigate-routing-routingengine-class">RoutingEngine</a>,
the resulting routes are optimized based on speed flow changes such as traffic jams,
street closures or road accidents.
To get the best result, it is recommended to not specify the
<a href="sdk-for-flutter-navigate-routing-routeoptions-departuretime">RouteOptions.departureTime</a> as then the current time is used by default.</p>
<p>The poll interval is defined by
<a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval">DynamicRoutingEngineOptions.pollInterval</a> and
triggered by <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation">DynamicRoutingEngine.updateCurrentLocation</a>.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-dynamicroutingengine">DynamicRoutingEngine</a></li><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-dynamicroutingengine-withsdkengine">DynamicRoutingEngine.withSdkEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-start">start</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypoints">startWithWaypoints</a></li><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypointsandroutingoptions">startWithWaypointsAndRoutingOptions</a></li><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-stop">stop</a></li><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-tostring">toString</a></li><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation">updateCurrentLocation</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
