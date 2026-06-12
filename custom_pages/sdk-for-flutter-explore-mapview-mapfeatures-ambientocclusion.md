---
title: "ambientOcclusion property"
slug: "sdk-for-flutter-explore-mapview-mapfeatures-ambientocclusion"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ambientOcclusion.html -->


<div>
<h1>ambientOcclusion property</h1></div>

        
        String
        ambientOcclusion
<div class="features">final</div>


<p>Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).</p>
<p>Supports only one mode: <a href="/sdk-for-flutter-explore-mapview-mapfeaturemodes-ambientocclusionall">MapFeatureModes.ambientOcclusionAll</a>.</p>
<p>This visual effect has a performance impact and should be considered only for devices with
sufficient performance.</p>
<p>Not supported for <a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.satellite</a>, <a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkDay</a>,
<a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkNight</a> and all hybrid schemes: <a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.hybridDay</a>
<a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.hybridNight</a>, <a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.liteHybridDay</a>
<a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.liteHybridNight</a>, <a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.logisticsHybridDay</a> and
<a href="/sdk-for-flutter-explore-mapview-mapscheme">MapScheme.logisticsHybridNight</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
By default, this map feature is not enabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static final String ambientOcclusion = "ambient occlusion";</code></pre>

 



</div>
`
}</HTMLBlock>
