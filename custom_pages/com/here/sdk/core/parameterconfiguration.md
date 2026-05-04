---
title: "ParameterConfiguration (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestparameterconfiguration"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ParameterConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.ParameterConfiguration
------------------------------------------------------------------------
public final class ParameterConfiguration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains values of configurable parameters that are used in SDK. This is a BETA feature and thus there can be bugs and unexpected behavior.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport")

  [transportSpecification](#transportSpecification)

Stores default values related to pedestrian, vehicle, scooter and taxi specifications.

## Constructor Summary

Constructors

Constructor

  Description

  [ParameterConfiguration](#%3Cinit%3E())`()`

Creates a new instance of [`ParameterConfiguration`](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core") with the default values set.

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

### transportSpecification

@NonNull public [TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") transportSpecification

    Stores default values related to pedestrian, vehicle, scooter and taxi specifications.

## Constructor Details

  - ()" class="section detail">

### ParameterConfiguration

public ParameterConfiguration()

    Creates a new instance of [`ParameterConfiguration`](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core") with the default values set. **Note** By default, the \[ParameterConfiguration.transport_specification\] will return a valid [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") object with the \[sdk.transport.TransportSpecification.transport_mode\] set to [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR).

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
