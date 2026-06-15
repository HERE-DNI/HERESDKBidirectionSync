---
title: "importRouteWithRoutingOptions abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-importroutewithroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importRouteWithRoutingOptions.html -->


<div>
<h1>importRouteWithRoutingOptions abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
importRouteWithRoutingOptions(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-core-location-class">Location</a>&gt; locations, </li>
<li><a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a> options, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously creates a route from a sequence of geographic coordinates very close to each other.</p>
<p>The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <a href="sdk-for-flutter-explore-routing-section-sectionnotices">Section.sectionNotices</a>.</p>
<ul>
<li><code>locations</code> The list of locations used to calculate the route. Note that only the <a href="sdk-for-flutter-explore-core-location-coordinates">Location.coordinates</a> of a location are used to import the route.</li>
</ul>
<p>An <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the location list
size is not in the range [2,50000].</p>
<ul>
<li>
<p><code>options</code> The options define the vehicle and route options to calculate the route.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle importRouteWithRoutingOptions(List&lt;Location&gt; locations, RoutingOptions options, CalculateRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
