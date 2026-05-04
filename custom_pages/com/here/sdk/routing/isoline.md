---
title: "Isoline (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestisoline"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Isoline

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.Isoline
------------------------------------------------------------------------
public final class Isoline extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents an isoline polygon around a center point. Any possible route between the center and any point on the edges of the polygon can be travelled within the given range restriction. The edges of the polygon are not guaranteed to be on the road as all reachable road endpoints are smoothened to fit into one polygon shape. This process can be influenced by setting [`IsolineOptions.Calculation.maxPoints`](sdk-for-android-explore-api-reference-latestisolineoptions-calculation#maxPoints).

## Constructor Summary

Constructors

Constructor

  Description

  [Isoline](#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,double,com.here.sdk.routing.MapMatchedCoordinates,java.util.List))`(`[`IsolineRangeType`](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")` rangeType, double rangeValue, `[`MapMatchedCoordinates`](sdk-for-android-explore-api-reference-latestmapmatchedcoordinates "class in com.here.sdk.routing")` center, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")`> polygons)`

Constructs an isoline instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`MapMatchedCoordinates`](sdk-for-android-explore-api-reference-latestmapmatchedcoordinates "class in com.here.sdk.routing")

  [getCenter](#getCenter())`()`

Gets the center point that was used to calculate this isoline.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")`>`

  [getPolygons](#getPolygons())`()`

Gets a list of polygons that belong to this isoline.

[`IsolineRangeType`](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")

  [getRangeType](#getRangeType())`()`

Gets the type of the restriction that was used to calculate this isoline.

`double`

  [getRangeValue](#getRangeValue())`()`

Gets the numerical value of the restriction that was used to calculate this isoline.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.routing.IsolineRangeType,double,com.here.sdk.routing.MapMatchedCoordinates,java.util.List)" class="section detail">

### Isoline

public Isoline(@NonNull [IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing") rangeType, double rangeValue, @NonNull [MapMatchedCoordinates](sdk-for-android-explore-api-reference-latestmapmatchedcoordinates "class in com.here.sdk.routing") center, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")\> polygons)

    Constructs an isoline instance. This instance is provided by the [`CalculateIsolineCallback`](sdk-for-android-explore-api-reference-latestcalculateisolinecallback "interface in com.here.sdk.routing").
Parameters:
    `rangeType` -

    Specifies the range type of the provided `rangeValue` list.

    `rangeValue` -

    A list of range values. At least one value must be set.

    `center` -

    The center of the isoline.

    `polygons` -

    A list of polygons that belong to this isoline. At least one value must be set.

## Method Details

### getRangeType

@NonNull public [IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing") getRangeType()

    Gets the type of the restriction that was used to calculate this isoline.
Returns:
    Specifies the type of the restriction that was used to calculate this isoline.

### getRangeValue

public double getRangeValue()

    Gets the numerical value of the restriction that was used to calculate this isoline.
Returns:
    Specifies the numerical value of the restriction that was used to calculate this isoline.

### getCenter

@NonNull public [MapMatchedCoordinates](sdk-for-android-explore-api-reference-latestmapmatchedcoordinates "class in com.here.sdk.routing") getCenter()

    Gets the center point that was used to calculate this isoline.

    Specifies the center point that was used to calculate this isoline. This includes the original center that was passed to the RoutingEngine.
Returns:
    The center point that was used to calculate this isoline.

### getPolygons

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")\> getPolygons()

    Gets a list of polygons that belong to this isoline. An isoline can consist of multiple polygons. For example, islands that can be reached by a ferry are included. Each island is then represented as a separate polygon. However, in most cases only a single polygon is included.
Returns:
    A list of polygons that belong to this isoline. An isoline can consist of multiple polygons. For example, islands that can be reached by a ferry are included. Each island is then represented as a separate polygon. However, in most cases only a single polygon is included.
