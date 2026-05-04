---
title: "MaxAxleGroupWeight (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaxaxlegroupweight"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MaxAxleGroupWeight

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.MaxAxleGroupWeight
------------------------------------------------------------------------
public final class MaxAxleGroupWeight extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`MaxAxleGroupWeight` contains all the restriction details violated by an axle group weight.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [axleGroupType](#axleGroupType)

Type of the restriction's axle group

`int`

  [maxWeightInKilograms](#maxWeightInKilograms)

Limit of the axle weight in kilograms

## Constructor Summary

Constructors

Constructor

  Description

  [MaxAxleGroupWeight](#%3Cinit%3E(int,java.lang.String))`(int maxWeightInKilograms, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` axleGroupType)`

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

### maxWeightInKilograms

public int maxWeightInKilograms

    Limit of the axle weight in kilograms

### axleGroupType

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) axleGroupType

    Type of the restriction's axle group

## Constructor Details

  - (int,java.lang.String)" class="section detail">

### MaxAxleGroupWeight

public MaxAxleGroupWeight(int maxWeightInKilograms, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) axleGroupType)

    Creates a new instance.
Parameters:
    `maxWeightInKilograms` -

    Limit of the axle weight in kilograms

    `axleGroupType` -

    Type of the restriction's axle group

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
