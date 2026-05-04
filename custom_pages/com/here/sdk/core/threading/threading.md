---
title: "Threading (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestthreading"
hidden: false
---

Package [com.here.sdk.core.threading](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Threading

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.threading.Threading
------------------------------------------------------------------------
public final class Threading extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Initializes threading support on native side.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`PlatformThreading`](sdk-for-android-explore-api-reference-latestplatformthreading "interface in com.here.sdk.core.threading")

  [getPlatformThreading](#getPlatformThreading())`()`

Returns threading bridge which was set before.

`static void`

  [setPlatformThreading](#setPlatformThreading(com.here.sdk.core.threading.PlatformThreading))`(`[`PlatformThreading`](sdk-for-android-explore-api-reference-latestplatformthreading "interface in com.here.sdk.core.threading")` platformThreading)`

Sets threading bridge which is used for interaction with the platform side.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### setPlatformThreading

public static void setPlatformThreading(@NonNull [PlatformThreading](sdk-for-android-explore-api-reference-latestplatformthreading "interface in com.here.sdk.core.threading") platformThreading)

    Sets threading bridge which is used for interaction with the platform side.
Parameters:
    `platformThreading` -

    Platform threading bridge which should be implemented on the platform side.

### getPlatformThreading

@NonNull public static [PlatformThreading](sdk-for-android-explore-api-reference-latestplatformthreading "interface in com.here.sdk.core.threading") getPlatformThreading()

    Returns threading bridge which was set before.
Returns:
    Current platform threading bridge.
