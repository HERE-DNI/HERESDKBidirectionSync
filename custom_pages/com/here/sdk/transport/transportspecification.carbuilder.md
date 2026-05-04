---
title: "TransportSpecification.CarBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransportSpecification.CarBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.transport.TransportSpecification.CarBuilder
Enclosing class:
[TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport")

------------------------------------------------------------------------
public static final class TransportSpecification.CarBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a car.

## Constructor Summary

Constructors

Constructor

  Description

  [CarBuilder](#%3Cinit%3E())`()`

Creates a new instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport")

  [build](#build())`()`

Builds the [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object for a car with the specifications taken from the [`TransportSpecification.CarBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder "class in com.here.sdk.transport") object.

[`TransportSpecification.CarBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder "class in com.here.sdk.transport")

  [withVehicleSpecification](#withVehicleSpecification(com.here.sdk.transport.VehicleSpecification))`(`[`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")` vehicleSpecification)`

Sets the vehicle specification.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### CarBuilder

public CarBuilder()

    Creates a new instance of this class.

## Method Details

### withVehicleSpecification

@NonNull public [TransportSpecification.CarBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder "class in com.here.sdk.transport") withVehicleSpecification(@NonNull [VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") vehicleSpecification)

    Sets the vehicle specification.
Parameters:
    `vehicleSpecification` -

    The vehicle specification.

    Returns:
    The [`TransportSpecification.CarBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder "class in com.here.sdk.transport") object with the vehicle specification set to the new value.

### build

@NonNull public [TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") build()

    Builds the [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object for a car with the specifications taken from the [`TransportSpecification.CarBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder "class in com.here.sdk.transport") object.
Returns:
    The [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object created from the [`TransportSpecification.CarBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder "class in com.here.sdk.transport") object.
