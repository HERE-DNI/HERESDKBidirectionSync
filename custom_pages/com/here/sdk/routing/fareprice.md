---
title: "FarePrice (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestfareprice"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class FarePrice

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.FarePrice
------------------------------------------------------------------------
public final class FarePrice extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Price of a fare.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [currency](#currency)

Local currency of the price compliant to ISO 4217.

`boolean`

  [estimated](#estimated)

`True` when the fare price is estimated based on best guess and the actual price may differ.

`double`

  [maximum](#maximum)

Maximum price when the price is of [`FarePriceType.RANGE`](sdk-for-android-explore-api-reference-latestfarepricetype#RANGE) type.

`double`

  [minimum](#minimum)

Minimum price when the price is of [`FarePriceType.RANGE`](sdk-for-android-explore-api-reference-latestfarepricetype#RANGE) type.

[`FarePriceType`](sdk-for-android-explore-api-reference-latestfarepricetype "enum class in com.here.sdk.routing")

  [type](#type)

Type of price represented by this object.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [validityPeriod](#validityPeriod)

When set, the price is paid for a specific duration.

## Constructor Summary

Constructors

Constructor

  Description

  [FarePrice](#%3Cinit%3E())`()`

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

@NonNull public [FarePriceType](sdk-for-android-explore-api-reference-latestfarepricetype "enum class in com.here.sdk.routing") type

    Type of price represented by this object. Defaults to [`FarePriceType.VALUE`](sdk-for-android-explore-api-reference-latestfarepricetype#VALUE).

### estimated

public boolean estimated

    `True` when the fare price is estimated based on best guess and the actual price may differ. Defaults to `false`.

### currency

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) currency

    Local currency of the price compliant to ISO 4217. For example, "GBP" for the British pound sterling. Defaults to "EUR" string.

### minimum

public double minimum

    Minimum price when the price is of [`FarePriceType.RANGE`](sdk-for-android-explore-api-reference-latestfarepricetype#RANGE) type. Otherwise, it is equal to [`maximum`](#maximum). Defaults to 0.

### maximum

public double maximum

    Maximum price when the price is of [`FarePriceType.RANGE`](sdk-for-android-explore-api-reference-latestfarepricetype#RANGE) type. Otherwise, it is equal to [`minimum`](#minimum). Defaults to 0.

### validityPeriod

@Nullable public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") validityPeriod

    When set, the price is paid for a specific duration.

    **Examples**:

    3600 seconds - price for one hour

    28800 seconds - price for eight hours

    86400 seconds - price for one day

    **Note:** When the ticket validity period starts depends on the [`Agency`](sdk-for-android-explore-api-reference-latestagency "class in com.here.sdk.routing") providing the service. Defaults to `null`.

## Constructor Details

  - ()" class="section detail">

### FarePrice

public FarePrice()

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
