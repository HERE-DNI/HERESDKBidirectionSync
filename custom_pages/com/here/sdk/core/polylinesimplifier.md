---
title: "PolylineSimplifier (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolylinesimplifier"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PolylineSimplifier

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.PolylineSimplifier
------------------------------------------------------------------------
public final class PolylineSimplifier extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within [`PolylineSimplifier.Options`](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core").

Typical use case is to perform input preparation step before invoking computationally heavy API. Such API have an upper limit on the input collection size and is subject to reduced performance when collection is huge. Examples of such API are:

- `TrafficEngine` methods which accept a `GeoCorridor`;
- `RoutePrefetcher.prefetchGeoCorridor`.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [PolylineSimplifier.Options](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options)

Controls the strategy of [`simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) when reducing a size of polyline.

## Constructor Summary

Constructors

Constructor

  Description

  [PolylineSimplifier](#%3Cinit%3E())`()`

Creates a new instance of [`PolylineSimplifier`](sdk-for-android-explore-api-reference-latestpolylinesimplifier "class in com.here.sdk.core").

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [simplify](#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> polyline, `[`PolylineSimplifier.Options`](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core")` simplificationParameters, `[`PolylineSimplificationCallback`](sdk-for-android-explore-api-reference-latestpolylinesimplificationcallback "interface in com.here.sdk.core")` callback)`

Reduces the number of points in the input polyline.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### PolylineSimplifier

public PolylineSimplifier() throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of [`PolylineSimplifier`](sdk-for-android-explore-api-reference-latestpolylinesimplifier "class in com.here.sdk.core").
Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

## Method Details

### simplify

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") simplify(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> polyline, @NonNull [PolylineSimplifier.Options](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core") simplificationParameters, @NonNull [PolylineSimplificationCallback](sdk-for-android-explore-api-reference-latestpolylinesimplificationcallback "interface in com.here.sdk.core") callback)

    Reduces the number of points in the input polyline. Does this by removing points which are not significant according to the passed [`PolylineSimplifier.Options`](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core"). Simplification process is performed on the device without connecting to the network and is computationally intensive.
Parameters:
    `polyline` -

    Input polyline that should be reduced in size.

    `simplificationParameters` -

    Strategy, that controls the behavior of the underlying algorithm.

    `callback` -

    Callback, which will be invoked on the main thread, when operation is finished.

    Returns:
    Controls an asynchronous operation.
