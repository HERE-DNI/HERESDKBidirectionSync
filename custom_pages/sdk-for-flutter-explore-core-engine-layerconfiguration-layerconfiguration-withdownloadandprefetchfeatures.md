---
title: "LayerConfiguration.withDownloadAndPrefetchFeatures constructor"
slug: "sdk-for-flutter-explore-core-engine-layerconfiguration-layerconfiguration-withdownloadandprefetchfeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfiguration.withDownloadAndPrefetchFeatures.html -->


<div>
<h1>LayerConfiguration.withDownloadAndPrefetchFeatures constructor</h1></div>

LayerConfiguration.withDownloadAndPrefetchFeatures(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a>&gt; enabledFeatures, </li>
<li>List&lt;<a href="/sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a>&gt; implicitlyPrefetchedFeatures</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>enabledFeatures</code> Specifies feature configuration for enabling list of features enabled for map download.
Empty list disables map download, as no map content specified for download in this case.</li>
<li><code>implicitlyPrefetchedFeatures</code> Specifies the list of features enabled for implicit and explicit map prefetch.
Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.</li>
</ul>
<p>Allows to specify an empty list, effectively disabling implicit prefetching. In this case,
the system will prioritize minimal network usage, at the cost of reduced offline map availability.
When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<code>LayerConfiguration</code>. However, for new map data, it will be applied.</p>
<p>By default the list contains:</p>
<ul>
<li><a href="/sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a></li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LayerConfiguration.withDownloadAndPrefetchFeatures(this.enabledFeatures, this.implicitlyPrefetchedFeatures)
    : _onDemandImplicitlyPrefetchedFeatures = [LayerConfigurationFeature.detailRendering, LayerConfigurationFeature.navigation, LayerConfigurationFeature.offlineSearch, LayerConfigurationFeature.offlineRouting, LayerConfigurationFeature.rendering, LayerConfigurationFeature.truck, LayerConfigurationFeature.landmarks3d, LayerConfigurationFeature.rdsTraffic, LayerConfigurationFeature.ev, LayerConfigurationFeature.truckServiceAttributes, LayerConfigurationFeature.fuelStationAttributes, LayerConfigurationFeature.offlineBusRouting, LayerConfigurationFeature.junctionView3x4, LayerConfigurationFeature.junctionView16x9, LayerConfigurationFeature.junctionSign3x4, LayerConfigurationFeature.junctionSign3x5, LayerConfigurationFeature.junctionSign4x3, LayerConfigurationFeature.junctionSign5x3, LayerConfigurationFeature.junctionSign16x9, LayerConfigurationFeature.terrain, LayerConfigurationFeature.detailedTerrain, LayerConfigurationFeature.adas, LayerConfigurationFeature.ehorizon];</code></pre>

 



</div>
`
}</HTMLBlock>
