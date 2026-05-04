---
title: "MapPolyline.DashRepresentation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappolyline-dashrepresentation"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPolyline.DashRepresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
[com.here.sdk.mapview.MapItemRepresentation](sdk-for-android-explore-api-reference-latestmapitemrepresentation "class in com.here.sdk.mapview")
[com.here.sdk.mapview.MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")
com.here.sdk.mapview.MapPolyline.DashRepresentation
Enclosing class:
[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapPolyline.DashRepresentation extends [MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")
Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.

The length of the dash and gap are set independently, allowing for patterns like `' — — — —'` (dash length = gap length) or `' ——— ——— ———'` (dash length != gap length).

## Nested Class Summary

## Nested classes/interfaces inherited from class com.here.sdk.mapview.[MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")

  [`MapPolyline.Representation.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationerrorcode "enum class in com.here.sdk.mapview"), [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

## Constructor Summary

Constructors

Constructor

  Description

  [DashRepresentation](#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color))`(`[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` lineWidth, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` dashLength, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` gapLength, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` dashColor)`

Creates a representation for a dashed line.

[DashRepresentation](#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.core.Color))`(`[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` lineWidth, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` dashLength, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` gapLength, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` dashColor, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` gapColor)`

Creates a representation for a dashed line with both dash and the gap being colored.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getDashColor](#getDashColor())`()`

Gets the color of the dashes of the polyline.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getDashLength](#getDashLength())`()`

Gets the map measure dependent polyline dash length.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getGapColor](#getGapColor())`()`

Gets the color for the gaps of the polyline.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getGapLength](#getGapLength())`()`

Gets the map measure dependent polyline gap length.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getLineWidth](#getLineWidth())`()`

Gets the map measure dependent polyline width.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color)" class="section detail">

### DashRepresentation

public DashRepresentation(@NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") gapLength, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") dashColor) throws [MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    Creates a representation for a dashed line. Gaps are not displayed.

    At map measures smaller than the smallest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the smallest map measure in the respective [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") object.

    At map measures bigger than the biggest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the biggest map measure in the respective [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") object.

    At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

    For [`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported.

    For [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") only [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) is supported.

    All sizes must not be 0 ([`MapMeasureDependentRenderSize.sizes`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#sizes) with all values set to 0.0).
Parameters:
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `dashLength` -

    The dash length of the polyline depending on the map measure.

    `gapLength` -

    The gap length of the polyline depending on the map measure.

    `dashColor` -

    The dash color of the polyline.

    Throws:
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.
- (com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.core.Color)" class="section detail">

### DashRepresentation

public DashRepresentation(@NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") gapLength, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") dashColor, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") gapColor) throws [MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    Creates a representation for a dashed line with both dash and the gap being colored.

    At map measures smaller than the smallest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the smallest map measure in the respective [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") object.

    At map measures bigger than the biggest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the biggest map measure in the respective [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") object.

    At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

    For [`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported.

    For [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") only [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) is supported.

    All sizes must not be 0 ([`MapMeasureDependentRenderSize.sizes`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#sizes) with all values set to 0.0).
Parameters:
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `dashLength` -

    The dash length of the polyline depending on the map measure.

    `gapLength` -

    The gap length of the polyline depending on the map measure.

    `dashColor` -

    The color of the dashes.

    `gapColor` -

    The color of the gaps.

    Throws:
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.

## Method Details

### getLineWidth

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getLineWidth()

    Gets the map measure dependent polyline width.

    At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

    At map measures bigger than biggest map measure in the `lineWidth` line width is constant and equal to the width given for the biggest map measure in the `lineWidth`.

    At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.
Returns:
    The width of the polyline depending on the map measure.

### getDashLength

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getDashLength()

    Gets the map measure dependent polyline dash length.

    At map measures smaller than smallest map measure in the `dashLength` line width is constant and equal to the width given for the smallest map measure in the `dashLength`.

    At map measures bigger than biggest map measure in the `dashLength` line width is constant and equal to the width given for the biggest map measure in the `dashLength`.

    At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.
Returns:
    The dash length of the polyline depending on the map measure.

### getGapLength

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getGapLength()

    Gets the map measure dependent polyline gap length.

    At map measures smaller than smallest map measure in the `gapLength` line width is constant and equal to the width given for the smallest map measure in the `gapLength`.

    At map measures bigger than biggest map measure in the `gapLength` line width is constant and equal to the width given for the biggest map measure in the `gapLength`.

    At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.
Returns:
    The gap length of the polyline depending on the map measure.

### getDashColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getDashColor()

    Gets the color of the dashes of the polyline.
Returns:
    The color of the dashes of the polyline.

### getGapColor

@Nullable public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getGapColor()

    Gets the color for the gaps of the polyline. Returns `null` if no color is used.
Returns:
    The color for the gaps of the polyline. The default value is `null` and no color is used.
