---
title: "originalId property"
slug: "sdk-for-flutter-explore-traffic-trafficincident-originalid"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- originalId.html -->


<div>
<h1>originalId property</h1></div>
<section id="getter">

String
originalId


<p>The unique identifier of the first traffic incident.
The original id remains the same whenever the traffic incident is updated and <a href="/sdk-for-flutter-explore-traffic-trafficincident-id">TrafficIncident.id</a> is changed.
Once an incident chain has been created, this value will never change.
The traffic incident an be looked up by original id using <a href="/sdk-for-flutter-explore-traffic-trafficengine-lookupincident">TrafficEngine.lookupIncident</a>.
Gets the unique identifier of the first traffic incident.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String get originalId;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
