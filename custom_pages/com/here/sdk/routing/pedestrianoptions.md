---
title: "PedestrianOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpedestrianoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PedestrianOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.PedestrianOptions
------------------------------------------------------------------------
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public final class PedestrianOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Deprecated.
Will be removed in v4.28.0. Use `RoutingOptions` class instead.
All the options to specify how a pedestrian route should be calculated.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing")

  [avoidanceOptions](#avoidanceOptions)

Deprecated.

  Options to specify restrictions for route calculations.

[`RouteOptions`](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing")

  [routeOptions](#routeOptions)

Deprecated.

  Specifies the common route calculation options.

[`RouteTextOptions`](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing")

  [textOptions](#textOptions)

Deprecated.

  Customize textual content returned from the route calculation, such as localization, format, and unit system.

`double`

  [walkSpeedInMetersPerSecond](#walkSpeedInMetersPerSecond)

Deprecated.

  Specifies the speed that will be used by the service as the walking speed for pedestrian routing in meters per second.

## Constructor Summary

Constructors

Constructor

  Description

  [PedestrianOptions](#%3Cinit%3E())`()`

Deprecated.

  Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods
  Deprecated Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

Deprecated.

`static `[`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing")

  [fromDefaultParameterConfiguration](#fromDefaultParameterConfiguration())`()`

Deprecated.

  Returns PedestrianOptions instance with default values used in SDK.

`int`

  [hashCode](#hashCode())`()`

Deprecated.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### routeOptions

@NonNull public [RouteOptions](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing") routeOptions

    Deprecated.

    Specifies the common route calculation options.

### textOptions

@NonNull public [RouteTextOptions](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing") textOptions

    Deprecated.

    Customize textual content returned from the route calculation, such as localization, format, and unit system.

### avoidanceOptions

@NonNull public [AvoidanceOptions](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing") avoidanceOptions

    Deprecated.

    Options to specify restrictions for route calculations. By default no restrictions are applied.

### walkSpeedInMetersPerSecond

public double walkSpeedInMetersPerSecond

    Deprecated.

    Specifies the speed that will be used by the service as the walking speed for pedestrian routing in meters per second. It influences the duration of walking segments along the route. The provided value must be in the range \[0.5, 2.0\]. When the value is outside this range, an invalid parameter error is raised. Refer to [`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") for details. The default speed is 1 meter per second.

## Constructor Details

  - ()" class="section detail">

### PedestrianOptions

public PedestrianOptions()

    Deprecated.

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)

    Deprecated.
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()

    Deprecated.
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### fromDefaultParameterConfiguration

@NonNull public static [PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing") fromDefaultParameterConfiguration()

    Deprecated.

    Returns PedestrianOptions instance with default values used in SDK.
Returns:
    A [`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing") instance with default values used in SDK.
