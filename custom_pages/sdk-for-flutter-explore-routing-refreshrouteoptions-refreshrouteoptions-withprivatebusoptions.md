---
title: "RefreshRouteOptions.withPrivateBusOptions constructor"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withprivatebusoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions.withPrivateBusOptions.html -->


<div>
<h1>RefreshRouteOptions.withPrivateBusOptions constructor</h1></div>

RefreshRouteOptions.withPrivateBusOptions(<ol class="parameter-list single-line"> <li><a class="deprecated" href="/sdk-for-flutter-explore-routing-privatebusoptions-class">PrivateBusOptions</a> privateBusOptions</li>
</ol>)
    

<p>Constructs a RefreshRouteOptions object with <a class="deprecated" href="/sdk-for-flutter-explore-routing-privatebusoptions-class">PrivateBusOptions</a>.</p>
<ul>
<li><code>privateBusOptions</code> Converts the route to a private bus route, if a different transport mode was used for the
<a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible,
an <a href="/sdk-for-flutter-explore-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteOptions.withPrivateBusOptions(PrivateBusOptions privateBusOptions) =&gt; $prototype.withPrivateBusOptions(privateBusOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
