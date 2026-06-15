---
title: "trafficFlow property"
slug: "sdk-for-flutter-explore-mapview-mapfeatures-trafficflow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficFlow.html -->


<div>
<h1>trafficFlow property</h1></div>

        
        String
        trafficFlow
<div class="features">final</div>


<p>Traffic flow speed. An online connection is required for the traffic
flow to be shown.</p>
<p>If the offline-mode is enabled for offline maps usage,
the live traffic flow can still be shown in offline mode by enabling
pass-through feature for traffic flow on <code>sdk.core.engine.SDKNativeEngine</code>.
See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.</p>
<p>Supported modes:</p>
<ul>
<li><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficflowjapanwithoutfreeflow">MapFeatureModes.trafficFlowJapanWithoutFreeFlow</a>,</li>
<li><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficflowwithfreeflow">MapFeatureModes.trafficFlowWithFreeFlow</a>,</li>
<li><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficflowwithoutfreeflow">MapFeatureModes.trafficFlowWithoutFreeFlow</a>.</li>
</ul>
<p>Default mode is <a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficflowwithfreeflow">MapFeatureModes.trafficFlowWithFreeFlow</a>.</p>
<p>Not supported for <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkDay</a>
and <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkNight</a>.
By default, this map feature is not enabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static final String trafficFlow = "traffic flow";</code></pre>

 



</div>
`
}</HTMLBlock>
