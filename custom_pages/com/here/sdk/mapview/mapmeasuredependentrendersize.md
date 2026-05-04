---
title: "MapMeasureDependentRenderSize (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMeasureDependentRenderSize

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapMeasureDependentRenderSize
------------------------------------------------------------------------
public final class MapMeasureDependentRenderSize extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a render size, described as map measure dependent values.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapMeasureDependentRenderSize.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationerrorcode)

Describes a reason for failing to create a [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview").

`static final class `

  [MapMeasureDependentRenderSize.InstantiationException](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationexception)

Thrown when a problem occurs while trying to create [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview").

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview")

  [measureKind](#measureKind)

The unit used for the key in [`sizes`](#sizes).

`final `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`>`

  [sizes](#sizes)

The dictionary describing the size (value) per map measure (key).

`final `[`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")

  [sizeUnit](#sizeUnit)

The unit used for the value in [`sizes`](#sizes).

## Constructor Summary

Constructors

Constructor

  Description

  [MapMeasureDependentRenderSize](#%3Cinit%3E(com.here.sdk.mapview.MapMeasure.Kind,com.here.sdk.mapview.RenderSize.Unit,java.util.Map))`(`[`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview")` measureKind, `[`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")` sizeUnit, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> sizes)`

Constructs a `MapMeasureDependentRenderSize` from given parameters.

[MapMeasureDependentRenderSize](#%3Cinit%3E(com.here.sdk.mapview.RenderSize.Unit,double))`(`[`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")` sizeUnit, double size)`

Constructs a `MapMeasureDependentRenderSize` from single size value which is constant across all map measures.

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

### measureKind

@NonNull public final [MapMeasure.Kind](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") measureKind

    The unit used for the key in [`sizes`](#sizes).

### sizeUnit

@NonNull public final [RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") sizeUnit

    The unit used for the value in [`sizes`](#sizes).

### sizes

@NonNull public final [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> sizes

    The dictionary describing the size (value) per map measure (key).

    Units of keys and values are defined in [`measureKind`](#measureKind) and [`sizeUnit`](#sizeUnit).

    `sizes` with a single entry indicates using a fixed size value across all map measures.

## Constructor Details

  - (com.here.sdk.mapview.MapMeasure.Kind,com.here.sdk.mapview.RenderSize.Unit,java.util.Map)" class="section detail">

### MapMeasureDependentRenderSize

public MapMeasureDependentRenderSize(@NonNull [MapMeasure.Kind](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") measureKind, @NonNull [RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") sizeUnit, @NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> sizes) throws [MapMeasureDependentRenderSize.InstantiationException](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")

    Constructs a `MapMeasureDependentRenderSize` from given parameters.

    Supplying `sizes` map with a single entry indicates using a fixed size value across all map measures.
Parameters:
    `measureKind` -

    The unit used for the key in `sizes`.

    `sizeUnit` -

    The unit used for the value in `sizes`.

    `sizes` -

    The dictionary describing the size (value) per map measure (key).

    Throws:
    [`MapMeasureDependentRenderSize.InstantiationException`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview") -

    Instantiation error if `sizes` map is empty or contains negative keys or values.
- (com.here.sdk.mapview.RenderSize.Unit,double)" class="section detail">

### MapMeasureDependentRenderSize

public MapMeasureDependentRenderSize(@NonNull [RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") sizeUnit, double size) throws [MapMeasureDependentRenderSize.InstantiationException](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")

    Constructs a `MapMeasureDependentRenderSize` from single size value which is constant across all map measures.

    The given `size` value is stored in [`sizes`](#sizes) map at key 0 and [`measureKind`](#measureKind) is set to [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL).
Parameters:
    `sizeUnit` -

    The unit used for the value in `size`.

    `size` -

    The size independent of map measure. Must not be negative.

    Throws:
    [`MapMeasureDependentRenderSize.InstantiationException`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview") -

    Instantiation error if `size` is negative.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
