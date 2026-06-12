---
title: "calculateTrafficOnRoute abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTrafficOnRoute.html -->


<div>
<h1>calculateTrafficOnRoute abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
calculateTrafficOnRoute(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-routing-route-class">Route</a> route, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li><a href="/sdk-for-flutter-explore-routing-calculatetrafficonroutecallback">CalculateTrafficOnRouteCallback</a> callback, </li>
</ol>)

      

    

<p>Asynchronously calculates the traffic along a route starting from the index of the last
traveled route section and an offset (in meters) from the last visited position on the
section.</p>
<p>Call this when only the contained traffic information or the latest ETA duration
is needed. This can be called periodically to retrieve updated ETA values during navigation.</p>
<p><strong>Note:</strong> Calling this method will trigger a new "HERE Traffic" transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
<ul>
<li>
<p><code>route</code> A <a href="/sdk-for-flutter-explore-routing-route-class">Route</a> calculated using the online routing engine. Its
<a href="/sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> and the original route calculation options will be used to
compute the traffic on the route. The original route remains untouched.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't
be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset, in meters, to the last visited position on the route section defined by the last
traveled section index.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route traffic has been calculated.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateTrafficOnRoute(Route route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, CalculateTrafficOnRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
