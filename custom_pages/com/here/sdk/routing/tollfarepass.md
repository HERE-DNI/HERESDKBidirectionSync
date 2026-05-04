---
title: "TollFarePass (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttollfarepass"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TollFarePass

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TollFarePass
------------------------------------------------------------------------
public final class TollFarePass extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[`TollFare`](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing") multi-travel pass characteristics.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [returnJourney](#returnJourney)

This pass includes the fare for the return journey.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [seniorPass](#seniorPass)

This pass is valid only if presented by a senior person.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [transfers](#transfers)

Indicates if transfers are permitted with this pass, and if so, how many.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [travels](#travels)

This pass allows for the specified number of travels.

[`FarePassValidityPeriod`](sdk-for-android-explore-api-reference-latestfarepassvalidityperiod "class in com.here.sdk.routing")

  [validityPeriod](#validityPeriod)

Specifies a temporal validity period for a pass.

## Constructor Summary

Constructors

Constructor

  Description

  [TollFarePass](#%3Cinit%3E())`()`

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

### returnJourney

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) returnJourney

    This pass includes the fare for the return journey.

### validityPeriod

@Nullable public [FarePassValidityPeriod](sdk-for-android-explore-api-reference-latestfarepassvalidityperiod "class in com.here.sdk.routing") validityPeriod

    Specifies a temporal validity period for a pass.

### travels

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) travels

    This pass allows for the specified number of travels.

### transfers

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) transfers

    Indicates if transfers are permitted with this pass, and if so, how many.

### seniorPass

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) seniorPass

    This pass is valid only if presented by a senior person.

## Constructor Details

  - ()" class="section detail">

### TollFarePass

public TollFarePass()

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
