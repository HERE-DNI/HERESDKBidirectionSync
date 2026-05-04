---
title: "TransitRouteOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransitrouteoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransitRouteOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TransitRouteOptions
------------------------------------------------------------------------
public final class TransitRouteOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
All the options to specify how a public transit route should be calculated.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `int`

  [alternatives](#alternatives)

Number of alternative routes to return aside from the optimal route.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [arrivalTime](#arrivalTime)

Optional time when travel is expected to end.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [changes](#changes)

Maximum number of changes or transfers allowed in a route.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [departureTime](#departureTime)

Optional time when travel is expected to start.

[`TransitModeFilter`](sdk-for-android-explore-api-reference-latesttransitmodefilter "enum class in com.here.sdk.routing")

  [modeFilter](#modeFilter)

Defines inclusion or exclusion of transit modes for route calculation.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TransitMode`](sdk-for-android-explore-api-reference-latesttransitmode "enum class in com.here.sdk.routing")`>`

  [modes](#modes)

This list is used to determine which transit modes should be used for route calculation, [`modeFilter`](#modeFilter) specifies whether this list is an inclusion or an exclusion.

`int`

  [pedestrianMaxDistanceInMeters](#pedestrianMaxDistanceInMeters)

Maximum allowed walking distance in meters (e.g.

`double`

  [pedestrianSpeedInMetersPerSecond](#pedestrianSpeedInMetersPerSecond)

Walking speed in meters per second.

[`RouteTextOptions`](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing")

  [textOptions](#textOptions)

Customize textual content returned from the route calculation, such as localization, format, and unit system.

## Constructor Summary

Constructors

Constructor

  Description

  [TransitRouteOptions](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `static `[`TransitRouteOptions`](sdk-for-android-explore-api-reference-latesttransitrouteoptions "class in com.here.sdk.routing")

  [fromDefaultParameterConfiguration](#fromDefaultParameterConfiguration())`()`

Returns TransitRouteOptions instance with default values used in SDK.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### departureTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime

    Optional time when travel is expected to start. If it is not specified, it is set to the current time.

### arrivalTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime

    Optional time when travel is expected to end.

### alternatives

public int alternatives

    Number of alternative routes to return aside from the optimal route. The provided value must be in the range \[0, 6\]. By default, it is 0 and only one route is calculated.

### changes

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) changes

    Maximum number of changes or transfers allowed in a route. When it is not set, unlimited number of changes is permitted. The provided value must be in the range \[0, 6\].

### modeFilter

@NonNull public [TransitModeFilter](sdk-for-android-explore-api-reference-latesttransitmodefilter "enum class in com.here.sdk.routing") modeFilter

    Defines inclusion or exclusion of transit modes for route calculation. By default, the inclusion mode is used.

### modes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TransitMode](sdk-for-android-explore-api-reference-latesttransitmode "enum class in com.here.sdk.routing")\> modes

    This list is used to determine which transit modes should be used for route calculation, [`modeFilter`](#modeFilter) specifies whether this list is an inclusion or an exclusion. For example, specifying subway and bus transit modes with the include filter, returns only subway and bus transit modes, and with the exclude filter, returns all the transit modes except subway and bus. When not set, all the supported transit modes are permitted. By default, this list is empty.

### pedestrianSpeedInMetersPerSecond

public double pedestrianSpeedInMetersPerSecond

    Walking speed in meters per second. Influences the duration of walking segments from origin to a station, from a station to destination and in-between the stations (e.g. if transfer is needed). The provided value must be in the range \[0.5, 2.0\]. The default value is 1.0 mps.

### pedestrianMaxDistanceInMeters

public int pedestrianMaxDistanceInMeters

    Maximum allowed walking distance in meters (e.g. when looking for nearest stations). The provided value must be in the range \[0, 6000\]. The default value is 2000 meters.

### textOptions

@NonNull public [RouteTextOptions](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing") textOptions

    Customize textual content returned from the route calculation, such as localization, format, and unit system.

## Constructor Details

  - ()" class="section detail">

### TransitRouteOptions

public TransitRouteOptions()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### fromDefaultParameterConfiguration

@NonNull public static [TransitRouteOptions](sdk-for-android-explore-api-reference-latesttransitrouteoptions "class in com.here.sdk.routing") fromDefaultParameterConfiguration()

    Returns TransitRouteOptions instance with default values used in SDK.
Returns:
    An [`TransitRouteOptions`](sdk-for-android-explore-api-reference-latesttransitrouteoptions "class in com.here.sdk.routing") instance with default values used in SDK.
