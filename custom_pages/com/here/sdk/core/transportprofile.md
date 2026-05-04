---
title: "TransportProfile (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransportprofile"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransportProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.TransportProfile
------------------------------------------------------------------------
public final class TransportProfile extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains values of transport profile. This is a BETA feature and thus there can be bugs and unexpected behavior.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`PedestrianProfile`](sdk-for-android-explore-api-reference-latestpedestrianprofile "class in com.here.sdk.core")

  [pedestrianProfile](#pedestrianProfile)

Defines the pedestrian profile.

[`VehicleProfile`](sdk-for-android-explore-api-reference-latestvehicleprofile "class in com.here.sdk.transport")

  [vehicleProfile](#vehicleProfile)

Defines the vehicle profile.

## Constructor Summary

Constructors

Constructor

  Description

  [TransportProfile](#%3Cinit%3E())`()`

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

### pedestrianProfile

@NonNull public [PedestrianProfile](sdk-for-android-explore-api-reference-latestpedestrianprofile "class in com.here.sdk.core") pedestrianProfile

    Defines the pedestrian profile.

### vehicleProfile

@Nullable public [VehicleProfile](sdk-for-android-explore-api-reference-latestvehicleprofile "class in com.here.sdk.transport") vehicleProfile

    Defines the vehicle profile.

## Constructor Details

  - ()" class="section detail">

### TransportProfile

public TransportProfile()

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
