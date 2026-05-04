---
title: "Authentication (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestauthentication"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Authentication

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.Authentication
------------------------------------------------------------------------
public final class Authentication extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Use the authentication class to authenticate and retrieve a secure token that can be used with other HERE services.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`AuthenticationData`](sdk-for-android-explore-api-reference-latestauthenticationdata "class in com.here.sdk.core")

  [authenticate](#authenticate(com.here.sdk.core.engine.SDKNativeEngine))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkNativeEngine)`

Uses the authentication service that is connected to the given SDK engine to authenticate and retrieve a secure token.

`static void`

  [authenticate](#authenticate(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.core.AuthenticationCallback))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkNativeEngine, `[`AuthenticationCallback`](sdk-for-android-explore-api-reference-latestauthenticationcallback "interface in com.here.sdk.core")` callback)`

Uses the authentication service that is connected to the given SDK engine to authenticate and retrieve a secure token.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### authenticate

public static void authenticate(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkNativeEngine, @NonNull [AuthenticationCallback](sdk-for-android-explore-api-reference-latestauthenticationcallback "interface in com.here.sdk.core") callback)

    Uses the authentication service that is connected to the given SDK engine to authenticate and retrieve a secure token. This method operates asynchronously.
Parameters:
    `sdkNativeEngine` -

    The SDK engine instance.

    `callback` -

    Callback to retrieve an authentication token on the main thread.

### authenticate

@NonNull public static [AuthenticationData](sdk-for-android-explore-api-reference-latestauthenticationdata "class in com.here.sdk.core") authenticate(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkNativeEngine) throws [AuthenticationException](sdk-for-android-explore-api-reference-latestauthenticationexception "class in com.here.sdk.core")

    Uses the authentication service that is connected to the given SDK engine to authenticate and retrieve a secure token. This method operates synchronously.
Parameters:
    `sdkNativeEngine` -

    The SDK engine instance.

    Returns:
    Authentication data.

    Throws:
    [`AuthenticationException`](sdk-for-android-explore-api-reference-latestauthenticationexception "class in com.here.sdk.core") -

    Authentication exception that describes the error.
