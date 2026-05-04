---
title: "Fare (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestfare"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Fare

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.Fare
------------------------------------------------------------------------
public final class Fare extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Holds all the fare data.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [name](#name)

Name of a fare

[`FarePrice`](sdk-for-android-explore-api-reference-latestfareprice "class in com.here.sdk.routing")

  [price](#price)

Price of a fare.

[`FareReason`](sdk-for-android-explore-api-reference-latestfarereason "enum class in com.here.sdk.routing")

  [reason](#reason)

Reason of this cost.

## Constructor Summary

Constructors

Constructor

  Description

  [Fare](#%3Cinit%3E(java.lang.String,com.here.sdk.routing.FarePrice,com.here.sdk.routing.FareReason))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`FarePrice`](sdk-for-android-explore-api-reference-latestfareprice "class in com.here.sdk.routing")` price, `[`FareReason`](sdk-for-android-explore-api-reference-latestfarereason "enum class in com.here.sdk.routing")` reason)`

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

### name

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name

    Name of a fare

### price

@Nullable public [FarePrice](sdk-for-android-explore-api-reference-latestfareprice "class in com.here.sdk.routing") price

    Price of a fare. It is `null` when no price data is available.

### reason

@NonNull public [FareReason](sdk-for-android-explore-api-reference-latestfarereason "enum class in com.here.sdk.routing") reason

    Reason of this cost.

## Constructor Details

  - (java.lang.String,com.here.sdk.routing.FarePrice,com.here.sdk.routing.FareReason)" class="section detail">

### Fare

public Fare(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @Nullable [FarePrice](sdk-for-android-explore-api-reference-latestfareprice "class in com.here.sdk.routing") price, @NonNull [FareReason](sdk-for-android-explore-api-reference-latestfarereason "enum class in com.here.sdk.routing") reason)

    Creates a new instance.
Parameters:
    `name` -

    Name of a fare

    `price` -

    Price of a fare. It is `null` when no price data is available.

    `reason` -

    Reason of this cost.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
