---
title: "AngleRange (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestanglerange"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AngleRange

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.AngleRange
------------------------------------------------------------------------
public final class AngleRange extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent. They both define a sector on a circle. All angles are in degrees and are clockwise-oriented. By default, the AngleRange represents the entire circle, the value is in the range of \[0, 360\]. Values will be corrected during construction using normalization for the start angle and clamping for the extent angle, ensuring a valid range for all possible inputs.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final double`

  [extent](#extent)

The angle range extent, running clockwise, in degrees from start.

`final double`

  [start](#start)

Start angle, running clockwise, in degrees from north.

## Constructor Summary

Constructors

Constructor

  Description

  [AngleRange](#%3Cinit%3E())`()`

Constructs a range covering a full circle.

[AngleRange](#%3Cinit%3E(double,double))`(double start, double extent)`

Constructs an AngleRange from the provided start and extent angles.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `double`

  [closestInRange](#closestInRange(double))`(double angleClockwiseInDegreesFromNorth)`

Get the angle that is closest to the given one and in range.

`boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `static `[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")

  [fromDirectionDegreesClockwise](#fromDirectionDegreesClockwise(double,double))`(double center, double extent)`

Constructs an AngleRange from the provided center angle defining the direction and an angular width to extent the range by 50% clockwise and 50% counter-clockwise from its center angle.

`static `[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")

  [fromMinMaxDegreesClockwise](#fromMinMaxDegreesClockwise(double,double))`(double min, double max)`

Constructs an AngleRange from the provided minimum and maximum angles.

`int`

  [hashCode](#hashCode())`()`

  `boolean`

  [inRange](#inRange(double))`(double angleClockwiseInDegreesFromNorth)`

Check if a given angle in degrees, clockwise from north is in range or not.

`double`

  [max](#max())`()`

Get the maximum angle defined by the range in degrees, clockwise from north, normalized to \[0,360).

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### start

public final double start

    Start angle, running clockwise, in degrees from north. The value is in the range of \[0, 360) degrees.

### extent

public final double extent

    The angle range extent, running clockwise, in degrees from start. The value is in the range of \[0, 360\] degrees.

## Constructor Details

  - (double,double)" class="section detail">

### AngleRange

public AngleRange(double start, double extent)

    Constructs an AngleRange from the provided start and extent angles. Corrects values if they exceed the ranges.
Parameters:
    `start` -

    Start angle, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    `extent` -

    The range's extent, running clockwise, in degrees from start. The value will be clamped to the range of \[0, 360\] degrees.
- ()" class="section detail">

### AngleRange

public AngleRange()

    Constructs a range covering a full circle.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### fromMinMaxDegreesClockwise

@NonNull public static [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") fromMinMaxDegreesClockwise(double min, double max)

    Constructs an AngleRange from the provided minimum and maximum angles. Corrects values if they exceed the ranges. The angles are always interpreted in clockwise orientation.
Parameters:
    `min` -

    Angle where to start the circular sector, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    `max` -

    Angle where the circular sector ends, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    Returns:
    Created AngleRange from the provided minimum and maximum angles.

### fromDirectionDegreesClockwise

@NonNull public static [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") fromDirectionDegreesClockwise(double center, double extent)

    Constructs an AngleRange from the provided center angle defining the direction and an angular width to extent the range by 50% clockwise and 50% counter-clockwise from its center angle. Corrects values if they exceed the ranges. Example: direction = 90, extent = 10 means the circle sector is pointing east, with an extent of 5 degrees north-wards and 5 degrees south-wards.
Parameters:
    `center` -

    Start angle, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    `extent` -

    The range's extent, running clockwise, in degrees from start. The value will be clamped to the range of \[0, 360\] degrees.

    Returns:
    Created AngleRange from the provided center angle and the range's extent.

### inRange

public boolean inRange(double angleClockwiseInDegreesFromNorth)

    Check if a given angle in degrees, clockwise from north is in range or not.
Parameters:
    `angleClockwiseInDegreesFromNorth` -

    An angle in degrees from north. Will be normalized before testing.

    Returns:
    `True`, if an angle is in range, `false` otherwise.

### closestInRange

public double closestInRange(double angleClockwiseInDegreesFromNorth)

    Get the angle that is closest to the given one and in range. If the angle to both ends of the range is the same, the value in the clockwise direction is returned. If the given angle is in range already, it will be returned as normalized angle.
Parameters:
    `angleClockwiseInDegreesFromNorth` -

    An angle in degrees from north. Will be normalized.

    Returns:
    The closest, normalized in-range angle in degrees, clockwise from north. If the given angle is in range already, the given angle will be returned as normalized angle in degree, clockwise from north.

### max

public double max()

    Get the maximum angle defined by the range in degrees, clockwise from north, normalized to \[0,360).
Returns:
    Maximum angle of the range in degrees, clockwise from north, normalized to \[0,360).
