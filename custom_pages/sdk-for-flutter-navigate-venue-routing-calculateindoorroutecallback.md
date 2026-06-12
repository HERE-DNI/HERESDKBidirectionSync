---
title: "CalculateIndoorRouteCallback typedef"
slug: "sdk-for-flutter-navigate-venue-routing-calculateindoorroutecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CalculateIndoorRouteCallback.html -->


<div>
<h1>CalculateIndoorRouteCallback typedef</h1></div>

CalculateIndoorRouteCallback =
     void Function(<a href="/sdk-for-flutter-navigate-venue-routing-indoorroutingerror">IndoorRoutingError</a>? indoorRoutingError, List&lt;<a href="/sdk-for-flutter-navigate-routing-route-class">Route</a>&gt;? routeList)


<p>A function which is called by the IndoorRoutingEngine after route calculation has completed.</p>
<p>It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
The second argument is the calculated routes. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>indoorRoutingError</code> The error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>routeList</code> The calculated routes. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef CalculateIndoorRouteCallback = void Function(IndoorRoutingError? indoorRoutingError, List&lt;Route&gt;? routeList);</code></pre>

 



</div>
`
}</HTMLBlock>
