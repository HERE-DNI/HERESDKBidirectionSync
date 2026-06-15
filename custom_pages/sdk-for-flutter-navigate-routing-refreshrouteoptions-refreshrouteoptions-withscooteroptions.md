---
title: "RefreshRouteOptions.withScooterOptions constructor"
slug: "sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withscooteroptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions.withScooterOptions.html -->


<div>
<h1>RefreshRouteOptions.withScooterOptions constructor</h1></div>

RefreshRouteOptions.withScooterOptions(<ol class="parameter-list single-line"> <li><a class="deprecated" href="sdk-for-flutter-navigate-routing-scooteroptions-class">ScooterOptions</a> scooterOptions</li>
</ol>)
    

<p>Constructs a RefreshRouteOptions object with <a class="deprecated" href="sdk-for-flutter-navigate-routing-scooteroptions-class">ScooterOptions</a>.</p>
<ul>
<li><code>scooterOptions</code> Converts the route to a scooter route, if a different transport mode was used for the
<a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible,
an <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteOptions.withScooterOptions(ScooterOptions scooterOptions) =&gt; $prototype.withScooterOptions(scooterOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
