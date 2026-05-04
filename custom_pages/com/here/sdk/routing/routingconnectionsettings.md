---
title: "RoutingConnectionSettings (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutingconnectionsettings"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RoutingConnectionSettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RoutingConnectionSettings
------------------------------------------------------------------------
public final class RoutingConnectionSettings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Defines the settings for the retry logic when connecting to the HERE routing backend.

When a timeout is triggered, the next connection attempt starts with a increased timeout. new_timeout = initial_timeout + increment \* retry_count

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [connectionTimeoutRetryIncrease](#connectionTimeoutRetryIncrease)

Defines the increase of the timeout for the transfer of data.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [initialConnectionTimeout](#initialConnectionTimeout)

Defines the initial time out for connection to the backend.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [initialTransferTimeout](#initialTransferTimeout)

Defines the initial time out for data transfer from the backend.

`int`

  [maxRetryCount](#maxRetryCount)

Defines the max amount of retries before the route request failes with connection related error codes.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [transferTimeoutRetryIncrease](#transferTimeoutRetryIncrease)

Defines the increase of the timeout for the connection.

## Constructor Summary

Constructors

Constructor

  Description

  [RoutingConnectionSettings](#%3Cinit%3E())`()`

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

### initialConnectionTimeout

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") initialConnectionTimeout

    Defines the initial time out for connection to the backend. By default, the initial connection timeout is 5 seconds.

### connectionTimeoutRetryIncrease

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") connectionTimeoutRetryIncrease

    Defines the increase of the timeout for the transfer of data. By default, the initial connection increment per timeout 10 seconds.

### initialTransferTimeout

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") initialTransferTimeout

    Defines the initial time out for data transfer from the backend. By default, the initial transfer timeout is 10 seconds.

### transferTimeoutRetryIncrease

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") transferTimeoutRetryIncrease

    Defines the increase of the timeout for the connection. By default, the initial transfer increment per timeout is 2 seconds.

### maxRetryCount

public int maxRetryCount

    Defines the max amount of retries before the route request failes with connection related error codes. By default, the max amount of retries is 3.

## Constructor Details

  - ()" class="section detail">

### RoutingConnectionSettings

public RoutingConnectionSettings()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
