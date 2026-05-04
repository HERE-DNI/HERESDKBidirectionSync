---
title: "FuelStation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestfuelstation"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class FuelStation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.FuelStation
------------------------------------------------------------------------
public final class FuelStation extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains information about a specific fuel station.

Use [`PlaceCategory.BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION`](sdk-for-android-explore-api-reference-latestplacecategory#BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION) to find fuel stations. In the `Details` of a `Place` result you can find the associated fuel station information, if any.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GenericFuel`](sdk-for-android-explore-api-reference-latestgenericfuel "class in com.here.sdk.search")`>`

  [fuels](#fuels)

The list of car fuel types associated with the fuel station.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [highVolumePumps](#highVolumePumps)

Indicates if high volume pumps are available or not.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [payAtThePump](#payAtThePump)

Indicates if paying at the pump is supported or not.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TruckFuel`](sdk-for-android-explore-api-reference-latesttruckfuel "class in com.here.sdk.search")`>`

  [truckFuels](#truckFuels)

The list of truck fuel types associated with the fuel station.

## Constructor Summary

Constructors

Constructor

  Description

  [FuelStation](#%3Cinit%3E())`()`

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

### fuels

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GenericFuel](sdk-for-android-explore-api-reference-latestgenericfuel "class in com.here.sdk.search")\> fuels

    The list of car fuel types associated with the fuel station. The list can be empty when no generic fuels are offered or when the information is unknown.

### truckFuels

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TruckFuel](sdk-for-android-explore-api-reference-latesttruckfuel "class in com.here.sdk.search")\> truckFuels

    The list of truck fuel types associated with the fuel station. The list can be empty when no truck fuels are offered or when the information is unknown.

### payAtThePump

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) payAtThePump

    Indicates if paying at the pump is supported or not. `null` means information is unknown.

### highVolumePumps

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) highVolumePumps

    Indicates if high volume pumps are available or not. `null` means information is unknown.

## Constructor Details

  - ()" class="section detail">

### FuelStation

public FuelStation()

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
