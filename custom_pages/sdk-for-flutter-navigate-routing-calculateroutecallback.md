---
title: "CalculateRouteCallback typedef"
slug: "sdk-for-flutter-navigate-routing-calculateroutecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CalculateRouteCallback.html -->


<div>
<h1>CalculateRouteCallback typedef</h1></div>

CalculateRouteCallback =
     void Function(<a href="/sdk-for-flutter-navigate-routing-routingerror">RoutingError</a>? routingError, List&lt;<a href="/sdk-for-flutter-navigate-routing-route-class">Route</a>&gt;? routeList)


<p>A function which is called by the RoutingEngine after route calculation has completed.</p>
<p>It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
The second argument is the calculated routes. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>routingError</code> The error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>routeList</code> The calculated routes. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef CalculateRouteCallback = void Function(RoutingError? routingError, List&lt;Route&gt;? routeList);</code></pre>

 



</div>
`
}</HTMLBlock>
