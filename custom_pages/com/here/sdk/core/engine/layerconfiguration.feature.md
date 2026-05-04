---
title: "LayerConfiguration.Feature (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlayerconfiguration-feature"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class LayerConfiguration.Feature

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\>
com.here.sdk.core.engine.LayerConfiguration.Feature
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[LayerConfiguration](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine")

------------------------------------------------------------------------
public static enum LayerConfiguration.Feature extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\>
Defines a list of possible map data features that can be enabled / disabled. See [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration)

Following features are enabled by default:

- [`DETAIL_RENDERING`](#DETAIL_RENDERING)
- [`LANDMARKS_3D`](#LANDMARKS_3D)
- [`NAVIGATION`](#NAVIGATION)
- [`OFFLINE_SEARCH`](#OFFLINE_SEARCH)
- [`OFFLINE_ROUTING`](#OFFLINE_ROUTING)
- [`RENDERING`](#RENDERING)
- [`TRUCK`](#TRUCK)

All other features are disabled, by default.

Each feature enables a set of OCM layer groups to be downloaded by `sdk.maploader.MapDownloader`. Detailed description of each layer group available in the [HERE Optimized Client Map Developer Guide](https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html)

Following features are enabled by default for implicit prefetch:

- [`DETAIL_RENDERING`](#DETAIL_RENDERING)
- [`NAVIGATION`](#NAVIGATION)
- [`OFFLINE_SEARCH`](#OFFLINE_SEARCH)
- [`OFFLINE_ROUTING`](#OFFLINE_ROUTING)
- [`RENDERING`](#RENDERING)
- [`TRUCK`](#TRUCK)

Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView. Explicit prefetching is done using `sdk.prefetcher.RoutePrefetcher` and `sdk.prefetcher.PolygonPrefetcher`.

Feature might have more than one layer group predefined to enable full experience. For example, [`NAVIGATION`](#NAVIGATION) requires routing attributes, visual-friendly street names, maneuvers data and ability to interconnect those data sets.

The same map data is useful for different features, for example [`RENDERING`](#RENDERING) uses Places data to present it on the MapView, while [`OFFLINE_SEARCH`](#OFFLINE_SEARCH) uses the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ADAS](#ADAS)

Map data which provides ADAS information which includes slope, elevation and curvature information.

[DETAIL_RENDERING](#DETAIL_RENDERING)

Additional rendering details like buildings.

[DETAILED_TERRAIN](#DETAILED_TERRAIN)

Map data that provides detailed topography information.

[EHORIZON](#EHORIZON)

Map data which provides information about the parts of foreign segments in a tile, where a foreign segment is a segment that is stored in another tile but intersects the current tile.

[EV](#EV)

Offline map data for `EVChargingStation`.

[FUEL_STATION_ATTRIBUTES](#FUEL_STATION_ATTRIBUTES)

Enables fuel attributes to be returned by Offline Search engine.

[JUNCTION_SIGN_16X9](#JUNCTION_SIGN_16X9)

Map data that provides junction sign images with aspect ratio 16x9.

[JUNCTION_SIGN_3X4](#JUNCTION_SIGN_3X4)

Map data that provides junction sign images with aspect ratio 3x4.

[JUNCTION_SIGN_3X5](#JUNCTION_SIGN_3X5)

Map data that provides junction sign images with aspect ratio 3x5.

[JUNCTION_SIGN_4X3](#JUNCTION_SIGN_4X3)

Map data that provides junction sign images with aspect ratio 4x3.

[JUNCTION_SIGN_5X3](#JUNCTION_SIGN_5X3)

Map data that provides junction sign images with aspect ratio 5x3.

[JUNCTION_VIEW_16X9](#JUNCTION_VIEW_16X9)

Map data that provides junction view images and assets with aspect ratio 16x9.

[JUNCTION_VIEW_3X4](#JUNCTION_VIEW_3X4)

Map data that provides junction view images and assets with aspect ratio 3x4.

[LANDMARKS_3D](#LANDMARKS_3D)

Map data that is used to render 3D landmarks.

[NAVIGATION](#NAVIGATION)

Map data that is used for map matching during navigation.

[OFFLINE_BUS_ROUTING](#OFFLINE_BUS_ROUTING)

Map data that is used to calculate bus routes.

[OFFLINE_ROUTING](#OFFLINE_ROUTING)

Map data that is used to calculate routes.

[OFFLINE_SEARCH](#OFFLINE_SEARCH)

Map data that is used to search.

[OFFLINE_SEARCH_GLOBAL](#OFFLINE_SEARCH_GLOBAL)

Map data used for global search indexing.

[RDS_TRAFFIC](#RDS_TRAFFIC)

Map data that provides traffic broadcast functionality using RDS-TMC format.

[RENDERING](#RENDERING)

A basic set of rendering features such as carto POIs.

[TERRAIN](#TERRAIN)

Map data that provides topography information.

[TRUCK](#TRUCK)

Map data that is used to calculate truck routes.

[TRUCK_SERVICE_ATTRIBUTES](#TRUCK_SERVICE_ATTRIBUTES)

Enables truck related attributes to be returned by Offline Search engine.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### DETAIL_RENDERING

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") DETAIL_RENDERING

    Additional rendering details like buildings. Only used for the MapView. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. However, during online usage such data may still be downloaded into the cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.

    Feature enables following OCM layer groups:

    - "detailed_rendering"

### NAVIGATION

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") NAVIGATION

    Map data that is used for map matching during navigation. When not set, navigation may not work properly when being used offline. Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.

    Feature enables following OCM layer groups:

    - "interop"
    - "rendering"
    - "navigation"
    - "routing"

### OFFLINE_SEARCH

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") OFFLINE_SEARCH

    Map data that is used to search. When not set, the OfflineSearchEngine may not work properly when being used offline.

    Feature enables following OCM layer groups:

    - "rendering"
    - "routing"
    - "search"

### OFFLINE_SEARCH_GLOBAL

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") OFFLINE_SEARCH_GLOBAL

    Map data used for global search indexing. This feature enables searches across broader geographic areas and improves both performance and accuracy by leveraging global search indices. By default this feature is disabled.

    Enables HERE SDK to use the enhanced offline search algorithm when `OFFLINE_SEARCH_GLOBAL` is present in [`LayerConfiguration.enabledFeatures`](sdk-for-android-explore-api-reference-latestlayerconfiguration#enabledFeatures) and downloaded map regions exist with required OCM layer groups listed below. Note: Currently, this algorithm supports only offline maps stored in persistent (protected) storage.

    To prevent excessive map size growth, it is recommended to enable only one of `OFFLINE_SEARCH_GLOBAL` or `OFFLINE_SEARCH` at a time.

    Enabling this feature increases the size of downloaded map regions by approximately 11–16% when enabled via [`LayerConfiguration.enabledFeatures`](sdk-for-android-explore-api-reference-latestlayerconfiguration#enabledFeatures).

    Feature enables following OCM layer groups:

    - "search_global"
    - "search_data"

    **Note:** This is an alpha release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### OFFLINE_ROUTING

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") OFFLINE_ROUTING

    Map data that is used to calculate routes. When not set, the OfflineRoutingEngine may not work properly when being used offline. Increase of 12-16.5% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.

    Feature enables following OCM layer groups:

    - "rendering"
    - "navigation"
    - "routing"
    - "interop"
    - "car_offline_routing"

### RENDERING

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") RENDERING

    A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.

    Feature enables following OCM layer groups:

    - "rendering"

### TRUCK

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") TRUCK

    Map data that is used to calculate truck routes. When not set, the `OfflineRoutingEngine` may not work properly when being used to calculate truck routes. It is also used for map matching during truck navigation. When not set, truck navigation may not work properly when being used offline. Online truck navigation will still work when the device has an online connection. Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature.

    Feature enables following OCM layer groups:

    - "truck"
    - "long_truck_offline_routing"
    - "truck_offline_routing"

### LANDMARKS_3D

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") LANDMARKS_3D

    Map data that is used to render 3D landmarks. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. When the `landmarks` `MapFeature` is set to be visible for a `MapScene`, 3D landmarks will still be loaded and visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.

    3D landmark rendering is enabled by default in grayscale on normal, logistics and topo schemes, and in textureless mode on lite schemes. However, when this map data feature is disabled, the 3D landmark rendering for the above schemes will not work in offline mode with the downloaded map packages. Feature enables following OCM layer groups:

    - "landmarks"

### EV

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") EV

    Offline map data for `EVChargingStation`.

    Feature enables following OCM layer groups:

    - "ev_charging_station_rendering_premium"
    - "ev_charging_station_search_premium"

### TRUCK_SERVICE_ATTRIBUTES

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") TRUCK_SERVICE_ATTRIBUTES

    Enables truck related attributes to be returned by Offline Search engine. Feature enables following OCM layer groups:

    - "truck_service_premium"

### FUEL_STATION_ATTRIBUTES

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") FUEL_STATION_ATTRIBUTES

    Enables fuel attributes to be returned by Offline Search engine.

    Feature enables following OCM layer groups:

    - "fueling_station_premium"

### OFFLINE_BUS_ROUTING

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") OFFLINE_BUS_ROUTING

    Map data that is used to calculate bus routes. When not set, the `OfflineRoutingEngine` may not be able to calculate routes with `BusOptions`.

    Feature enables following OCM layer groups:

    - "bus_offline_routing"

### JUNCTION_VIEW_3X4

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") JUNCTION_VIEW_3X4

    Map data that provides junction view images and assets with aspect ratio 3x4. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.

    Feature enables following OCM layer groups:

    - "junction_view_file_3x4"
    - "junction_view_asset_3x4"
    - "junction_view_asset_common"

### JUNCTION_VIEW_16X9

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") JUNCTION_VIEW_16X9

    Map data that provides junction view images and assets with aspect ratio 16x9. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.

    Feature enables following OCM layer groups:

    - "junction_view_file_16x9"
    - "junction_view_asset_16x9"
    - "junction_view_asset_common"

### JUNCTION_SIGN_3X4

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") JUNCTION_SIGN_3X4

    Map data that provides junction sign images with aspect ratio 3x4. By default this feature is disabled.

    Feature enables following OCM layer groups:

    - "junction_sign_file_3x4"

### JUNCTION_SIGN_3X5

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") JUNCTION_SIGN_3X5

    Map data that provides junction sign images with aspect ratio 3x5. By default this feature is disabled.

    Feature enables following OCM layer groups:

    - "junction_sign_file_3x5"

### JUNCTION_SIGN_4X3

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") JUNCTION_SIGN_4X3

    Map data that provides junction sign images with aspect ratio 4x3. By default this feature is disabled.

    Feature enables following OCM layer groups:

    - "junction_sign_file_4x3"

### JUNCTION_SIGN_5X3

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") JUNCTION_SIGN_5X3

    Map data that provides junction sign images with aspect ratio 5x3. By default this feature is disabled. Feature enables following OCM layer groups:

    - "junction_sign_file_5x3"

### JUNCTION_SIGN_16X9

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") JUNCTION_SIGN_16X9

    Map data that provides junction sign images with aspect ratio 16x9. By default this feature is disabled.

    Feature enables following OCM layer groups:

    - "junction_sign_file_16x9"

### TERRAIN

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") TERRAIN

    Map data that provides topography information. The related map feature with mode is enabled by default on topo map schemes. It is disabled by default on all other schemes.

    Note that this change has performance implications, with additional data consumption and impact on rendering frame rate. If performance is a concern, this feature can be disabled from the application side when loading the map scene. However, when this map data feature is disabled, the terrain rendering for the above schemes will not work in offline mode with the downloaded map packages. Feature enables following OCM layer groups:

    - "terrain"

### DETAILED_TERRAIN

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") DETAILED_TERRAIN

    Map data that provides detailed topography information. By default this feature is disabled. Feature enables following OCM layer groups:

    - "detailed_terrain"

### ADAS

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") ADAS

    Map data which provides ADAS information which includes slope, elevation and curvature information. By default this feature is disabled. Feature enables following OCM layer groups:

    - "adas"

### EHORIZON

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") EHORIZON

    Map data which provides information about the parts of foreign segments in a tile, where a foreign segment is a segment that is stored in another tile but intersects the current tile. By default this feature is disabled. Feature enables following OCM layer groups:

    - "ehorizon"

### RDS_TRAFFIC

public static final [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") RDS_TRAFFIC

    Map data that provides traffic broadcast functionality using RDS-TMC format. It should be used when there is no internet connection, so that the routing module can utilize traffic data coming over the radio channel to build a route in the offline mode. Feature enables following OCM layer groups:

    - "traffic"

## Method Details

### values

public static [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
