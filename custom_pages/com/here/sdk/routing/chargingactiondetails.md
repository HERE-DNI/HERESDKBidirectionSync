---
title: "ChargingActionDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestchargingactiondetails"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ChargingActionDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ChargingActionDetails
------------------------------------------------------------------------
public final class ChargingActionDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Parameters related to the electric vehicle's charging action.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [arrivalChargeInKilowattHours](#arrivalChargeInKilowattHours)

Estimated vehicle battery charge before this action (in kWh).

`double`

  [consumablePowerInKilowatts](#consumablePowerInKilowatts)

Maximum charging power (in kW) available to the vehicle, based on the properties of the charging station and the vehicle.

`double`

  [targetChargeInKilowattHours](#targetChargeInKilowattHours)

Level to which vehicle battery should be charged by this action (in kWh).

## Constructor Summary

Constructors

Constructor

  Description

  [ChargingActionDetails](#%3Cinit%3E())`()`

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

### consumablePowerInKilowatts

public double consumablePowerInKilowatts

    Maximum charging power (in kW) available to the vehicle, based on the properties of the charging station and the vehicle. A valid [`ChargingActionDetails`](sdk-for-android-explore-api-reference-latestchargingactiondetails "class in com.here.sdk.routing") object will have positive [`consumablePowerInKilowatts`](#consumablePowerInKilowatts). Defaults to 0.

### arrivalChargeInKilowattHours

public double arrivalChargeInKilowattHours

    Estimated vehicle battery charge before this action (in kWh). A valid [`ChargingActionDetails`](sdk-for-android-explore-api-reference-latestchargingactiondetails "class in com.here.sdk.routing") object will have positive [`arrivalChargeInKilowattHours`](#arrivalChargeInKilowattHours). Defaults to 0.

### targetChargeInKilowattHours

public double targetChargeInKilowattHours

    Level to which vehicle battery should be charged by this action (in kWh). A valid [`ChargingActionDetails`](sdk-for-android-explore-api-reference-latestchargingactiondetails "class in com.here.sdk.routing") object will have positive [`targetChargeInKilowattHours`](#targetChargeInKilowattHours). Defaults to 0.

## Constructor Details

  - ()" class="section detail">

### ChargingActionDetails

public ChargingActionDetails()

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
