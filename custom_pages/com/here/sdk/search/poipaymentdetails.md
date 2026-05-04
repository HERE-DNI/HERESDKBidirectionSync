---
title: "POIPaymentDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpoipaymentdetails"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class POIPaymentDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.POIPaymentDetails
------------------------------------------------------------------------
public final class POIPaymentDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Details about the payment options at the POI.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [acceptedCashCurrencies](#acceptedCashCurrencies)

Accepted currencies for cash payment, represented by their ISO 4217 code, for example "EUR", "USD", "CNY" etc.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [acceptedMethods](#acceptedMethods)

Accepted payment methods.

## Constructor Summary

Constructors

Constructor

  Description

  [POIPaymentDetails](#%3Cinit%3E())`()`

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

### acceptedMethods

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> acceptedMethods

    Accepted payment methods. Currently supported methods are defined in [`POIPaymentMethod`](sdk-for-android-explore-api-reference-latestpoipaymentmethod "class in com.here.sdk.search").

### acceptedCashCurrencies

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> acceptedCashCurrencies

    Accepted currencies for cash payment, represented by their ISO 4217 code, for example "EUR", "USD", "CNY" etc. See the full list of [ISO 421 codes](https://en.wikipedia.org/wiki/ISO_4217). If cash is not an accepted payment method or the list of accepted currencies is not available, it is set to `null`.

## Constructor Details

  - ()" class="section detail">

### POIPaymentDetails

public POIPaymentDetails()

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
