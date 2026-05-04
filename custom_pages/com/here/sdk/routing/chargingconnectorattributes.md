---
title: "ChargingConnectorAttributes (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestchargingconnectorattributes"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ChargingConnectorAttributes

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ChargingConnectorAttributes
------------------------------------------------------------------------
public final class ChargingConnectorAttributes extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Details of the connector that is suggested to be used in the section's [`PostAction`](sdk-for-android-explore-api-reference-latestpostaction "class in com.here.sdk.routing")'s for charging.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")

  [connectorType](#connectorType)

Suggested connector for charging at this station.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [currentInAmperes](#currentInAmperes)

Current of the suggested connector in Amperes.

`double`

  [powerInKilowatts](#powerInKilowatts)

Power supplied by the suggested connector in kW.

[`ChargingSupplyType`](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing")

  [supplyType](#supplyType)

Supply type of the suggested connector.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [voltageInVolts](#voltageInVolts)

Voltage of the suggested connector in Volts.

## Constructor Summary

Constructors

Constructor

  Description

  [ChargingConnectorAttributes](#%3Cinit%3E(double,java.lang.Double,java.lang.Double,com.here.sdk.routing.ChargingSupplyType,com.here.sdk.routing.ChargingConnectorType))`(double powerInKilowatts, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` currentInAmperes, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` voltageInVolts, `[`ChargingSupplyType`](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing")` supplyType, `[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")` connectorType)`

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

    Power supplied by the suggested connector in kW.

### currentInAmperes

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) currentInAmperes

    Current of the suggested connector in Amperes.

### voltageInVolts

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) voltageInVolts

    Voltage of the suggested connector in Volts.

### supplyType

@Nullable public [ChargingSupplyType](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing") supplyType

    Supply type of the suggested connector.

### connectorType

@Nullable public [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") connectorType

    Suggested connector for charging at this station.

## Constructor Details

  - (double,java.lang.Double,java.lang.Double,com.here.sdk.routing.ChargingSupplyType,com.here.sdk.routing.ChargingConnectorType)" class="section detail">

### ChargingConnectorAttributes

public ChargingConnectorAttributes(double powerInKilowatts, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) currentInAmperes, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) voltageInVolts, @Nullable [ChargingSupplyType](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing") supplyType, @Nullable [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") connectorType)

    Creates a new instance.
Parameters:
    `powerInKilowatts` -

    Power supplied by the suggested connector in kW.

    `currentInAmperes` -

    Current of the suggested connector in Amperes.

    `voltageInVolts` -

    Voltage of the suggested connector in Volts.

    `supplyType` -

    Supply type of the suggested connector.

    `connectorType` -

    Suggested connector for charging at this station.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
