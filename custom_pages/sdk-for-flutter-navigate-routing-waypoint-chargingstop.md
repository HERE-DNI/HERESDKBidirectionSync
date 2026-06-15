---
title: "chargingStop property"
slug: "sdk-for-flutter-navigate-routing-waypoint-chargingstop"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- chargingStop.html -->


<div>
<h1>chargingStop property</h1></div>

<a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>?
        chargingStop
<div class="features">getter/setter pair</div>


<p>Specifies of a user-planned charging stop.
The resulting <code>Route</code> may contain this waypoint as a <code>RoutePlace</code> with a non-null <code>ChargingStation</code> member
when the provided specifications indicate that a stop is required to charge the EV battery.
<strong>Note:</strong>
If <code>EVCarOptions.ensure_reachability</code> is not set as <code>true</code> and <code>ChargingStop.min_duration</code> is not provided,
route calculation may suggest a better charging stop instead of this stop.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStop? chargingStop;</code></pre>

 



</div>
`
}</HTMLBlock>
