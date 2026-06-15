---
title: "refreshRouteWithRouteHandleAndRefreshRouteParameters abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-refreshroutewithroutehandleandrefreshrouteparameters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- refreshRouteWithRouteHandleAndRefreshRouteParameters.html -->


<div>
<h1>refreshRouteWithRouteHandleAndRefreshRouteParameters abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
refreshRouteWithRouteHandleAndRefreshRouteParameters(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-routing-refreshrouteparameters-class">RefreshRouteParameters</a> refreshRouteParameters, </li>
<li><a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a> routingOptions, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>, updating
the starting point and route metadata based on <a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a>.</p>
<p>The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated.</p>
<ul>
<li>
<p><code>refreshRouteParameters</code> The parameters used to refresh the route</p>
</li>
<li>
<p><code>routingOptions</code> The options define the vehicle and route options used to calculate the route.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after refreshing the route.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle refreshRouteWithRouteHandleAndRefreshRouteParameters(RefreshRouteParameters refreshRouteParameters, RoutingOptions routingOptions, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
