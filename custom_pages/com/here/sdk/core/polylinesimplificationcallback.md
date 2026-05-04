---
title: "PolylineSimplificationCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolylinesimplificationcallback"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PolylineSimplificationCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface PolylineSimplificationCallback
The method will be called on the main thread when [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) is finished.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onPolylineSimplified](#onPolylineSimplified(com.here.sdk.core.PolylineSimplificationError,java.util.List))`(`[`PolylineSimplificationError`](sdk-for-android-explore-api-reference-latestpolylinesimplificationerror "enum class in com.here.sdk.core")` queryError, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> result)`

The method will be called on the main thread when [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) is finished.

## Method Details

### onPolylineSimplified

void onPolylineSimplified(@Nullable [PolylineSimplificationError](sdk-for-android-explore-api-reference-latestpolylinesimplificationerror "enum class in com.here.sdk.core") queryError, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> result)

    The method will be called on the main thread when [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) is finished.
Parameters:
    `queryError` -

    The optional error, which occurred during simplification.

    `result` -

    The simplified polyline with number of points less or equal to the input polyline of [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)).
