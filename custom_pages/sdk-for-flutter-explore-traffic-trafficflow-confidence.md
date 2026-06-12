---
title: "confidence property"
slug: "sdk-for-flutter-explore-traffic-trafficflow-confidence"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confidence.html -->


<div>
<h1>confidence property</h1></div>
<section id="getter">

double?
confidence


<p>The confidence field indicates the proportion of real-time data included in the speed calculation.
It is a normalized value between 0.0 and 1.0 with the following meaning:</p>
<ul>
<li>0.7 &lt; confidence &lt;= 1.0 indicates real time speeds</li>
<li>0.5 &lt; confidence &lt;= 0.7 indicates historical speeds</li>
<li>0.0 &lt; confidence &lt;= 0.5 indicates speed limit</li>
</ul>
<p>This field can be used to identify whether the data for a location is derived from
real-time probe sources or historical information only.
All confidence data 0.71 and above is based on real-time information,
where a confidence value of 0.75 or greater indicates high confidence real-time information.
A confidence value equal to 0.70 or lower means that the data is derived from historical data only.
Gets the confidence field value which is normalized value between 0.0 and 1.0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? get confidence;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
