---
title: "MapPolygon (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappolygon"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPolygon

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapPolygon
------------------------------------------------------------------------
public final class MapPolygon extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A visual representation of a polygon on the map. Can be used to visualize areas of all shapes and sizes.

The geometry to be visualized is represented by an instance of [`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core"). To display circular areas (for example, a position accuracy indicator) use a GeoPolygon created from a [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") using [`GeoPolygon(GeoCircle)`](sdk-for-android-explore-api-reference-latestgeopolygon#%3Cinit%3E(com.here.sdk.core.GeoBox)).

Note:

- The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
- Polygons which are self-intersecting are not supported and may lead to render artifacts.
- The inner boundaries (holes) specified in the GeoPolygon are ignored.

## Constructor Summary

Constructors

Constructor

  Description

  [MapPolygon](#%3Cinit%3E(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color))`(`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")` geometry, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color)`

Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.

[MapPolygon](#%3Cinit%3E(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color,com.here.sdk.core.Color,double))`(`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")` geometry, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` outlineColor, double outlineWidthInPixels)`

Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `int`

  [getDrawOrder](#getDrawOrder())`()`

Gets the draw order of this map polygon relative to other map polygons.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getFillColor](#getFillColor())`()`

Gets the current color of the fill.

[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")

  [getGeometry](#getGeometry())`()`

Gets the current geometry of the polygon.

[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")

  [getMetadata](#getMetadata())`()`

Gets the Metadata instance attached to this polygon.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getOutlineColor](#getOutlineColor())`()`

Gets the color of the polygon outline.

`double`

  [getOutlineWidth](#getOutlineWidth())`()`

Gets the outline width of the polygon in pixels.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`>`

  [getVisibilityRanges](#getVisibilityRanges())`()`

Gets the list of visibility ranges.

`void`

  [setDrawOrder](#setDrawOrder(int))`(int value)`

Sets the draw order of this map polygon relative to other map polygons.

`void`

  [setFillColor](#setFillColor(com.here.sdk.core.Color))`(`[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` value)`

Sets the current color of the fill.

`void`

  [setGeometry](#setGeometry(com.here.sdk.core.GeoPolygon))`(`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")` value)`

Sets a new geometry to update the appearance.

`void`

  [setMetadata](#setMetadata(com.here.sdk.core.Metadata))`(`[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")` value)`

Sets the Metadata instance to be attached to this polygon.

`void`

  [setOutlineColor](#setOutlineColor(com.here.sdk.core.Color))`(`[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` value)`

Sets the color of the polygon outline.

`void`

  [setOutlineWidth](#setOutlineWidth(double))`(double value)`

Sets the outline width of the polygon in pixels.

`void`

  [setVisibilityRanges](#setVisibilityRanges(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`> value)`

Sets visibility ranges for this map polygon.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color)" class="section detail">

### MapPolygon

public MapPolygon(@NonNull [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") geometry, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color)

    Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.

    The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

    Note:

    - The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
    - Polygons which are self-intersecting are not supported and may lead to render artifacts.
    - The inner boundaries (holes) specified in the GeoPolygon are ignored.
Parameters:
    `geometry` -

    The list of vertices representing the outer boundary of polygon.

    `color` -

    The fill color for the polygon
- (com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color,com.here.sdk.core.Color,double)" class="section detail">

### MapPolygon

public MapPolygon(@NonNull [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") geometry, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") outlineColor, double outlineWidthInPixels)

    Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.

    Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque by interpreting the alpha value as 1.

    The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

    Note:

    - The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
    - Polygons which are self-intersecting are not supported and may lead to render artifacts.
    - The inner boundaries (holes) specified in the GeoPolygon are ignored.
Parameters:
    `geometry` -

    The list of vertices representing the outer boundary of polygon.

    `color` -

    The fill color for the polygon.

    `outlineColor` -

    The color of the polygon outline, alpha channel is ignored and treated as 1.

    `outlineWidthInPixels` -

    The width of the polygon outline (in pixels). Negative values are clamped to 0.

## Method Details

### getGeometry

@NonNull public [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") getGeometry()

    Gets the current geometry of the polygon.
Returns:
    The geometry of the polygon. Setting a new geometry will update the appearance.

### setGeometry

public void setGeometry(@NonNull [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") value)

    Sets a new geometry to update the appearance.

    The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

    Note:

    - The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
    - Polygons which are self-intersecting are not supported and may lead to render artifacts.
    - The inner boundaries (holes) specified in the GeoPolygon are ignored.
Parameters:
    `value` -

    The geometry of the polygon. Setting a new geometry will update the appearance.

### getMetadata

@Nullable public [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") getMetadata()

    Gets the Metadata instance attached to this polygon.
Returns:
    The Metadata instance attached to this polygon, `null` by default.

### setMetadata

public void setMetadata(@Nullable [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") value)

    Sets the Metadata instance to be attached to this polygon.
Parameters:
    `value` -

    The Metadata instance attached to this polygon, `null` by default.

### getFillColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getFillColor()

    Gets the current color of the fill.
Returns:
    Color of the polygon's fill.

### setFillColor

public void setFillColor(@NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") value)

    Sets the current color of the fill.

    Fully transparent color (alpha set to 0) disables the fill completely.
Parameters:
    `value` -

    Color of the polygon's fill.

### getDrawOrder

public int getDrawOrder()

    Gets the draw order of this map polygon relative to other map polygons. Default value is 0.
Returns:
    The draw order of this map polygon relative to other map polygons.

### setDrawOrder

public void setDrawOrder(int value)

    Sets the draw order of this map polygon relative to other map polygons.

    Polygon with higher draw order value are drawn on top of polygons with lower draw order.

    In case multiple polygons have the same draw order value then the order in which they were added to the scene matters. Last added polygon is drawn on top.

    Allowed range is 0-1023. Values outside this range will be clamped.
Parameters:
    `value` -

    The draw order of this map polygon relative to other map polygons.

### getVisibilityRanges

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> getVisibilityRanges()

    Gets the list of visibility ranges. The map polygon is visible only inside these map measure ranges. When empty (the default), the map polygon is visible without map measure restrictions.
Returns:
    The list of visibility ranges. The map polygon is visible only inside these map measure ranges.

### setVisibilityRanges

public void setVisibilityRanges(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> value)

    Sets visibility ranges for this map polygon. A range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range. The map polygon is visible only inside these map measure ranges.

    When empty (the default), the map polygon is visible without map measure restrictions. Only `MapMeasureRange`(s) of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type are supported. `MapMeasureRange`(s) of other unsupported types will be ignored.
Parameters:
    `value` -

    The list of visibility ranges. The map polygon is visible only inside these map measure ranges.

### getOutlineColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getOutlineColor()

    Gets the color of the polygon outline. The default outline color is opaque white.
Returns:
    The color of the polygon outline.

### setOutlineColor

public void setOutlineColor(@NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") value)

    Sets the color of the polygon outline.

    Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque.
Parameters:
    `value` -

    The color of the polygon outline.

### getOutlineWidth

public double getOutlineWidth()

    Gets the outline width of the polygon in pixels.

    By default, the outline width is set to zero.
Returns:
    The width of the polygon outline in pixels.

### setOutlineWidth

public void setOutlineWidth(double value)

    Sets the outline width of the polygon in pixels.

    The value should be greater than or equal to 0. Negative values are clamped to zero.
Parameters:
    `value` -

    The width of the polygon outline in pixels.
