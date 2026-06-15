---
title: "trafficIncidents property"
slug: "sdk-for-flutter-explore-mapview-mapfeatures-trafficincidents"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficIncidents.html -->


<div>
<h1>trafficIncidents property</h1></div>

        
        String
        trafficIncidents
<div class="features">final</div>


<p>Traffic incidents. An online connection is required for the traffic
incidents to be shown.</p>
<p>If the offline-mode is enabled for offline maps usage,
the live traffic incidents can still be shown in offline mode by enabling
pass-through feature for traffic incidents on <code>sdk.core.engine.SDKNativeEngine</code>.
See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.</p>
<p>Supports only one mode: <a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficincidentsall">MapFeatureModes.trafficIncidentsAll</a>.</p>
<p>Not supported for <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkDay</a>
and <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkNight</a>.
By default, this map feature is not enabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static final String trafficIncidents = "traffic incidents";</code></pre>

 



</div>
`
}</HTMLBlock>
