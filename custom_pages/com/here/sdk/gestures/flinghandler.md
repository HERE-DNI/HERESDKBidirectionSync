---
title: "FlingHandler (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestflinghandler"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class FlingHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.gestures.FlingHandler
------------------------------------------------------------------------
public final class FlingHandler extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class handles fling events by performing a kinetic move on the map. Initial velocity of kinetic move is the one provided to [`onFling(float, float)`](#onFling(float,float)). Subsequently, velocity decays exponentially.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [onFling](#onFling(float,float))`(float velocityX, float velocityY)`

To be called to trigger fling gesture handling.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### onFling

public void onFling(float velocityX, float velocityY)

    To be called to trigger fling gesture handling.
Parameters:
    `velocityX` -

    Velocity of fling in pixels per second along the x axis. Values \> 0 are interpreted as fling left and values \< 0 as fling right.

    `velocityY` -

    Velocity of fling in pixels per second along the y axis. Values \> 0 are interpreted as fling up and values \< 0 as fling down.
