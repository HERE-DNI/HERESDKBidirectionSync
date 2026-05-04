---
title: "Easing (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesteasing"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Easing

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.animation.Easing
------------------------------------------------------------------------
public final class Easing extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Animation easing representing an easing function to be used during animations.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [Easing.InstantiationErrorCode](sdk-for-android-explore-api-reference-latesteasing-instantiationerrorcode)

Describes a reason for failing to create an [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation").

`static final class `

  [Easing.InstantiationException](sdk-for-android-explore-api-reference-latesteasing-instantiationexception)

Thrown when a problem occurs while trying to create an [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation").

## Constructor Summary

Constructors

Constructor

  Description

  [Easing](#%3Cinit%3E(com.here.sdk.animation.EasingFunction))`(`[`EasingFunction`](sdk-for-android-explore-api-reference-latesteasingfunction "enum class in com.here.sdk.animation")` easingFunction)`

Creates an instance of [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") using a predefined easing function.

[Easing](#%3Cinit%3E(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")`> points)`

Creates an instance of customized [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") using a specified number of points describing an easing function.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.animation.EasingFunction)" class="section detail">

### Easing

public Easing(@NonNull [EasingFunction](sdk-for-android-explore-api-reference-latesteasingfunction "enum class in com.here.sdk.animation") easingFunction)

    Creates an instance of [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") using a predefined easing function.
Parameters:
    `easingFunction` -

    Easing function.
- (java.util.List)" class="section detail">

### Easing

public Easing(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")\> points) throws [Easing.InstantiationException](sdk-for-android-explore-api-reference-latesteasing-instantiationexception "class in com.here.sdk.animation")

    Creates an instance of customized [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") using a specified number of points describing an easing function.
Parameters:
    `points` -

    List of sampled data points that define an easing function. X describes normalized time values in the range \[0, 1\]. Y describes normalized animated value changes. Values can fall outside of the range \[0, 1\]. During an animation run animated target value is multiplied with Y value. In case resulting animated target value falls outside of its own supported range it will be clamped to its range (e.g. when negative values used for color animation). X values must increase monotonically. There must be at least 2 data points specified. The first point's X value must be 0, the last point's X value must be 1. During an animation run for any given time value X' from the animation engine that satisfies the relation X(i) \< X' \< X(i+1) for the given X data points the corresponding Y' value will be calculated by linearly interpolating between Y(i) and Y(i+1) data points. The higher the sampling rate of the easing curve used for the data points the more precise the results. In order to achieve the same animation precision for animations with different durations (shorter vs longer) it is recommended to use a higher sampling rate for longer animation duration.

    Throws:
    [`Easing.InstantiationException`](sdk-for-android-explore-api-reference-latesteasing-instantiationexception "class in com.here.sdk.animation") -

    Instantiation error in case of invalid input parameters.
