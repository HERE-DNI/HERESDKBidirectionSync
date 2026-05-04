---
title: "TransportSpecification.PrivateBusBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransportSpecification.PrivateBusBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.transport.TransportSpecification.PrivateBusBuilder
Enclosing class:
[TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport")

------------------------------------------------------------------------
public static final class TransportSpecification.PrivateBusBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a private bus.

## Constructor Summary

Constructors

Constructor

  Description

  [PrivateBusBuilder](#%3Cinit%3E())`()`

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

Builds the [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object for a private bus with the specifications taken from the [`TransportSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder "class in com.here.sdk.transport") object.

[`TransportSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder "class in com.here.sdk.transport")

  [withVehicleSpecification](#withVehicleSpecification(com.here.sdk.transport.VehicleSpecification))`(`[`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")` vehicleSpecification)`

Sets the vehicle specification.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### PrivateBusBuilder

public PrivateBusBuilder()

    Creates a new instance of this class.

## Method Details

### withVehicleSpecification

@NonNull public [TransportSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder "class in com.here.sdk.transport") withVehicleSpecification(@NonNull [VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") vehicleSpecification)

    Sets the vehicle specification.
Parameters:
    `vehicleSpecification` -

    The vehicle specification.

    Returns:
    The [`TransportSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder "class in com.here.sdk.transport") object with the vehicle specification set to the new value.

### build

@NonNull public [TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") build()

    Builds the [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object for a private bus with the specifications taken from the [`TransportSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder "class in com.here.sdk.transport") object.
Returns:
    The [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object created from the [`TransportSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder "class in com.here.sdk.transport") object.
