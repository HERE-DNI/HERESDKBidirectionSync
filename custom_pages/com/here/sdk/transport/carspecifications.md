---
title: "CarSpecifications (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcarspecifications"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class CarSpecifications

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.CarSpecifications
------------------------------------------------------------------------
public final class CarSpecifications extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [axleCount](#axleCount)

Defines total number of axles in the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [grossWeightInKilograms](#grossWeightInKilograms)

Car weight including trailers and shipped goods in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [heightInCentimeters](#heightInCentimeters)

Car height in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [lengthInCentimeters](#lengthInCentimeters)

Car length in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [trailerAxleCount](#trailerAxleCount)

Defines total number of axles across all the trailers attached to the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [trailerCount](#trailerCount)

Defines number of trailers attached to the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [widthInCentimeters](#widthInCentimeters)

Car width in centimeters.

## Constructor Summary

Constructors

Constructor

  Description

  [CarSpecifications](#%3Cinit%3E())`()`

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

### grossWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) grossWeightInKilograms

    Car weight including trailers and shipped goods in kilograms. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.

### heightInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) heightInCentimeters

    Car height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

### widthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) widthInCentimeters

    Car width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

### lengthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lengthInCentimeters

    Car length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

### axleCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) axleCount

    Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. When specifying [`trailerAxleCount`](#trailerAxleCount), then [`axleCount`](#axleCount) is required and must be greater than [`trailerAxleCount`](#trailerAxleCount).

### trailerCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) trailerCount

    Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 1\]. By default, it is not set. When specifying [`trailerAxleCount`](#trailerAxleCount), then [`trailerCount`](#trailerCount) is required and must be greater than 0.

### trailerAxleCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) trailerAxleCount

    Defines total number of axles across all the trailers attached to the vehicle. This number is included in [`axleCount`](#axleCount), hence [`trailerAxleCount`](#trailerAxleCount) must be less than [`axleCount`](#axleCount) and greater than or equal to 1. [`axleCount`](#axleCount) and [`trailerCount`](#trailerCount) are required to specify [`trailerAxleCount`](#trailerAxleCount). By default, it is not set.

## Constructor Details

  - ()" class="section detail">

### CarSpecifications

public CarSpecifications()

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
