---
title: "importPedestrianRouteWithStops abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-importpedestrianroutewithstops"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importPedestrianRouteWithStops.html -->


<div>
<h1>importPedestrianRouteWithStops abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the import_route() methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
importPedestrianRouteWithStops(<ol class="parameter-list"> <li>List&lt;<a href="sdk-for-flutter-explore-core-location-class">Location</a>&gt; locations, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-routing-routestop-class">RouteStop</a>&gt; routeStops, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-pedestrianoptions-class">PedestrianOptions</a> pedestrianOptions, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback, </li>
</ol>)

      

    

<p>Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other.</p>
<p>The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <a href="sdk-for-flutter-explore-routing-section-sectionnotices">Section.sectionNotices</a> .</p>
<ul>
<li><code>locations</code> The list of locations used to calculate the route. Note that only the <a href="sdk-for-flutter-explore-core-location-coordinates">Location.coordinates</a> of a location are used to import the route.</li>
</ul>
<p>An <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the location list
size is not in the range [2,50000].</p>
<ul>
<li><code>routeStops</code> The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.</li>
</ul>
<p>An <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the route stops list
size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p>
<ul>
<li>
<p><code>pedestrianOptions</code> Options specific for pedestrian route calculation, along with
common route options. Note that <a href="sdk-for-flutter-explore-routing-optimizationmode">OptimizationMode.shortest</a>
is not supported for pedestrians and converted to
<a href="sdk-for-flutter-explore-routing-optimizationmode">OptimizationMode.fastest</a> automatically.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the import_route() methods with RoutingOptions parameter instead.")

TaskHandle importPedestrianRouteWithStops(List&lt;Location&gt; locations, List&lt;RouteStop&gt; routeStops, PedestrianOptions pedestrianOptions, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
