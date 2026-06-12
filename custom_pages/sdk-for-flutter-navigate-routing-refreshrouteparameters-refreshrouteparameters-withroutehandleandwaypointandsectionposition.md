---
title: "RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition constructor"
slug: "sdk-for-flutter-navigate-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypointandsectionposition"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition.html -->


<div>
<h1>RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition constructor</h1></div>

RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> routeHandle, </li>
<li><a href="/sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a> startingPoint, </li>
<li>int startingSectionIndex, </li>
<li>int traveledDistanceOnStartingSectionInMeters, </li>
</ol>)
    

<p>Create a new instance of <a href="/sdk-for-flutter-navigate-routing-refreshrouteparameters-class">RefreshRouteParameters</a> with the new starting point and the section position on the route.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle holding the route to be refreshed.</p>
</li>
<li>
<p><code>startingPoint</code> Identify the new starting point of the route.</p>
</li>
<li>
<p><code>startingSectionIndex</code> Indicates the index of the last traveled route section.</p>
</li>
<li>
<p><code>traveledDistanceOnStartingSectionInMeters</code> Provides an indication on how much of the starting section is already traveled.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition(RouteHandle routeHandle, Waypoint startingPoint, int startingSectionIndex, int traveledDistanceOnStartingSectionInMeters) =&gt; $prototype.withRouteHandleAndWaypointAndSectionPosition(routeHandle, startingPoint, startingSectionIndex, traveledDistanceOnStartingSectionInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
