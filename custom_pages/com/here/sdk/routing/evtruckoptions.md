---
title: "EVTruckOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevtruckoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class EVTruckOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.EVTruckOptions
------------------------------------------------------------------------
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public final class EVTruckOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Deprecated.
Will be removed in v4.28.0. Use `RoutingOptions` class instead.
All the options to specify how a route for an electric truck should be calculated.

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

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TruckRoadType`](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport")`>`

  [avoidedTruckRoadTypes](#avoidedTruckRoadTypes)

Deprecated.

  Specifies a list of avoided truck road types for vehicle.

[`EVConsumptionModel`](sdk-for-android-explore-api-reference-latestevconsumptionmodel "class in com.here.sdk.routing")

  [consumptionModel](#consumptionModel)

Deprecated.

  Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")`>`

  [hazardousMaterials](#hazardousMaterials)

Deprecated.

  Specifies a list of hazardous materials shipped in the vehicle.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [lastCharacterOfLicensePlate](#lastCharacterOfLicensePlate)

Deprecated.

  Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones.

[`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")

  [linkTunnelCategory](#linkTunnelCategory)

Deprecated.

  Specifies the tunnel categories to restrict certain route links.

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

[`TruckSpecifications`](sdk-for-android-explore-api-reference-latesttruckspecifications "class in com.here.sdk.transport")

  [truckSpecifications](#truckSpecifications)

Deprecated.

  Detailed truck specifications such as dimensions and weight.

## Constructor Summary

Constructors

Constructor

  Description

  [EVTruckOptions](#%3Cinit%3E())`()`

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

### truckSpecifications

@NonNull public [TruckSpecifications](sdk-for-android-explore-api-reference-latesttruckspecifications "class in com.here.sdk.transport") truckSpecifications

    Deprecated.

    Detailed truck specifications such as dimensions and weight.

### linkTunnelCategory

@Nullable public [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") linkTunnelCategory

    Deprecated.

    Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to [`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") for the available options.

### hazardousMaterials

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")\> hazardousMaterials

    Deprecated.

    Specifies a list of hazardous materials shipped in the vehicle. Refer to [`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") for the available options.

### avoidedTruckRoadTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TruckRoadType](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport")\> avoidedTruckRoadTypes

    Deprecated.

    Specifies a list of avoided truck road types for vehicle. Refer to [`TruckRoadType`](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport") for the available options.

### consumptionModel

@NonNull public [EVConsumptionModel](sdk-for-android-explore-api-reference-latestevconsumptionmodel "class in com.here.sdk.routing") consumptionModel

    Deprecated.

    Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.

## Constructor Details

  - ()" class="section detail">

### EVTruckOptions

public EVTruckOptions()

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
