---
title: "CalculateIsolineCallback typedef"
slug: "sdk-for-flutter-explore-routing-calculateisolinecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CalculateIsolineCallback.html -->


<div>
<h1>CalculateIsolineCallback typedef</h1></div>

CalculateIsolineCallback =
     void Function(<a href="/sdk-for-flutter-explore-routing-routingerror">RoutingError</a>? routingError, List&lt;<a href="/sdk-for-flutter-explore-routing-isoline-class">Isoline</a>&gt;? isolines)


<p>A function which is called by the RoutingEngine after isoline calculation has completed.</p>
<p>It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
The second argument holds a list of calculated isolines. The list is <code>null</code> in case of an error.
The size of the list matches the size of the provided sdk.routing.IsolineOptions.range_values:
For each range limit, one isoline is calculated.</p>
<ul>
<li>
<p><code>routingError</code> The error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>isolines</code> Holds a list of calculated isolines. The list is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef CalculateIsolineCallback = void Function(RoutingError? routingError, List&lt;Isoline&gt;? isolines);</code></pre>

 



</div>
`
}</HTMLBlock>
