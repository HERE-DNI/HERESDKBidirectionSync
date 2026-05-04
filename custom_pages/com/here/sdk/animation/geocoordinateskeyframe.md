---
title: "GeoCoordinatesKeyframe (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoCoordinatesKeyframe

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.animation.GeoCoordinatesKeyframe
------------------------------------------------------------------------
public final class GeoCoordinatesKeyframe extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A GeoCoordinatesKeyframe consists of a GeoCoordinates and an animation duration.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [duration](#duration)

Relative animation duration for reaching the keyframe value from previous keyframe value.

`final `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [value](#value)

GeoCoordinates keyframe value.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoCoordinatesKeyframe](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.time.Duration))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` value, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Constructs a GeoCoordinatesKeyframe from the value and offset.

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

### value

@NonNull public final [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") value

    GeoCoordinates keyframe value. Altitude component is ignored.

### duration

@NonNull public final [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration

    Relative animation duration for reaching the keyframe value from previous keyframe value. Negative duration value gets clamped to 0.

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates,com.here.time.Duration)" class="section detail">

### GeoCoordinatesKeyframe

public GeoCoordinatesKeyframe(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") value, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Constructs a GeoCoordinatesKeyframe from the value and offset.
Parameters:
    `value` -

    GeoCoordinates keyframe value.

    `duration` -

    Relative animation duration for reaching the keyframe value. Negative duration value gets clamped to 0.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
