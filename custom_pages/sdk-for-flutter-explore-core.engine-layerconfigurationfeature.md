---
title: "LayerConfigurationFeature enum - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-layerconfigurationfeature"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfigurationFeature.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/LayerConfigurationFeature-enum-sidebar.html">

<div>

# <span class="kind-enum">LayerConfigurationFeature</span> enum

</div>

<div class="section desc markdown">

Defines a list of possible map data features that can be enabled / disabled.

See <a href="sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>

Following features are enabled by default:

- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.detailRendering</a>
- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.landmarks3d</a>
- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a>
- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineSearch</a>
- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineRouting</a>
- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.rendering</a>

All other features are disabled, by default.

Each feature enables a set of OCM layer groups to be downloaded by `sdk.maploader.MapDownloader`. Detailed description of each layer group available in the <a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a>

Following features are enabled by default for implicit prefetch:

- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a>

Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView. Explicit prefetching is done using `sdk.prefetcher.RoutePrefetcher` and `sdk.prefetcher.PolygonPrefetcher`.

Feature might have more than one layer group predefined to enable full experience. For example, <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a> requires routing attributes, visual-friendly street names, maneuvers data and ability to interconnect those data sets.

The same map data is useful for different features, for example <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.rendering</a> uses Places data to present it on the MapView, while <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineSearch</a> uses the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.

</div>

## Values

<span class="name">detailRendering</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Additional rendering details like buildings. Only used for the MapView. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. However, during online usage such data may still be downloaded into the cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.

Feature enables following OCM layer groups:

- "detailed_rendering"

<span class="name">navigation</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that is used for map matching during navigation. When not set, navigation may not work properly when being used offline. Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.

Feature enables following OCM layer groups:

- "interop"
- "rendering"
- "navigation"
- "routing"

<span class="name">offlineSearch</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that is used to search. When not set, the OfflineSearchEngine may not work properly when being used offline.

Feature enables following OCM layer groups:

- "rendering"
- "routing"
- "search"

<span class="name">offlineSearchGlobal</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data used for global search indexing. This feature enables searches across broader geographic areas and improves both performance and accuracy by leveraging global search indices. By default this feature is disabled.

Enables the HERE SDK to use the enhanced offline search algorithm for downloaded map regions when:

- `OFFLINE_SEARCH_GLOBAL` is included in <a href="sdk-for-flutter-explore-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a> and
- downloaded map regions contain the required OCM layer groups listed below.

Also enables the enhanced offline search algorithm for implicitly prefetched map content when:

- `OFFLINE_SEARCH_GLOBAL` is included in <a href="sdk-for-flutter-explore-core-engine-layerconfiguration-implicitlyprefetchedfeatures">LayerConfiguration.implicitlyPrefetchedFeatures</a> and
- downloaded map regions (if present) contain the required OCM layer groups.

Both options can be enabled together. However, if enabling the feature for implicitly prefetched content, it is recommended to also enable it for downloaded map regions to ensure consistent search behavior.

**Important**: After enabling this feature, make sure to update the cached offline maps. If the cached maps are not updated, the algorithm will either:

1.  Fall back to the stable offline search if `OFFLINE_SEARCH` is still included in <a href="sdk-for-flutter-explore-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>, or
2.  Produce a `LAYERS_NOT_DOWNLOADED` error if the necessary layers are missing.

To prevent excessive map size growth, it is recommended to enable only one of `OFFLINE_SEARCH_GLOBAL` or `OFFLINE_SEARCH` at a time.

Enabling this feature increases storage requirements:

- Downloaded map region size by ~11–16% when enabled via <a href="sdk-for-flutter-explore-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.
- Map cache size by ~40–140% when enabled via <a href="sdk-for-flutter-explore-core-engine-layerconfiguration-implicitlyprefetchedfeatures">LayerConfiguration.implicitlyPrefetchedFeatures</a> (upper bound occurs for long routes, e.g., Paris → Rome).

Feature enables following OCM layer groups:

- "search_global"
- "search_data"

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<span class="name">offlineRouting</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that is used to calculate routes. When not set, the OfflineRoutingEngine may not work properly when being used offline. Increase of 12-16.5% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.

Feature enables following OCM layer groups:

- "rendering"
- "navigation"
- "routing"
- "interop"
- "car_offline_routing"

<span class="name">rendering</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.

Feature enables following OCM layer groups:

- "rendering"

