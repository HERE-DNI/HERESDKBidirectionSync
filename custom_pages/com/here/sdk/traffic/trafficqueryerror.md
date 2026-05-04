---
title: "TrafficQueryError (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficqueryerror"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class TrafficQueryError

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")\>
com.here.sdk.traffic.TrafficQueryError
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`TrafficQueryError`](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum TrafficQueryError extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")\>
Represents various errors that could occur from a traffic queries.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [AUTHENTICATION_FAILED](#AUTHENTICATION_FAILED)

Incident query/flow operation is not authenticated.

[BAD_REQUEST](#BAD_REQUEST)

Bad request.

[FAILED_TO_RETRIEVE_RESULT](#FAILED_TO_RETRIEVE_RESULT)

Failed to retrieve result since the server has returned an error or invalid result that couldn't be processed correctly.

[FORBIDDEN](#FORBIDDEN)

The provided credentials don't give access to the requested resource.

[HTTP_ERROR](#HTTP_ERROR)

Network request error.

[INCIDENT_ID_NOT_FOUND](#INCIDENT_ID_NOT_FOUND)

Incident ID is not found in the system.

[INTERNAL_ERROR](#INTERNAL_ERROR)

Internal error.

[INVALID_FILTER_OPTIONS](#INVALID_FILTER_OPTIONS)

One or several filter options are invalid.

[INVALID_GEOMETRY](#INVALID_GEOMETRY)

Invalid geometry: bounding box, circle, or corridor.

[INVALID_IN](#INVALID_IN)

Invalid "in" parameter: wrong type, missing or invalid "in".

[INVALID_INCIDENT](#INVALID_INCIDENT)

Invalid incident ID, type, earliestStartTime or latestEndTime.

[INVALID_PARAMETER](#INVALID_PARAMETER)

One or more input parameters in the query is not valid.

[OFFLINE](#OFFLINE)

The device has no internet connection.

[OPERATION_CANCELLED](#OPERATION_CANCELLED)

Operation cancelled.

[PROXY_AUTHENTICATION_FAILED](#PROXY_AUTHENTICATION_FAILED)

Proxy is not authenticated.

[PROXY_SERVER_UNREACHABLE](#PROXY_SERVER_UNREACHABLE)

Proxy server unreachable.

[SERVER_UNREACHABLE](#SERVER_UNREACHABLE)

Server unreachable.

[TIMED_OUT](#TIMED_OUT)

The request timed out.

[TOO_MANY_REQUESTS](#TOO_MANY_REQUESTS)

Server has received an excessive number of requests from client within a specific timeframe and client should slow down or wait before sending more requests.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`TrafficQueryError`](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`TrafficQueryError`](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### FAILED_TO_RETRIEVE_RESULT

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") FAILED_TO_RETRIEVE_RESULT

    Failed to retrieve result since the server has returned an error or invalid result that couldn't be processed correctly.

### AUTHENTICATION_FAILED

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") AUTHENTICATION_FAILED

    Incident query/flow operation is not authenticated. Check your credentials.

### FORBIDDEN

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") FORBIDDEN

    The provided credentials don't give access to the requested resource.

### SERVER_UNREACHABLE

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") SERVER_UNREACHABLE

    Server unreachable.

### TIMED_OUT

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") TIMED_OUT

    The request timed out.

### OFFLINE

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") OFFLINE

    The device has no internet connection.

### HTTP_ERROR

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") HTTP_ERROR

    Network request error.

### INVALID_IN

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") INVALID_IN

    Invalid "in" parameter: wrong type, missing or invalid "in".

### INVALID_GEOMETRY

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") INVALID_GEOMETRY

    Invalid geometry: bounding box, circle, or corridor.

### INVALID_INCIDENT

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") INVALID_INCIDENT

    Invalid incident ID, type, earliestStartTime or latestEndTime.

### INCIDENT_ID_NOT_FOUND

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") INCIDENT_ID_NOT_FOUND

    Incident ID is not found in the system.

### INVALID_FILTER_OPTIONS

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") INVALID_FILTER_OPTIONS

    One or several filter options are invalid.

### INVALID_PARAMETER

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") INVALID_PARAMETER

    One or more input parameters in the query is not valid.

### INTERNAL_ERROR

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") INTERNAL_ERROR

    Internal error.

### OPERATION_CANCELLED

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") OPERATION_CANCELLED

    Operation cancelled.

### PROXY_AUTHENTICATION_FAILED

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") PROXY_AUTHENTICATION_FAILED

    Proxy is not authenticated. Check your proxy credentials.

### PROXY_SERVER_UNREACHABLE

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") PROXY_SERVER_UNREACHABLE

    Proxy server unreachable. Error indicates a problem with a proxy server's accessibility or connectivity.

### BAD_REQUEST

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") BAD_REQUEST

    Bad request. Error indicates server could not understand or process the request made by the client because the request itself was malformed or incorrect.

### TOO_MANY_REQUESTS

public static final [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") TOO_MANY_REQUESTS

    Server has received an excessive number of requests from client within a specific timeframe and client should slow down or wait before sending more requests.

## Method Details

### values

public static [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
