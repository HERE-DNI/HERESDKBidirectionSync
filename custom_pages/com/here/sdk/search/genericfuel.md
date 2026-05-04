---
title: "GenericFuel (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgenericfuel"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GenericFuel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.GenericFuel
------------------------------------------------------------------------
public final class GenericFuel extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains generic fuel type info of fuel station.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`FuelAdditive`](sdk-for-android-explore-api-reference-latestfueladditive "class in com.here.sdk.search")`>`

  [additives](#additives)

The list of available fuel additives.

[`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")

  [type](#type)

The type of the fuel.

## Constructor Summary

Constructors

Constructor

  Description

  [GenericFuel](#%3Cinit%3E(com.here.sdk.transport.FuelType))`(`[`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")` type)`

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

@NonNull public [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") type

    The type of the fuel.

### additives

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[FuelAdditive](sdk-for-android-explore-api-reference-latestfueladditive "class in com.here.sdk.search")\> additives

    The list of available fuel additives. The list can be empty when no fuel additives are available or when the information is unknown.

## Constructor Details

  - (com.here.sdk.transport.FuelType)" class="section detail">

### GenericFuel

public GenericFuel(@NonNull [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") type)

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
