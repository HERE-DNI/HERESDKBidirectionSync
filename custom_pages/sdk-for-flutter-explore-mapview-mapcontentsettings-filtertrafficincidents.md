---
title: "filterTrafficIncidents static method"
slug: "sdk-for-flutter-explore-mapview-mapcontentsettings-filtertrafficincidents"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- filterTrafficIncidents.html -->


<div>
<h1>filterTrafficIncidents static method</h1></div>

void
filterTrafficIncidents(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType</a>&gt; trafficIncidents</li>
</ol>)

      

    

<p>Filters the displayed traffic incidents so that only the ones applicable to the specified
criteria are shown when general display of traffic incidents is enabled.</p>
<p>The display of traffic incidents can be enabled using <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> with
<a href="sdk-for-flutter-explore-mapview-mapfeatures-trafficincidents">MapFeatures.trafficIncidents</a>.</p>
<ul>
<li><code>trafficIncidents</code> The traffic incidents to filter for, so that only applicable incidents are displayed.
When the list is empty, then all traffic incidents will be displayed.
If the <code>MapContentSettings.filterTrafficIncidents.trafficIncidents</code> contains <a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType.unknown</a>, then the
traffic filter will be applied ignoring this element.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void filterTrafficIncidents(List&lt;TrafficIncidentType&gt; trafficIncidents) =&gt; $prototype.filterTrafficIncidents(trafficIncidents);</code></pre>

 



</div>
`
}</HTMLBlock>
