---
title: "RefreshRouteOptions.withBusOptions constructor"
slug: "sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withbusoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions.withBusOptions.html -->


<div>
<h1>RefreshRouteOptions.withBusOptions constructor</h1></div>

RefreshRouteOptions.withBusOptions(<ol class="parameter-list single-line"> <li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-busoptions-class">BusOptions</a> busOptions</li>
</ol>)
    

<p>Constructs a RefreshRouteOptions object with <a class="deprecated" href="/sdk-for-flutter-navigate-routing-busoptions-class">BusOptions</a>.</p>
<ul>
<li><code>busOptions</code> Converts the route to a bus route, if a different transport mode was used for the
<a href="/sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible,
an <a href="/sdk-for-flutter-navigate-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteOptions.withBusOptions(BusOptions busOptions) =&gt; $prototype.withBusOptions(busOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
