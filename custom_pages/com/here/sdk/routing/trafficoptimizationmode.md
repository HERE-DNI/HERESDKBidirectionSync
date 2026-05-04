---
title: "TrafficOptimizationMode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficoptimizationmode"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class TrafficOptimizationMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.TrafficOptimizationMode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum TrafficOptimizationMode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")\>
Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [DISABLED](#DISABLED)

Traffic optimization is completely disabled, including long-term road closures.

[LONG_TERM_CLOSURES_ONLY](#LONG_TERM_CLOSURES_ONLY)

Only long-term road closures are taken into account.

[TIME_DEPENDENT](#TIME_DEPENDENT)

Traffic optimization is enabled, the shape of the route will be adjusted according to the traffic situation that depends on the [`RouteOptions.departureTime`](sdk-for-android-explore-api-reference-latestrouteoptions#departureTime) or [`RouteOptions.arrivalTime`](sdk-for-android-explore-api-reference-latestrouteoptions#arrivalTime).

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### TIME_DEPENDENT

public static final [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") TIME_DEPENDENT

    Traffic optimization is enabled, the shape of the route will be adjusted according to the traffic situation that depends on the [`RouteOptions.departureTime`](sdk-for-android-explore-api-reference-latestrouteoptions#departureTime) or [`RouteOptions.arrivalTime`](sdk-for-android-explore-api-reference-latestrouteoptions#arrivalTime). As a result, streets with heavy traffic will be avoided whenever possible. Note that this mode enables traffic-aware routing.

### LONG_TERM_CLOSURES_ONLY

public static final [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") LONG_TERM_CLOSURES_ONLY

    Only long-term road closures are taken into account. Both [`RouteOptions.departureTime`](sdk-for-android-explore-api-reference-latestrouteoptions#departureTime) and [`RouteOptions.arrivalTime`](sdk-for-android-explore-api-reference-latestrouteoptions#arrivalTime) are ignored, and the route will be shaped disregarding all the available current and historical traffic information, except long-term road closures. Note that this mode disables traffic-aware routing regardless of other settings.

### DISABLED

public static final [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") DISABLED

    Traffic optimization is completely disabled, including long-term road closures. Both [`RouteOptions.departureTime`](sdk-for-android-explore-api-reference-latestrouteoptions#departureTime) and [`RouteOptions.arrivalTime`](sdk-for-android-explore-api-reference-latestrouteoptions#arrivalTime) are ignored, and the route will be shaped disregarding all the available current and historical traffic information. Note that seasonal closures are not excluded. To exclude seasonal closures, use [`RoadFeatures.SEASONAL_CLOSURE`](sdk-for-android-explore-api-reference-latestroadfeatures#SEASONAL_CLOSURE). Note that this mode disables traffic-aware routing regardless of other settings.

## Method Details

### values

public static [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
