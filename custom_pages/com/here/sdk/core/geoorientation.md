---
title: "GeoOrientation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeoorientation"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoOrientation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.GeoOrientation
------------------------------------------------------------------------
public final class GeoOrientation extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Geodetic orientation with bearing, tilt and roll.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final double`

  [bearing](#bearing)

Bearing in degrees, from the true North in clockwise direction.

`final double`

  [tilt](#tilt)

Tilt in degrees.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoOrientation](#%3Cinit%3E(double,double))`(double bearing, double tilt)`

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

### bearing

public final double bearing

    Bearing in degrees, from the true North in clockwise direction. Bearing axis is perpendicular to the ground and passes through the target coordinate.

### tilt

public final double tilt

    Tilt in degrees. Tilt axis is parallel to the ground and passes through the target coordinate.

## Constructor Details

  - (double,double)" class="section detail">

### GeoOrientation

public GeoOrientation(double bearing, double tilt)
Parameters:
    `bearing` -

    Bearing in degrees. NaN value is converted to 0.0.

    `tilt` -

    Tilt in degrees. NaN value is converted to 0.0.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
