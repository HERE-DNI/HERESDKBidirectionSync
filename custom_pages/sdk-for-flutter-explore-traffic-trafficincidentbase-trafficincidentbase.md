---
title: "TrafficIncidentBase constructor"
slug: "sdk-for-flutter-explore-traffic-trafficincidentbase-trafficincidentbase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentBase.html -->


<div>
<h1>TrafficIncidentBase constructor</h1></div>

TrafficIncidentBase(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-traffic-trafficincidentimpact">TrafficIncidentImpact</a> impactGetLambda(), </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType</a> typeGetLambda(), </li>
<li><a href="sdk-for-flutter-explore-core-localizedtext-class">LocalizedText</a> descriptionGetLambda(), </li>
<li>DateTime? startTimeGetLambda(), </li>
<li>DateTime? endTimeGetLambda(), </li>
</ol>)
    

<p>TrafficIncident provides details about a traffic incident.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TrafficIncidentBase(
  TrafficIncidentImpact Function() impactGetLambda,
  TrafficIncidentType Function() typeGetLambda,
  LocalizedText Function() descriptionGetLambda,
  DateTime? Function() startTimeGetLambda,
  DateTime? Function() endTimeGetLambda
) =&gt; TrafficIncidentBase$Lambdas(
  impactGetLambda,
  typeGetLambda,
  descriptionGetLambda,
  startTimeGetLambda,
  endTimeGetLambda
);</code></pre>

 



</div>
`
}</HTMLBlock>
