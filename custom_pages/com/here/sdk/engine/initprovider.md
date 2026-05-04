---
title: "InitProvider (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestinitprovider"
hidden: false
---

Package [com.here.sdk.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class InitProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.engine.InitProvider
------------------------------------------------------------------------
public class InitProvider extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Performs global initialization of the SDK. Normally this class is not needed because initialization of the SDK must be done automatically during the first access to [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") or [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine"). However in some cases it's more convenient to initialize SDK explicitly with this class. For example in integration tests where hard to predict the order of access to SDK.

## Constructor Summary

Constructors

Constructor

  Description

  [InitProvider](#%3Cinit%3E())`()`

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static void`

  [initialize](#initialize(android.content.Context))`(android.content.Context appContext)`

Loads HERE dynamic libraries and sets up initial and global states.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### InitProvider

public InitProvider()

## Method Details

### initialize

public static void initialize(@NonNull android.content.Context appContext)

    Loads HERE dynamic libraries and sets up initial and global states.
Parameters:
    `appContext` - The Android context.
