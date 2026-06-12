---
title: "routeLabels property"
slug: "sdk-for-flutter-explore-routing-route-routelabels"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- routeLabels.html -->


<div>
<h1>routeLabels property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-explore-routing-routelabel-class">RouteLabel</a>&gt;
routeLabels


<p>A collection containing a maximum of 2 <code>RouteLabel</code> instances for the route. It will return an empty list if no labels are available.
The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes.
The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives
when alternative routes have been quested via <code>RouteOptions</code>.
Gets route labels.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;RouteLabel&gt; get routeLabels;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
