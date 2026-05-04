---
title: "VehicleSpecification.ScooterBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class VehicleSpecification.ScooterBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.transport.VehicleSpecification.ScooterBuilder
Enclosing class:
[VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")

------------------------------------------------------------------------
public static final class VehicleSpecification.ScooterBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a scooter.

## Constructor Summary

Constructors

Constructor

  Description

  [ScooterBuilder](#%3Cinit%3E())`()`

Creates a new instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")

  [build](#build())`()`

Builds the [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") object for [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) with the specifications taken from the [`VehicleSpecification.ScooterBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport") object.

[`VehicleSpecification.ScooterBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport")

  [withEngineSizeInCubicCentimeters](#withEngineSizeInCubicCentimeters(int))`(int engineSizeInCubicCentimeters)`

Sets the vehicle engine size in cubic centimeters.

[`VehicleSpecification.ScooterBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport")

  [withOccupancy](#withOccupancy(int))`(int occupancy)`

Sets the vehicle occupants number.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### ScooterBuilder

public ScooterBuilder()

    Creates a new instance of this class.

## Method Details

### withEngineSizeInCubicCentimeters

@NonNull public [VehicleSpecification.ScooterBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport") withEngineSizeInCubicCentimeters(int engineSizeInCubicCentimeters)

    Sets the vehicle engine size in cubic centimeters.
Parameters:
    `engineSizeInCubicCentimeters` -

    The vehicle engine size in cubic centimeters.

    Returns:
    The [`VehicleSpecification.ScooterBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport") object with the engine size set to the new value.

### withOccupancy

@NonNull public [VehicleSpecification.ScooterBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport") withOccupancy(int occupancy)

    Sets the vehicle occupants number.
Parameters:
    `occupancy` -

    The vehicle occupants number.

    Returns:
    The [`VehicleSpecification.ScooterBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport") object with the vehicle occupants number set to the new value.

### build

@NonNull public [VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") build()

    Builds the [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") object for [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) with the specifications taken from the [`VehicleSpecification.ScooterBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport") object.
Returns:
    The [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") object created from the [`VehicleSpecification.ScooterBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport") object.
