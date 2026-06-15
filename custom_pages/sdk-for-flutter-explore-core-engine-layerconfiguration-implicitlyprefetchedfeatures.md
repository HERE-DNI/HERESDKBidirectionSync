---
title: "implicitlyPrefetchedFeatures property"
slug: "sdk-for-flutter-explore-core-engine-layerconfiguration-implicitlyprefetchedfeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- implicitlyPrefetchedFeatures.html -->


<div>
<h1>implicitlyPrefetchedFeatures property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a>&gt;
implicitlyPrefetchedFeatures
<div class="features">getter/setter pair</div>


<p>Specifies the list of features enabled for implicit and explicit map prefetch.
Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.</p>
<p>Allows to specify an empty list, effectively disabling implicit prefetching. In this case,
the system will prioritize minimal network usage, at the cost of reduced offline map availability.
When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<code>LayerConfiguration</code>. However, for new map data, it will be applied.</p>
<p>By default the list contains:</p>
<ul>
<li><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a></li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;LayerConfigurationFeature&gt; implicitlyPrefetchedFeatures;</code></pre>

 



</div>
`
}</HTMLBlock>
