---
title: "MapMeasureRange (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmeasurerange"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMeasureRange

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapMeasureRange
------------------------------------------------------------------------
public final class MapMeasureRange extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A map measure range.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview")

  [kind](#kind)

The kind of measure represented by value.

`final double`

  [maximumValue](#maximumValue)

The maximum measure value.

`final double`

  [minimumValue](#minimumValue)

The minimum measure value.

## Constructor Summary

Constructors

Constructor

  Description

  [MapMeasureRange](#%3Cinit%3E(com.here.sdk.mapview.MapMeasure.Kind,double,double))`(`[`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview")` kind, double minimumValue, double maximumValue)`

Constructs a MapMeasureRange from the kind and range values.

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

### kind

@NonNull public final [MapMeasure.Kind](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") kind

    The kind of measure represented by value.

### minimumValue

public final double minimumValue

    The minimum measure value.

### maximumValue

public final double maximumValue

    The maximum measure value.

## Constructor Details

  - (com.here.sdk.mapview.MapMeasure.Kind,double,double)" class="section detail">

### MapMeasureRange

public MapMeasureRange(@NonNull [MapMeasure.Kind](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") kind, double minimumValue, double maximumValue)

    Constructs a MapMeasureRange from the kind and range values.
Parameters:
    `kind` -

    The measure kind.

    `minimumValue` -

    The minimum measure value.

    `maximumValue` -

    The maximum measure value.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
