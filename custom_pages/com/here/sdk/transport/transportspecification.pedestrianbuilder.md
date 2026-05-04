---
title: "TransportSpecification.PedestrianBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransportSpecification.PedestrianBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.transport.TransportSpecification.PedestrianBuilder
Enclosing class:
[TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport")

------------------------------------------------------------------------
public static final class TransportSpecification.PedestrianBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for pedestrian.

## Constructor Summary

Constructors

Constructor

  Description

  [PedestrianBuilder](#%3Cinit%3E())`()`

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

Builds the [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object for a pedestrian profile with the specifications taken from the [`TransportSpecification.PedestrianBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder "class in com.here.sdk.transport") object.

[`TransportSpecification.PedestrianBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder "class in com.here.sdk.transport")

  [withPedestrianSpecification](#withPedestrianSpecification(com.here.sdk.transport.PedestrianSpecification))`(`[`PedestrianSpecification`](sdk-for-android-explore-api-reference-latestpedestrianspecification "class in com.here.sdk.transport")` pedestrianSpecification)`

Sets the pedestrian specification.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### PedestrianBuilder

public PedestrianBuilder()

    Creates a new instance of this class.

## Method Details

### withPedestrianSpecification

@NonNull public [TransportSpecification.PedestrianBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder "class in com.here.sdk.transport") withPedestrianSpecification(@NonNull [PedestrianSpecification](sdk-for-android-explore-api-reference-latestpedestrianspecification "class in com.here.sdk.transport") pedestrianSpecification)

    Sets the pedestrian specification.
Parameters:
    `pedestrianSpecification` -

    The pedestrian specification.

    Returns:
    The [`TransportSpecification.PedestrianBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder "class in com.here.sdk.transport") object with the pedestrian specification set to the new value.

### build

@NonNull public [TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") build()

    Builds the [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object for a pedestrian profile with the specifications taken from the [`TransportSpecification.PedestrianBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder "class in com.here.sdk.transport") object.
Returns:
    The [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object created from the [`TransportSpecification.PedestrianBuilder`](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder "class in com.here.sdk.transport") object.
