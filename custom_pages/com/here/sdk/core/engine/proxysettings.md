---
title: "ProxySettings (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestproxysettings"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ProxySettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.ProxySettings
------------------------------------------------------------------------
public final class ProxySettings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Proxy configuration for the HERE SDK network that is applied per request. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [ProxySettings.Credentials](sdk-for-android-explore-api-reference-latestproxysettings-credentials)

Authentication data

`static enum `

  [ProxySettings.ProxyType](sdk-for-android-explore-api-reference-latestproxysettings-proxytype)

Supported types of proxy connection.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`ProxySettings.Credentials`](sdk-for-android-explore-api-reference-latestproxysettings-credentials "class in com.here.sdk.core.engine")

  [credentials](#credentials)

Optional field to define credentials to authenticate a user to the proxy server.

[InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html)

  [ipAddress](#ipAddress)

Represents the IP Address of the proxy server.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [networkInterface](#networkInterface)

Network interface.

`int`

  [port](#port)

Represents the port number of the proxy server.

[`ProxySettings.ProxyType`](sdk-for-android-explore-api-reference-latestproxysettings-proxytype "enum class in com.here.sdk.core.engine")

  [type](#type)

Represents the type of the proxy server.

## Constructor Summary

Constructors

Constructor

  Description

  [ProxySettings](#%3Cinit%3E(com.here.sdk.core.engine.ProxySettings.ProxyType,java.net.InetAddress,int))`(`[`ProxySettings.ProxyType`](sdk-for-android-explore-api-reference-latestproxysettings-proxytype "enum class in com.here.sdk.core.engine")` type, `[InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html)` ipAddress, int port)`

Creates a new instance.

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

### type

@NonNull public [ProxySettings.ProxyType](sdk-for-android-explore-api-reference-latestproxysettings-proxytype "enum class in com.here.sdk.core.engine") type

    Represents the type of the proxy server.

### ipAddress

@NonNull public [InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html) ipAddress

    Represents the IP Address of the proxy server.

### networkInterface

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) networkInterface

    Network interface. It's taken into account when IPv6 is used. Default value is "wlan0". If not set then no interface is used.

### port

public int port

    Represents the port number of the proxy server.

### credentials

@Nullable public [ProxySettings.Credentials](sdk-for-android-explore-api-reference-latestproxysettings-credentials "class in com.here.sdk.core.engine") credentials

    Optional field to define credentials to authenticate a user to the proxy server.

## Constructor Details

  - (com.here.sdk.core.engine.ProxySettings.ProxyType,java.net.InetAddress,int)" class="section detail">

### ProxySettings

public ProxySettings(@NonNull [ProxySettings.ProxyType](sdk-for-android-explore-api-reference-latestproxysettings-proxytype "enum class in com.here.sdk.core.engine") type, @NonNull [InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html) ipAddress, int port)

    Creates a new instance.
Parameters:
    `type` -

    Represents the type of the proxy server.

    `ipAddress` -

    Represents the IP Address of the proxy server.

    `port` -

    Represents the port number of the proxy server.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
