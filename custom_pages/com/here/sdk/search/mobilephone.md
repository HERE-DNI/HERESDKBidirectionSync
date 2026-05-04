---
title: "MobilePhone (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmobilephone"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MobilePhone

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.MobilePhone
------------------------------------------------------------------------
public final class MobilePhone extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents data related to specific mobile phone number.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`>`

  [categories](#categories)

Categories associated with phone number.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [phoneNumber](#phoneNumber)

The phone number.

## Constructor Summary

Constructors

Constructor

  Description

  [MobilePhone](#%3Cinit%3E())`()`

Creates a new instance.

[MobilePhone](#%3Cinit%3E(java.lang.String,java.util.List))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` phoneNumber, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories)`

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

### phoneNumber

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) phoneNumber

    The phone number.

### categories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories

    Categories associated with phone number. Note: In case [`categories`](#categories) are not empty, then [`phoneNumber`](#phoneNumber) should be used according to given categories. Otherwise, [`phoneNumber`](#phoneNumber) is meant for general use.

## Constructor Details

  - ()" class="section detail">

### MobilePhone

public MobilePhone()

    Creates a new instance.

  - (java.lang.String,java.util.List)" class="section detail">

### MobilePhone

public MobilePhone(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) phoneNumber, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories)

    Creates a new instance.
Parameters:
    `phoneNumber` -

    The phone number.

    `categories` -

    Categories associated with phone number. Note: In case [`categories`](#categories) are not empty, then [`phoneNumber`](#phoneNumber) should be used according to given categories. Otherwise, [`phoneNumber`](#phoneNumber) is meant for general use.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
