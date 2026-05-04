---
title: "DashPattern (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdashpattern"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class DashPattern

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.DashPattern
------------------------------------------------------------------------
public final class DashPattern extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a dash pattern for map polyline.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final double`

  [firstDashLength](#firstDashLength)

Length of first dash in pixels.

`final double`

  [firstGapLength](#firstGapLength)

Length of first gap in pixels.

## Constructor Summary

Constructors

Constructor

  Description

  [DashPattern](#%3Cinit%3E(double))`(double dashLength)`

Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash.

[DashPattern](#%3Cinit%3E(double,double))`(double gapLength, double dashLength)`

Creates a simple dash pattern in which the lengths of a dash and gap can be different.

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

### firstGapLength

public final double firstGapLength

    Length of first gap in pixels.

### firstDashLength

public final double firstDashLength

    Length of first dash in pixels.

## Constructor Details

  - (double)" class="section detail">

### DashPattern

public DashPattern(double dashLength)

    Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash. This allows for patterns like `' — — — —'` or `' ——— ——— ———'`.
Parameters:
    `dashLength` -

    The length of a dash in pixels. The gap will have the same length. Clamped to the range of \[1, 500\].
- (double,double)" class="section detail">

### DashPattern

public DashPattern(double gapLength, double dashLength)

    Creates a simple dash pattern in which the lengths of a dash and gap can be different. This allows for patterns like `' — — — —'` or `' ——— ——— ———'`.
Parameters:
    `gapLength` -

    The length of a gap in pixels. Clamped to the range of \[1, 500\].

    `dashLength` -

    The length of a dash in pixels. Clamped to the range of \[1, 500\].

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
