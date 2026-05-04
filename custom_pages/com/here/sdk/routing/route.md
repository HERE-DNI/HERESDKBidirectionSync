---
title: "Route (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroute"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Route

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.Route
------------------------------------------------------------------------
public final class Route extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A route is a path through a road network over which someone travels.

**Note:** Each [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") of a route contains a list of [`SectionNotice`](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing") objects that describe *potential issues* after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")

  [deserialize](#deserialize(byte%5B%5D))`(byte[] routeData)`

Creates route from the given binary data.

[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [getBoundingBox](#getBoundingBox())`()`

Gets the closest rectangular area where this route fits in.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getConsumptionInKilowattHours](#getConsumptionInKilowattHours())`()`

Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getDuration](#getDuration())`()`

Gets the estimated time in seconds needed to travel along this route, including real-time traffic delays if available.

[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")

  [getGeometry](#getGeometry())`()`

Gets the [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this route.

[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")

  [getLanguage](#getLanguage())`()`

Gets the language requested for all textual information related to this route.

`int`

  [getLengthInMeters](#getLengthInMeters())`()`

Gets the length of this route in meters.

[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")

  [getOptimizationMode](#getOptimizationMode())`()`

Gets the optimization mode requested for route calculation.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteRailwayCrossing`](sdk-for-android-explore-api-reference-latestrouterailwaycrossing "class in com.here.sdk.routing")`>`

  [getRailwayCrossings](#getRailwayCrossings())`()`

Gets railway crossings.

[`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")

  [getRequestedTransportMode](#getRequestedTransportMode())`()`

Gets the transport mode requested for route calculation.

[`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")

  [getRouteHandle](#getRouteHandle())`()`

Gets the route handle of this route.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteLabel`](sdk-for-android-explore-api-reference-latestroutelabel "class in com.here.sdk.routing")`>`

  [getRouteLabels](#getRouteLabels())`()`

Gets route labels.

[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")

  [getRoutingOptions](#getRoutingOptions())`()`

Gets the options used to calculate this route.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing")`>`

  [getSections](#getSections())`()`

Gets the sections that make up this route.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getTrafficDelay](#getTrafficDelay())`()`

Gets the estimated time in seconds spent in traffic along this route.

`static byte[]`

  [serialize](#serialize(com.here.sdk.routing.Route))`(`[`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")` route)`

Serializes given route to a binary data.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### serialize

@Nullable public static byte\[\] serialize(@NonNull [Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") route)

    Serializes given route to a binary data. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `route` -

    The route which should be serialized.

    Returns:
    The binary data of the route.

### deserialize

@Nullable public static [Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") deserialize(@NonNull byte\[\] routeData)

    Creates route from the given binary data. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `routeData` -

    The binary of a serialized route.

    Returns:
    The route object restored from the binary data.

### getSections

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Section](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing")\> getSections()

    Gets the sections that make up this route.
Returns:
    The sections that make up this route.

### getGeometry

@NonNull public [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") getGeometry()

    Gets the [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route.
Returns:
    The [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route.

### getBoundingBox

@NonNull public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") getBoundingBox()

    Gets the closest rectangular area where this route fits in.
Returns:
    The closest rectangular area where this route fits in.

### getLengthInMeters

public int getLengthInMeters()

    Gets the length of this route in meters.
Returns:
    The length of this route in meters.

### getLanguage

@NonNull public [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") getLanguage()

    Gets the language requested for all textual information related to this route.
Returns:
    Indicates the language requested for all textual information related to this route.

### getOptimizationMode

@NonNull public [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") getOptimizationMode()

    Gets the optimization mode requested for route calculation.
Returns:
    The optimization mode requested for route calculation.

### getRequestedTransportMode

@NonNull public [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") getRequestedTransportMode()

    Gets the transport mode requested for route calculation.
Returns:
    The transport mode requested for route calculation.

### getConsumptionInKilowattHours

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getConsumptionInKilowattHours()

    Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.
Returns:
    Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

### getRouteHandle

@Nullable public [RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") getRouteHandle()

    Gets the route handle of this route. Note that it is provided only if [`RouteOptions.enableRouteHandle`](sdk-for-android-explore-api-reference-latestrouteoptions#enableRouteHandle) is set before route calculation.
Returns:
    The route handle of this route. Note that it is provided only if [`RouteOptions.enableRouteHandle`](sdk-for-android-explore-api-reference-latestrouteoptions#enableRouteHandle) is set before route calculation.

### getDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getDuration()

    Gets the estimated time in seconds needed to travel along this route, including real-time traffic delays if available.
Returns:
    The estimated time in seconds needed to travel along this route, including real-time traffic delays if available.

### getTrafficDelay

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getTrafficDelay()

    Gets the estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual.
Returns:
    The estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual.

### getRoutingOptions

@Nullable public [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") getRoutingOptions()

    Gets the options used to calculate this route.
Returns:
    The set of options used to calculate the route.

### getRailwayCrossings

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteRailwayCrossing](sdk-for-android-explore-api-reference-latestrouterailwaycrossing "class in com.here.sdk.routing")\> getRailwayCrossings()

    Gets railway crossings.

    Railway crossing information is only available for routes created with the online `RoutingEngine`.
Returns:
    Collection of railway crossings along the route.

### getRouteLabels

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteLabel](sdk-for-android-explore-api-reference-latestroutelabel "class in com.here.sdk.routing")\> getRouteLabels()

    Gets route labels.

    The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes. The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives when alternative routes have been quested via `RouteOptions`.
Returns:
    A collection containing a maximum of 2 `RouteLabel` instances for the route. It will return an empty list if no labels are available.
