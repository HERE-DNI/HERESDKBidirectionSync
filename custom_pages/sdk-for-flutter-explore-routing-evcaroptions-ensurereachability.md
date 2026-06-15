---
title: "ensureReachability property"
slug: "sdk-for-flutter-explore-routing-evcaroptions-ensurereachability"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ensureReachability.html -->


<div>
<h1>ensureReachability property</h1></div>

        
        bool
        ensureReachability
<div class="features">getter/setter pair</div>


<p>Ensure that the vehicle does not run out of energy along the way.
Requires valid <a href="sdk-for-flutter-explore-routing-evcaroptions-batteryspecifications">EVCarOptions.batterySpecifications</a>.
It also requires that
<a href="sdk-for-flutter-explore-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a> = <a href="sdk-for-flutter-explore-routing-optimizationmode">OptimizationMode.fastest</a>,
<a href="sdk-for-flutter-explore-routing-routeoptions-speedcapinmeterspersecond">RouteOptions.speedCapInMetersPerSecond</a> is not set, and
<a href="sdk-for-flutter-explore-routing-avoidanceoptions-class">AvoidanceOptions</a> is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.
<strong>Note</strong> An <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> is generated when
the <code>sdk.routing.EVCarOptions.ensure_reachability</code> is set to <code>true</code> in case <code>sdk.routing.RoutingEngine.import_route</code> is called.
Defaults to <code>false</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool ensureReachability;</code></pre>

 



</div>
`
}</HTMLBlock>
