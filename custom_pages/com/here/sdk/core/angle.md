---
title: "Angle (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestangle"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Angle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.Angle
------------------------------------------------------------------------
public final class Angle extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents an angle independent of the unit of measurement.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`Angle`](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core")

  [fromDegrees](#fromDegrees(double))`(double angle)`

Creates a new angle object based on the supplied angle value in degrees.

`static `[`Angle`](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core")

  [fromRadians](#fromRadians(double))`(double angle)`

Creates a new angle object based on the supplied angle value in radians.

`double`

  [getDegrees](#getDegrees())`()`

Gets the value of this angle in degrees.

`double`

  [getRadians](#getRadians())`()`

Gets the value of this angle in radians.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### fromDegrees

@NonNull public static [Angle](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core") fromDegrees(double angle)

    Creates a new angle object based on the supplied angle value in degrees.
Parameters:
    `angle` -

    Angle value in degrees.

    Returns:
    The angle as specified by input in degrees.

### fromRadians

@NonNull public static [Angle](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core") fromRadians(double angle)

    Creates a new angle object based on the supplied angle value in radians.
Parameters:
    `angle` -

    Angle value in radians.

    Returns:
    The angle as specified by input in radians.

### getDegrees

public double getDegrees()

    Gets the value of this angle in degrees.
Returns:
    The value of this angle in degrees.

### getRadians

public double getRadians()

    Gets the value of this angle in radians.
Returns:
    The value of this angle in radians.
