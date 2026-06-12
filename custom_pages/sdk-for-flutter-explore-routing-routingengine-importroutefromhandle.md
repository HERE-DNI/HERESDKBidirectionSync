---
title: "importRouteFromHandle abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-importroutefromhandle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importRouteFromHandle.html -->


<div>
<h1>importRouteFromHandle abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the import_route() methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
importRouteFromHandle(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> routeHandle, </li>
<li><a class="deprecated" href="/sdk-for-flutter-explore-routing-refreshrouteoptions-class">RefreshRouteOptions</a> refreshRouteOptions, </li>
<li><a href="/sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously recreates a route from the <a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> provided, i.e.</p>
<p>refreshes a previously
calculated route, with the specified <a class="deprecated" href="/sdk-for-flutter-explore-routing-refreshrouteoptions-class">RefreshRouteOptions</a>.</p>
<p>A route handle can be invalid when the map data changes that is used by the HERE backend to recreate the route. This happens regularly.
Therefore, the route handle is not meant to be persisted for a longer time. Instead, a possible use case can be to plan a route with another HERE service.
For example, a HERE REST API that allows to calculate a route on a desktop. Then this route can be transferred via the handle to a mobile device for further use with the HERE SDK.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle holding the route to be refreshed.</p>
</li>
<li>
<p><code>refreshRouteOptions</code> The options define the vehicle and route options to calculate the route.
<strong>Note</strong> An <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> is generated when the <code>sdk.routing.ElectricVehicleOptions.ensure_reachability</code> option is set to <code>true</code>.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after refreshing the route.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the import_route() methods with RoutingOptions parameter instead.")

TaskHandle importRouteFromHandle(RouteHandle routeHandle, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
