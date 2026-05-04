---
title: "BusSpecifications (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestbusspecifications"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class BusSpecifications

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.BusSpecifications
------------------------------------------------------------------------
public final class BusSpecifications extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Bus specifications contain vehicle related attributes. Examples: height, weight, width. Only the fields that are set are considered for restriction handling.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [grossWeightInKilograms](#grossWeightInKilograms)

Total vehicle weight in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [heightInCentimeters](#heightInCentimeters)

Bus height in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [lengthInCentimeters](#lengthInCentimeters)

Bus length in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [widthInCentimeters](#widthInCentimeters)

Bus width in centimeters.

## Constructor Summary

Constructors

Constructor

  Description

  [BusSpecifications](#%3Cinit%3E())`()`

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

### grossWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) grossWeightInKilograms

    Total vehicle weight in kilograms. By default, it is not set.

### heightInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) heightInCentimeters

    Bus height in centimeters. By default, it is not set.

### widthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) widthInCentimeters

    Bus width in centimeters. By default, it is not set.

### lengthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lengthInCentimeters

    Bus length in centimeters. By default, it is not set.

## Constructor Details

  - ()" class="section detail">

### BusSpecifications

public BusSpecifications()

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
