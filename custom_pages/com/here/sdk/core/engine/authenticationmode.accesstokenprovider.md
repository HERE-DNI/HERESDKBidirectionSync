---
title: "AuthenticationMode.AccessTokenProvider (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestauthenticationmode-accesstokenprovider"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface AuthenticationMode.AccessTokenProvider

Enclosing class:
[AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface AuthenticationMode.AccessTokenProvider
This lambda is used to retrieve access token in synchronous manner. It returns the access token or null if it is not set. The lambda is called each time the access token is needed and it is executed on the main thread of the application.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [apply](#apply())`()`

This lambda is used to retrieve access token in synchronous manner.

## Method Details

### apply

@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) apply()

    This lambda is used to retrieve access token in synchronous manner. It returns the access token or null if it is not set. The lambda is called each time the access token is needed and it is executed on the main thread of the application.
Returns:
    Access token in case it is set or null otherwise.
