---
title: "shadows property"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-shadows"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- shadows.html -->


<div>
<h1>shadows property</h1></div>

        
        String
        shadows
<div class="features">final</div>


<p>Shadows for all building types (extruded buildings and landmarks).</p>
<p>Supports only one mode: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-shadowsall">MapFeatureModes.shadowsAll</a>.</p>
<p>A <a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality</a> must be set on the MapContext through a MapView or the feature has no
effect.</p>
<p>Shadows have a performance impact and should be considered only for devices with
sufficient performance.</p>
<p>Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a>,
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a> and all hybrid schemes: <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.hybridDay</a>
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.hybridNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteHybridDay</a>
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteHybridNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsHybridDay</a> and
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsHybridNight</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
By default, this map feature is not enabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static final String shadows = "shadows";</code></pre>

 



</div>
`
}</HTMLBlock>
