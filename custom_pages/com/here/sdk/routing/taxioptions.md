---
title: "TaxiOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttaxioptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TaxiOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TaxiOptions
------------------------------------------------------------------------
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public final class TaxiOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Deprecated.
Will be removed in v4.28.0. Use `RoutingOptions` class instead.
All the options to specify how a taxi route should be calculated. See, [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI).

**Note:** Specify the optional [`Waypoint.sideOfStreetHint`](sdk-for-android-explore-api-reference-latestwaypoint#sideOfStreetHint) to indicate at which side of the street a passenger wants to leave the taxi.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [allowDriveThroughTaxiRoads](#allowDriveThroughTaxiRoads)

Deprecated.

  Specifies if a vehicle is allowed to drive through the taxi-only roads and lanes.

[`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing")

  [avoidanceOptions](#avoidanceOptions)

Deprecated.

  Options to specify restrictions for route calculations.

[`CarSpecifications`](sdk-for-android-explore-api-reference-latestcarspecifications "class in com.here.sdk.transport")

  [carSpecifications](#carSpecifications)

Deprecated.

  Detailed car specifications such as dimensions and weight.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [lastCharacterOfLicensePlate](#lastCharacterOfLicensePlate)

Deprecated.

  Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MaxSpeedOnSegment`](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")`>`

  [maxSpeedOnSegments](#maxSpeedOnSegments)

Deprecated.

  Segments with restriction on maximum [`DynamicSpeedInfo.baseSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo#baseSpeedInMetersPerSecond).

[`RouteOptions`](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing")

  [routeOptions](#routeOptions)

Deprecated.

  Specifies the common route calculation options.

[`RouteTextOptions`](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing")

  [textOptions](#textOptions)

Deprecated.

  Customize textual content returned from the route calculation, such as localization, format, and unit system.

[`TollOptions`](sdk-for-android-explore-api-reference-latesttolloptions "class in com.here.sdk.routing")

  [tollOptions](#tollOptions)

Deprecated.

  Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

## Constructor Summary

Constructors

Constructor

  Description

  [TaxiOptions](#%3Cinit%3E())`()`

Deprecated.

  Creates a new instance.

[TaxiOptions](#%3Cinit%3E(com.here.sdk.routing.RouteOptions,com.here.sdk.routing.RouteTextOptions,com.here.sdk.routing.AvoidanceOptions))`(`[`RouteOptions`](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing")` routeOptions, `[`RouteTextOptions`](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing")` textOptions, `[`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing")` avoidanceOptions)`

Deprecated.

  Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods
  Deprecated Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

Deprecated.

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

### tollOptions

@NonNull public [TollOptions](sdk-for-android-explore-api-reference-latesttolloptions "class in com.here.sdk.routing") tollOptions

    Deprecated.

    Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

### lastCharacterOfLicensePlate

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lastCharacterOfLicensePlate

    Deprecated.

    Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

    If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

### maxSpeedOnSegments

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MaxSpeedOnSegment](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")\> maxSpeedOnSegments

    Deprecated.

    Segments with restriction on maximum [`DynamicSpeedInfo.baseSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo#baseSpeedInMetersPerSecond).

### allowDriveThroughTaxiRoads

public boolean allowDriveThroughTaxiRoads

    Deprecated.

    Specifies if a vehicle is allowed to drive through the taxi-only roads and lanes. When set to `false`, it is still allowed on taxi roads after the route start and before the route destination.

### carSpecifications

@NonNull public [CarSpecifications](sdk-for-android-explore-api-reference-latestcarspecifications "class in com.here.sdk.transport") carSpecifications

    Deprecated.

    Detailed car specifications such as dimensions and weight.

## Constructor Details

  - ()" class="section detail">

### TaxiOptions

public TaxiOptions()

    Deprecated.

    Creates a new instance.

  - (com.here.sdk.routing.RouteOptions,com.here.sdk.routing.RouteTextOptions,com.here.sdk.routing.AvoidanceOptions)" class="section detail">

### TaxiOptions

public TaxiOptions(@NonNull [RouteOptions](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing") routeOptions, @NonNull [RouteTextOptions](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing") textOptions, @NonNull [AvoidanceOptions](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing") avoidanceOptions)

    Deprecated.

    Creates a new instance.
Parameters:
    `routeOptions` -

    Specifies the common route calculation options.

    `textOptions` -

    Customize textual content returned from the route calculation, such as localization, format, and unit system.

    `avoidanceOptions` -

    Options to specify restrictions for route calculations. By default no restrictions are applied.

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
