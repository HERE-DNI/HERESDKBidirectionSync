---
title: "LayerConfiguration.withDownloadAndPrefetchFeatures constructor - LayerConfiguration - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-layerconfiguration-layerconfiguration-withdownloadandprefetchfeatures"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LayerConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LayerConfiguration.withDownloadAndPrefetchFeatures</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LayerConfiguration.withDownloadAndPrefetchFeatures</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withDownloadAndPrefetchFeatures-param-enabledFeatures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span> <span class="parameter-name">enabledFeatures</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withDownloadAndPrefetchFeatures-param-implicitlyPrefetchedFeatures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span> <span class="parameter-name">implicitlyPrefetchedFeatures</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `enabledFeatures` Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.
- `implicitlyPrefetchedFeatures` Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.

Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the `LayerConfiguration`. However, for new map data, it will be applied.

By default the list contains:

- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a>

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
LayerConfiguration.withDownloadAndPrefetchFeatures(this.enabledFeatures, this.implicitlyPrefetchedFeatures)
    : _onDemandImplicitlyPrefetchedFeatures = [LayerConfigurationFeature.detailRendering, LayerConfigurationFeature.navigation, LayerConfigurationFeature.offlineSearch, LayerConfigurationFeature.offlineRouting, LayerConfigurationFeature.rendering, LayerConfigurationFeature.truck, LayerConfigurationFeature.landmarks3d, LayerConfigurationFeature.rdsTraffic, LayerConfigurationFeature.ev, LayerConfigurationFeature.truckServiceAttributes, LayerConfigurationFeature.fuelStationAttributes, LayerConfigurationFeature.offlineBusRouting, LayerConfigurationFeature.junctionView3x4, LayerConfigurationFeature.junctionView16x9, LayerConfigurationFeature.junctionSign3x4, LayerConfigurationFeature.junctionSign3x5, LayerConfigurationFeature.junctionSign4x3, LayerConfigurationFeature.junctionSign5x3, LayerConfigurationFeature.junctionSign16x9, LayerConfigurationFeature.terrain, LayerConfigurationFeature.detailedTerrain, LayerConfigurationFeature.adas, LayerConfigurationFeature.ehorizon];
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

