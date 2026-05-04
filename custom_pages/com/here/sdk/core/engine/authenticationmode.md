---
title: "AuthenticationMode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestauthenticationmode"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AuthenticationMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.engine.AuthenticationMode
------------------------------------------------------------------------
public final class AuthenticationMode extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This is a bearer authentication mode which adds or does not add a header ("Authorization", "Bearer \$Token") to each online request of the module the object is added to. The token (if used) can be provided or is retrieved via key/secret from a dedicated backend.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [AuthenticationMode.AccessTokenProvider](sdk-for-android-explore-api-reference-latestauthenticationmode-accesstokenprovider)

This lambda is used to retrieve access token in synchronous manner.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` rhs)`

  `int`

  [hashCode](#hashCode())`()`

  `static `[`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")

  [withExternal](#withExternal())`()`

Assumes the authentication is provided by the client.

`static `[`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")

  [withKeySecret](#withKeySecret(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` accessKeyId, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` accessKeySecret)`

SDK will authenticate with access key id access key secret to obtain authentication token.

`static `[`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")

  [withToken](#withToken(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` accessToken)`

SDK will pass access token as a Bearer.

`static `[`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")

  [withTokenProvider](#withTokenProvider(com.here.sdk.core.engine.AuthenticationMode.AccessTokenProvider))`(`[`AuthenticationMode.AccessTokenProvider`](sdk-for-android-explore-api-reference-latestauthenticationmode-accesstokenprovider "interface in com.here.sdk.core.engine")` tokenProvider)`

SDK will use access token provider to retrieve access token.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) rhs)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### withToken

@NonNull public static [AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") withToken(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) accessToken)

    SDK will pass access token as a Bearer.
Parameters:
    `accessToken` -

    Access token

    Returns:
    Instance of [`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") configured to use token

### withTokenProvider

@NonNull public static [AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") withTokenProvider(@NonNull [AuthenticationMode.AccessTokenProvider](sdk-for-android-explore-api-reference-latestauthenticationmode-accesstokenprovider "interface in com.here.sdk.core.engine") tokenProvider)

    SDK will use access token provider to retrieve access token.
Parameters:
    `tokenProvider` -

    Access token provider

    Returns:
    Instance of [`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") configured to use token provider

### withExternal

@NonNull public static [AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") withExternal()

    Assumes the authentication is provided by the client.
Returns:
    Instance of [`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") configured to use externally provided authentication

### withKeySecret

@NonNull public static [AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") withKeySecret(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) accessKeyId, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) accessKeySecret)

    SDK will authenticate with access key id access key secret to obtain authentication token.
Parameters:
    `accessKeyId` -

    The access key id

    `accessKeySecret` -

    The access key secret

    Returns:
    Instance of [`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") configured to use key ID and secret
