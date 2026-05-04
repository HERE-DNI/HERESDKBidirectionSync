---
title: "RouteStop (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutestop"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RouteStop

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RouteStop
------------------------------------------------------------------------
public final class RouteStop extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Route stop that should be used together with import route functionality. It specifies location index within provided route locations track. Route stop can have additional stop delay, which will be included in expected time to arrival. During navigation the stop will be treated as stopover and will be reported as milestone when passing-by. Only available for the Navigate licence.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `int`

  [locationIndex](#locationIndex)

Index of location, used for route stop.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [stopDuration](#stopDuration)

Time that will be spent on route stop.

## Constructor Summary

Constructors

Constructor

  Description

  [RouteStop](#%3Cinit%3E(int))`(int locationIndex)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### locationIndex

public int locationIndex

    Index of location, used for route stop. Index should be \>= 1, which prevents user from using origin location as route stop.

### stopDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") stopDuration

    Time that will be spent on route stop.

## Constructor Details

  - (int)" class="section detail">

### RouteStop

public RouteStop(int locationIndex)

    Creates a new instance.
Parameters:
    `locationIndex` -

    Index of location, used for route stop. Index should be \>= 1, which prevents user from using origin location as route stop.
