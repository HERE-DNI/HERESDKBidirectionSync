---
title: "MaxSpeedOnSegment (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaxspeedonsegment"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MaxSpeedOnSegment

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.MaxSpeedOnSegment
------------------------------------------------------------------------
public final class MaxSpeedOnSegment extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
New base speed for a segment. Affects route calculation and the ETA. Cannot increase base speed on segment.

**Note:** This option can only be used with the `RoutingEngine`. The `OfflineRoutingEngine` is not supported and the option will be ignored. Note that the `OfflineRoutingEngine` is only available for the Navigate license.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [baseSpeedInMetersPerSecond](#baseSpeedInMetersPerSecond)

New maximum value in m/s of baseSpeed on segment.

[`SegmentReference`](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")

  [segment](#segment)

A segment for which the new base speed is specified.

## Constructor Summary

Constructors

Constructor

  Description

  [MaxSpeedOnSegment](#%3Cinit%3E(com.here.sdk.routing.SegmentReference,double))`(`[`SegmentReference`](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")` segment, double baseSpeedInMetersPerSecond)`

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

### segment

@NonNull public [SegmentReference](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing") segment

    A segment for which the new base speed is specified. Only the `segmendId` and `travelDirection` parameters are used, other parameters are ignored. Setting a `segmendId` is mandatory.

    **Note:** The `SegmentReference` is not directly accessible from the map via the HERE SDK. Although, after route calculation you can retrieve the related segments for each [`Span`](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing"). The segment IDs are the same that are also used by, for example, the [Routing REST API](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html). These IDs are mostly stable and only change when the underlying map data changes due to a new road or similar changes in the real world.

### baseSpeedInMetersPerSecond

public double baseSpeedInMetersPerSecond

    New maximum value in m/s of baseSpeed on segment. The provided value must be in the range \[1.0, 70.0\]. Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.

## Constructor Details

  - (com.here.sdk.routing.SegmentReference,double)" class="section detail">

### MaxSpeedOnSegment

public MaxSpeedOnSegment(@NonNull [SegmentReference](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing") segment, double baseSpeedInMetersPerSecond)

    Creates a new instance.
Parameters:
    `segment` -

    A segment for which the new base speed is specified. Only the `segmendId` and `travelDirection` parameters are used, other parameters are ignored. Setting a `segmendId` is mandatory.

    **Note:** The `SegmentReference` is not directly accessible from the map via the HERE SDK. Although, after route calculation you can retrieve the related segments for each [`Span`](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing"). The segment IDs are the same that are also used by, for example, the [Routing REST API](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html). These IDs are mostly stable and only change when the underlying map data changes due to a new road or similar changes in the real world.

    `baseSpeedInMetersPerSecond` -

    New maximum value in m/s of baseSpeed on segment. The provided value must be in the range \[1.0, 70.0\]. Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
