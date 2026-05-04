---
title: "BatterySpecifications (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestbatteryspecifications"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class BatterySpecifications

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.BatterySpecifications
------------------------------------------------------------------------
public final class BatterySpecifications extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Parameters related to the electric vehicle's battery.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`>`

  [chargingCurve](#chargingCurve)

Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh).

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [chargingSetupDuration](#chargingSetupDuration)

Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`>`

  [connectorTypes](#connectorTypes)

List of available charging connector types.

`double`

  [initialChargeInKilowattHours](#initialChargeInKilowattHours)

Charge level of the vehicle's battery at the start of the route (in kWh).

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxChargingCurrentInAmperes](#maxChargingCurrentInAmperes)

Maximum charging current supported by the vehicle's battery in Amperes.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxChargingVoltageInVolts](#maxChargingVoltageInVolts)

Maximum charging voltage supported by the vehicle's battery in Volts.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxPowerAtLowVoltageInKilowatts](#maxPowerAtLowVoltageInKilowatts)

The maximum power in kilowatts at which a vehicle can charge under given these conditions: The charging station connector's maximum supply voltage is less than 800 V. [`maxChargingVoltageInVolts`](#maxChargingVoltageInVolts) is greater than or equal to 800 V.

`double`

  [minChargeAtChargingStationInKilowattHours](#minChargeAtChargingStationInKilowattHours)

Minimum charge when arriving at a charging station in kWh.

`double`

  [minChargeAtDestinationInKilowattHours](#minChargeAtDestinationInKilowattHours)

Minimum charge at the final route destination in kWh.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [minChargeAtFirstChargingStationInKilowattHours](#minChargeAtFirstChargingStationInKilowattHours)

Minimum charge when arriving at first charging station in kWh.

`double`

  [targetChargeInKilowattHours](#targetChargeInKilowattHours)

Maximum charge to which the battery should be charged at a charging station (in kWh).

`double`

  [totalCapacityInKilowattHours](#totalCapacityInKilowattHours)

Total capacity of the vehicle's battery (in kWh).

## Constructor Summary

Constructors

Constructor

  Description

  [BatterySpecifications](#%3Cinit%3E())`()`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double))`(double totalCapacityInKilowattHours)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes, double minChargeAtChargingStationInKilowattHours)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes, double minChargeAtChargingStationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` minChargeAtFirstChargingStationInKilowattHours)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes, double minChargeAtChargingStationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes, double minChargeAtChargingStationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxChargingVoltageInVolts)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes, double minChargeAtChargingStationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxChargingVoltageInVolts, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxChargingCurrentInAmperes)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes, double minChargeAtChargingStationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxChargingVoltageInVolts, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxChargingCurrentInAmperes, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` chargingSetupDuration)`

Creates a new instance.

[BatterySpecifications](#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration,java.lang.Double))`(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> chargingCurve, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`> connectorTypes, double minChargeAtChargingStationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxChargingVoltageInVolts, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxChargingCurrentInAmperes, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` chargingSetupDuration, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` maxPowerAtLowVoltageInKilowatts)`

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

### totalCapacityInKilowattHours

public double totalCapacityInKilowattHours

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

### initialChargeInKilowattHours

public double initialChargeInKilowattHours

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

### targetChargeInKilowattHours

public double targetChargeInKilowattHours

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

### chargingCurve

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

### connectorTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

### minChargeAtChargingStationInKilowattHours

public double minChargeAtChargingStationInKilowattHours

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

### minChargeAtFirstChargingStationInKilowattHours

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minChargeAtFirstChargingStationInKilowattHours

    Minimum charge when arriving at first charging station in kWh. This overrides [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) for the first charging station. If not specified, [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

### minChargeAtDestinationInKilowattHours

public double minChargeAtDestinationInKilowattHours

    Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

### maxChargingVoltageInVolts

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingVoltageInVolts

    Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `null`.

### maxChargingCurrentInAmperes

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingCurrentInAmperes

    Maximum charging current supported by the vehicle's battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to `null`.

### chargingSetupDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") chargingSetupDuration

    Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing. Defaults to 0 seconds.

### maxPowerAtLowVoltageInKilowatts

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxPowerAtLowVoltageInKilowatts

    The maximum power in kilowatts at which a vehicle can charge under given these conditions:

    - The charging station connector's maximum supply voltage is less than 800 V.
    - [`maxChargingVoltageInVolts`](#maxChargingVoltageInVolts) is greater than or equal to 800 V. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** The feature is not supported by the `OfflineRoutingEngine`.

## Constructor Details

  - ()" class="section detail">

### BatterySpecifications

public BatterySpecifications()

    Creates a new instance.

  - (double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.
- (double,double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.
- (double,double,double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.
- (double,double,double,java.util.Map)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.
- (double,double,double,java.util.Map,java.util.List)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.
- (double,double,double,java.util.Map,java.util.List,double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes, double minChargeAtChargingStationInKilowattHours)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.
- (double,double,double,java.util.Map,java.util.List,double,java.lang.Double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes, double minChargeAtChargingStationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minChargeAtFirstChargingStationInKilowattHours)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This overrides [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) for the first charging station. If not specified, [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.
- (double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes, double minChargeAtChargingStationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This overrides [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) for the first charging station. If not specified, [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.
- (double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes, double minChargeAtChargingStationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingVoltageInVolts)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This overrides [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) for the first charging station. If not specified, [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `null`.
- (double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes, double minChargeAtChargingStationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingVoltageInVolts, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingCurrentInAmperes)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This overrides [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) for the first charging station. If not specified, [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `null`.

    `maxChargingCurrentInAmperes` -

    Maximum charging current supported by the vehicle's battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to `null`.
- (double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes, double minChargeAtChargingStationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingVoltageInVolts, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingCurrentInAmperes, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") chargingSetupDuration)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This overrides [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) for the first charging station. If not specified, [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `null`.

    `maxChargingCurrentInAmperes` -

    Maximum charging current supported by the vehicle's battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to `null`.

    `chargingSetupDuration` -

    Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing. Defaults to 0 seconds.
- (double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration,java.lang.Double)" class="section detail">

### BatterySpecifications

public BatterySpecifications(double totalCapacityInKilowattHours, double initialChargeInKilowattHours, double targetChargeInKilowattHours, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> chargingCurve, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes, double minChargeAtChargingStationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minChargeAtFirstChargingStationInKilowattHours, double minChargeAtDestinationInKilowattHours, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingVoltageInVolts, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxChargingCurrentInAmperes, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") chargingSetupDuration, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxPowerAtLowVoltageInKilowatts)

    Creates a new instance.
Parameters:
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of [`totalCapacityInKilowattHours`](#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, [`targetChargeInKilowattHours`](#targetChargeInKilowattHours)\], otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one charging connector type added, otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This overrides [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) for the first charging station. If not specified, [`minChargeAtChargingStationInKilowattHours`](#minChargeAtChargingStationInKilowattHours) will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of [`targetChargeInKilowattHours`](#targetChargeInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `null`.

    `maxChargingCurrentInAmperes` -

    Maximum charging current supported by the vehicle's battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to `null`.

    `chargingSetupDuration` -

    Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing. Defaults to 0 seconds.

    `maxPowerAtLowVoltageInKilowatts` -

    The maximum power in kilowatts at which a vehicle can charge under given these conditions:

    - The charging station connector's maximum supply voltage is less than 800 V.
    - [`maxChargingVoltageInVolts`](#maxChargingVoltageInVolts) is greater than or equal to 800 V. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** The feature is not supported by the `OfflineRoutingEngine`.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
