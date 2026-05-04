---
title: "AuthenticationCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestauthenticationcallback"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface AuthenticationCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface AuthenticationCallback
Callback passed to [`Authentication.authenticate(SDKNativeEngine)`](sdk-for-android-explore-api-reference-latestauthentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine)). This callback is called on the main thread asynchronously when an authenticate call has completed.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTokenReceived](#onTokenReceived(com.here.sdk.core.AuthenticationError,com.here.sdk.core.AuthenticationData))`(`[`AuthenticationError`](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")` authenticationError, `[`AuthenticationData`](sdk-for-android-explore-api-reference-latestauthenticationdata "class in com.here.sdk.core")` authenticationData)`

Callback passed to [`Authentication.authenticate(SDKNativeEngine)`](sdk-for-android-explore-api-reference-latestauthentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine)).

## Method Details

### onTokenReceived

void onTokenReceived(@Nullable [AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core") authenticationError, @Nullable [AuthenticationData](sdk-for-android-explore-api-reference-latestauthenticationdata "class in com.here.sdk.core") authenticationData)

    Callback passed to [`Authentication.authenticate(SDKNativeEngine)`](sdk-for-android-explore-api-reference-latestauthentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine)). This callback is called on the main thread asynchronously when an authenticate call has completed.
Parameters:
    `authenticationError` -

    Represents the operation status. It is 'null' for an operation that succeeds.

    `authenticationData` -

    Represents the authentication data.
