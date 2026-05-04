---
title: "PolylineSimplifier.Options (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolylinesimplifier-options"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PolylineSimplifier.Options

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.PolylineSimplifier.Options
Enclosing class:
[PolylineSimplifier](sdk-for-android-explore-api-reference-latestpolylinesimplifier "class in com.here.sdk.core")

------------------------------------------------------------------------
public static final class PolylineSimplifier.Options extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Controls the strategy of [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) when reducing a size of polyline.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `long`

  [maxPoints](#maxPoints)

Sets the upper limit on the resulting collection for the [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)).

`static final long`

  [SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL](#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL)

Value for simplification tolerance for 14 zoom level without significant artifacts.

`long`

  [simplificationToleranceInMeters](#simplificationToleranceInMeters)

Sets the accuracy limit for the [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)): higher tolerance results in more simplification (fewer points); lower tolerance keeps the line closer to its original shape.

## Constructor Summary

Constructors

Constructor

  Description

  [Options](#%3Cinit%3E())`()`

Creates default options with [`maxPoints`](#maxPoints) equal to 0 and [`simplificationToleranceInMeters`](#simplificationToleranceInMeters) equal to [`SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL`](#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL).

[Options](#%3Cinit%3E(long,long))`(long maxPoints, long simplificationToleranceInMeters)`

Creates options with explicitly specified [`maxPoints`](#maxPoints) and [`simplificationToleranceInMeters`](#simplificationToleranceInMeters).

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL

public static final long SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL

    Value for simplification tolerance for 14 zoom level without significant artifacts.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.core.PolylineSimplifier.Options.SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL)

### maxPoints

public long maxPoints

    Sets the upper limit on the resulting collection for the [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)). Lower value results in the lower accuracy of the resulting polyline. If `maxPoints` is less than `2` then resulting polyline will not have an upper limit on the size and only [`simplificationToleranceInMeters`](#simplificationToleranceInMeters) will be considered. When `maxPoints` is greater than size of the passed polyline then simplification algorithm will take into account only [`simplificationToleranceInMeters`](#simplificationToleranceInMeters).

### simplificationToleranceInMeters

public long simplificationToleranceInMeters

    Sets the accuracy limit for the [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)):

    - higher tolerance results in more simplification (fewer points);
    - lower tolerance keeps the line closer to its original shape.

    If removing a point produces polyline, which deviates from the original one more than `simplificationToleranceInMeters`, then this point is left in the collection.

    If specified tolerance will not allow to create a polyline conforming to [`maxPoints`](#maxPoints), then `simplificationToleranceInMeters` is ignored.

    Default value is equal to [`SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL`](#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL).

## Constructor Details

  - ()" class="section detail">

### Options

public Options()

    Creates default options with [`maxPoints`](#maxPoints) equal to 0 and [`simplificationToleranceInMeters`](#simplificationToleranceInMeters) equal to [`SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL`](#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL).

  - (long,long)" class="section detail">

### Options

public Options(long maxPoints, long simplificationToleranceInMeters)

    Creates options with explicitly specified [`maxPoints`](#maxPoints) and [`simplificationToleranceInMeters`](#simplificationToleranceInMeters).
Parameters:
    `maxPoints` -

    Sets the upper limit on the resulting collection for the [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)). Lower value results in the lower accuracy of the resulting polyline. If `maxPoints` is less than `2` then resulting polyline will not have an upper limit on the size and only [`simplificationToleranceInMeters`](#simplificationToleranceInMeters) will be considered. When `maxPoints` is greater than size of the passed polyline then simplification algorithm will take into account only [`simplificationToleranceInMeters`](#simplificationToleranceInMeters).

    `simplificationToleranceInMeters` -

    Sets the accuracy limit for the [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)):

    - higher tolerance results in more simplification (fewer points);
    - lower tolerance keeps the line closer to its original shape.

    If removing a point produces polyline, which deviates from the original one more than `simplificationToleranceInMeters`, then this point is left in the collection.

    If specified tolerance will not allow to create a polyline conforming to [`maxPoints`](#maxPoints), then `simplificationToleranceInMeters` is ignored.

    Default value is equal to [`SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL`](#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL).
