---
title: "ScalarKeyframe (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestscalarkeyframe"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ScalarKeyframe

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.animation.ScalarKeyframe
------------------------------------------------------------------------
public final class ScalarKeyframe extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A ScalarKeyframe consists of a scalar value (e.g,: distance in meters) and an animation duration.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [duration](#duration)

Relative animation duration for reaching the keyframe value from previous keyframe value.

`final double`

  [value](#value)

Scalar keyframe value.

## Constructor Summary

Constructors

Constructor

  Description

  [ScalarKeyframe](#%3Cinit%3E(double,com.here.time.Duration))`(double value, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Constructs a ScalarKeyframe from the value and offset.

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

public final double value

    Scalar keyframe value.

### duration

@NonNull public final [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration

    Relative animation duration for reaching the keyframe value from previous keyframe value. Negative duration value gets clamped to 0.

## Constructor Details

  - (double,com.here.time.Duration)" class="section detail">

### ScalarKeyframe

public ScalarKeyframe(double value, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Constructs a ScalarKeyframe from the value and offset.
Parameters:
    `value` -

    Scalar keyframe value.

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
