---
title: "EVCarOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevcaroptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class EVCarOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.EVCarOptions
------------------------------------------------------------------------
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public final class EVCarOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Deprecated.
Will be removed in v4.28.0. Use `RoutingOptions` class instead.
All the options to specify how a route for an electric car should be calculated. At minimum, a valid [`EVConsumptionModel`](sdk-for-android-explore-api-reference-latestevconsumptionmodel "class in com.here.sdk.routing") must be set or the route calculation will fail.
Note: [`ensureReachability`](#ensureReachability) must be `true` to make sure that all stopovers are reachable. For this, charging stations may be added to the route. If [`ensureReachability`](#ensureReachability) is true, you need to specify the required route options and battery specifications that include the current charge level of the battery ([`BatterySpecifications.initialChargeInKilowattHours`](sdk-for-android-explore-api-reference-latestbatteryspecifications#initialChargeInKilowattHours)). See the parameter description below for more details.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`AllowOptions`](sdk-for-android-explore-api-reference-latestallowoptions "class in com.here.sdk.routing")

  [allowOptions](#allowOptions)

Deprecated.

  The options explicitly allowed by user for route calculations.

[`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing")

  [avoidanceOptions](#avoidanceOptions)

Deprecated.

  Options to specify restrictions for route calculations.

[`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing")

  [batterySpecifications](#batterySpecifications)

Deprecated.

  Parameters that describe the electric vehicle's battery.

[`CarSpecifications`](sdk-for-android-explore-api-reference-latestcarspecifications "class in com.here.sdk.transport")

  [carSpecifications](#carSpecifications)

Deprecated.

  Detailed car specifications such as dimensions and weight.

[`EVConsumptionModel`](sdk-for-android-explore-api-reference-latestevconsumptionmodel "class in com.here.sdk.routing")

  [consumptionModel](#consumptionModel)

Deprecated.

  Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.

`boolean`

  [ensureReachability](#ensureReachability)

Deprecated.

  Ensure that the vehicle does not run out of energy along the way.

[`EVMobilityServiceProviderPreferences`](sdk-for-android-explore-api-reference-latestevmobilityserviceproviderpreferences "class in com.here.sdk.routing")

  [evMobilityServiceProviderPreferences](#evMobilityServiceProviderPreferences)

Deprecated.

  Defines the preferred E-Mobility Service Providers.

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

  Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes.

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

  [EVCarOptions](#%3Cinit%3E())`()`

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

### allowOptions

@NonNull public [AllowOptions](sdk-for-android-explore-api-reference-latestallowoptions "class in com.here.sdk.routing") allowOptions

    Deprecated.

    The options explicitly allowed by user for route calculations. By default no options are opt in.

### occupantsNumber

public int occupantsNumber

    Deprecated.

    Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.

    **Note:** This parameter has no effect unless HOV and/or HOT lane usage is enabled via [`allowOptions`](#allowOptions) and such lanes are available in the selected country.

### lastCharacterOfLicensePlate

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lastCharacterOfLicensePlate

    Deprecated.

    Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

    If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

### maxSpeedOnSegments

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MaxSpeedOnSegment](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")\> maxSpeedOnSegments

    Deprecated.

    Segments with restriction on maximum [`DynamicSpeedInfo.baseSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo#baseSpeedInMetersPerSecond).

### ensureReachability

public boolean ensureReachability

    Deprecated.

    Ensure that the vehicle does not run out of energy along the way. Requires valid [`batterySpecifications`](#batterySpecifications). It also requires that [`RouteOptions.optimizationMode`](sdk-for-android-explore-api-reference-latestrouteoptions#optimizationMode) = [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST), [`RouteOptions.speedCapInMetersPerSecond`](sdk-for-android-explore-api-reference-latestrouteoptions#speedCapInMetersPerSecond) is not set, and [`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing") is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.EVCarOptions.ensure_reachability\] is set to `true` in case \[sdk.routing.RoutingEngine.import_route\] is called. Defaults to `false`.

### consumptionModel

@NonNull public [EVConsumptionModel](sdk-for-android-explore-api-reference-latestevconsumptionmodel "class in com.here.sdk.routing") consumptionModel

    Deprecated.

    Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.

### batterySpecifications

@NonNull public [BatterySpecifications](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") batterySpecifications

    Deprecated.

    Parameters that describe the electric vehicle's battery.

### carSpecifications

@NonNull public [CarSpecifications](sdk-for-android-explore-api-reference-latestcarspecifications "class in com.here.sdk.transport") carSpecifications

    Deprecated.

    Detailed car specifications such as dimensions and weight.

### evMobilityServiceProviderPreferences

@NonNull public [EVMobilityServiceProviderPreferences](sdk-for-android-explore-api-reference-latestevmobilityserviceproviderpreferences "class in com.here.sdk.routing") evMobilityServiceProviderPreferences

    Deprecated.

    Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used.

## Constructor Details

  - ()" class="section detail">

### EVCarOptions

public EVCarOptions()

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
