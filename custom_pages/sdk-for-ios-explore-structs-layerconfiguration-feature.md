---
title: "Feature Enumeration Reference"
slug: "sdk-for-ios-explore-structs-layerconfiguration-feature"
---

# Feature

<div class="declaration">

<div class="language">

``` highlight
public enum Feature : UInt32, CaseIterable, Codable
```

</div>

</div>

Defines a list of possible map data features that can be enabled / disabled. See <a href="sdk-for-ios-explore-structs-sdkoptions#sdk-for-ios-explore-s-7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>

Following features are enabled by default:

- <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF">`LayerConfiguration.Feature.detailRendering`</a>
- <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF">`LayerConfiguration.Feature.landmarks3d`</a>
- <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a>
- <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">`LayerConfiguration.Feature.offlineSearch`</a>
- <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF">`LayerConfiguration.Feature.offlineRouting`</a>
- <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">`LayerConfiguration.Feature.rendering`</a>

All other features are disabled, by default.

Each feature enables a set of OCM layer groups to be downloaded by `sdk.maploader.MapDownloader`. Detailed description of each layer group available in the <a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a>

Following features are enabled by default for implicit prefetch:

- <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a>

Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView. Explicit prefetching is done using `sdk.prefetcher.RoutePrefetcher` and `sdk.prefetcher.PolygonPrefetcher`.

Feature might have more than one layer group predefined to enable full experience. For example, <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a> requires routing attributes, visual-friendly street names, maneuvers data and ability to interconnect those data sets.

