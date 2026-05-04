---
title: "IsolineOptions.Calculation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestisolineoptions-calculation"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class IsolineOptions.Calculation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.IsolineOptions.Calculation
Enclosing class:
[IsolineOptions](sdk-for-android-explore-api-reference-latestisolineoptions "class in com.here.sdk.routing")

------------------------------------------------------------------------
public static final class IsolineOptions.Calculation extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Specifies isoline parameters. Setting at least one limit to [`rangeValues`](#rangeValues) is mandatory or the calculation will fail.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`IsolineCalculationMode`](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing")

  [isolineCalculationMode](#isolineCalculationMode)

Specifies how isoline calculation is optimized.

[`RoutePlaceDirection`](sdk-for-android-explore-api-reference-latestrouteplacedirection "enum class in com.here.sdk.routing")

  [isolineDirection](#isolineDirection)

Specifies if calculations will be from or to a specific point.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxPoints](#maxPoints)

Limits the number of points in the resulting isoline polygon.

[`IsolineRangeType`](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")

  [rangeType](#rangeType)

Specifies the range of values to be included in the isoline.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [rangeValues](#rangeValues)

A list of ranges.

## Constructor Summary

Constructors

Constructor

  Description

  [Calculation](#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List))`(`[`IsolineRangeType`](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")` rangeType, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`> rangeValues)`

  [Calculation](#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode))`(`[`IsolineRangeType`](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")` rangeType, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`> rangeValues, `[`IsolineCalculationMode`](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing")` isolineCalculationMode)`

  [Calculation](#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode,java.lang.Integer,com.here.sdk.routing.RoutePlaceDirection))`(`[`IsolineRangeType`](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")` rangeType, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`> rangeValues, `[`IsolineCalculationMode`](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing")` isolineCalculationMode, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` maxPoints, `[`RoutePlaceDirection`](sdk-for-android-explore-api-reference-latestrouteplacedirection "enum class in com.here.sdk.routing")` isolineDirection)`

  [Calculation](#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.RoutePlaceDirection))`(`[`IsolineRangeType`](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")` rangeType, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`> rangeValues, `[`RoutePlaceDirection`](sdk-for-android-explore-api-reference-latestrouteplacedirection "enum class in com.here.sdk.routing")` isolineDirection)`

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### rangeType

@NonNull public [IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing") rangeType

    Specifies the range of values to be included in the isoline.

### rangeValues

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> rangeValues

    A list of ranges. The unit is defined by the type parameter. Each range defines the maximum allowed value to reach a destination. For each value an [`Isoline`](sdk-for-android-explore-api-reference-latestisoline "class in com.here.sdk.routing") is calculated indicating the reachable area. If empty, [`IsolineOptions`](sdk-for-android-explore-api-reference-latestisolineoptions "class in com.here.sdk.routing") object is considered invalid.

### isolineCalculationMode

@NonNull public [IsolineCalculationMode](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing") isolineCalculationMode

    Specifies how isoline calculation is optimized. The default waypoint type is [`IsolineCalculationMode.BALANCED`](sdk-for-android-explore-api-reference-latestisolinecalculationmode#BALANCED).

### maxPoints

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxPoints

    Limits the number of points in the resulting isoline polygon. If the isoline consists of multiple polygons, the sum of points from all polygons is considered. Note that this parameter does not affect the calculation, but the shape of the polygon. Look at [`IsolineCalculationMode`](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing") parameter to optimize performance. A higher value will result in a more accurate polygon shape. Rendering a polygon with a high number of points can negatively impact rendering performance. The minimum allowed value is 30, lower values will be ignored.

### isolineDirection

@NonNull public [RoutePlaceDirection](sdk-for-android-explore-api-reference-latestrouteplacedirection "enum class in com.here.sdk.routing") isolineDirection

    Specifies if calculations will be from or to a specific point. The default isoline direction is [`RoutePlaceDirection.DEPARTURE`](sdk-for-android-explore-api-reference-latestrouteplacedirection#DEPARTURE).

## Constructor Details

  - (com.here.sdk.routing.IsolineRangeType,java.util.List)" class="section detail">

### Calculation

public Calculation(@NonNull [IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing") rangeType, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> rangeValues)
Parameters:
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.
- (com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.RoutePlaceDirection)" class="section detail">

### Calculation

public Calculation(@NonNull [IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing") rangeType, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> rangeValues, @NonNull [RoutePlaceDirection](sdk-for-android-explore-api-reference-latestrouteplacedirection "enum class in com.here.sdk.routing") isolineDirection)
Parameters:
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.

    `isolineDirection` -

    The isoline direction.
- (com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode)" class="section detail">

### Calculation

public Calculation(@NonNull [IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing") rangeType, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> rangeValues, @NonNull [IsolineCalculationMode](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing") isolineCalculationMode)
Parameters:
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.

    `isolineCalculationMode` -

    The isoline calculation mode.
- (com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode,java.lang.Integer,com.here.sdk.routing.RoutePlaceDirection)" class="section detail">

### Calculation

public Calculation(@NonNull [IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing") rangeType, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> rangeValues, @NonNull [IsolineCalculationMode](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing") isolineCalculationMode, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxPoints, @NonNull [RoutePlaceDirection](sdk-for-android-explore-api-reference-latestrouteplacedirection "enum class in com.here.sdk.routing") isolineDirection)
Parameters:
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.

    `isolineCalculationMode` -

    The isoline calculation mode.

    `maxPoints` -

    The max points number.

    `isolineDirection` -

    The isoline direction.
