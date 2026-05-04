---
title: "PassThroughFeature (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpassthroughfeature"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class PassThroughFeature

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")\>
com.here.sdk.core.engine.PassThroughFeature
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`PassThroughFeature`](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum PassThroughFeature extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")\>
Represents features that are allowed to consume online data when the HERE SDK's offline mode is activated via [`SDKNativeEngine.isOfflineMode()`](sdk-for-android-explore-api-reference-latestsdknativeengine#isOfflineMode()) and/or [`SDKOptions.offlineMode`](sdk-for-android-explore-api-reference-latestsdkoptions#offlineMode).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ONLINE_ROUTING](#ONLINE_ROUTING)

When set, online routing can be performed by the HERE SDK, allowing the retrieval of up-to-date routing information from online services even when offline mode is enabled.

[ONLINE_SEARCH](#ONLINE_SEARCH)

When set, online search can be performed by the HERE SDK, allowing the retrieval of up-to-date search information from online services even when offline mode is enabled.

[TRAFFIC_DATA](#TRAFFIC_DATA)

When set, then the `TrafficEngine` is not blocked from initiating online connections to search for traffic data such as incidents.

[TRAFFIC_TILES_FLOW](#TRAFFIC_TILES_FLOW)

When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic flow data.

[TRAFFIC_TILES_INCIDENTS](#TRAFFIC_TILES_INCIDENTS)

When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic incident data.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`PassThroughFeature`](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`PassThroughFeature`](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### TRAFFIC_DATA

public static final [PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine") TRAFFIC_DATA

    When set, then the `TrafficEngine` is not blocked from initiating online connections to search for traffic data such as incidents.

### TRAFFIC_TILES_FLOW

public static final [PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine") TRAFFIC_TILES_FLOW

    When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic flow data.

### TRAFFIC_TILES_INCIDENTS

public static final [PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine") TRAFFIC_TILES_INCIDENTS

    When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic incident data.

### ONLINE_ROUTING

public static final [PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine") ONLINE_ROUTING

    When set, online routing can be performed by the HERE SDK, allowing the retrieval of up-to-date routing information from online services even when offline mode is enabled.

### ONLINE_SEARCH

public static final [PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine") ONLINE_SEARCH

    When set, online search can be performed by the HERE SDK, allowing the retrieval of up-to-date search information from online services even when offline mode is enabled.

## Method Details

### values

public static [PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
