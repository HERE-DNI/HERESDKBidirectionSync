---
title: "MapViewOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapviewoptions"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapViewOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapViewOptions
------------------------------------------------------------------------
public final class MapViewOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Options used for initialization of map view

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [initialBackgroundColor](#initialBackgroundColor)

Initial loading background color that will be shown between rendering the first frame without a scene loaded and before rendering the first frame after a scene is loaded.If not set, it will default to

[`MapProjection`](sdk-for-android-explore-api-reference-latestmapprojection "enum class in com.here.sdk.mapview")

  [projection](#projection)

Projection of map

[`MapRenderMode`](sdk-for-android-explore-api-reference-latestmaprendermode "enum class in com.here.sdk.mapview")

  [renderMode](#renderMode)

Specifies whether the `MapView` will use `SurfaceView` or `TextureView` for map rendering.

## Constructor Summary

Constructors

Constructor

  Description

  [MapViewOptions](#%3Cinit%3E())`()`

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

### projection

@NonNull public [MapProjection](sdk-for-android-explore-api-reference-latestmapprojection "enum class in com.here.sdk.mapview") projection

    Projection of map

### initialBackgroundColor

@Nullable public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") initialBackgroundColor

    Initial loading background color that will be shown between rendering the first frame without a scene loaded and before rendering the first frame after a scene is loaded.If not set, it will default to

    \#D3D3D3. Alpha value gets ignored and is assumed as 1.0.

### renderMode

@NonNull public [MapRenderMode](sdk-for-android-explore-api-reference-latestmaprendermode "enum class in com.here.sdk.mapview") renderMode

    Specifies whether the `MapView` will use `SurfaceView` or `TextureView` for map rendering. Defaults to [`MapRenderMode.SURFACE`](sdk-for-android-explore-api-reference-latestmaprendermode#SURFACE).

## Constructor Details

  - ()" class="section detail">

### MapViewOptions

public MapViewOptions()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
