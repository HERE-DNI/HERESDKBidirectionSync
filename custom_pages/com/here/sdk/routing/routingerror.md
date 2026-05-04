---
title: "RoutingError (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutingerror"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class RoutingError

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.RoutingError
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum RoutingError extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")\>
Specifies possible errors that may result from the calculation of a route.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ACTIVE_MAP_UPDATE](#ACTIVE_MAP_UPDATE)

Route cannot be calculated due to active map update.

[AUTHENTICATION_FAILED](#AUTHENTICATION_FAILED)

Routing operation is not authenticated.

[COULD_NOT_MATCH_DESTINATION](#COULD_NOT_MATCH_DESTINATION)

Destination waypoint could not be matched to a road network.

[COULD_NOT_MATCH_ORIGIN](#COULD_NOT_MATCH_ORIGIN)

Origin waypoint could not be matched to a road network.

[EXCEEDED_USAGE_LIMIT](#EXCEEDED_USAGE_LIMIT)

Credentials exceeded the allowed requests limit.

[FAILED_ROUTE_HANDLE_CREATION](#FAILED_ROUTE_HANDLE_CREATION)

No RouteHandle was created.

[FORBIDDEN](#FORBIDDEN)

The provided credentials don't give access to the requested resource.

[HTTP_ERROR](#HTTP_ERROR)

A general network request error.

[IMPORT_FAILED](#IMPORT_FAILED)

No route section was found for imported waypoints.

[INTERNAL_ERROR](#INTERNAL_ERROR)

Generic internal error.

[INVALID_PARAMETER](#INVALID_PARAMETER)

An invalid input parameter.

[NO_ISOLINE_FOUND](#NO_ISOLINE_FOUND)

No isoline can be calculated for the given input.

[NO_REACHABLE_CHARGING_STATION_FOUND](#NO_REACHABLE_CHARGING_STATION_FOUND)

Initial charge is not enough to reach any known charging stations.

[NO_ROUTE_FOUND](#NO_ROUTE_FOUND)

No route can be calculated for the given input.

[NO_ROUTE_HANDLE](#NO_ROUTE_HANDLE)

The route has no [`Route.getRouteHandle()`](sdk-for-android-explore-api-reference-latestroute#getRouteHandle()), but it was used for a feature that requires one.

[OFFLINE](#OFFLINE)

The device has no internet connection.

[OPERATION_CANCELLED](#OPERATION_CANCELLED)

Operation cancelled.

[PARSING_ERROR](#PARSING_ERROR)

Error while parsing route data.

[PROXY_AUTHENTICATION_FAILED](#PROXY_AUTHENTICATION_FAILED)

Proxy is not authenticated.

[PROXY_SERVER_UNREACHABLE](#PROXY_SERVER_UNREACHABLE)

Proxy server unreachable.

[ROUTE_CALCULATION_FAILED](#ROUTE_CALCULATION_FAILED)

Calculation did not succeed.

[ROUTE_LENGTH_LIMIT_EXCEEDED](#ROUTE_LENGTH_LIMIT_EXCEEDED)

Distance between waypoints is too large for current options.

[SERVER_UNREACHABLE](#SERVER_UNREACHABLE)

Routing server is unreachable.

[TIMED_OUT](#TIMED_OUT)

The request timed out.

[VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING](#VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING)

Route handle decoding failed due to forbidden segments for the specified transport mode.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### INTERNAL_ERROR

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") INTERNAL_ERROR

    Generic internal error.

### INVALID_PARAMETER

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") INVALID_PARAMETER

    An invalid input parameter.

### SERVER_UNREACHABLE

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") SERVER_UNREACHABLE

    Routing server is unreachable.

### HTTP_ERROR

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") HTTP_ERROR

    A general network request error.

### AUTHENTICATION_FAILED

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") AUTHENTICATION_FAILED

    Routing operation is not authenticated. Check your credentials.

### FORBIDDEN

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") FORBIDDEN

    The provided credentials don't give access to the requested resource.

### EXCEEDED_USAGE_LIMIT

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") EXCEEDED_USAGE_LIMIT

    Credentials exceeded the allowed requests limit.

### PARSING_ERROR

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") PARSING_ERROR

    Error while parsing route data. This is not expected to happen. Try updating to the newest version of the SDK. If the problem persists, please report a bug in the SDK.

### NO_ROUTE_FOUND

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") NO_ROUTE_FOUND

    No route can be calculated for the given input.

### TIMED_OUT

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") TIMED_OUT

    The request timed out.

### OFFLINE

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") OFFLINE

    The device has no internet connection.

### NO_ISOLINE_FOUND

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") NO_ISOLINE_FOUND

    No isoline can be calculated for the given input.

### NO_ROUTE_HANDLE

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") NO_ROUTE_HANDLE

    The route has no [`Route.getRouteHandle()`](sdk-for-android-explore-api-reference-latestroute#getRouteHandle()), but it was used for a feature that requires one. Consider to recalculate the route with a route handle. See [`RouteOptions.enableRouteHandle`](sdk-for-android-explore-api-reference-latestrouteoptions#enableRouteHandle).

### OPERATION_CANCELLED

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") OPERATION_CANCELLED

    Operation cancelled.

### COULD_NOT_MATCH_DESTINATION

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") COULD_NOT_MATCH_DESTINATION

    Destination waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.

### COULD_NOT_MATCH_ORIGIN

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") COULD_NOT_MATCH_ORIGIN

    Origin waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.

### FAILED_ROUTE_HANDLE_CREATION

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") FAILED_ROUTE_HANDLE_CREATION

    No RouteHandle was created.

### IMPORT_FAILED

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") IMPORT_FAILED

    No route section was found for imported waypoints.

### NO_REACHABLE_CHARGING_STATION_FOUND

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") NO_REACHABLE_CHARGING_STATION_FOUND

    Initial charge is not enough to reach any known charging stations.

### ROUTE_CALCULATION_FAILED

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") ROUTE_CALCULATION_FAILED

    Calculation did not succeed.

### ROUTE_LENGTH_LIMIT_EXCEEDED

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") ROUTE_LENGTH_LIMIT_EXCEEDED

    Distance between waypoints is too large for current options.

### VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING

    Route handle decoding failed due to forbidden segments for the specified transport mode.

### PROXY_AUTHENTICATION_FAILED

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") PROXY_AUTHENTICATION_FAILED

    Proxy is not authenticated. Check your proxy credentials.

### PROXY_SERVER_UNREACHABLE

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") PROXY_SERVER_UNREACHABLE

    Proxy server unreachable.

### ACTIVE_MAP_UPDATE

public static final [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") ACTIVE_MAP_UPDATE

    Route cannot be calculated due to active map update. Please, repeat the request after map update is finished successfully.

## Method Details

### values

public static [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
