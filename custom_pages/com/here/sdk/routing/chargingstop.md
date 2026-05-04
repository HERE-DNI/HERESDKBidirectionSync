---
title: "ChargingStop (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestchargingstop"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ChargingStop

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ChargingStop
------------------------------------------------------------------------
public final class ChargingStop extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify a user-planned charging stop. **Note:** In order to specify this [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing"), it is also required to set \[sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours\], \[sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours\], and \[sdk.routing.BatterySpecifications.charging_curve\]. Without all of them, the route calculation will fail as an invalid parameter error.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [currentInAmperes](#currentInAmperes)

The value of rated current of the connector (in A).

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [maxDuration](#maxDuration)

The maximum duration the user plans to charge at the station, including [`BatterySpecifications.chargingSetupDuration`](sdk-for-android-explore-api-reference-latestbatteryspecifications#chargingSetupDuration).

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [minDuration](#minDuration)

The minimum duration the user expects to charge at the station, including [`BatterySpecifications.chargingSetupDuration`](sdk-for-android-explore-api-reference-latestbatteryspecifications#chargingSetupDuration).

`double`

  [powerInKilowatts](#powerInKilowatts)

The value of rated power of the connector (in kW).

[`ChargingSupplyType`](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing")

  [supplyType](#supplyType)

Supply type of the suggested connector.

`double`

  [voltageInVolts](#voltageInVolts)

The value of rated voltage of the connector (in V).

## Constructor Summary

Constructors

Constructor

  Description

  [ChargingStop](#%3Cinit%3E())`()`

Creates a new instance.

[ChargingStop](#%3Cinit%3E(double,double,double,com.here.sdk.routing.ChargingSupplyType,com.here.time.Duration,com.here.time.Duration))`(double powerInKilowatts, double currentInAmperes, double voltageInVolts, `[`ChargingSupplyType`](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing")` supplyType, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` minDuration, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` maxDuration)`

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

### powerInKilowatts

public double powerInKilowatts

    The value of rated power of the connector (in kW).

### currentInAmperes

public double currentInAmperes

    The value of rated current of the connector (in A).

### voltageInVolts

public double voltageInVolts

    The value of rated voltage of the connector (in V).

### supplyType

@Nullable public [ChargingSupplyType](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing") supplyType

    Supply type of the suggested connector.

### minDuration

@Nullable public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") minDuration

    The minimum duration the user expects to charge at the station, including [`BatterySpecifications.chargingSetupDuration`](sdk-for-android-explore-api-reference-latestbatteryspecifications#chargingSetupDuration). **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

### maxDuration

@Nullable public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") maxDuration

    The maximum duration the user plans to charge at the station, including [`BatterySpecifications.chargingSetupDuration`](sdk-for-android-explore-api-reference-latestbatteryspecifications#chargingSetupDuration). **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

## Constructor Details

  - ()" class="section detail">

### ChargingStop

public ChargingStop()

    Creates a new instance.

  - (double,double,double,com.here.sdk.routing.ChargingSupplyType,com.here.time.Duration,com.here.time.Duration)" class="section detail">

### ChargingStop

public ChargingStop(double powerInKilowatts, double currentInAmperes, double voltageInVolts, @Nullable [ChargingSupplyType](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing") supplyType, @Nullable [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") minDuration, @Nullable [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") maxDuration)

    Creates a new instance.
Parameters:
    `powerInKilowatts` -

    The value of rated power of the connector (in kW).

    `currentInAmperes` -

    The value of rated current of the connector (in A).

    `voltageInVolts` -

    The value of rated voltage of the connector (in V).

    `supplyType` -

    Supply type of the suggested connector.

    `minDuration` -

    The minimum duration the user expects to charge at the station, including [`BatterySpecifications.chargingSetupDuration`](sdk-for-android-explore-api-reference-latestbatteryspecifications#chargingSetupDuration). **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

    `maxDuration` -

    The maximum duration the user plans to charge at the station, including [`BatterySpecifications.chargingSetupDuration`](sdk-for-android-explore-api-reference-latestbatteryspecifications#chargingSetupDuration). **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
