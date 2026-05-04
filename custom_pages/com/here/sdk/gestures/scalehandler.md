---
title: "ScaleHandler (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestscalehandler"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ScaleHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.gestures.ScaleHandler
------------------------------------------------------------------------
public final class ScaleHandler extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class handles scale events by zooming the map accordingly.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [onScale](#onScale(float,float,float))`(float originX, float originY, float factor)`

To be called to trigger scale gesture handling.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### onScale

public void onScale(float originX, float originY, float factor)

    To be called to trigger scale gesture handling.
Parameters:
    `originX` -

    Origin of the scaling on x axis in pixels.

    `originY` -

    Origin of the scaling on y axis in pixels.

    `factor` -

    The scale factor. Values above 1.0 will zoom in and values below will zoom out.
