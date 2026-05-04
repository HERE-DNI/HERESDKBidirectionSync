---
title: "MapPolyline.SolidRepresentation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappolyline-solidrepresentation"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPolyline.SolidRepresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
[com.here.sdk.mapview.MapItemRepresentation](sdk-for-android-explore-api-reference-latestmapitemrepresentation "class in com.here.sdk.mapview")
[com.here.sdk.mapview.MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")
com.here.sdk.mapview.MapPolyline.SolidRepresentation
Enclosing class:
[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapPolyline.SolidRepresentation extends [MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")
Representation for a solid line without outline.

Can represent polylines that have constant width or width dependent on the map zoom.

To achieve constant width lines, use [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") with a single value.

To achieve line width dependent on map zoom, use [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") with multiple values.

For [`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported.

For [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") only [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) is supported.

## Nested Class Summary

## Nested classes/interfaces inherited from class com.here.sdk.mapview.[MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")

  [`MapPolyline.Representation.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationerrorcode "enum class in com.here.sdk.mapview"), [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

## Constructor Summary

Constructors

Constructor

  Description

  [SolidRepresentation](#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap))`(`[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` lineWidth, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color, `[`LineCap`](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview")` capShape)`

Creates a representation for a solid line without outline.

[SolidRepresentation](#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap))`(`[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` lineWidth, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` outlineWidth, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` outlineColor, `[`LineCap`](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview")` capShape)`

Creates a representation for a solid line with outline.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`LineCap`](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview")

  [getCapShape](#getCapShape())`()`

Returns the cap shape of the polyline and its outline.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getLineColor](#getLineColor())`()`

Gets the color of the polyline.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getLineWidth](#getLineWidth())`()`

Gets the map measure dependent polyline width.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getOutlineColor](#getOutlineColor())`()`

Gets the color of outline of the polyline.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getOutlineWidth](#getOutlineWidth())`()`

Gets the map measure dependent polyline outline width.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)" class="section detail">

### SolidRepresentation

public SolidRepresentation(@NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color, @NonNull [LineCap](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview") capShape) throws [MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    Creates a representation for a solid line without outline.

    At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

    At map measures bigger than biggest map measure in the `lineWidth` line width is constant and equal to the width given for the biggest map measure in the `lineWidth`.

    At map measures between two nearest given map measures line width is linearly interpolated between width values given for these map measures.

    For [`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported.

    For [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") only [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) is supported.

    `lineWidth` must not be 0 (`lineWidth.sizes` with all values set to 0.0).
Parameters:
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `color` -

    The color of the polyline.

    `capShape` -

    The cap shape applied to both ends of the polyline.

    Throws:
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.
- (com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)" class="section detail">

### SolidRepresentation

public SolidRepresentation(@NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") outlineWidth, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") outlineColor, @NonNull [LineCap](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview") capShape) throws [MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    Creates a representation for a solid line with outline.

    The total width of the polyline is `line width + 2 * outline width`.

    At map measures smaller than smallest map measure in the `lineWidth` and `outlineWidth`, the value is constant and equal to the width given for the smallest map measure in the `lineWidth` and `outlineWidth`.

    At map measures bigger than biggest map measure in the `lineWidth` and `outlineWidth`, the value is constant and equal to the width given for the biggest map measure in the `lineWidth` and `outlineWidth`.

    At map measures between two nearest given map measure is linearly interpolated between width values given for these map measures.

    For [`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported.

    For [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") only [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) is supported.

    `lineWidth` must not be 0 (`lineWidth.sizes` with all values set to 0.0).
Parameters:
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `color` -

    The color of the polyline.

    `outlineWidth` -

    The width of the outline on one side of the polyline depending on the map measure.

    `outlineColor` -

    The outline color of the polyline.

    `capShape` -

    The cap shape applied to both ends of the polyline.

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

### getLineColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getLineColor()

    Gets the color of the polyline.
Returns:
    The color of the polyline.

### getOutlineWidth

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getOutlineWidth()

    Gets the map measure dependent polyline outline width.

    The total width of the polyline is `line width + 2 * outline width`.

    At map measures smaller than smallest map measure in the `outlineWidth`, outline width is constant and equal to the width given for the smallest map measure in the `outlineWidth`.

    At map measures bigger than biggest map measure in the `outlineWidth`, outline width is constant and equal to the width given for the biggest map measure in the `outlineWidth`.

    At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.
Returns:
    The width of the outline on one side of the polyline depending on the map measure.

### getOutlineColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getOutlineColor()

    Gets the color of outline of the polyline.
Returns:
    The outline color of the polyline.

### getCapShape

@NonNull public [LineCap](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview") getCapShape()

    Returns the cap shape of the polyline and its outline.
Returns:
    The cap shape applied to both ends of the polyline and its outline.
