---
title: "RefreshRouteParameters.withRouteHandleAndSectionPosition constructor"
slug: "sdk-for-flutter-explore-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandsectionposition"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteParameters.withRouteHandleAndSectionPosition.html -->


<div>
<h1>RefreshRouteParameters.withRouteHandleAndSectionPosition constructor</h1></div>

RefreshRouteParameters.withRouteHandleAndSectionPosition(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> routeHandle, </li>
<li>int startingSectionIndex, </li>
<li>int traveledDistanceOnStartingSectionInMeters</li>
</ol>)
    

<p>Create a new instance of <a href="/sdk-for-flutter-explore-routing-refreshrouteparameters-class">RefreshRouteParameters</a> with the point on the section of the route as a new starting point.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle holding the route to be refreshed.</p>
</li>
<li>
<p><code>startingSectionIndex</code> Indicates the index of the last traveled route section.</p>
</li>
<li>
<p><code>traveledDistanceOnStartingSectionInMeters</code> Provides an indication on how much of the starting section is already traveled.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteParameters.withRouteHandleAndSectionPosition(RouteHandle routeHandle, int startingSectionIndex, int traveledDistanceOnStartingSectionInMeters) =&gt; $prototype.withRouteHandleAndSectionPosition(routeHandle, startingSectionIndex, traveledDistanceOnStartingSectionInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
