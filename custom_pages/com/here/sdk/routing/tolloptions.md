---
title: "TollOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttolloptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TollOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TollOptions
------------------------------------------------------------------------
public final class TollOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The option to specify how the tolls should be calculated. **Note** Not used for offline calculations.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [TollOptions.EmissionType](sdk-for-android-explore-api-reference-latesttolloptions-emissiontype)

Supported options of emission type

`static enum `

  [TollOptions.VehicleCategory](sdk-for-android-explore-api-reference-latesttolloptions-vehiclecategory)

Supported options of vehicle category for toll calculation.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [co2Class](#co2Class)

Defines the CO2 class of the vehicle as defined by the toll operator.

[`TollOptions.EmissionType`](sdk-for-android-explore-api-reference-latesttolloptions-emissiontype "enum class in com.here.sdk.routing")

  [emissionType](#emissionType)

Defines the emission type as defined by the toll operator for toll calculation based on vehicle emissions class.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [transponders](#transponders)

Specifies the toll collection systems for which the user has valid transponders.

[`TollOptions.VehicleCategory`](sdk-for-android-explore-api-reference-latesttolloptions-vehiclecategory "enum class in com.here.sdk.routing")

  [vehicleCategory](#vehicleCategory)

Defines special vehicle category for toll calculation.

## Constructor Summary

Constructors

Constructor

  Description

  [TollOptions](#%3Cinit%3E())`()`

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

### transponders

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> transponders

    Specifies the toll collection systems for which the user has valid transponders. Note: currently, the only valid value is "all". This means the user has a transponder that is accepted by all toll systems.

### vehicleCategory

@Nullable public [TollOptions.VehicleCategory](sdk-for-android-explore-api-reference-latesttolloptions-vehiclecategory "enum class in com.here.sdk.routing") vehicleCategory

    Defines special vehicle category for toll calculation. Usual types like car or truck are determined from transport mode.

### emissionType

@Nullable public [TollOptions.EmissionType](sdk-for-android-explore-api-reference-latesttolloptions-emissiontype "enum class in com.here.sdk.routing") emissionType

    Defines the emission type as defined by the toll operator for toll calculation based on vehicle emissions class. The emission type is based on the European emission standards (Euro 1 to Euro 6, and Euro EEV).

### co2Class

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) co2Class

    Defines the CO2 class of the vehicle as defined by the toll operator. CO2 class is used with `emissionType`. Allowed values for CO2 class are 1, 2, 3, 4, or 5, where a lower value generally indicates lower CO2 emissions.

## Constructor Details

  - ()" class="section detail">

### TollOptions

public TollOptions()

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
