---
title: "RefreshRouteOptions.withTaxiOptions constructor"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtaxioptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions.withTaxiOptions.html -->


<div>
<h1>RefreshRouteOptions.withTaxiOptions constructor</h1></div>

RefreshRouteOptions.withTaxiOptions(<ol class="parameter-list single-line"> <li><a class="deprecated" href="sdk-for-flutter-explore-routing-taxioptions-class">TaxiOptions</a> taxiOptions</li>
</ol>)
    

<p>Constructs a RefreshRouteOptions object with <a class="deprecated" href="sdk-for-flutter-explore-routing-taxioptions-class">TaxiOptions</a>.</p>
<ul>
<li><code>taxiOptions</code> Converts the route to a taxi route, if a different transport mode was used for the
<a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible,
an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteOptions.withTaxiOptions(TaxiOptions taxiOptions) =&gt; $prototype.withTaxiOptions(taxiOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
