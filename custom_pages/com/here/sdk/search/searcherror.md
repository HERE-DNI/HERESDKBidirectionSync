---
title: "SearchError (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsearcherror"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class SearchError

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")\>
com.here.sdk.search.SearchError
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum SearchError extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")\>
Specifies possible errors that may result from a search query.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [AUTHENTICATION_FAILED](#AUTHENTICATION_FAILED)

Search operation is not authenticated.

[BAD_REQUEST](#BAD_REQUEST)

Bad network request

[EXCEEDED_USAGE_LIMIT](#EXCEEDED_USAGE_LIMIT)

Credentials exceeded the allowed requests limit.

[FILTER_EMPTY](#FILTER_EMPTY)

Filter is empty

[FILTER_TOO_LONG](#FILTER_TOO_LONG)

Filter is too long, max.

[FORBIDDEN](#FORBIDDEN)

The credentials given do not provide access to the resource requested.

[HTTP_ERROR](#HTTP_ERROR)

Network request error.

[INVALID_AREA](#INVALID_AREA)

Box or circle area of query is invalid

[INVALID_CORRIDOR_POLYLINE](#INVALID_CORRIDOR_POLYLINE)

Corridor area polyline size is less than 2 points

[INVALID_CUSTOM_OPTION_FORMAT](#INVALID_CUSTOM_OPTION_FORMAT)

Custom options are set in an invalid format in the query

[INVALID_TRUCK_CLASS](#INVALID_TRUCK_CLASS)

Light truck class is passed in the filter

[INVALID_URL](#INVALID_URL)

Url is invalid

[LAYERS_NOT_DOWNLOADED](#LAYERS_NOT_DOWNLOADED)

Downloaded regions missing [`LayerConfiguration.Feature.OFFLINE_SEARCH_GLOBAL`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_SEARCH_GLOBAL) feature.

[MAP_NOT_READY](#MAP_NOT_READY)

Offline map data is incomplete for the requested operation.

[MAX_ITEMS_OUT_OF_RANGE](#MAX_ITEMS_OUT_OF_RANGE)

Should be in the range \[1, 100\].

[NO_RESULTS_FOUND](#NO_RESULTS_FOUND)

No results found.

[OFFLINE](#OFFLINE)

The device does not have an internet connection.

[OPERATION_CANCELLED](#OPERATION_CANCELLED)

Operation cancelled.

[OPERATION_FAILED](#OPERATION_FAILED)

Operation failed due to an internal error.

[PARSING_ERROR](#PARSING_ERROR)

Error while parsing response data.

[PROXY_AUTHENTICATION_FAILED](#PROXY_AUTHENTICATION_FAILED)

Proxy is not authenticated.

[PROXY_SERVER_UNREACHABLE](#PROXY_SERVER_UNREACHABLE)

Proxy server unreachable.

[QUERY_EMPTY](#QUERY_EMPTY)

Empty query

[QUERY_TOO_LONG](#QUERY_TOO_LONG)

Query is too long, max.

[SERVER_UNREACHABLE](#SERVER_UNREACHABLE)

Server unreachable.

[TIMED_OUT](#TIMED_OUT)

The request timed out.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### AUTHENTICATION_FAILED

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") AUTHENTICATION_FAILED

    Search operation is not authenticated. Check your credentials.

### MAX_ITEMS_OUT_OF_RANGE

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") MAX_ITEMS_OUT_OF_RANGE

    Should be in the range \[1, 100\].

### PARSING_ERROR

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") PARSING_ERROR

    Error while parsing response data.

### NO_RESULTS_FOUND

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") NO_RESULTS_FOUND

    No results found.

### HTTP_ERROR

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") HTTP_ERROR

    Network request error.

### SERVER_UNREACHABLE

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") SERVER_UNREACHABLE

    Server unreachable.

### FORBIDDEN

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") FORBIDDEN

    The credentials given do not provide access to the resource requested.

### EXCEEDED_USAGE_LIMIT

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") EXCEEDED_USAGE_LIMIT

    Credentials exceeded the allowed requests limit.

### OPERATION_FAILED

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") OPERATION_FAILED

    Operation failed due to an internal error.

### OPERATION_CANCELLED

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") OPERATION_CANCELLED

    Operation cancelled.

### TIMED_OUT

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") TIMED_OUT

    The request timed out.

### OFFLINE

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") OFFLINE

    The device does not have an internet connection.

### QUERY_TOO_LONG

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") QUERY_TOO_LONG

    Query is too long, max. size is 300 characters.

### FILTER_TOO_LONG

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") FILTER_TOO_LONG

    Filter is too long, max. size is 300 characters.

### PROXY_AUTHENTICATION_FAILED

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") PROXY_AUTHENTICATION_FAILED

    Proxy is not authenticated. Check your proxy credentials.

### PROXY_SERVER_UNREACHABLE

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") PROXY_SERVER_UNREACHABLE

    Proxy server unreachable.

### QUERY_EMPTY

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") QUERY_EMPTY

    Empty query

### INVALID_AREA

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") INVALID_AREA

    Box or circle area of query is invalid

### FILTER_EMPTY

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") FILTER_EMPTY

    Filter is empty

### INVALID_CORRIDOR_POLYLINE

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") INVALID_CORRIDOR_POLYLINE

    Corridor area polyline size is less than 2 points

### INVALID_URL

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") INVALID_URL

    Url is invalid

### INVALID_CUSTOM_OPTION_FORMAT

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") INVALID_CUSTOM_OPTION_FORMAT

    Custom options are set in an invalid format in the query

### INVALID_TRUCK_CLASS

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") INVALID_TRUCK_CLASS

    Light truck class is passed in the filter

### BAD_REQUEST

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") BAD_REQUEST

    Bad network request

### MAP_NOT_READY

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") MAP_NOT_READY

    Offline map data is incomplete for the requested operation. Regions are not downloaded or are in the `Pending` state.

    **Note:** This is an alpha release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### LAYERS_NOT_DOWNLOADED

public static final [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") LAYERS_NOT_DOWNLOADED

    Downloaded regions missing [`LayerConfiguration.Feature.OFFLINE_SEARCH_GLOBAL`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_SEARCH_GLOBAL) feature. Update or redownload regions with enabled feature.

    **Note:** This is an alpha release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Method Details

### values

public static [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
