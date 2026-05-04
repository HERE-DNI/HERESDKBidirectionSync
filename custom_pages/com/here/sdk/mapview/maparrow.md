---
title: "MapArrow (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaparrow"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapArrow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapArrow
------------------------------------------------------------------------
public final class MapArrow extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A visual representation of an arrow on the map. It consists of a tail - a polyline with an arbitrary number of points - and a head at its end.

The map arrows are only visible on zoom levels \>= 13.

Altitude component of `GeoPolyline`'s vertices is ignored.

## Constructor Summary

Constructors

Constructor

  Description

  [MapArrow](#%3Cinit%3E(com.here.sdk.core.GeoPolyline,double,com.here.sdk.core.Color))`(`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")` geometry, double widthInPixels, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color)`

Creates a new `MapArrow` instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview"), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`>`

  [getMeasureDependentTailWidth](#getMeasureDependentTailWidth())`()`

Gets the [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") dependent arrow tail width in pixels.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`>`

  [getVisibilityRanges](#getVisibilityRanges())`()`

Gets the list of visibility ranges.

`void`

  [setMeasureDependentTailWidth](#setMeasureDependentTailWidth(java.util.Map))`(`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview"), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`> value)`

Sets the [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") dependent arrow tail width in pixels.

`void`

  [setVisibilityRanges](#setVisibilityRanges(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`> value)`

Sets visibility ranges for this map arrow.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.core.GeoPolyline,double,com.here.sdk.core.Color)" class="section detail">

### MapArrow

public MapArrow(@NonNull [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") geometry, double widthInPixels, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color)

    Creates a new `MapArrow` instance.

    Altitude component of `GeoPolyline`'s vertices is ignored.
Parameters:
    `geometry` -

    The geometry of the arrow tail. The last coordinate in the list defines the position where the head of the arrow is located.

    `widthInPixels` -

    The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.

    `color` -

    The color of the arrow. The alpha channel is ignored, the color is interpreted as fully opaque.

## Method Details

### getMeasureDependentTailWidth

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview"),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> getMeasureDependentTailWidth()

    Gets the [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") dependent arrow tail width in pixels.

    If tail width was configured without [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") dependency, then `measureDependentTailWidth` contains single entry with measure 0 of type [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) and width value equal to `widthInPixels`.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Returns:
    The width of the arrow tail in pixels, where the key is a [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") and the value is a tail width in pixels at this [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview").

### setMeasureDependentTailWidth

public void setMeasureDependentTailWidth(@NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview"),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> value)

    Sets the [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") dependent arrow tail width in pixels.

    The width values are linearly interpolated between nearest map entries. Width values for [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") outside the map entries are kept constant, using the value of the largest/smallest key.

    Only [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type is supported. Other [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") types are unsupported and hence, will be ignored.

    Map with a single entry is equivalent to use of the `widthInPixels` value in the constructor, so a constant width setting, independent of camera.

    Empty input is ignored and existing width is maintained.

    The width values should be positive. Map entries with width values less than or equal to 0 are ignored.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `value` -

    The width of the arrow tail in pixels, where the key is a [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") and the value is a tail width in pixels at this [`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview").

### getVisibilityRanges

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> getVisibilityRanges()

    Gets the list of visibility ranges.

    A range is half-open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

    When empty (the default), the map arrows are visible without map measure restrictions. Only `MapMeasureRange`(s) of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type are supported. `MapMeasureRange`(s) of other unsupported types will be ignored.}
Returns:
    The list of visibility ranges, in which the map arrow is visible.

### setVisibilityRanges

public void setVisibilityRanges(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> value)

    Sets visibility ranges for this map arrow.

    A range is half-open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

    When empty (the default), the map arrows are visible without map measure restrictions. Only `MapMeasureRange`(s) of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type are supported. `MapMeasureRange`(s) of other unsupported types will be ignored.}
Parameters:
    `value` -

    The list of visibility ranges, in which the map arrow is visible.
