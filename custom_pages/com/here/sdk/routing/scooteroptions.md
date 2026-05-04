---
title: "ScooterOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestscooteroptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ScooterOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ScooterOptions
------------------------------------------------------------------------
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public final class ScooterOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Deprecated.
Will be removed in v4.28.0. Use `RoutingOptions` class instead.
All the options to specify how a scooter route should be calculated.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [allowHighway](#allowHighway)

Deprecated.

  Specifies whether scooter is allowed on highway or not.

[`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing")

  [avoidanceOptions](#avoidanceOptions)

Deprecated.

  Options to specify restrictions for route calculations.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [engineSizeInCubicCentimeters](#engineSizeInCubicCentimeters)

Deprecated.

  Engine size of the scooter in cubic centimeters.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [lastCharacterOfLicensePlate](#lastCharacterOfLicensePlate)

Deprecated.

  Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MaxSpeedOnSegment`](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")`>`

  [maxSpeedOnSegments](#maxSpeedOnSegments)

Deprecated.

  Segments with restriction on maximum [`DynamicSpeedInfo.baseSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo#baseSpeedInMetersPerSecond).

`int`

  [occupantsNumber](#occupantsNumber)

Deprecated.

  Specifies the number of occupants in the vehicle, including driver.

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

  [ScooterOptions](#%3Cinit%3E())`()`

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

### occupantsNumber

public int occupantsNumber

    Deprecated.

    Specifies the number of occupants in the vehicle, including driver. Shouldn't be less than 1 or greater than 255. Defaults to 1. This option is only relevant for Japan and will be ignored for other countries.

### lastCharacterOfLicensePlate

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lastCharacterOfLicensePlate

    Deprecated.

    Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

    If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

### maxSpeedOnSegments

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MaxSpeedOnSegment](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")\> maxSpeedOnSegments

    Deprecated.

    Segments with restriction on maximum [`DynamicSpeedInfo.baseSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo#baseSpeedInMetersPerSecond).

### allowHighway

public boolean allowHighway

    Deprecated.

    Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. By default it is set to `false`. Note that there is a similar parameter in [`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing"), to disallow highway usage, see [`RoadFeatures.CONTROLLED_ACCESS_HIGHWAY`](sdk-for-android-explore-api-reference-latestroadfeatures#CONTROLLED_ACCESS_HIGHWAY). As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a [`SectionNotice`](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing") will be provided in the related [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") to indicate that the highway usage restriction is violated on this route. A few examples:

    1 - If no avoidance option is set, and `allowHighway = false`, when no route is found without highway usage, a notice is received.

    2 - If no avoidance option is set, and `allowHighway = true`, when no route is found without highway usage, no notice is received.

    3 - If only `avoid[features] = controlledAccessHighway` is set, when no route is found without highway usage, a notice is received.

    4 - If both `avoid[features] = controlledAccessHighway` and `allowHighway = true` are set, when no route is found without highway usage, a notice is received.

### engineSizeInCubicCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) engineSizeInCubicCentimeters

    Deprecated.

    Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value is `null`, which means the scooter route calculation ignores all engine size limits on the road.

    **Note:** For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.

## Constructor Details

  - ()" class="section detail">

### ScooterOptions

public ScooterOptions()

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
