---
title: "Anchor2DKeyframe (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestanchor2dkeyframe"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Anchor2DKeyframe

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.animation.Anchor2DKeyframe
------------------------------------------------------------------------
public final class Anchor2DKeyframe extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
An Anchor2D keyframe. A keyframe consists of a value and an animation duration.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [duration](#duration)

Relative animation duration for reaching the keyframe value.

`final `[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")

  [value](#value)

Anchor2D keyframe value.

## Constructor Summary

Constructors

Constructor

  Description

  [Anchor2DKeyframe](#%3Cinit%3E(com.here.sdk.core.Anchor2D,com.here.time.Duration))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` value, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Constructs a Anchor2DKeyframe from the value and offset.

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

@NonNull public final [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") value

    Anchor2D keyframe value.

### duration

@NonNull public final [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration

    Relative animation duration for reaching the keyframe value. Negative duration value gets clamped to 0.

## Constructor Details

  - (com.here.sdk.core.Anchor2D,com.here.time.Duration)" class="section detail">

### Anchor2DKeyframe

public Anchor2DKeyframe(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") value, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Constructs a Anchor2DKeyframe from the value and offset.
Parameters:
    `value` -

    Anchor2D keyframe value.

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
