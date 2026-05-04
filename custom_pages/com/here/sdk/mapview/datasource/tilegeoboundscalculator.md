---
title: "TileGeoBoundsCalculator (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttilegeoboundscalculator"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TileGeoBoundsCalculator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.TileGeoBoundsCalculator
------------------------------------------------------------------------
public final class TileGeoBoundsCalculator extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A calculator of geodetic bounds for tiles identified by keys generated in a particular tiling scheme ([`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [TileGeoBoundsCalculator](#%3Cinit%3E(com.here.sdk.mapview.datasource.TilingScheme))`(`[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")` tilingScheme)`

Creates an instance of [`TileGeoBoundsCalculator`](sdk-for-android-explore-api-reference-latesttilegeoboundscalculator "class in com.here.sdk.mapview.datasource").

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [boundsOf](#boundsOf(com.here.sdk.mapview.datasource.TileKey))`(`[`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")` tileKey)`

Computes the geodetic bounds (as [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")) for a tile identified by [`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource").

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.datasource.TilingScheme)" class="section detail">

### TileGeoBoundsCalculator

public TileGeoBoundsCalculator(@NonNull [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme)

    Creates an instance of [`TileGeoBoundsCalculator`](sdk-for-android-explore-api-reference-latesttilegeoboundscalculator "class in com.here.sdk.mapview.datasource").
Parameters:
    `tilingScheme` -

    The tiling scheme used for generating the tile keys that are to be supported by this instance.

## Method Details

### boundsOf

@NonNull public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") boundsOf(@NonNull [TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") tileKey)

    Computes the geodetic bounds (as [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")) for a tile identified by [`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource").
Parameters:
    `tileKey` -

    [`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") to compute geodetic bounds for. The geodetic bounds would be calculated relative to the tiling scheme provided at this [`TileGeoBoundsCalculator`](sdk-for-android-explore-api-reference-latesttilegeoboundscalculator "class in com.here.sdk.mapview.datasource") instance creation.

    Returns:
    The geodetic bounds of tile identified by given [`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource").
