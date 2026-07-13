---
title: "LayerConfiguration.withDefaults constructor - LayerConfiguration - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-layerconfiguration-layerconfiguration-withdefaults"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LayerConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LayerConfiguration.withDefaults</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LayerConfiguration.withDefaults</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Initializes `enabled_features`, `implicitly_prefetched_features` and `on_demand_implicitly_prefetched_features` with it's default values.

</div>

## Implementation

``` dart
LayerConfiguration.withDefaults()
    : enabledFeatures = [LayerConfigurationFeature.detailRendering, LayerConfigurationFeature.landmarks3d, LayerConfigurationFeature.navigation, LayerConfigurationFeature.offlineSearch, LayerConfigurationFeature.offlineRouting, LayerConfigurationFeature.rendering], implicitlyPrefetchedFeatures = [LayerConfigurationFeature.navigation], _onDemandImplicitlyPrefetchedFeatures = [LayerConfigurationFeature.detailRendering, LayerConfigurationFeature.navigation, LayerConfigurationFeature.offlineSearch, LayerConfigurationFeature.offlineRouting, LayerConfigurationFeature.rendering, LayerConfigurationFeature.truck, LayerConfigurationFeature.landmarks3d, LayerConfigurationFeature.rdsTraffic, LayerConfigurationFeature.ev, LayerConfigurationFeature.truckServiceAttributes, LayerConfigurationFeature.fuelStationAttributes, LayerConfigurationFeature.offlineBusRouting, LayerConfigurationFeature.junctionView3x4, LayerConfigurationFeature.junctionView16x9, LayerConfigurationFeature.junctionSign3x4, LayerConfigurationFeature.junctionSign3x5, LayerConfigurationFeature.junctionSign4x3, LayerConfigurationFeature.junctionSign5x3, LayerConfigurationFeature.junctionSign16x9, LayerConfigurationFeature.terrain, LayerConfigurationFeature.detailedTerrain, LayerConfigurationFeature.adas, LayerConfigurationFeature.ehorizon];
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

