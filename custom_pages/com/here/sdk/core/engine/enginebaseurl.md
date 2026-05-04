---
title: "EngineBaseURL (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestenginebaseurl"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class EngineBaseURL

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")\>
com.here.sdk.core.engine.EngineBaseURL
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`EngineBaseURL`](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum EngineBaseURL extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")\>
Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [AUTHENTICATION](#AUTHENTICATION)

Indicates base url for `Authentication`.

[DS_PROXY](#DS_PROXY)

Specifies the endpoint URL for a map catalog.

[ISOLINE_ROUTING_ENGINE](#ISOLINE_ROUTING_ENGINE)

Indicates a `IsolineRoutingEngine` endpoint.

[RASTER_TILE_SERVICE](#RASTER_TILE_SERVICE)

Indicates a `Raster Tile API` endpoint.

[ROUTING_ENGINE](#ROUTING_ENGINE)

Indicates a `RoutingEngine` endpoint.

[SEARCH_ENGINE](#SEARCH_ENGINE)

Indicates a `SearchEngine` endpoint.

[TRAFFIC_DATA](#TRAFFIC_DATA)

Indicates a `Traffic Data` endpoint.

[TRAFFIC_VECTOR_TILE_SERVICE](#TRAFFIC_VECTOR_TILE_SERVICE)

Indicates a `Traffic Vector Tile API` endpoint.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`EngineBaseURL`](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`EngineBaseURL`](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### SEARCH_ENGINE

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") SEARCH_ENGINE

    Indicates a `SearchEngine` endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are "v1/discover", "v1/geocode", "v1/revgeocode", "v1/autosuggest", "v1/lookup" and "v1/browse". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the first endpoint looks like this: "https://www.my-company.com/v1/discover" appended with query data. You need to ensure that the provided base URL supports all required endpoints.

### ROUTING_ENGINE

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") ROUTING_ENGINE

    Indicates a `RoutingEngine` endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are "v8/routes", "v8/import". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the first endpoint looks like this: "https://www.my-company.com/v8/routes" appended with query data. You need to ensure that the provided base URL supports all required endpoints.

### AUTHENTICATION

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") AUTHENTICATION

    Indicates base url for `Authentication`. Note that the provided string value will replace the base URL. The endpoint name for this base url is "oauth2/token". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the endpoint looks like this: "https://www.my-company.com/oauth2/token" appended with query data. You need to ensure that the provided base URL supports required endpoint.

### DS_PROXY

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") DS_PROXY

    Specifies the endpoint URL for a map catalog. This is only relevant for the Navigate license that uses OCM based map data when a custom catalog configuration should be loaded. By default, the data Service proxy, in short [`DS_PROXY`](#DS_PROXY), is set to "https://direct.data.api.platform.here.com/direct/v1". When a custom catalog should be used, then the HERE SDK will internally do a lookup request to find out which URL to use to access catalog. In order to bypass this extra request, we recommend to set the URL upfront when initializing the HERE SDK. For example, a valid [`DS_PROXY`](#DS_PROXY) for a custom catalog may look like this: "https://data.api.platform.yourcompany.com/direct/v1". Note that this is not a network proxy setting. If you do not load a custom catalog configuration, you can ignore this setting.

### TRAFFIC_DATA

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") TRAFFIC_DATA

    Indicates a `Traffic Data` endpoint. Note that the provided string value will replace the base URL. This is only relevant for TrafficEngine. For traffic incident and flow presented in the map view, please use [`TRAFFIC_VECTOR_TILE_SERVICE`](#TRAFFIC_VECTOR_TILE_SERVICE).

### TRAFFIC_VECTOR_TILE_SERVICE

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") TRAFFIC_VECTOR_TILE_SERVICE

    Indicates a `Traffic Vector Tile API` endpoint. Note that the provided string value will replace the base URL. This is only relevant for traffic presented in the map view. For the TrafficEngine, please use [`TRAFFIC_DATA`](#TRAFFIC_DATA).

    The service needs to comply with https://www.here.com/docs/bundle/traffic-vector-tile-api-v2-api-reference/page/index.html The endpoint name for this engine is "v2/traffictiles". A valid base string value could look like "www.my-company.com". The resulting URL looks like this: "https://www.my-company.com/v2/traffictiles/{layer}/mc/{z}/{x}/{y}/omv", with concrete tile IDs in {x}, {y}, {z} and {layers} in (flow, incidents). You need to ensure that the provided base URL supports all required endpoints.

### RASTER_TILE_SERVICE

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") RASTER_TILE_SERVICE

    Indicates a `Raster Tile API` endpoint. Note that the provided string value will replace the URL template. A valid URL template value could look like: "https://www.my-company.com/satellite.day/{z}/{x}/{y}/512/jpg"

### ISOLINE_ROUTING_ENGINE

public static final [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") ISOLINE_ROUTING_ENGINE

    Indicates a `IsolineRoutingEngine` endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are "v8/isolines". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the first endpoint looks like this: "https://www.my-company.com/v8/isolines" appended with query data. You need to ensure that the provided base URL supports all required endpoints.

## Method Details

### values

public static [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
