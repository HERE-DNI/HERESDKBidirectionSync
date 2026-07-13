---
title: "UsageStatsFeature enum - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-usagestatsfeature"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/UsageStatsFeature-enum-sidebar.html">

<div>

# <span class="kind-enum">UsageStatsFeature</span> enum

</div>

<div class="section desc markdown">

Represents the feature enum associated with the gathered usage stats.

</div>

## Values

<span class="name">detailedRendering</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.detailRendering</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.

- Use `MapDownloader` to download and install a `Region`.

- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

      LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

  .

<span class="name">evRendering</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the "ev_charging_station_rendering_premium" layer group, enabled with <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a>. Note, that <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a> also enables "ev_charging_station_search_premium" layer group, which is represented with `UsageStats.Feature.EV_SEARCH`. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.
- Use `MapDownloader` to download and install a `Region`.
- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

<span class="name">evSearch</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the "ev_charging_station_search_premium" layer group, enabled with <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a>. Note, that <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a> also enables "ev_charging_station_rendering_premium" layer group, which is represented with `UsageStats.Feature.EV_RENDERING`. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.
- Use `MapDownloader` to download and install a `Region`.
- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

<span class="name">navigation</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the "adas", "ehorizon", "interop", "isa" OCM layers. In addition, it is also tracking the following layer configurations:

- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a>
- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.junctionView3x4</a>
- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.junctionView16x9</a>
- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.junctionSign3x4</a>
- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.junctionSign3x5</a>
- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.junctionSign4x3</a>
- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.junctionSign5x3</a>
- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.junctionSign16x9</a> Counted when data for the corresponding layer is requested by the application by performing one of the following actions:
- Pan the map view to areas that have not been cached, prefetched or installed before.
- Use `MapDownloader` to download and install a `Region`.
- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before.
- Using online navigation when the requested data is not cached, prefetched, or installed before. As of now, the above listed OCM layers cannot be turned off except for those that are exposed as layer configuration.

<span class="name">places</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for places search. This is legacy statistic which is now replaced by <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature.searchOnline</a>.

<span class="name">rdsTraffic</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.rdsTraffic</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.

- Use `MapDownloader` to download and install a `Region`.

- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

      LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

  .

<span class="name">rendering</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.rendering</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.

- Use `MapDownloader` to download and install a `Region`.

- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

      LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

  .

<span class="name">router</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the `RoutingEngine`. Includes the following transaction counts and APIs:

- **Routing Car, Bicycle, Pedestrian** with HRN `hrn:here:service::olp-here:routing-8:base` counted with the use of `RoutingEngine with CarOptions,BicycleOptions or PedestrianOptions`.

- **Routing Scooter** with HRN `hrn:here:service::olp-here:routing-8:scooter` counted with the use of `RoutingEngine with ScooterOptions`

- **Routing Taxi** with HRN `hrn:here:service::olp-here:routing-8:taxi` counted with the use of `RoutingEngine with TaxiOptions`

- **Routing Truck** with HRN `hrn:here:service::olp-here:routing-8:truck` counted with the use of `RoutingEngine with TruckOptions`

- **Time-Aware Routing** with HRN `hrn:here:service::olp-here:routing-8:traffic` counted with the use of `RouteOptions with arrivalTime or departureTime`

- **Routing EV** with HRN `hrn:here:service::olp-here:routing-8:ev` counted with the use of `RoutingEngine with EVTRuckOptions or EVCarOptions and evCarOptions.ensureReachability = `true`.`

- **Route Import** with HRN `hrn:here:service::olp-here:routing-8:import` counted with the use of

      RoutingEngine.importRoutes(...)

- **Toll Cost** with HRN `hrn:here:service::olp-here:routing-8:tolls` counted with the use of `RoutingEngine with RouteOptions.enableTolls`

- **Routing Bus** with HRN `hrn:here:service::olp-here:routing-8:bus` counted with the use of `RoutingEngine with BusOptions`

- **Isoline Routing** with HRN `hrn:here:service::olp-here:isoline-routing-8` counted with the use of `RoutingEngine with IsolineOptions`

<span class="name">routing</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the following layer configurations:

- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineRouting</a>

- <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineBusRouting</a> Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.

- Use `MapDownloader` to download and install a `Region`.

- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

      LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

  .

<span class="name">satellites</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics to show satellite map scheme. This includes a **Raster Tile Base** transaction count with HRN `hrn:here:service::olp-here:rendering-raster-tiles-3:base`.

<span class="name">search</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the "search", "ev_charging_station_search_premium", "fueling_station_premium" OCM layers. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.
- Use `MapDownloader` to download and install a `Region`.
- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, these layers cannot be turned off.

<span class="name">searchOnline</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the `SearchEngine`. Includes the following transaction counts and APIs:

- **Discover/Search** with HRN `hrn:here:service::olp-here:search-opensearch-1` counted with the use of `SearchEngine textquery search`
- **Geocode & Reverse Geocode** with HRN `hrn:here:service::olp-here:geocode-7` counted with the use of `SearchEngine addressQuery & GeoCoordinates search`
- **Autosuggest** with HRN `hrn:here:service::olp-here:search-autosuggest-7` counted with the use of `SearchEngine suggest`

<span class="name">transit</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the "transit" OCM layer. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.
- Use `MapDownloader` to download and install a `Region`.
- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

<span class="name">transitRoutingEngine</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the `TransitRoutingEngine`. This includes a **Public Transit** transaction count with HRN: `hrn:here:service::olp-here:transit-8`.

<span class="name">traffic</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the calls of `TrafficEngine`. All calls to `TrafficEngine` result in transaction counts for HRN `hrn:here:service::olp-here:traffic-api-7:standard`.

<span class="name">trafficVectorTiles</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for traffic vector tiles. This includes a **Traffic vector tile** transaction count with HRN: `hrn:here:service::olp-here:traffic-vector-tiles-2`.

<span class="name">truck</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.truck</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

- Pan the map view to areas that have not been cached, prefetched or installed before.

- Use `MapDownloader` to download and install a `Region`.

- Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling:

      LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()

  .

<span class="name">vectorTiles</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for online usage corresponding to the vector tiles. This includes a **Vector tile** transaction count with HRN: `hrn:here:service::olp-here:rendering-vector-tiles-2`. This statistic is only counted for the HERE SDK (Explore) when showing the map view.

<span class="name">other</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for feature that doesn't fit into other categories. Some examples include:

- Authentication
- Analytics
- Any feature not mapped in the existing list.

<span class="name">positioning</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents network traffic statistics for Here Positioning. This includes a **Network Positioning** transaction count with HRN `hrn:here:service::olp-here:positioning-2`.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-usagestatsfeature">UsageStatsFeature</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

