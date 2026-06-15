---
title: "terrain property"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-terrain"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- terrain.html -->


<div>
<h1>terrain property</h1></div>

        
        String
        terrain
<div class="features">final</div>


<p>Show elevation topography.</p>
<p>Supported modes: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade">MapFeatureModes.terrainHillshade</a>, <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrain3d">MapFeatureModes.terrain3d</a>.</p>
<p><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade">MapFeatureModes.terrainHillshade</a> is only supported for schemes <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.normalDay</a>,
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.normalNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteDay</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteNight</a>,
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoDay</a> and
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoNight</a>.</p>
<p>Default mode is <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade">MapFeatureModes.terrainHillshade</a> for the supporting schemes.</p>
<p>By default, terrain is disabled, except for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoNight</a>.</p>
<p>Note that this feature has performance implications, with extra data use and impact on
frame rate.
If performance is a concern, this feature can be disabled from the application side when
loading the map scene.</p>
<p>Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a>
and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static final String terrain = "terrain";</code></pre>

 



</div>
`
}</HTMLBlock>
