---
title: "Feature Enumeration Reference"
slug: "sdk-for-ios-explore-structs-usagestats-feature"
---

# Feature

<div class="declaration">

<div class="language">

``` highlight
public enum Feature : UInt32, CaseIterable, Codable
```

</div>

</div>

Represents the feature enum associated with the gathered usage stats.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO17detailedRenderingyA2EmF"></span>` `<span id="//apple_ref/swift/Element/detailedRendering" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO17detailedRenderingyA2EmF" class="token"><code>detailedRendering</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF">`LayerConfiguration.Feature.detailRendering`</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.

  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.

  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

        LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

    .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case detailedRendering
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO11evRenderingyA2EmF"></span>` `<span id="//apple_ref/swift/Element/evRendering" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO11evRenderingyA2EmF" class="token"><code>evRendering</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the “ev_charging_station_rendering_premium” layer group, enabled with <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a>. Note, that <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a> also enables “ev_charging_station_search_premium” layer group, which is represented with \[UsageStats.Feature.EV_SEARCH\]. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.
  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.
  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case evRendering
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO8evSearchyA2EmF"></span>` `<span id="//apple_ref/swift/Element/evSearch" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO8evSearchyA2EmF" class="token"><code>evSearch</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the “ev_charging_station_search_premium” layer group, enabled with <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a>. Note, that <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a> also enables “ev_charging_station_rendering_premium” layer group, which is represented with \[UsageStats.Feature.EV_RENDERING\]. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.
  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.
  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case evSearch
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO10navigationyA2EmF"></span>` `<span id="//apple_ref/swift/Element/navigation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO10navigationyA2EmF" class="token"><code>navigation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the “adas”, “ehorizon”, “interop”, “isa” OCM layers. In addition, it is also tracking the following layer configurations:

  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO15junctionView3x4yA2EmF">`LayerConfiguration.Feature.junctionView3x4`</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO16junctionView16x9yA2EmF">`LayerConfiguration.Feature.junctionView16x9`</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x4yA2EmF">`LayerConfiguration.Feature.junctionSign3x4`</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x5yA2EmF">`LayerConfiguration.Feature.junctionSign3x5`</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign4x3yA2EmF">`LayerConfiguration.Feature.junctionSign4x3`</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign5x3yA2EmF">`LayerConfiguration.Feature.junctionSign5x3`</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO16junctionSign16x9yA2EmF">`LayerConfiguration.Feature.junctionSign16x9`</a> Counted when data for the corresponding layer is requested by the application by performing one of the following actions:
  - Pan the map view to areas that have not been cached, prefetched or installed before.
  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.
  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before.
  - Using online navigation when the requested data is not cached, prefetched, or installed before. As of now, the above listed OCM layers cannot be turned off except for those that are exposed as layer configuration.

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

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO6placesyA2EmF"></span>` `<span id="//apple_ref/swift/Element/places" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO6placesyA2EmF" class="token"><code>places</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for places search. This is legacy statistic which is now replaced by <a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO12searchOnlineyA2EmF">`UsageStats.Feature.searchOnline`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case places
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO10rdsTrafficyA2EmF"></span>` `<span id="//apple_ref/swift/Element/rdsTraffic" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO10rdsTrafficyA2EmF" class="token"><code>rdsTraffic</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO10rdsTrafficyA2EmF">`LayerConfiguration.Feature.rdsTraffic`</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.

  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.

  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

        LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

    .

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

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO9renderingyA2EmF"></span>` `<span id="//apple_ref/swift/Element/rendering" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO9renderingyA2EmF" class="token"><code>rendering</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">`LayerConfiguration.Feature.rendering`</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.

  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.

  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

        LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

    .

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

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO6routeryA2EmF"></span>` `<span id="//apple_ref/swift/Element/router" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO6routeryA2EmF" class="token"><code>router</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a>. Includes the following transaction counts and APIs:

  - **Routing Car, Bicycle, Pedestrian** with HRN `hrn:here:service::olp-here:routing-8:base` counted with the use of `RoutingEngine with CarOptions,BicycleOptions or PedestrianOptions`.

  - **Routing Scooter** with HRN `hrn:here:service::olp-here:routing-8:scooter` counted with the use of `RoutingEngine with ScooterOptions`

  - **Routing Taxi** with HRN `hrn:here:service::olp-here:routing-8:taxi` counted with the use of `RoutingEngine with TaxiOptions`

  - **Routing Truck** with HRN `hrn:here:service::olp-here:routing-8:truck` counted with the use of `RoutingEngine with TruckOptions`

  - **Time-Aware Routing** with HRN `hrn:here:service::olp-here:routing-8:traffic` counted with the use of `RouteOptions with arrivalTime or departureTime`

  - **Routing EV** with HRN `hrn:here:service::olp-here:routing-8:ev` counted with the use of `RoutingEngine with EVTRuckOptions or EVCarOptions and evCarOptions.ensureReachability =`true`.`

  - **Route Import** with HRN `hrn:here:service::olp-here:routing-8:import` counted with the use of

        RoutingEngine.importRoutes(...)

  - **Toll Cost** with HRN `hrn:here:service::olp-here:routing-8:tolls` counted with the use of `RoutingEngine with RouteOptions.enableTolls`

  - **Routing Bus** with HRN `hrn:here:service::olp-here:routing-8:bus` counted with the use of `RoutingEngine with BusOptions`

  - **Isoline Routing** with HRN `hrn:here:service::olp-here:isoline-routing-8` counted with the use of `RoutingEngine with IsolineOptions`

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case router
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO7routingyA2EmF"></span>` `<span id="//apple_ref/swift/Element/routing" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO7routingyA2EmF" class="token"><code>routing</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the following layer configurations:

  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF">`LayerConfiguration.Feature.offlineRouting`</a>

  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO17offlineBusRoutingyA2EmF">`LayerConfiguration.Feature.offlineBusRouting`</a> Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.

  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.

  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

        LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

    .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case routing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO10satellitesyA2EmF"></span>` `<span id="//apple_ref/swift/Element/satellites" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO10satellitesyA2EmF" class="token"><code>satellites</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics to show satellite map scheme. This includes a **Raster Tile Base** transaction count with HRN `hrn:here:service::olp-here:rendering-raster-tiles-3:base`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case satellites
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO6searchyA2EmF"></span>` `<span id="//apple_ref/swift/Element/search" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO6searchyA2EmF" class="token"><code>search</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the “search”, “ev_charging_station_search_premium”, “fueling_station_premium” OCM layers. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.
  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.
  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. As of now, these layers cannot be turned off.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case search
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO12searchOnlineyA2EmF"></span>` `<span id="//apple_ref/swift/Element/searchOnline" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO12searchOnlineyA2EmF" class="token"><code>searchOnline</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>. Includes the following transaction counts and APIs:

  - **Discover/Search** with HRN `hrn:here:service::olp-here:search-opensearch-1` counted with the use of `SearchEngine textquery search`
  - **Geocode & Reverse Geocode** with HRN `hrn:here:service::olp-here:geocode-7` counted with the use of `SearchEngine addressQuery & GeoCoordinates search`
  - **Autosuggest** with HRN `hrn:here:service::olp-here:search-autosuggest-7` counted with the use of `SearchEngine suggest`

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case searchOnline
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO7transityA2EmF"></span>` `<span id="//apple_ref/swift/Element/transit" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO7transityA2EmF" class="token"><code>transit</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the “transit” OCM layer. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.
  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.
  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case transit
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO20transitRoutingEngineyA2EmF"></span>` `<span id="//apple_ref/swift/Element/transitRoutingEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO20transitRoutingEngineyA2EmF" class="token"><code>transitRoutingEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-ios-explore-classes-transitroutingengine">`TransitRoutingEngine`</a>. This includes a **Public Transit** transaction count with HRN: `hrn:here:service::olp-here:transit-8`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case transitRoutingEngine
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO7trafficyA2EmF"></span>` `<span id="//apple_ref/swift/Element/traffic" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO7trafficyA2EmF" class="token"><code>traffic</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the calls of <a href="sdk-for-ios-explore-classes-trafficengine">`TrafficEngine`</a>. All calls to <a href="sdk-for-ios-explore-classes-trafficengine">`TrafficEngine`</a> result in transaction counts for HRN `hrn:here:service::olp-here:traffic-api-7:standard`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case traffic
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO18trafficVectorTilesyA2EmF"></span>` `<span id="//apple_ref/swift/Element/trafficVectorTiles" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO18trafficVectorTilesyA2EmF" class="token"><code>trafficVectorTiles</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for traffic vector tiles. This includes a **Traffic vector tile** transaction count with HRN: `hrn:here:service::olp-here:traffic-vector-tiles-2`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case trafficVectorTiles
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO5truckyA2EmF"></span>` `<span id="//apple_ref/swift/Element/truck" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO5truckyA2EmF" class="token"><code>truck</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO5truckyA2EmF">`LayerConfiguration.Feature.truck`</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

  - Pan the map view to areas that have not been cached, prefetched or installed before.

  - Use <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> to download and install a <a href="sdk-for-ios-explore-structs-region">`Region`</a>.

  - Prefetch map data into the map cache with the <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

        LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

    .

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

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO11vectorTilesyA2EmF"></span>` `<span id="//apple_ref/swift/Element/vectorTiles" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO11vectorTilesyA2EmF" class="token"><code>vectorTiles</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for online usage corresponding to the vector tiles. This includes a **Vector tile** transaction count with HRN: `hrn:here:service::olp-here:rendering-vector-tiles-2`. This statistic is only counted for the HERE SDK (Explore) when showing the map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case vectorTiles
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO5otheryA2EmF"></span>` `<span id="//apple_ref/swift/Element/other" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO5otheryA2EmF" class="token"><code>other</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for feature that doesn’t fit into other categories. Some examples include:

  - Authentication
  - Analytics
  - Any feature not mapped in the existing list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case other
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV7FeatureO11positioningyA2EmF"></span>` `<span id="//apple_ref/swift/Element/positioning" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-usagestats-feature#/s:7heresdk10UsageStatsV7FeatureO11positioningyA2EmF" class="token"><code>positioning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents network traffic statistics for Here Positioning. This includes a **Network Positioning** transaction count with HRN `hrn:here:service::olp-here:positioning-2`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case positioning
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

