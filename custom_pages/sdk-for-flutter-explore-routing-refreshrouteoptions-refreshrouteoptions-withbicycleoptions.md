---
title: "RefreshRouteOptions.withBicycleOptions constructor"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withbicycleoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions.withBicycleOptions.html -->


<div>
<h1>RefreshRouteOptions.withBicycleOptions constructor</h1></div>

RefreshRouteOptions.withBicycleOptions(<ol class="parameter-list single-line"> <li><a class="deprecated" href="/sdk-for-flutter-explore-routing-bicycleoptions-class">BicycleOptions</a> bicycleOptions</li>
</ol>)
    

<p>Constructs a RefreshRouteOptions object with <a class="deprecated" href="/sdk-for-flutter-explore-routing-bicycleoptions-class">BicycleOptions</a>.</p>
<ul>
<li><code>bicycleOptions</code> Converts the route to a bicycle route, if a different transport mode was used for the
<a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible,
an <a href="/sdk-for-flutter-explore-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteOptions.withBicycleOptions(BicycleOptions bicycleOptions) =&gt; $prototype.withBicycleOptions(bicycleOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