The same map data is useful for different features, for example <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">`LayerConfiguration.Feature.rendering`</a> uses Places data to present it on the MapView, while <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">`LayerConfiguration.Feature.offlineSearch`</a> uses the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-detailRendering" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF" class="token"><code>detailRendering</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Additional rendering details like buildings. Only used for the MapView. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. However, during online usage such data may still be downloaded into the cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.

  Feature enables following OCM layer groups:

  - “detailed_rendering”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case detailRendering
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-navigation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF" class="token"><code>navigation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that is used for map matching during navigation. When not set, navigation may not work properly when being used offline. Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.

  Feature enables following OCM layer groups:

  - “interop”
  - “rendering”
  - “navigation”
  - “routing”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case navigation
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offlineSearch" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF" class="token"><code>offlineSearch</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that is used to search. When not set, the OfflineSearchEngine may not work properly when being used offline.

  Feature enables following OCM layer groups:

  - “rendering”
  - “routing”
  - “search”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offlineSearch
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO19offlineSearchGlobalyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offlineSearchGlobal" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO19offlineSearchGlobalyA2EmF" class="token"><code>offlineSearchGlobal</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data used for global search indexing. This feature enables searches across broader geographic areas and improves both performance and accuracy by leveraging global search indices. By default this feature is disabled.

  Enables the HERE SDK to use the enhanced offline search algorithm for downloaded map regions when:

  - `OFFLINE_SEARCH_GLOBAL` is included in <a href="sdk-for-ios-explore-structs-layerconfiguration#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a> and
  - downloaded map regions contain the required OCM layer groups listed below.

  Also enables the enhanced offline search algorithm for implicitly prefetched map content when:

  - `OFFLINE_SEARCH_GLOBAL` is included in <a href="sdk-for-ios-explore-structs-layerconfiguration#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp">`LayerConfiguration.implicitlyPrefetchedFeatures`</a> and
  - downloaded map regions (if present) contain the required OCM layer groups.

  Both options can be enabled together. However, if enabling the feature for implicitly prefetched content, it is recommended to also enable it for downloaded map regions to ensure consistent search behavior.

  **Important**: After enabling this feature, make sure to update the cached offline maps. If the cached maps are not updated, the algorithm will either:

  1.  Fall back to the stable offline search if `OFFLINE_SEARCH` is still included in <a href="sdk-for-ios-explore-structs-layerconfiguration#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>, or
  2.  Produce a `LAYERS_NOT_DOWNLOADED` error if the necessary layers are missing.

  To prevent excessive map size growth, it is recommended to enable only one of `OFFLINE_SEARCH_GLOBAL` or `OFFLINE_SEARCH` at a time.

  Enabling this feature increases storage requirements:

  - Downloaded map region size by ~11–16% when enabled via <a href="sdk-for-ios-explore-structs-layerconfiguration#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>.
  - Map cache size by ~40–140% when enabled via <a href="sdk-for-ios-explore-structs-layerconfiguration#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp">`LayerConfiguration.implicitlyPrefetchedFeatures`</a> (upper bound occurs for long routes, e.g., Paris → Rome).

  Feature enables following OCM layer groups:

  - “search_global”
  - “search_data”

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offlineSearchGlobal
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offlineRouting" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF" class="token"><code>offlineRouting</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that is used to calculate routes. When not set, the OfflineRoutingEngine may not work properly when being used offline. Increase of 12-16.5% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.

  Feature enables following OCM layer groups:

  - “rendering”
  - “navigation”
  - “routing”
  - “interop”
  - “car_offline_routing”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offlineRouting
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-rendering" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF" class="token"><code>rendering</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.

  Feature enables following OCM layer groups:

  - “rendering”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case rendering
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO5truckyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-truck" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO5truckyA2EmF" class="token"><code>truck</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that is used to calculate truck routes. When not set, the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> may not work properly when being used to calculate truck routes. It is also used for map matching during truck navigation and for vehicle restriction visualization. When not set, truck navigation may not work properly when being used offline. Online truck navigation will still work when the device has an online connection. Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature. By default this feature is disabled.

  Feature enables following OCM layer groups:

  - “truck”
  - “long_truck_offline_routing”
  - “truck_offline_routing”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case truck
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-landmarks3d" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF" class="token"><code>landmarks3d</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that is used to render 3D landmarks. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. When the `landmarks` `MapFeature` is set to be visible for a <a href="sdk-for-ios-explore-classes-mapscene">`MapScene`</a>, 3D landmarks will still be loaded and visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.

  3D landmark rendering is enabled by default in grayscale on normal, logistics and topo schemes, and in textureless mode on lite schemes. However, when this map data feature is disabled, the 3D landmark rendering for the above schemes will not work in offline mode with the downloaded map packages. Feature enables following OCM layer groups:

  - “landmarks”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case landmarks3d
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO2evyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-ev" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO2evyA2EmF" class="token"><code>ev</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Offline map data for <a href="sdk-for-ios-explore-structs-evchargingstation">`EVChargingStation`</a>.

  Feature enables following OCM layer groups:

  - “ev_charging_station_rendering_premium”
  - “ev_charging_station_search_premium”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case ev
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-truckServiceAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF" class="token"><code>truckServiceAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables truck related attributes to be returned by Offline Search engine. Feature enables following OCM layer groups:

  - “truck_service_premium”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case truckServiceAttributes
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-fuelStationAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF" class="token"><code>fuelStationAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables fuel attributes to be returned by Offline Search engine.

  Feature enables following OCM layer groups:

  - “fueling_station_premium”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case fuelStationAttributes
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO17offlineBusRoutingyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offlineBusRouting" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO17offlineBusRoutingyA2EmF" class="token"><code>offlineBusRouting</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that is used to calculate bus routes. When not set, the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> may not be able to calculate routes with <a href="sdk-for-ios-explore-structs-busoptions">`BusOptions`</a>.

  Feature enables following OCM layer groups:

  - “bus_offline_routing”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offlineBusRouting
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionView3x4yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-junctionView3x4" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionView3x4yA2EmF" class="token"><code>junctionView3x4</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides junction view images and assets with aspect ratio 3x4. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.

  Feature enables following OCM layer groups:

  - “junction_view_file_3x4”
  - “junction_view_asset_3x4”
  - “junction_view_asset_common”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case junctionView3x4
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO16junctionView16x9yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-junctionView16x9" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO16junctionView16x9yA2EmF" class="token"><code>junctionView16x9</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides junction view images and assets with aspect ratio 16x9. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.

  Feature enables following OCM layer groups:

  - “junction_view_file_16x9”
  - “junction_view_asset_16x9”
  - “junction_view_asset_common”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case junctionView16x9
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign3x4yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-junctionSign3x4" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign3x4yA2EmF" class="token"><code>junctionSign3x4</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides junction sign images with aspect ratio 3x4. By default this feature is disabled.

  Feature enables following OCM layer groups:

  - “junction_sign_file_3x4”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case junctionSign3x4
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign3x5yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-junctionSign3x5" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign3x5yA2EmF" class="token"><code>junctionSign3x5</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides junction sign images with aspect ratio 3x5. By default this feature is disabled.

  Feature enables following OCM layer groups:

  - “junction_sign_file_3x5”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case junctionSign3x5
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign4x3yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-junctionSign4x3" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign4x3yA2EmF" class="token"><code>junctionSign4x3</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides junction sign images with aspect ratio 4x3. By default this feature is disabled.

  Feature enables following OCM layer groups:

  - “junction_sign_file_4x3”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case junctionSign4x3
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign5x3yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-junctionSign5x3" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15junctionSign5x3yA2EmF" class="token"><code>junctionSign5x3</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides junction sign images with aspect ratio 5x3. By default this feature is disabled. Feature enables following OCM layer groups:

  - “junction_sign_file_5x3”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case junctionSign5x3
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO16junctionSign16x9yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-junctionSign16x9" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO16junctionSign16x9yA2EmF" class="token"><code>junctionSign16x9</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides junction sign images with aspect ratio 16x9. By default this feature is disabled.

  Feature enables following OCM layer groups:

  - “junction_sign_file_16x9”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case junctionSign16x9
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO7terrainyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-terrain" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO7terrainyA2EmF" class="token"><code>terrain</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides topography information. The related map feature terrain with mode hillshade is enabled by default on topo map schemes. It is disabled by default on all other schemes.

  Note that this change has performance implications, with additional data consumption and impact on rendering frame rate. If performance is a concern, this feature can be disabled from the application side when loading the map scene. However, when this map data feature is disabled, the terrain rendering for the above schemes will not work in offline mode with the downloaded map packages. Feature enables following OCM layer groups:

  - “terrain”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case terrain
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15detailedTerrainyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-detailedTerrain" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO15detailedTerrainyA2EmF" class="token"><code>detailedTerrain</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides detailed topography information. By default this feature is disabled. Feature enables following OCM layer groups:

  - “detailed_terrain”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case detailedTerrain
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO4adasyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-adas" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO4adasyA2EmF" class="token"><code>adas</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data which provides ADAS information which includes slope, elevation and curvature information. By default this feature is disabled. Feature enables following OCM layer groups:

  - “adas”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case adas
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO8ehorizonyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-ehorizon" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO8ehorizonyA2EmF" class="token"><code>ehorizon</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data which provides information about the parts of foreign segments in a tile, where a foreign segment is a segment that is stored in another tile but intersects the current tile. By default this feature is disabled. Feature enables following OCM layer groups:

  - “ehorizon”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case ehorizon
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO10rdsTrafficyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-rdsTraffic" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO10rdsTrafficyA2EmF" class="token"><code>rdsTraffic</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data that provides traffic broadcast functionality using RDS-TMC format. It should be used when there is no internet connection, so that the routing module can utilize traffic data coming over the radio channel to build a route in the offline mode. Feature enables following OCM layer groups:

  - “traffic”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case rdsTraffic
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

