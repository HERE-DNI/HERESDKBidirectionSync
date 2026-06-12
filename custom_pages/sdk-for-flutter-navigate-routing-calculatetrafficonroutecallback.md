---
title: "CalculateTrafficOnRouteCallback typedef"
slug: "sdk-for-flutter-navigate-routing-calculatetrafficonroutecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CalculateTrafficOnRouteCallback.html -->


<div>
<h1>CalculateTrafficOnRouteCallback typedef</h1></div>

CalculateTrafficOnRouteCallback =
     void Function(<a href="/sdk-for-flutter-navigate-routing-routingerror">RoutingError</a>? routingError, <a href="/sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>? trafficOnRoute)


<p>A function which is called by the RoutingEngine after route traffic calculation has completed.</p>
<p>It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
The second argument is the calculated route traffic. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>routingError</code> The error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>trafficOnRoute</code> The calculated route traffic. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef CalculateTrafficOnRouteCallback = void Function(RoutingError? routingError, TrafficOnRoute? trafficOnRoute);</code></pre>

 



</div>
`
}</HTMLBlock>
