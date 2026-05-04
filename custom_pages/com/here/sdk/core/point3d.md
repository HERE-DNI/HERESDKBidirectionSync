---
title: "Point3D (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpoint3d"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Point3D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.Point3D
------------------------------------------------------------------------
public final class Point3D extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a point in 3D space.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [x](#x)

Position along the X axis.

`double`

  [y](#y)

Position along the Y axis.

`double`

  [z](#z)

Position along the Z axis.

## Constructor Summary

Constructors

Constructor

  Description

  [Point3D](#%3Cinit%3E())`()`

Constructs Point3D instance at coordinate system's origin.

[Point3D](#%3Cinit%3E(double,double,double))`(double x, double y, double z)`

Constructs Point3D instance from the provided x,y and z values.

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

### x

public double x

    Position along the X axis. The default value is 0.

### y

public double y

    Position along the Y axis. The default value is 0.

### z

public double z

    Position along the Z axis. The default value is 0.

## Constructor Details

  - ()" class="section detail">

### Point3D

public Point3D()

    Constructs Point3D instance at coordinate system's origin.

  - (double,double,double)" class="section detail">

### Point3D

public Point3D(double x, double y, double z)

    Constructs Point3D instance from the provided x,y and z values.
Parameters:
    `x` -

    Position along the X axis. The default value is 0.

    `y` -

    Position along the Y axis. The default value is 0.

    `z` -

    Position along the Z axis. The default value is 0.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
