---
title: "ElectricVehicleOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestelectricvehicleoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ElectricVehicleOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ElectricVehicleOptions
------------------------------------------------------------------------
public final class ElectricVehicleOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
These options define the parameters of the electric vehicle. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing")

  [batterySpecifications](#batterySpecifications)

Parameters that describe the electric vehicle's battery.

[`EmpiricalConsumptionModel`](sdk-for-android-explore-api-reference-latestempiricalconsumptionmodel "class in com.here.sdk.routing")

  [empiricalConsumptionModel](#empiricalConsumptionModel)

Defines the empirical consumption model.

`boolean`

  [ensureReachability](#ensureReachability)

Ensure that the vehicle does not run out of energy along the way.

[`EVMobilityServiceProviderPreferences`](sdk-for-android-explore-api-reference-latestevmobilityserviceproviderpreferences "class in com.here.sdk.routing")

  [evMobilityServiceProviderPreferences](#evMobilityServiceProviderPreferences)

Defines the preferred E-Mobility Service Providers.

[`PhysicalConsumptionModel`](sdk-for-android-explore-api-reference-latestphysicalconsumptionmodel "class in com.here.sdk.routing")

  [physicalConsumptionModel](#physicalConsumptionModel)

Defines the physical consumption model.

## Constructor Summary

Constructors

Constructor

  Description

  [ElectricVehicleOptions](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### ensureReachability

public boolean ensureReachability

    Ensure that the vehicle does not run out of energy along the way. Requires valid `battery_specifications`. It also requires that [`RouteOptions.optimizationMode`](sdk-for-android-explore-api-reference-latestrouteoptions#optimizationMode) = [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST), [`RouteOptions.speedCapInMetersPerSecond`](sdk-for-android-explore-api-reference-latestrouteoptions#speedCapInMetersPerSecond) is not set, and [`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing") is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations.

    **Note** An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) is generated when this option is set to `true` in case `sdk.routing.RoutingEngine.import_route` is called. Defaults to `false`.

    **Note** Not supported for offline routing.

    **Note** Only supported for car routing.

### evMobilityServiceProviderPreferences

@NonNull public [EVMobilityServiceProviderPreferences](sdk-for-android-explore-api-reference-latestevmobilityserviceproviderpreferences "class in com.here.sdk.routing") evMobilityServiceProviderPreferences

    Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used. **Note** Not yet supported for offline routing.

### empiricalConsumptionModel

@Nullable public [EmpiricalConsumptionModel](sdk-for-android-explore-api-reference-latestempiricalconsumptionmodel "class in com.here.sdk.routing") empiricalConsumptionModel

    Defines the empirical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.

### physicalConsumptionModel

@Nullable public [PhysicalConsumptionModel](sdk-for-android-explore-api-reference-latestphysicalconsumptionmodel "class in com.here.sdk.routing") physicalConsumptionModel

    Defines the physical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.

### batterySpecifications

@Nullable public [BatterySpecifications](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") batterySpecifications

    Parameters that describe the electric vehicle's battery. By default, it is set to `null`.

## Constructor Details

  - ()" class="section detail">

### ElectricVehicleOptions

public ElectricVehicleOptions()

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
