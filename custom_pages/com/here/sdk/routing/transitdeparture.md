---
title: "TransitDeparture (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransitdeparture"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransitDeparture

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TransitDeparture
------------------------------------------------------------------------
public final class TransitDeparture extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This struct holds the transit departure or arrival information.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [delay](#delay)

The accumulated delay in seconds from the scheduled time of the event.

[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")

  [place](#place)

The departure or arrival place.

[`TransitDepartureStatus`](sdk-for-android-explore-api-reference-latesttransitdeparturestatus "enum class in com.here.sdk.routing")

  [status](#status)

Status of the departure.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [time](#time)

Expected departure or arrival time of the event.

## Constructor Summary

Constructors

Constructor

  Description

  [TransitDeparture](#%3Cinit%3E(com.here.sdk.routing.RoutePlace,java.util.Date,java.lang.Integer,com.here.sdk.routing.TransitDepartureStatus))`(`[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")` place, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` time, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` delay, `[`TransitDepartureStatus`](sdk-for-android-explore-api-reference-latesttransitdeparturestatus "enum class in com.here.sdk.routing")` status)`

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

### place

@NonNull public [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") place

    The departure or arrival place.

### time

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) time

    Expected departure or arrival time of the event.

### delay

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) delay

    The accumulated delay in seconds from the scheduled time of the event.

### status

@Nullable public [TransitDepartureStatus](sdk-for-android-explore-api-reference-latesttransitdeparturestatus "enum class in com.here.sdk.routing") status

    Status of the departure.

## Constructor Details

  - (com.here.sdk.routing.RoutePlace,java.util.Date,java.lang.Integer,com.here.sdk.routing.TransitDepartureStatus)" class="section detail">

### TransitDeparture

public TransitDeparture(@NonNull [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") place, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) time, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) delay, @Nullable [TransitDepartureStatus](sdk-for-android-explore-api-reference-latesttransitdeparturestatus "enum class in com.here.sdk.routing") status)

    Creates a new instance.
Parameters:
    `place` -

    The departure or arrival place.

    `time` -

    Expected departure or arrival time of the event.

    `delay` -

    The accumulated delay in seconds from the scheduled time of the event.

    `status` -

    Status of the departure.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
