---
title: "LayerConfiguration.withDefaults constructor"
slug: "sdk-for-flutter-explore-core-engine-layerconfiguration-layerconfiguration-withdefaults"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfiguration.withDefaults.html -->


<div>
<h1>LayerConfiguration.withDefaults constructor</h1></div>

LayerConfiguration.withDefaults()
    

<p>Initializes <code>enabled_features</code>, <code>implicitly_prefetched_features</code> and <code>on_demand_implicitly_prefetched_features</code> with it's default values.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LayerConfiguration.withDefaults()
    : enabledFeatures = [LayerConfigurationFeature.detailRendering, LayerConfigurationFeature.landmarks3d, LayerConfigurationFeature.navigation, LayerConfigurationFeature.offlineSearch, LayerConfigurationFeature.offlineRouting, LayerConfigurationFeature.rendering], implicitlyPrefetchedFeatures = [LayerConfigurationFeature.navigation], _onDemandImplicitlyPrefetchedFeatures = [LayerConfigurationFeature.detailRendering, LayerConfigurationFeature.navigation, LayerConfigurationFeature.offlineSearch, LayerConfigurationFeature.offlineRouting, LayerConfigurationFeature.rendering, LayerConfigurationFeature.truck, LayerConfigurationFeature.landmarks3d, LayerConfigurationFeature.rdsTraffic, LayerConfigurationFeature.ev, LayerConfigurationFeature.truckServiceAttributes, LayerConfigurationFeature.fuelStationAttributes, LayerConfigurationFeature.offlineBusRouting, LayerConfigurationFeature.junctionView3x4, LayerConfigurationFeature.junctionView16x9, LayerConfigurationFeature.junctionSign3x4, LayerConfigurationFeature.junctionSign3x5, LayerConfigurationFeature.junctionSign4x3, LayerConfigurationFeature.junctionSign5x3, LayerConfigurationFeature.junctionSign16x9, LayerConfigurationFeature.terrain, LayerConfigurationFeature.detailedTerrain, LayerConfigurationFeature.adas, LayerConfigurationFeature.ehorizon];</code></pre>

 



</div>
`
}</HTMLBlock>
