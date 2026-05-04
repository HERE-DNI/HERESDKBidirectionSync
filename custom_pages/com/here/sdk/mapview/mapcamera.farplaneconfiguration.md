---
title: "MapCamera.FarPlaneConfiguration (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcamera-farplaneconfiguration"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapCamera.FarPlaneConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapCamera.FarPlaneConfiguration
Enclosing class:
[MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapCamera.FarPlaneConfiguration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Far plane distance configuration for a zoom level.

Effective far plane is computed from both parameters as: farPlaneInMeters = max( minDistanceInMeters, distanceToTargetInMeters \* distanceFactor )

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [distanceFactor](#distanceFactor)

Multiplier applied to the camera distance to target when calculating the far plane.

`double`

  [minDistanceInMeters](#minDistanceInMeters)

Minimum far plane clamp in meters.

## Constructor Summary

Constructors

Constructor

  Description

  [FarPlaneConfiguration](#%3Cinit%3E(double,double))`(double distanceFactor, double minDistanceInMeters)`

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

### distanceFactor

public double distanceFactor

    Multiplier applied to the camera distance to target when calculating the far plane.

### minDistanceInMeters

public double minDistanceInMeters

    Minimum far plane clamp in meters.

## Constructor Details

  - (double,double)" class="section detail">

### FarPlaneConfiguration

public FarPlaneConfiguration(double distanceFactor, double minDistanceInMeters)

    Creates a new instance.
Parameters:
    `distanceFactor` -

    Multiplier applied to the camera distance to target when calculating the far plane.

    `minDistanceInMeters` -

    Minimum far plane clamp in meters.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
