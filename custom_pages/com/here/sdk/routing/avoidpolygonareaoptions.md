---
title: "AvoidPolygonAreaOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestavoidpolygonareaoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AvoidPolygonAreaOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.AvoidPolygonAreaOptions
------------------------------------------------------------------------
public final class AvoidPolygonAreaOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify polygon shape which routes must not cross.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")

  [avoidPolygonArea](#avoidPolygonArea)

Area of polygon shape which routes must not cross.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")`>`

  [boundingBoxExceptionAreas](#boundingBoxExceptionAreas)

Areas of rectangular shape to exclude from avoidance.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")`>`

  [corridorExceptionAreas](#corridorExceptionAreas)

Areas of corridor shape to exclude from avoidance.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")`>`

  [polygonExceptionAreas](#polygonExceptionAreas)

Areas of polygon shape to exclude from avoidance.

## Constructor Summary

Constructors

Constructor

  Description

  [AvoidPolygonAreaOptions](#%3Cinit%3E(com.here.sdk.core.GeoPolygon))`(`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")` avoidPolygonArea)`

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

### avoidPolygonArea

@NonNull public [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") avoidPolygonArea

    Area of polygon shape which routes must not cross. Strictly enforced. Violations are reported as [`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_BLOCKED_ROAD). **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated.

### boundingBoxExceptionAreas

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")\> boundingBoxExceptionAreas

    Areas of rectangular shape to exclude from avoidance.

### polygonExceptionAreas

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")\> polygonExceptionAreas

    Areas of polygon shape to exclude from avoidance.

### corridorExceptionAreas

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")\> corridorExceptionAreas

    Areas of corridor shape to exclude from avoidance. **Note:** Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

## Constructor Details

  - (com.here.sdk.core.GeoPolygon)" class="section detail">

### AvoidPolygonAreaOptions

public AvoidPolygonAreaOptions(@NonNull [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") avoidPolygonArea)

    Creates a new instance.
Parameters:
    `avoidPolygonArea` -

    Area of polygon shape which routes must not cross. Strictly enforced. Violations are reported as [`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_BLOCKED_ROAD). **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
