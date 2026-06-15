---
title: "speedCapInMetersPerSecond property"
slug: "sdk-for-flutter-navigate-routing-routeoptions-speedcapinmeterspersecond"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- speedCapInMetersPerSecond.html -->


<div>
<h1>speedCapInMetersPerSecond property</h1></div>

        
        double?
        speedCapInMetersPerSecond
<div class="features">getter/setter pair</div>


<p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>,
<a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a> and <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.scooter</a> transport modes.
For car, truck and scooter transport modes, it will affect <a href="sdk-for-flutter-navigate-routing-route-duration">Route.duration</a> of
the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
which means that no speed cap is set.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? speedCapInMetersPerSecond;</code></pre>

 



</div>
`
}</HTMLBlock>
