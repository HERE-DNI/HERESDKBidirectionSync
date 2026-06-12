---
title: "onBetterRouteFound abstract method"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-onbetterroutefound"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onBetterRouteFound.html -->


<div>
<h1>onBetterRouteFound abstract method</h1></div>

void
onBetterRouteFound(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-routing-route-class">Route</a> newRoute, </li>
<li>int etaDifferenceInSeconds, </li>
<li>int distanceDifferenceInMeters</li>
</ol>)

      

    

<p>This event is issued when a better route could be found,
as defined by <a href="/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>.</p>
<p>To find a better route, two routes are calculated.
The updated current route: A route that is calculated via the route specified.
The dynamic route: A route that starts at the current position on the route specified
and passes through the remaining waypoints.</p>
<ul>
<li>
<p><code>newRoute</code> The newly calculated route with the remaining waypoints starting from the
current location.</p>
</li>
<li>
<p><code>etaDifferenceInSeconds</code> The difference in seconds:
eta of the current updated route - eta of the dynamic route.</p>
</li>
<li>
<p><code>distanceDifferenceInMeters</code> The difference in meters:
distance of the current updated route - distance of the dynamic route.
The value can be negative in case the current updated route has
a shorter distance, but its now assumed to be longer than the dynamic route.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onBetterRouteFound(Route newRoute, int etaDifferenceInSeconds, int distanceDifferenceInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
