---
title: "ScrollHandler (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestscrollhandler"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ScrollHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.gestures.ScrollHandler
------------------------------------------------------------------------
public final class ScrollHandler extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class handles scroll events by panning the map accordingly.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [onScroll](#onScroll(float,float))`(float translationX, float translationY)`

To be called to trigger scroll gesture handling.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### onScroll

public void onScroll(float translationX, float translationY)

    To be called to trigger scroll gesture handling.
Parameters:
    `translationX` -

    Translation along x axis in pixels. Values \> 0 are interpreted as translation left and values \< 0 as translation right.

    `translationY` -

    Translation along y axis in pixels. Values \> 0 are interpreted as translation up and values \< 0 as translation down.
