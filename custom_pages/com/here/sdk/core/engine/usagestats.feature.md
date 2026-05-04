---
title: "UsageStats.Feature (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestusagestats-feature"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class UsageStats.Feature

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")\>
com.here.sdk.core.engine.UsageStats.Feature
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`UsageStats.Feature`](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[UsageStats](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine")

------------------------------------------------------------------------
public static enum UsageStats.Feature extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")\>
Represents the feature enum associated with the gathered usage stats.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [DETAILED_RENDERING](#DETAILED_RENDERING)

Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.DETAIL_RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#DETAIL_RENDERING) layer configuration.

[EV_RENDERING](#EV_RENDERING)

Represents network traffic statistics for online usage corresponding to the "ev_charging_station_rendering_premium" layer group, enabled with [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV).

[EV_SEARCH](#EV_SEARCH)

Represents network traffic statistics for online usage corresponding to the "ev_charging_station_search_premium" layer group, enabled with [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV).

[NAVIGATION](#NAVIGATION)

Represents network traffic statistics for online usage corresponding to the "adas", "ehorizon", "interop", "isa" OCM layers.

[OTHER](#OTHER)

Represents network traffic statistics for feature that doesn't fit into other categories.

[PLACES](#PLACES)

Represents network traffic statistics for places search.

[POSITIONING](#POSITIONING)

Represents network traffic statistics for Here Positioning.

[RDS_TRAFFIC](#RDS_TRAFFIC)

Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.RDS_TRAFFIC`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#RDS_TRAFFIC) layer configuration.

[RENDERING](#RENDERING)

Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#RENDERING) layer configuration.

[ROUTER](#ROUTER)

Represents network traffic statistics for online usage corresponding to the `RoutingEngine`.

[ROUTING](#ROUTING)

Represents network traffic statistics for online usage corresponding to the following layer configurations: [`LayerConfiguration.Feature.OFFLINE_ROUTING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_ROUTING) [`LayerConfiguration.Feature.OFFLINE_BUS_ROUTING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_BUS_ROUTING) Counted when data for the corresponding layer is requested by the application by performing one of the following actions: Pan the map view to areas that have not been cached, prefetched or installed before. Use `MapDownloader` to download and install a `Region`. Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before.

[SATELLITES](#SATELLITES)

Represents network traffic statistics to show satellite map scheme.

[SEARCH](#SEARCH)

Represents network traffic statistics for online usage corresponding to the "search", "ev_charging_station_search_premium", "fueling_station_premium" OCM layers.

[SEARCH_ONLINE](#SEARCH_ONLINE)

Represents network traffic statistics for online usage corresponding to the `SearchEngine`.

[TRAFFIC](#TRAFFIC)

Represents network traffic statistics for online usage corresponding to the calls of `TrafficEngine`.

[TRAFFIC_VECTOR_TILES](#TRAFFIC_VECTOR_TILES)

Represents network traffic statistics for traffic vector tiles.

[TRANSIT](#TRANSIT)

Represents network traffic statistics for online usage corresponding to the "transit" OCM layer.

[TRANSIT_ROUTING_ENGINE](#TRANSIT_ROUTING_ENGINE)

Represents network traffic statistics for online usage corresponding to the `TransitRoutingEngine`.

[TRUCK](#TRUCK)

Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.TRUCK`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK) layer configuration.

[VECTOR_TILES](#VECTOR_TILES)

Represents network traffic statistics for online usage corresponding to the vector tiles.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`UsageStats.Feature`](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`UsageStats.Feature`](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### DETAILED_RENDERING

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") DETAILED_RENDERING

    Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.DETAIL_RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#DETAIL_RENDERING) layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling: `LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()`.

### EV_RENDERING

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") EV_RENDERING

    Represents network traffic statistics for online usage corresponding to the "ev_charging_station_rendering_premium" layer group, enabled with [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV). Note, that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) also enables "ev_charging_station_search_premium" layer group, which is represented with \[UsageStats.Feature.EV_SEARCH\]. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

### EV_SEARCH

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") EV_SEARCH

    Represents network traffic statistics for online usage corresponding to the "ev_charging_station_search_premium" layer group, enabled with [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV). Note, that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) also enables "ev_charging_station_rendering_premium" layer group, which is represented with \[UsageStats.Feature.EV_RENDERING\]. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

### NAVIGATION

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") NAVIGATION

    Represents network traffic statistics for online usage corresponding to the "adas", "ehorizon", "interop", "isa" OCM layers. In addition, it is also tracking the following layer configurations:

    - [`LayerConfiguration.Feature.NAVIGATION`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#NAVIGATION)
    - [`LayerConfiguration.Feature.JUNCTION_VIEW_3X4`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#JUNCTION_VIEW_3X4)
    - [`LayerConfiguration.Feature.JUNCTION_VIEW_16X9`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#JUNCTION_VIEW_16X9)
    - [`LayerConfiguration.Feature.JUNCTION_SIGN_3X4`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#JUNCTION_SIGN_3X4)
    - [`LayerConfiguration.Feature.JUNCTION_SIGN_3X5`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#JUNCTION_SIGN_3X5)
    - [`LayerConfiguration.Feature.JUNCTION_SIGN_4X3`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#JUNCTION_SIGN_4X3)
    - [`LayerConfiguration.Feature.JUNCTION_SIGN_5X3`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#JUNCTION_SIGN_5X3)
    - [`LayerConfiguration.Feature.JUNCTION_SIGN_16X9`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#JUNCTION_SIGN_16X9) Counted when data for the corresponding layer is requested by the application by performing one of the following actions:
    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before.
    - Using online navigation when the requested data is not cached, prefetched, or installed before. As of now, the above listed OCM layers cannot be turned off except for those that are exposed as layer configuration.

### PLACES

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") PLACES

    Represents network traffic statistics for places search. This is legacy statistic which is now replaced by [`SEARCH_ONLINE`](#SEARCH_ONLINE).

### RDS_TRAFFIC

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") RDS_TRAFFIC

    Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.RDS_TRAFFIC`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#RDS_TRAFFIC) layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling: `LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()`.

### RENDERING

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") RENDERING

    Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#RENDERING) layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling: `LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()`.

### ROUTER

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") ROUTER

    Represents network traffic statistics for online usage corresponding to the `RoutingEngine`. Includes the following transaction counts and APIs:

    - **Routing Car, Bicycle, Pedestrian** with HRN `hrn:here:service::olp-here:routing-8:base` counted with the use of `RoutingEngine with CarOptions,BicycleOptions or PedestrianOptions`.
    - **Routing Scooter** with HRN `hrn:here:service::olp-here:routing-8:scooter` counted with the use of `RoutingEngine with ScooterOptions`
    - **Routing Taxi** with HRN `hrn:here:service::olp-here:routing-8:taxi` counted with the use of `RoutingEngine with TaxiOptions`
    - **Routing Truck** with HRN `hrn:here:service::olp-here:routing-8:truck` counted with the use of `RoutingEngine with TruckOptions`
    - **Time-Aware Routing** with HRN `hrn:here:service::olp-here:routing-8:traffic` counted with the use of `RouteOptions with arrivalTime or departureTime`
    - **Routing EV** with HRN `hrn:here:service::olp-here:routing-8:ev` counted with the use of `RoutingEngine with EVTRuckOptions or EVCarOptions and evCarOptions.ensureReachability =`true`.`
    - **Route Import** with HRN `hrn:here:service::olp-here:routing-8:import` counted with the use of `RoutingEngine.importRoutes(...)`
    - **Toll Cost** with HRN `hrn:here:service::olp-here:routing-8:tolls` counted with the use of `RoutingEngine with RouteOptions.enableTolls`
    - **Routing Bus** with HRN `hrn:here:service::olp-here:routing-8:bus` counted with the use of `RoutingEngine with BusOptions`
    - **Isoline Routing** with HRN `hrn:here:service::olp-here:isoline-routing-8` counted with the use of `RoutingEngine with IsolineOptions`

### ROUTING

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") ROUTING

    Represents network traffic statistics for online usage corresponding to the following layer configurations:

    - [`LayerConfiguration.Feature.OFFLINE_ROUTING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_ROUTING)
    - [`LayerConfiguration.Feature.OFFLINE_BUS_ROUTING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_BUS_ROUTING) Counted when data for the corresponding layer is requested by the application by performing one of the following actions:
    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling: `LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()`.

### SATELLITES

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") SATELLITES

    Represents network traffic statistics to show satellite map scheme. This includes a **Raster Tile Base** transaction count with HRN `hrn:here:service::olp-here:rendering-raster-tiles-3:base`.

### SEARCH

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") SEARCH

    Represents network traffic statistics for online usage corresponding to the "search", "ev_charging_station_search_premium", "fueling_station_premium" OCM layers. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, these layers cannot be turned off.

### SEARCH_ONLINE

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") SEARCH_ONLINE

    Represents network traffic statistics for online usage corresponding to the `SearchEngine`. Includes the following transaction counts and APIs:

    - **Discover/Search** with HRN `hrn:here:service::olp-here:search-opensearch-1` counted with the use of `SearchEngine textquery search`
    - **Geocode & Reverse Geocode** with HRN `hrn:here:service::olp-here:geocode-7` counted with the use of `SearchEngine addressQuery & GeoCoordinates search`
    - **Autosuggest** with HRN `hrn:here:service::olp-here:search-autosuggest-7` counted with the use of `SearchEngine suggest`

### TRANSIT

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") TRANSIT

    Represents network traffic statistics for online usage corresponding to the "transit" OCM layer. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. As of now, this layer cannot be turned off.

### TRANSIT_ROUTING_ENGINE

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") TRANSIT_ROUTING_ENGINE

    Represents network traffic statistics for online usage corresponding to the `TransitRoutingEngine`. This includes a **Public Transit** transaction count with HRN: `hrn:here:service::olp-here:transit-8`.

### TRAFFIC

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") TRAFFIC

    Represents network traffic statistics for online usage corresponding to the calls of `TrafficEngine`. All calls to `TrafficEngine` result in transaction counts for HRN `hrn:here:service::olp-here:traffic-api-7:standard`.

### TRAFFIC_VECTOR_TILES

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") TRAFFIC_VECTOR_TILES

    Represents network traffic statistics for traffic vector tiles. This includes a **Traffic vector tile** transaction count with HRN: `hrn:here:service::olp-here:traffic-vector-tiles-2`.

### TRUCK

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") TRUCK

    Represents network traffic statistics for online usage corresponding to the [`LayerConfiguration.Feature.TRUCK`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK) layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:

    - Pan the map view to areas that have not been cached, prefetched or installed before.
    - Use `MapDownloader` to download and install a `Region`.
    - Prefetch map data into the map cache with the `RoutePrefetcher` for areas that have not been cached, prefetched or installed before. Note that you can enable or disable this feature by calling: `LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()`.

### VECTOR_TILES

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") VECTOR_TILES

    Represents network traffic statistics for online usage corresponding to the vector tiles. This includes a **Vector tile** transaction count with HRN: `hrn:here:service::olp-here:rendering-vector-tiles-2`. This statistic is only counted for the HERE SDK (Explore) when showing the map view.

### OTHER

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") OTHER

    Represents network traffic statistics for feature that doesn't fit into other categories. Some examples include:

    - Authentication
    - Analytics
    - Any feature not mapped in the existing list.

### POSITIONING

public static final [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") POSITIONING

    Represents network traffic statistics for Here Positioning. This includes a **Network Positioning** transaction count with HRN `hrn:here:service::olp-here:positioning-2`.

## Method Details

### values

public static [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
