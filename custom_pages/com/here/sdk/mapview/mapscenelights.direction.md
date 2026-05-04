---
title: "MapSceneLights.Direction (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscenelights-direction"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapSceneLights.Direction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapSceneLights.Direction
Enclosing class:
[MapSceneLights](sdk-for-android-explore-api-reference-latestmapscenelights "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapSceneLights.Direction extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The direction of lights as a pair of azimuth and altitude angles. See https://en.wikipedia.org/wiki/Horizontal_coordinate_system

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [altitude](#altitude)

Direction altitude value in degrees in the range \[0, 90\].

`double`

  [azimuth](#azimuth)

Direction azimuth value in degrees in the range \[0, 360).

## Constructor Summary

Constructors

Constructor

  Description

  [Direction](#%3Cinit%3E())`()`

Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.

[Direction](#%3Cinit%3E(double,double))`(double azimuth, double altitude)`

Constructs a Direction from the values.

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

### azimuth

public double azimuth

    Direction azimuth value in degrees in the range \[0, 360). The default value is 0.0. The azimuth range is half-open, meaning the maximum value is not included in the range. If the azimuth value falls outside the range, it is wrapped to stay within \[0, 360). Specifically, values less than 0 will be increased by 360 until they fall within the range, and values greater than or equal to 360 will be reduced by 360 until they fall within the range. By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise. Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.

### altitude

public double altitude

    Direction altitude value in degrees in the range \[0, 90\]. The default value is 0.0. The altitude value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90. Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly. For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90. When both azimuth and altitude values are provided, they are adjusted independently: For instance, (0, -10) is changed to (0, 0) rather than (180, 10).

## Constructor Details

  - ()" class="section detail">

### Direction

public Direction()

    Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.

  - (double,double)" class="section detail">

### Direction

public Direction(double azimuth, double altitude)

    Constructs a Direction from the values.
Parameters:
    `azimuth` -

    Direction azimuth value in degrees in the range \[0, 360). The default value is 0.0. The azimuth range is half-open, meaning the maximum value is not included in the range. If the azimuth value falls outside the range, it is wrapped to stay within \[0, 360). Specifically, values less than 0 will be increased by 360 until they fall within the range, and values greater than or equal to 360 will be reduced by 360 until they fall within the range. By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise. Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.

    `altitude` -

    Direction altitude value in degrees in the range \[0, 90\]. The default value is 0.0. The altitude value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90. Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly. For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90. When both azimuth and altitude values are provided, they are adjusted independently: For instance, (0, -10) is changed to (0, 0) rather than (180, 10).

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
