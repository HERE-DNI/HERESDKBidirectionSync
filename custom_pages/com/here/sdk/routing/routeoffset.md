---
title: "RouteOffset (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrouteoffset"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RouteOffset

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RouteOffset
------------------------------------------------------------------------
public final class RouteOffset extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a specific location along the route. A `RouteOffset` is a location on the route defined by the section index and the distance in meters from the start of that section to the specified location on the route. An offset in meters indicates the distance that needs to be traveled to reach a specific location along the route, such as a railway crossing. For the latter case, the location of a railway crossing can be retrieved from `RouteRailwayCrossing.coordinates`.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [offsetInMeters](#offsetInMeters)

Offset from the start of the indexed [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") to the specified location along the route.

`int`

  [sectionIndex](#sectionIndex)

Index of the corresponding route [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing").

## Constructor Summary

Constructors

Constructor

  Description

  [RouteOffset](#%3Cinit%3E(int,double))`(int sectionIndex, double offsetInMeters)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### sectionIndex

public int sectionIndex

    Index of the corresponding route [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing"). The start of the section indicates the start of the offset.

### offsetInMeters

public double offsetInMeters

    Offset from the start of the indexed [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") to the specified location along the route. The maximum possible offset is limited by the length of the section and cannot exceed it.

## Constructor Details

  - (int,double)" class="section detail">

### RouteOffset

public RouteOffset(int sectionIndex, double offsetInMeters)

    Creates a new instance.
Parameters:
    `sectionIndex` -

    Index of the corresponding route [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing"). The start of the section indicates the start of the offset.

    `offsetInMeters` -

    Offset from the start of the indexed [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") to the specified location along the route. The maximum possible offset is limited by the length of the section and cannot exceed it.
