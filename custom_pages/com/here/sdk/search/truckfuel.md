---
title: "TruckFuel (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttruckfuel"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TruckFuel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.TruckFuel
------------------------------------------------------------------------
public final class TruckFuel extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains truck fuel type info of fuel station. Note: This is a BETA feature and thus subject to change.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`TruckClass`](sdk-for-android-explore-api-reference-latesttruckclass "enum class in com.here.sdk.transport")

  [maximumTruckClass](#maximumTruckClass)

The maximum truck class that this fuel type supports.

[`TruckFuelType`](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport")

  [type](#type)

The type of the fuel.

## Constructor Summary

Constructors

Constructor

  Description

  [TruckFuel](#%3Cinit%3E(com.here.sdk.transport.TruckFuelType))`(`[`TruckFuelType`](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport")` type)`

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

### type

@NonNull public [TruckFuelType](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport") type

    The type of the fuel.

### maximumTruckClass

@Nullable public [TruckClass](sdk-for-android-explore-api-reference-latesttruckclass "enum class in com.here.sdk.transport") maximumTruckClass

    The maximum truck class that this fuel type supports. `null` means information is unknown.

## Constructor Details

  - (com.here.sdk.transport.TruckFuelType)" class="section detail">

### TruckFuel

public TruckFuel(@NonNull [TruckFuelType](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport") type)

    Creates a new instance.
Parameters:
    `type` -

    The type of the fuel.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
