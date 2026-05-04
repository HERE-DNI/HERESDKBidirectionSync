---
title: "ChargingStation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestchargingstation"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ChargingStation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ChargingStation
------------------------------------------------------------------------
public final class ChargingStation extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Data for an electric vehicle charging station.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`NameID`](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")

  [brand](#brand)

Charging station brand.

[`NameID`](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")

  [chargePointOperator](#chargePointOperator)

Charging station charge-point-operator.

[`ChargingConnectorAttributes`](sdk-for-android-explore-api-reference-latestchargingconnectorattributes "class in com.here.sdk.routing")

  [connectorAttributes](#connectorAttributes)

Details of the connector suggested to be used.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [id](#id)

Identifier of this charging station.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`NameID`](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")`>`

  [matchingEMobilityServiceProviders](#matchingEMobilityServiceProviders)

List of matched E-Mobility Service Providers.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [name](#name)

Human readable name of this charging station.

## Constructor Summary

Constructors

Constructor

  Description

  [ChargingStation](#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` id, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`ChargingConnectorAttributes`](sdk-for-android-explore-api-reference-latestchargingconnectorattributes "class in com.here.sdk.routing")` connectorAttributes)`

Creates a new instance.

[ChargingStation](#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes,com.here.sdk.core.NameID,com.here.sdk.core.NameID,java.util.List))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` id, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`ChargingConnectorAttributes`](sdk-for-android-explore-api-reference-latestchargingconnectorattributes "class in com.here.sdk.routing")` connectorAttributes, `[`NameID`](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")` brand, `[`NameID`](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")` chargePointOperator, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`NameID`](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")`> matchingEMobilityServiceProviders)`

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

### id

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id

    Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

### name

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name

    Human readable name of this charging station. It can be null when there is no name associated with the station.

### connectorAttributes

@Nullable public [ChargingConnectorAttributes](sdk-for-android-explore-api-reference-latestchargingconnectorattributes "class in com.here.sdk.routing") connectorAttributes

    Details of the connector suggested to be used.

### brand

@Nullable public [NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core") brand

    Charging station brand. [`NameID.name`](sdk-for-android-explore-api-reference-latestnameid#name) reflect to charging station brand name. [`NameID.id`](sdk-for-android-explore-api-reference-latestnameid#id) reflect to charging station brand unique ID.

### chargePointOperator

@Nullable public [NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core") chargePointOperator

    Charging station charge-point-operator. [`NameID.name`](sdk-for-android-explore-api-reference-latestnameid#name) reflect to charge-point-operator name. [`NameID.id`](sdk-for-android-explore-api-reference-latestnameid#id) reflect to charge-point-operator ID.

### matchingEMobilityServiceProviders

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")\> matchingEMobilityServiceProviders

    List of matched E-Mobility Service Providers. Populated only when [`ElectricVehicleOptions.evMobilityServiceProviderPreferences`](sdk-for-android-explore-api-reference-latestelectricvehicleoptions#evMobilityServiceProviderPreferences) was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter [`ElectricVehicleOptions.evMobilityServiceProviderPreferences`](sdk-for-android-explore-api-reference-latestelectricvehicleoptions#evMobilityServiceProviderPreferences). [`NameID.name`](sdk-for-android-explore-api-reference-latestnameid#name) in each list item reflect to E-Mobility Service Provider name. [`NameID.id`](sdk-for-android-explore-api-reference-latestnameid#id) in each list item reflect to E-Mobility Service Provider id.

## Constructor Details

  - (java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes)" class="section detail">

### ChargingStation

public ChargingStation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @Nullable [ChargingConnectorAttributes](sdk-for-android-explore-api-reference-latestchargingconnectorattributes "class in com.here.sdk.routing") connectorAttributes)

    Creates a new instance.
Parameters:
    `id` -

    Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

    `name` -

    Human readable name of this charging station. It can be null when there is no name associated with the station.

    `connectorAttributes` -

    Details of the connector suggested to be used.
- (java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes,com.here.sdk.core.NameID,com.here.sdk.core.NameID,java.util.List)" class="section detail">

### ChargingStation

public ChargingStation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @Nullable [ChargingConnectorAttributes](sdk-for-android-explore-api-reference-latestchargingconnectorattributes "class in com.here.sdk.routing") connectorAttributes, @Nullable [NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core") brand, @Nullable [NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core") chargePointOperator, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")\> matchingEMobilityServiceProviders)

    Creates a new instance.
Parameters:
    `id` -

    Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

    `name` -

    Human readable name of this charging station. It can be null when there is no name associated with the station.

    `connectorAttributes` -

    Details of the connector suggested to be used.

    `brand` -

    Charging station brand. [`NameID.name`](sdk-for-android-explore-api-reference-latestnameid#name) reflect to charging station brand name. [`NameID.id`](sdk-for-android-explore-api-reference-latestnameid#id) reflect to charging station brand unique ID.

    `chargePointOperator` -

    Charging station charge-point-operator. [`NameID.name`](sdk-for-android-explore-api-reference-latestnameid#name) reflect to charge-point-operator name. [`NameID.id`](sdk-for-android-explore-api-reference-latestnameid#id) reflect to charge-point-operator ID.

    `matchingEMobilityServiceProviders` -

    List of matched E-Mobility Service Providers. Populated only when [`ElectricVehicleOptions.evMobilityServiceProviderPreferences`](sdk-for-android-explore-api-reference-latestelectricvehicleoptions#evMobilityServiceProviderPreferences) was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter [`ElectricVehicleOptions.evMobilityServiceProviderPreferences`](sdk-for-android-explore-api-reference-latestelectricvehicleoptions#evMobilityServiceProviderPreferences). [`NameID.name`](sdk-for-android-explore-api-reference-latestnameid#name) in each list item reflect to E-Mobility Service Provider name. [`NameID.id`](sdk-for-android-explore-api-reference-latestnameid#id) in each list item reflect to E-Mobility Service Provider id.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
