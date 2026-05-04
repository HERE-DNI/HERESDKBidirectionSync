---
title: "MapPolyline (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappolyline"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPolyline

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapPolyline
------------------------------------------------------------------------
public final class MapPolyline extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A visual representation of a line on the map.

The geometry to be visualized is represented by an instance of [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core").

Altitude component of `GeoPolyline`'s vertices is ignored.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [MapPolyline.DashImageRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-dashimagerepresentation)

Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.

`static final class `

  [MapPolyline.DashRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-dashrepresentation)

Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.

`static class `

  [MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation)

Base class to represent the visual appearance of a [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview").

`static final class `

  [MapPolyline.SolidRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-solidrepresentation)

Representation for a solid line without outline.

## Constructor Summary

Constructors

Constructor

  Description

  [MapPolyline](#%3Cinit%3E(com.here.sdk.core.GeoPolyline,com.here.sdk.mapview.MapPolyline.Representation))`(`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")` geometry, `[`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")` representation)`

Creates a new `MapPolyline` instance with a specified visual representation.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [cancelAnimation](#cancelAnimation(com.here.sdk.animation.MapPolylineAnimation))`(`[`MapPolylineAnimation`](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation")` animation)`

Cancels single ongoing animation of this map polyline.

`int`

  [getDrawOrder](#getDrawOrder())`()`

Gets the draw order of the polyline.

[`DrawOrderType`](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")

  [getDrawOrderType](#getDrawOrderType())`()`

Gets the draw order type of the polyline.

[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")

  [getGeometry](#getGeometry())`()`

Gets the geometry of the polyline.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapContentCategory`](sdk-for-android-explore-api-reference-latestmapcontentcategory "enum class in com.here.sdk.mapview")`>`

  [getMapContentCategoriesToBlock](#getMapContentCategoriesToBlock())`()`

Gets list of map content categories this polyline should block.

[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")

  [getMetadata](#getMetadata())`()`

Gets the `Metadata` instance attached to this polyline.

`double`

  [getProgress](#getProgress())`()`

Gets the progress of the polyline, 0 by default.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getProgressColor](#getProgressColor())`()`

Gets the progress color of the polyline, opaque white by default.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getProgressGradientLength](#getProgressGradientLength())`()`

Gets the maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getProgressOutlineColor](#getProgressOutlineColor())`()`

Gets the progress outline color of the polyline, opaque white by default.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`>`

  [getVisibilityRanges](#getVisibilityRanges())`()`

Gets the list of visibility ranges.

`void`

  [setDrawOrder](#setDrawOrder(int))`(int value)`

Sets the draw order of the polyline.

`void`

  [setDrawOrderType](#setDrawOrderType(com.here.sdk.mapview.DrawOrderType))`(`[`DrawOrderType`](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")` value)`

Sets the draw order type of the polyline.

`void`

  [setGeometry](#setGeometry(com.here.sdk.core.GeoPolyline))`(`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")` value)`

Sets the geometry of the polyline.

`void`

  [setMapContentCategoriesToBlock](#setMapContentCategoriesToBlock(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapContentCategory`](sdk-for-android-explore-api-reference-latestmapcontentcategory "enum class in com.here.sdk.mapview")`> value)`

Sets list of map content categories this polyline should block.

`void`

  [setMetadata](#setMetadata(com.here.sdk.core.Metadata))`(`[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")` value)`

Sets the `Metadata` instance attached to this polyline.

`void`

  [setProgress](#setProgress(double))`(double value)`

Sets the progress of the polyline from its starting point as a ratio of its total length clamped to the range \[0; 1\].

`void`

  [setProgressColor](#setProgressColor(com.here.sdk.core.Color))`(`[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` value)`

Sets the progress color of the polyline.

`void`

  [setProgressGradientLength](#setProgressGradientLength(com.here.sdk.mapview.MapMeasureDependentRenderSize))`(`[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` value)`

Sets the maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels.

`void`

  [setProgressOutlineColor](#setProgressOutlineColor(com.here.sdk.core.Color))`(`[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` value)`

Sets the progress outline color of the polyline.

`void`

  [setRepresentation](#setRepresentation(com.here.sdk.mapview.MapPolyline.Representation))`(`[`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")` representation)`

Changes the appearance of the `MapPolyline` instance.

`void`

  [setVisibilityRanges](#setVisibilityRanges(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`> value)`

Sets visibility ranges for this map polyline.

`void`

  [startAnimation](#startAnimation(com.here.sdk.animation.MapPolylineAnimation,com.here.sdk.animation.AnimationListener))`(`[`MapPolylineAnimation`](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation")` animation, `[`AnimationListener`](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation")` listener)`

Starts an animation of this map polyline.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.core.GeoPolyline,com.here.sdk.mapview.MapPolyline.Representation)" class="section detail">

### MapPolyline

public MapPolyline(@NonNull [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") geometry, @NonNull [MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview") representation)

    Creates a new `MapPolyline` instance with a specified visual representation.

    Altitude component of `GeoPolyline`'s vertices is ignored.

    After creating a `MapPolyline` with this representation, the deprecated `MapPolyline` properties do not work and any change to them will be ignored. Any modifications to polyline's appearance must be done with [`setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)`](#setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)).
Parameters:
    `geometry` -

    The list of vertices representing the polyline.

    `representation` -

    The styling properties of the polyline.

## Method Details

### setRepresentation

public void setRepresentation(@NonNull [MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview") representation)

    Changes the appearance of the `MapPolyline` instance.
Parameters:
    `representation` -

    The representation describing a new appearance of the `MapPolyline`.

### startAnimation

public void startAnimation(@NonNull [MapPolylineAnimation](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation") animation, @NonNull [AnimationListener](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation") listener)

    Starts an animation of this map polyline.

    The `MapPolylineAnimation` may be shared between multiple instances of `MapPolyline`.

    Starting animation on one polyline does not influence any ongoing animations on other polylines. Any ongoing animation of this map polyline will get cancelled.
Parameters:
    `animation` -

    The animation to start.

    `listener` -

    The listener to receive notifications about animation start, completion or cancellation.

### cancelAnimation

public void cancelAnimation(@NonNull [MapPolylineAnimation](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation") animation)

    Cancels single ongoing animation of this map polyline.

    Does nothing if the specified animation is not currently in progress for this polyline. Does not affect other polylines that might be running this animation.
Parameters:
    `animation` -

    The animation to cancel

### getGeometry

@NonNull public [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") getGeometry()

    Gets the geometry of the polyline.
Returns:
    The list of vertices that represent the geometry of the polyline.

### setGeometry

public void setGeometry(@NonNull [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") value)

    Sets the geometry of the polyline. Altitude component of `GeoPolyline`'s vertices is ignored.
Parameters:
    `value` -

    The list of vertices that represent the geometry of the polyline.

### getMetadata

@Nullable public [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") getMetadata()

    Gets the `Metadata` instance attached to this polyline. This will be `null` if nothing has been attached before.
Returns:
    The `Metadata` instance attached to this polyline.

### setMetadata

public void setMetadata(@Nullable [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") value)

    Sets the `Metadata` instance attached to this polyline.
Parameters:
    `value` -

    The `Metadata` instance attached to this polyline.

### getDrawOrder

public int getDrawOrder()

    Gets the draw order of the polyline.

    The default draw order is 0.
Returns:
    The draw order of the polyline.

### setDrawOrder

public void setDrawOrder(int value)

    Sets the draw order of the polyline.

    Polylines with a higher draw order are drawn on top of polylines with a lower draw order.

    In case multiple polylines have the same draw order, they can be rendered in different ways depending on the [`getDrawOrderType()`](#getDrawOrderType()) set.

    Supplied value is clamped to the range \[0; 1023\].
Parameters:
    `value` -

    The draw order of the polyline.

### getDrawOrderType

@NonNull public [DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview") getDrawOrderType()

    Gets the draw order type of the polyline.

    The default value is [`DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT`](sdk-for-android-explore-api-reference-latestdrawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT).
Returns:
    The draw order type of the polyline.

### setDrawOrderType

public void setDrawOrderType(@NonNull [DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview") value)

    Sets the draw order type of the polyline.

    For [`DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT`](sdk-for-android-explore-api-reference-latestdrawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT), map polylines with outlines having the same draw order are drawn as a whole in the order of addition to a map scene. There is no possibility that parts of another polyline, regardless of its draw order value, are drawn between outline and mainline of another polyline.

    With [`DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT`](sdk-for-android-explore-api-reference-latestdrawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT), polylines are rendered one by one.

    For [`DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT`](sdk-for-android-explore-api-reference-latestdrawordertype#MAP_SCENE_ADDITION_ORDER_INDEPENDENT), for multiple polylines with outlines having the same draw order, all outlines are rendered first in an arbitrary order and then all mainlines are drawn on top of those polylines in an arbitrary order.

    [`DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT`](sdk-for-android-explore-api-reference-latestdrawordertype#MAP_SCENE_ADDITION_ORDER_INDEPENDENT) allows speeding up the rendering process and keeping high frame rates when many similar polylines (with same styling attributes and [`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")) are present in a map scene.
Parameters:
    `value` -

    The draw order type of the polyline.

### getVisibilityRanges

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> getVisibilityRanges()

    Gets the list of visibility ranges. The map polyline is visible only inside these map measure ranges. When empty (the default), the map polyline is visible without map measure restrictions.
Returns:
    The list of visibility ranges. The map polyline is visible only inside these map measure ranges.

### setVisibilityRanges

public void setVisibilityRanges(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> value)

    Sets visibility ranges for this map polyline. A range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range. The map polyline is visible only inside these map measure ranges.

    When empty (the default), the map polyline is visible without map measure restrictions. Only `MapMeasureRange`(s) of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type are supported. `MapMeasureRange`(s) of other unsupported types will be ignored.
Parameters:
    `value` -

    The list of visibility ranges. The map polyline is visible only inside these map measure ranges.

### getProgress

public double getProgress()

    Gets the progress of the polyline, 0 by default.
Returns:
    The progress from the polyline's starting point, as a ratio of its total length clamped to the range \[0, 1\].

### setProgress

public void setProgress(double value)

    Sets the progress of the polyline from its starting point as a ratio of its total length clamped to the range \[0; 1\].

    As the progress varies, the equivalent part of the polyline gets covered by the progress color and progress outline color. The rest of the polyline until its end point retains the line color and outline color along with an optional dash pattern.
Parameters:
    `value` -

    The progress from the polyline's starting point, as a ratio of its total length clamped to the range \[0, 1\].

### getProgressColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getProgressColor()

    Gets the progress color of the polyline, opaque white by default.
Returns:
    The color used for the progress part of the polyline.

### setProgressColor

public void setProgressColor(@NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") value)

    Sets the progress color of the polyline.
Parameters:
    `value` -

    The color used for the progress part of the polyline.

### getProgressOutlineColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getProgressOutlineColor()

    Gets the progress outline color of the polyline, opaque white by default.
Returns:
    The color used for outline of the progress part of the polyline.

### setProgressOutlineColor

public void setProgressOutlineColor(@NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") value)

    Sets the progress outline color of the polyline.
Parameters:
    `value` -

    The color used for outline of the progress part of the polyline.

### getProgressGradientLength

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getProgressGradientLength()

    Gets the maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels.
Returns:
    The maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels.

### setProgressGradientLength

public void setProgressGradientLength(@NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") value)

    Sets the maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels. To achieve a constant gradient length, use [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") with a single value. To achieve a gradient length dependent on map zoom, use [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") with multiple values. The default value is a constant gradient length of zero pixels. The gradient is guaranteed to fit into polyline, i.e. the actual gradient can be shorter then `progressGradientLength`.

    For [`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported. For [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") only [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) is supported. A parameter with unsupported values is ignored.
Parameters:
    `value` -

    The maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels.

### getMapContentCategoriesToBlock

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapContentCategory](sdk-for-android-explore-api-reference-latestmapcontentcategory "enum class in com.here.sdk.mapview")\> getMapContentCategoriesToBlock()

    Gets list of map content categories this polyline should block.

    Default value is an empty list meaning none of the map categories will be blocked.
Returns:
    List of map content categories this polyline should block.

### setMapContentCategoriesToBlock

public void setMapContentCategoriesToBlock(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapContentCategory](sdk-for-android-explore-api-reference-latestmapcontentcategory "enum class in com.here.sdk.mapview")\> value)

    Sets list of map content categories this polyline should block.

    Map content categories overlapping the polyline geometry (progress and non-progress) will be discarded from being rendered.

    Duplicate entries will be ignored and will have no additional effect.
Parameters:
    `value` -

    List of map content categories this polyline should block.
