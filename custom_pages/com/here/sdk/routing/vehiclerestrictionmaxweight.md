---
title: "VehicleRestrictionMaxWeight (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweight"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class VehicleRestrictionMaxWeight

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.VehicleRestrictionMaxWeight
------------------------------------------------------------------------
public final class VehicleRestrictionMaxWeight extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`VehicleRestrictionMaxWeight` contains max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`VehicleRestrictionMaxWeightType`](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")

  [type](#type)

Represents the specific type of the maximum permitted weight restriction.

`int`

  [valueInKilograms](#valueInKilograms)

Max permitted weight during the trip, in kilograms.

## Constructor Summary

Constructors

Constructor

  Description

  [VehicleRestrictionMaxWeight](#%3Cinit%3E(int,com.here.sdk.routing.VehicleRestrictionMaxWeightType))`(int valueInKilograms, `[`VehicleRestrictionMaxWeightType`](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")` type)`

Created a new instance.

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

### valueInKilograms

public int valueInKilograms

    Max permitted weight during the trip, in kilograms.

### type

@NonNull public [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing") type

    Represents the specific type of the maximum permitted weight restriction.

## Constructor Details

  - (int,com.here.sdk.routing.VehicleRestrictionMaxWeightType)" class="section detail">

### VehicleRestrictionMaxWeight

public VehicleRestrictionMaxWeight(int valueInKilograms, @NonNull [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing") type)

    Created a new instance.
Parameters:
    `valueInKilograms` -

    Max permitted weight during the trip, in kilograms.

    `type` -

    Represents the specific type of the maximum permitted weight restriction.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
