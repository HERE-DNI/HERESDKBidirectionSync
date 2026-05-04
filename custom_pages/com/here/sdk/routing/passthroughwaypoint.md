---
title: "PassThroughWaypoint (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpassthroughwaypoint"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PassThroughWaypoint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.PassThroughWaypoint
------------------------------------------------------------------------
public final class PassThroughWaypoint extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This structure provides all the information for a passthrough waypoint. The location information and offset of the waypoint are stored in [`place`](#place) and [`offset`](#offset) respectively.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [offset](#offset)

Index over [`Section.getGeometry()`](sdk-for-android-explore-api-reference-latestsection#getGeometry()) where the passthrough waypoint is located.

[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")

  [place](#place)

The location information of passthrough waypoint.

## Constructor Summary

Constructors

Constructor

  Description

  [PassThroughWaypoint](#%3Cinit%3E(com.here.sdk.routing.RoutePlace))`(`[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")` place)`

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

    The location information of passthrough waypoint.

### offset

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) offset

    Index over [`Section.getGeometry()`](sdk-for-android-explore-api-reference-latestsection#getGeometry()) where the passthrough waypoint is located.

## Constructor Details

  - (com.here.sdk.routing.RoutePlace)" class="section detail">

### PassThroughWaypoint

public PassThroughWaypoint(@NonNull [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") place)

    Creates a new instance.
Parameters:
    `place` -

    The location information of passthrough waypoint.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
