---
title: "RoutingOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutingoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RoutingOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RoutingOptions
------------------------------------------------------------------------
public final class RoutingOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options defines how a route should be calculated.

The options are used for all transport modes and engines.

\*\* Electric vehicle specific requirements \*\* Electric vehicle consumption are estimated when at least one consumption model is defined. Currently two models are supported:

- PhysicalConsumptionModel Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:
  - [`VehicleSpecification.currentWeightInKilograms`](sdk-for-android-explore-api-reference-latestvehiclespecification#currentWeightInKilograms) from [`TransportSpecification.vehicleSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification#vehicleSpecification) from [`transportSpecification`](#transportSpecification)
  - Additionally [`Waypoint.currentWeightChangeInKilograms`](sdk-for-android-explore-api-reference-latestwaypoint#currentWeightChangeInKilograms) can be defined.
- EmpiricalConsumptionModel

By setting [`ElectricVehicleOptions.ensureReachability`](sdk-for-android-explore-api-reference-latestelectricvehicleoptions#ensureReachability) the `RoutingEngine` inserts additional charging stations to reach the waypoints. This feature requires setting the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing"). By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints. See the parameter description below for more details.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`AllowOptions`](sdk-for-android-explore-api-reference-latestallowoptions "class in com.here.sdk.routing")

  [allowOptions](#allowOptions)

The options explicitly allowed by user for route calculations.

[`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing")

  [avoidanceOptions](#avoidanceOptions)

Options to specify restrictions for route calculations.

[`ElectricVehicleOptions`](sdk-for-android-explore-api-reference-latestelectricvehicleoptions "class in com.here.sdk.routing")

  [evOptions](#evOptions)

Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MaxSpeedOnSegment`](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")`>`

  [maxSpeedOnSegments](#maxSpeedOnSegments)

Segments with restriction on maximum [`DynamicSpeedInfo.baseSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo#baseSpeedInMetersPerSecond).

[`RouteOptions`](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing")

  [routeOptions](#routeOptions)

Specifies the common route calculation options.

[`RouteTextOptions`](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing")

  [textOptions](#textOptions)

Customize textual content returned from the route calculation, such as localization, format, and unit system.

[`TollOptions`](sdk-for-android-explore-api-reference-latesttolloptions "class in com.here.sdk.routing")

  [tollOptions](#tollOptions)

Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

[`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport")

  [transportSpecification](#transportSpecification)

Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen.

## Constructor Summary

Constructors

Constructor

  Description

  [RoutingOptions](#%3Cinit%3E())`()`

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

  `static `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")

  [fromDefaultParameterConfiguration](#fromDefaultParameterConfiguration())`()`

Returns the default configuration for the transport specification selected in [`ParameterConfiguration.transportSpecification`](sdk-for-android-explore-api-reference-latestparameterconfiguration#transportSpecification) from [`SDKNativeEngine.getParameterConfig()`](sdk-for-android-explore-api-reference-latestsdknativeengine#getParameterConfig()).

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### transportSpecification

@NonNull public [TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") transportSpecification

    Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen. **Notes:**

    - The transport mode [`TransportMode.PUBLIC_TRANSIT`](sdk-for-android-explore-api-reference-latesttransportmode#PUBLIC_TRANSIT) is not supported.
    - By default all vehicle specifications from [`transportSpecification`](#transportSpecification) are set to `null` and the [`TransportSpecification.transportMode`](sdk-for-android-explore-api-reference-latesttransportspecification#transportMode) from [`transportSpecification`](#transportSpecification) is set to [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR).
    - A route can be calculated with only the [`TransportSpecification.transportMode`](sdk-for-android-explore-api-reference-latesttransportspecification#transportMode) from [`transportSpecification`](#transportSpecification) set.
    - It is highly recommended to define the [`TruckCategory`](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport") that is being used in [`VehicleSpecification.truckCategory`](sdk-for-android-explore-api-reference-latestvehiclespecification#truckCategory) from [`TransportSpecification.vehicleSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification#vehicleSpecification) from [`transportSpecification`](#transportSpecification), if the [`TransportSpecification.transportMode`](sdk-for-android-explore-api-reference-latesttransportspecification#transportMode) from [`transportSpecification`](#transportSpecification) is set to [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK).
    - The [`VehicleSpecification.occupancy`](sdk-for-android-explore-api-reference-latestvehiclespecification#occupancy) from [`TransportSpecification.vehicleSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification#vehicleSpecification) won't have effect if HOV and/or HOT lane usage is not allowed using [`EVTruckOptions.allowOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions#allowOptions).
    - The [`PedestrianSpecification.walkingSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestpedestrianspecification#walkingSpeedInMetersPerSecond) from [`TransportSpecification.pedestrianSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification#pedestrianSpecification) if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking along the route. The provided value must be in the range \[0.5, 2.0\]. When the value is outside this range, an invalid parameter error is raised. Refer to [`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") for details. The default speed is 1 meter per second.

### routeOptions

@NonNull public [RouteOptions](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing") routeOptions

    Specifies the common route calculation options.

### textOptions

@NonNull public [RouteTextOptions](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing") textOptions

    Customize textual content returned from the route calculation, such as localization, format, and unit system.

### avoidanceOptions

@NonNull public [AvoidanceOptions](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing") avoidanceOptions

    Options to specify restrictions for route calculations. By default no restrictions are applied.

### allowOptions

@NonNull public [AllowOptions](sdk-for-android-explore-api-reference-latestallowoptions "class in com.here.sdk.routing") allowOptions

    The options explicitly allowed by user for route calculations. By default no options are opt in.

### tollOptions

@NonNull public [TollOptions](sdk-for-android-explore-api-reference-latesttolloptions "class in com.here.sdk.routing") tollOptions

    Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type. **Note** Not used for offline calculations.

### maxSpeedOnSegments

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MaxSpeedOnSegment](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")\> maxSpeedOnSegments

    Segments with restriction on maximum [`DynamicSpeedInfo.baseSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo#baseSpeedInMetersPerSecond). **Note** Not used for offline calculations.

### evOptions

@Nullable public [ElectricVehicleOptions](sdk-for-android-explore-api-reference-latestelectricvehicleoptions "class in com.here.sdk.routing") evOptions

    Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability. When no EV options are defined an internal combustion engine is assumed.

## Constructor Details

  - ()" class="section detail">

### RoutingOptions

public RoutingOptions()

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

@NonNull public static [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") fromDefaultParameterConfiguration()

    Returns the default configuration for the transport specification selected in [`ParameterConfiguration.transportSpecification`](sdk-for-android-explore-api-reference-latestparameterconfiguration#transportSpecification) from [`SDKNativeEngine.getParameterConfig()`](sdk-for-android-explore-api-reference-latestsdknativeengine#getParameterConfig()). **Note** By default, the \[sdk.core.ParameterConfiguration.transport_specification\] from \[sdk.core.engine.SDKNativeEngine.parameter_config\] will return a valid [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object with the \[sdk.transport.TransportSpecification.transport_mode\] set to [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR).
Returns:
    The [`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") object with the default configuration for the transport specification selected in [`ParameterConfiguration.transportSpecification`](sdk-for-android-explore-api-reference-latestparameterconfiguration#transportSpecification) from [`SDKNativeEngine.getParameterConfig()`](sdk-for-android-explore-api-reference-latestsdknativeengine#getParameterConfig()).
