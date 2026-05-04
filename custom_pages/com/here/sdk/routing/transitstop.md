---
title: "TransitStop (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransitstop"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransitStop

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TransitStop
------------------------------------------------------------------------
public final class TransitStop extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A transit stop between the departure and destination of a transit section.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`TransitDeparture`](sdk-for-android-explore-api-reference-latesttransitdeparture "class in com.here.sdk.routing")

  [departure](#departure)

Departure.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [duration](#duration)

Stop duration.

## Constructor Summary

Constructors

Constructor

  Description

  [TransitStop](#%3Cinit%3E(com.here.sdk.routing.TransitDeparture))`(`[`TransitDeparture`](sdk-for-android-explore-api-reference-latesttransitdeparture "class in com.here.sdk.routing")` departure)`

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

### departure

@NonNull public [TransitDeparture](sdk-for-android-explore-api-reference-latesttransitdeparture "class in com.here.sdk.routing") departure

    Departure.

### duration

@Nullable public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration

    Stop duration. If not set, the vehicle departs as soon as people are on board. Defaults to `null`.

## Constructor Details

  - (com.here.sdk.routing.TransitDeparture)" class="section detail">

### TransitStop

public TransitStop(@NonNull [TransitDeparture](sdk-for-android-explore-api-reference-latesttransitdeparture "class in com.here.sdk.routing") departure)

    Creates a new instance.
Parameters:
    `departure` -

    Departure.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
