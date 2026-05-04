---
title: "AvoidCorridorAreaOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestavoidcorridorareaoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AvoidCorridorAreaOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.AvoidCorridorAreaOptions
------------------------------------------------------------------------
public final class AvoidCorridorAreaOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Area of corridor shape which routes must not cross and exceptions for this area.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")

  [avoidCorridorArea](#avoidCorridorArea)

Area of corridor shape which routes must not cross.

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

  [AvoidCorridorAreaOptions](#%3Cinit%3E(com.here.sdk.core.GeoCorridor))`(`[`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")` avoidCorridorArea)`

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

### avoidCorridorArea

@NonNull public [GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core") avoidCorridorArea

    Area of corridor shape which routes must not cross. Strictly enforced. Violations are reported as [`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_BLOCKED_ROAD). **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

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

  - (com.here.sdk.core.GeoCorridor)" class="section detail">

### AvoidCorridorAreaOptions

public AvoidCorridorAreaOptions(@NonNull [GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core") avoidCorridorArea)

    Creates a new instance.
Parameters:
    `avoidCorridorArea` -

    Area of corridor shape which routes must not cross. Strictly enforced. Violations are reported as [`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_BLOCKED_ROAD). **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
