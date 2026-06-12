---
title: "arrivalTime property"
slug: "sdk-for-flutter-navigate-routing-routeoptions-arrivaltime"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- arrivalTime.html -->


<div>
<h1>arrivalTime property</h1></div>

        
        DateTime?
        arrivalTime
<div class="features">getter/setter pair</div>


<p>Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <a href="/sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode">RouteOptions.trafficOptimizationMode</a>.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.</p>
<p><strong>Note</strong>:</p>
<ul>
<li>Both <a href="/sdk-for-flutter-navigate-routing-routeoptions-departuretime">RouteOptions.departureTime</a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">DateTime? arrivalTime;</code></pre>

 



</div>
`
}</HTMLBlock>
