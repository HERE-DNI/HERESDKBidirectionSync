---
title: "GeoOrientationUpdate (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeoorientationupdate"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoOrientationUpdate

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.GeoOrientationUpdate
------------------------------------------------------------------------
public final class GeoOrientationUpdate extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Describes geodetic orientation update with bearing and tilt. Updating an orientation value can be skipped by setting `null` in an appriopriate field. For example, if one wants bearing not to be updated set it to `null`.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [bearing](#bearing)

Bearing in degrees.

`final `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [tilt](#tilt)

Tilt in degrees.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoOrientationUpdate](#%3Cinit%3E(com.here.sdk.core.GeoOrientation))`(`[`GeoOrientation`](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core")` orientation)`

Constructs a new GeoOrientationUpdate instance from a GeoOrientation instance.

[GeoOrientationUpdate](#%3Cinit%3E(java.lang.Double,java.lang.Double))`(`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` bearing, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` tilt)`

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

@Nullable public final [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) bearing

    Bearing in degrees. 0 is north up, positive is clockwise. A `null` value means that bearing is not updated and the current value is kept.

### tilt

@Nullable public final [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) tilt

    Tilt in degrees. 0 is perpendicular to earth surface, a positive value turns the camera's nose up and changes the camera's location to ensure that the camera target is not changed. A `null` value means that tilt is not updated and the current value is kept.

## Constructor Details

  - (java.lang.Double,java.lang.Double)" class="section detail">

### GeoOrientationUpdate

public GeoOrientationUpdate(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) bearing, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) tilt)
Parameters:
    `bearing` -

    Bearing in degrees. When the passed value is `null` bearing is not updated and the current value is kept. NaN value is converted to `null`.

    `tilt` -

    Tilt in degrees. When the passed value is `null` tilt is not updated and the current value is kept. NaN value is converted to `null`.
- (com.here.sdk.core.GeoOrientation)" class="section detail">

### GeoOrientationUpdate

public GeoOrientationUpdate(@NonNull [GeoOrientation](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core") orientation)

    Constructs a new GeoOrientationUpdate instance from a GeoOrientation instance.
Parameters:
    `orientation` -

    A GeoOrientation instance used as a source for a GeoOrientationUpdate instance's values.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
