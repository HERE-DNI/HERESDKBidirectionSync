---
title: "MapLayerVisibilityRange (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaplayervisibilityrange"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapLayerVisibilityRange

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapLayerVisibilityRange
------------------------------------------------------------------------
public final class MapLayerVisibilityRange extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A layer's visibility along a zoom level range. The range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final double`

  [maximumZoomLevel](#maximumZoomLevel)

Minimum zoom level from which the layer will not be visible.

`final double`

  [minimumZoomLevel](#minimumZoomLevel)

Minimum zoom level on which the layer will be visible.

## Constructor Summary

Constructors

Constructor

  Description

  [MapLayerVisibilityRange](#%3Cinit%3E(double,double))`(double minimumZoomLevel, double maximumZoomLevel)`

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

### minimumZoomLevel

public final double minimumZoomLevel

    Minimum zoom level on which the layer will be visible. The value must be greater than or equal to the `MapCameraLimits.MIN_ZOOM_LEVEL`.

### maximumZoomLevel

public final double maximumZoomLevel

    Minimum zoom level from which the layer will not be visible. The value must be less than or equal to the `MapCameraLimits.MAX_ZOOM_LEVEL`. Note that the map layer is not visible at the maximum zoom level.

## Constructor Details

  - (double,double)" class="section detail">

### MapLayerVisibilityRange

public MapLayerVisibilityRange(double minimumZoomLevel, double maximumZoomLevel)

    Creates a new instance.
Parameters:
    `minimumZoomLevel` -

    Minimum zoom level on which the layer will be visible. The value must be greater than or equal to the `MapCameraLimits.MIN_ZOOM_LEVEL`.

    `maximumZoomLevel` -

    Minimum zoom level from which the layer will not be visible. The value must be less than or equal to the `MapCameraLimits.MAX_ZOOM_LEVEL`. Note that the map layer is not visible at the maximum zoom level.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
