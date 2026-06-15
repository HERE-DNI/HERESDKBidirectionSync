---
title: "RefreshRouteOptions.withEVCarOptions constructor"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withevcaroptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions.withEVCarOptions.html -->


<div>
<h1>RefreshRouteOptions.withEVCarOptions constructor</h1></div>

RefreshRouteOptions.withEVCarOptions(<ol class="parameter-list single-line"> <li><a class="deprecated" href="sdk-for-flutter-explore-routing-evcaroptions-class">EVCarOptions</a> evCarOptions</li>
</ol>)
    

<p>Constructs a RefreshRouteOptions object with <a class="deprecated" href="sdk-for-flutter-explore-routing-evcaroptions-class">EVCarOptions</a>.</p>
<ul>
<li><code>evCarOptions</code> Converts the route to an electric car route, if a different transport mode was used for the
<a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible,
an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RefreshRouteOptions.withEVCarOptions(EVCarOptions evCarOptions) =&gt; $prototype.withEVCarOptions(evCarOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
