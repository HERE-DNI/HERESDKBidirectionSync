---
title: "Rectangle2D (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrectangle2d"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Rectangle2D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.Rectangle2D
------------------------------------------------------------------------
public final class Rectangle2D extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a 2D rectangle defined by the origin and size.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")

  [origin](#origin)

The origin specifies the top-left corner of the rectangle.

[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

  [size](#size)

The size specifies the width and height of the rectangle.

## Constructor Summary

Constructors

Constructor

  Description

  [Rectangle2D](#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.sdk.core.Size2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin, `[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")` size)`

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

### origin

@NonNull public [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin

    The origin specifies the top-left corner of the rectangle. When this point is used to indicate the coordinates on a view, then (0,0) will mark the top-left corner of the view. The size determines the width and height of the rectangle. The width expands towards the right of the view. The height expands towards the bottom of the view.

### size

@NonNull public [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") size

    The size specifies the width and height of the rectangle.

## Constructor Details

  - (com.here.sdk.core.Point2D,com.here.sdk.core.Size2D)" class="section detail">

### Rectangle2D

public Rectangle2D(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin, @NonNull [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") size)

    Creates a new instance.
Parameters:
    `origin` -

    The origin specifies the top-left corner of the rectangle. When this point is used to indicate the coordinates on a view, then (0,0) will mark the top-left corner of the view. The size determines the width and height of the rectangle. The width expands towards the right of the view. The height expands towards the bottom of the view.

    `size` -

    The size specifies the width and height of the rectangle.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
