---
title: "RefreshRouteOptions.withCarOptions constructor"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withcaroptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions.withCarOptions.html -->


<div>
<h1>RefreshRouteOptions.withCarOptions constructor</h1></div>

RefreshRouteOptions.withCarOptions(<ol class="parameter-list single-line"> <li><a class="deprecated" href="sdk-for-flutter-explore-routing-caroptions-class">CarOptions</a> carOptions</li>
</ol>)
    

<p>Constructs a RefreshRouteOptions object with <a class="deprecated" href="sdk-for-flutter-explore-routing-caroptions-class">CarOptions</a>.</p>
<ul>
<li><code>carOptions</code> Converts the route to a car route, if a different transport mode was used for the
<a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible,
an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteOptions.withCarOptions(CarOptions carOptions) =&gt; $prototype.withCarOptions(carOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
