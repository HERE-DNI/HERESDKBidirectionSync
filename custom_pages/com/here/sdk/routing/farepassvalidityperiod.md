---
title: "FarePassValidityPeriod (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestfarepassvalidityperiod"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class FarePassValidityPeriod

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.FarePassValidityPeriod
------------------------------------------------------------------------
public final class FarePassValidityPeriod extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Specifies a temporal validity period for a pass

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [count](#count)

Specifies how many [`periodType`](#periodType)s are covered by the pass.

[`FarePassValidityPeriodType`](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype "enum class in com.here.sdk.routing")

  [periodType](#periodType)

Specifies one of the [`FarePassValidityPeriodType`](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype "enum class in com.here.sdk.routing") periods.

## Constructor Summary

Constructors

Constructor

  Description

  [FarePassValidityPeriod](#%3Cinit%3E())`()`

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

### periodType

@NonNull public [FarePassValidityPeriodType](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype "enum class in com.here.sdk.routing") periodType

    Specifies one of the [`FarePassValidityPeriodType`](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype "enum class in com.here.sdk.routing") periods.

### count

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) count

    Specifies how many [`periodType`](#periodType)s are covered by the pass. Present if [`periodType`](#periodType) is [`FarePassValidityPeriodType.MINUTES`](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype#MINUTES), [`FarePassValidityPeriodType.DAYS`](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype#DAYS) or [`FarePassValidityPeriodType.MONTHS`](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype#MONTHS).

## Constructor Details

  - ()" class="section detail">

### FarePassValidityPeriod

public FarePassValidityPeriod()

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
