---
title: "BusinessDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestbusinessdetails"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class BusinessDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.BusinessDetails
------------------------------------------------------------------------
public final class BusinessDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains place details such as contacts, opening hours and some electro vehicle info.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`>`

  [contacts](#contacts)

The list of contact information of the place.

[`EVChargingPool`](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")

  [evChargingPool](#evChargingPool)

EV charging pool details.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`>`

  [openingHours](#openingHours)

The list of opening hours information of the place (not available in result of suggest request).

## Constructor Summary

Constructors

Constructor

  Description

  [BusinessDetails](#%3Cinit%3E())`()`

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

### contacts

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts

    The list of contact information of the place.

### openingHours

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours

    The list of opening hours information of the place (not available in result of suggest request).

### evChargingPool

@Nullable public [EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search") evChargingPool

    EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. Charging stations data are only available to users with valid contracts with HERE.

## Constructor Details

  - ()" class="section detail">

### BusinessDetails

public BusinessDetails()

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
