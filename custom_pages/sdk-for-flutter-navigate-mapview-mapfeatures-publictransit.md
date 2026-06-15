---
title: "publicTransit property"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-publictransit"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- publicTransit.html -->


<div>
<h1>publicTransit property</h1></div>

        
        String
        publicTransit
<div class="features">final</div>


<p>Toggles the display of public transit lines for systems like subway, tram, train, monorail,
and ferry, based on the selected mode.</p>
<p>Supported modes: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitall">MapFeatureModes.publicTransitAll</a>, <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia">MapFeatureModes.publicTransitAsia</a>.</p>
<p><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia">MapFeatureModes.publicTransitAsia</a> is supported only when credentials enabled for the
enriched Japan map are used.</p>
<p>Public transit is disabled by default for all map
schemes when using Rest-of-World map data. When using enriched Japan map
data, public transit is enabled by default with
<a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia">MapFeatureModes.publicTransitAsia</a> on normal, lite and topo schemes
(including their hybrid variants) and disabled by default on logistics
schemes.</p>
<p>Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a>
and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static final String publicTransit = "public transit";</code></pre>

 



</div>
`
}</HTMLBlock>
