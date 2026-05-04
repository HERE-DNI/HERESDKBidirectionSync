---
title: "TrafficOnRoute (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficonroute"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficOnRoute

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TrafficOnRoute
------------------------------------------------------------------------
public final class TrafficOnRoute extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Traffic information on a route. Information for the already traveled portion of the route is omitted.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `int`

  [lastTraveledSectionIndex](#lastTraveledSectionIndex)

Indicates the index of the last traveled route section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficOnSection`](sdk-for-android-explore-api-reference-latesttrafficonsection "class in com.here.sdk.routing")`>`

  [trafficSections](#trafficSections)

List of traffic sections.

`int`

  [traveledDistanceOnLastSectionInMeters](#traveledDistanceOnLastSectionInMeters)

Offset, in meter, to the last visited position on the route section defined by the last traveled section index.

## Constructor Summary

Constructors

Constructor

  Description

  [TrafficOnRoute](#%3Cinit%3E())`()`

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

### lastTraveledSectionIndex

public int lastTraveledSectionIndex

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

### traveledDistanceOnLastSectionInMeters

public int traveledDistanceOnLastSectionInMeters

    Offset, in meter, to the last visited position on the route section defined by the last traveled section index.

### trafficSections

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficOnSection](sdk-for-android-explore-api-reference-latesttrafficonsection "class in com.here.sdk.routing")\> trafficSections

    List of traffic sections.

## Constructor Details

  - ()" class="section detail">

### TrafficOnRoute

public TrafficOnRoute()

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
