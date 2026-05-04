---
title: "NetworkEndpoint (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestnetworkendpoint"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class NetworkEndpoint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.NetworkEndpoint
------------------------------------------------------------------------
public final class NetworkEndpoint extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Network endpoint.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html)

  [address](#address)

The IP Address of the network endpoint.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [port](#port)

Optional port number of the network endpoint.

## Constructor Summary

Constructors

Constructor

  Description

  [NetworkEndpoint](#%3Cinit%3E(java.net.InetAddress))`(`[InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html)` address)`

Creates a new instance.

[NetworkEndpoint](#%3Cinit%3E(java.net.InetAddress,java.lang.Integer))`(`[InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html)` address, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` port)`

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

### address

@NonNull public [InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html) address

    The IP Address of the network endpoint.

### port

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) port

    Optional port number of the network endpoint.

## Constructor Details

  - (java.net.InetAddress,java.lang.Integer)" class="section detail">

### NetworkEndpoint

public NetworkEndpoint(@NonNull [InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html) address, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) port)

    Creates a new instance.
Parameters:
    `address` -

    The IP Address of the network endpoint.

    `port` -

    Optional port number of the network endpoint.
- (java.net.InetAddress)" class="section detail">

### NetworkEndpoint

public NetworkEndpoint(@NonNull [InetAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html) address)

    Creates a new instance.
Parameters:
    `address` -

    The IP Address of the network endpoint.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
