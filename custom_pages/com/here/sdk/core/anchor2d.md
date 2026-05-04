---
title: "Anchor2D (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestanchor2d"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Anchor2D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.Anchor2D
------------------------------------------------------------------------
public final class Anchor2D extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a point in a rectangle as a ratio of this rectangle's width and height.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [horizontal](#horizontal)

Defines the x axis where the left is 0, the right is 1 and the middle is 0.5.

`double`

  [vertical](#vertical)

Defines the y axis where the top is 0, the bottom is 1 and the middle is 0.5.

## Constructor Summary

Constructors

Constructor

  Description

  [Anchor2D](#%3Cinit%3E())`()`

Creates a new instance of an Anchor2D with the default parameters

[Anchor2D](#%3Cinit%3E(double,double))`(double horizontal, double vertical)`

Creates a new instance of an Anchor2D.

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

### horizontal

public double horizontal

    Defines the x axis where the left is 0, the right is 1 and the middle is 0.5. The default value is 0.5.

### vertical

public double vertical

    Defines the y axis where the top is 0, the bottom is 1 and the middle is 0.5. The default value is 0.5.

## Constructor Details

  - ()" class="section detail">

### Anchor2D

public Anchor2D()

    Creates a new instance of an Anchor2D with the default parameters

  - (double,double)" class="section detail">

### Anchor2D

public Anchor2D(double horizontal, double vertical)

    Creates a new instance of an Anchor2D.
Parameters:
    `horizontal` -

    Defines the x axis where the left is 0, the right is 1 and the middle is 0.5.

    `vertical` -

    Defines the y axis where the top is 0, the bottom is 1 and the middle is 0.5.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
