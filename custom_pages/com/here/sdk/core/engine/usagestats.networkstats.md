---
title: "UsageStats.NetworkStats (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestusagestats-networkstats"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class UsageStats.NetworkStats

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.UsageStats.NetworkStats
Enclosing class:
[UsageStats](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine")

------------------------------------------------------------------------
public static final class UsageStats.NetworkStats extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Provides network statistics in bytes per method.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [methodCall](#methodCall)

Name or description of the method being called.

`long`

  [receivedBytes](#receivedBytes)

Number of bytes received from the network.

`long`

  [requestCounter](#requestCounter)

Amount of calls for particular family of methodCall.

`long`

  [sentBytes](#sentBytes)

Number of bytes sent over the network.

## Constructor Summary

Constructors

Constructor

  Description

  [NetworkStats](#%3Cinit%3E(long,long,java.lang.String,long))`(long sentBytes, long receivedBytes, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` methodCall, long requestCounter)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### sentBytes

public long sentBytes

    Number of bytes sent over the network.

### receivedBytes

public long receivedBytes

    Number of bytes received from the network.

### methodCall

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) methodCall

    Name or description of the method being called.

### requestCounter

public long requestCounter

    Amount of calls for particular family of methodCall. methodCall in this case is considered as base request, additional query params are ignored, all calculated as one request. e.g. https://search.hereapi.com/someparams and https://search.hereapi.com/someparams2 will be considered as 1 methodCall, and requestCounter is 2.

## Constructor Details

  - (long,long,java.lang.String,long)" class="section detail">

### NetworkStats

public NetworkStats(long sentBytes, long receivedBytes, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) methodCall, long requestCounter)

    Creates a new instance.
Parameters:
    `sentBytes` -

    Number of bytes sent over the network.

    `receivedBytes` -

    Number of bytes received from the network.

    `methodCall` -

    Name or description of the method being called.

    `requestCounter` -

    Amount of calls for particular family of methodCall. methodCall in this case is considered as base request, additional query params are ignored, all calculated as one request. e.g. https://search.hereapi.com/someparams and https://search.hereapi.com/someparams2 will be considered as 1 methodCall, and requestCounter is 2.