<span class="name">truck</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that is used to calculate truck routes. When not set, the `OfflineRoutingEngine` may not work properly when being used to calculate truck routes. It is also used for map matching during truck navigation and for vehicle restriction visualization. When not set, truck navigation may not work properly when being used offline. Online truck navigation will still work when the device has an online connection. Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature. By default this feature is disabled.

Feature enables following OCM layer groups:

- "truck"
- "long_truck_offline_routing"
- "truck_offline_routing"

<span class="name">landmarks3d</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that is used to render 3D landmarks. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. When the `landmarks` `MapFeature` is set to be visible for a `MapScene`, 3D landmarks will still be loaded and visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.

3D landmark rendering is enabled by default in grayscale on normal, logistics and topo schemes, and in textureless mode on lite schemes. However, when this map data feature is disabled, the 3D landmark rendering for the above schemes will not work in offline mode with the downloaded map packages. Feature enables following OCM layer groups:

- "landmarks"

<span class="name">ev</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Offline map data for `EVChargingStation`.

Feature enables following OCM layer groups:

- "ev_charging_station_rendering_premium"
- "ev_charging_station_search_premium"

<span class="name">truckServiceAttributes</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Enables truck related attributes to be returned by Offline Search engine. Feature enables following OCM layer groups:

- "truck_service_premium"

<span class="name">fuelStationAttributes</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Enables fuel attributes to be returned by Offline Search engine.

Feature enables following OCM layer groups:

- "fueling_station_premium"

<span class="name">offlineBusRouting</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that is used to calculate bus routes. When not set, the `OfflineRoutingEngine` may not be able to calculate routes with `BusOptions`.

Feature enables following OCM layer groups:

- "bus_offline_routing"

<span class="name">junctionView3x4</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides junction view images and assets with aspect ratio 3x4. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.

Feature enables following OCM layer groups:

- "junction_view_file_3x4"
- "junction_view_asset_3x4"
- "junction_view_asset_common"

<span class="name">junctionView16x9</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides junction view images and assets with aspect ratio 16x9. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.

Feature enables following OCM layer groups:

- "junction_view_file_16x9"
- "junction_view_asset_16x9"
- "junction_view_asset_common"

<span class="name">junctionSign3x4</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides junction sign images with aspect ratio 3x4. By default this feature is disabled.

Feature enables following OCM layer groups:

- "junction_sign_file_3x4"

<span class="name">junctionSign3x5</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides junction sign images with aspect ratio 3x5. By default this feature is disabled.

Feature enables following OCM layer groups:

- "junction_sign_file_3x5"

<span class="name">junctionSign4x3</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides junction sign images with aspect ratio 4x3. By default this feature is disabled.

Feature enables following OCM layer groups:

- "junction_sign_file_4x3"

<span class="name">junctionSign5x3</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides junction sign images with aspect ratio 5x3. By default this feature is disabled. Feature enables following OCM layer groups:

- "junction_sign_file_5x3"

<span class="name">junctionSign16x9</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides junction sign images with aspect ratio 16x9. By default this feature is disabled.

Feature enables following OCM layer groups:

- "junction_sign_file_16x9"

<span class="name">terrain</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides topography information. The related map feature terrain with mode hillshade is enabled by default on topo map schemes. It is disabled by default on all other schemes.

Note that this change has performance implications, with additional data consumption and impact on rendering frame rate. If performance is a concern, this feature can be disabled from the application side when loading the map scene. However, when this map data feature is disabled, the terrain rendering for the above schemes will not work in offline mode with the downloaded map packages. Feature enables following OCM layer groups:

- "terrain"

<span class="name">detailedTerrain</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides detailed topography information. By default this feature is disabled. Feature enables following OCM layer groups:

- "detailed_terrain"

<span class="name">adas</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data which provides ADAS information which includes slope, elevation and curvature information. By default this feature is disabled. Feature enables following OCM layer groups:

- "adas"

<span class="name">ehorizon</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data which provides information about the parts of foreign segments in a tile, where a foreign segment is a segment that is stored in another tile but intersects the current tile. By default this feature is disabled. Feature enables following OCM layer groups:

- "ehorizon"

<span class="name">rdsTraffic</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Map data that provides traffic broadcast functionality using RDS-TMC format. It should be used when there is no internet connection, so that the routing module can utilize traffic data coming over the radio channel to build a route in the offline mode. Feature enables following OCM layer groups:

- "traffic"

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
