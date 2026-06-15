---
title: "departureTime property"
slug: "sdk-for-flutter-explore-routing-routeoptions-departuretime"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- departureTime.html -->


<div>
<h1>departureTime property</h1></div>

        
        DateTime?
        departureTime
<div class="features">getter/setter pair</div>


<p>Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode">RouteOptions.trafficOptimizationMode</a>.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.</p>
<p><strong>Note</strong>:</p>
<ul>
<li>Both departure time and <a href="sdk-for-flutter-explore-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">DateTime? departureTime;</code></pre>

 



</div>
`
}</HTMLBlock>
