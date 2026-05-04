---
title: "MapViewBase (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapviewbase"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapViewBase

All Known Implementing Classes:
[`MapSurface`](sdk-for-android-explore-api-reference-latestmapsurface "class in com.here.sdk.mapview"), [`MapView`](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public interface MapViewBase
Represents the available public API from `MapView`.

## Nested Class Summary

Nested Classes

Modifier and Type

  Interface

  Description

  `static interface `

  [MapViewBase.MapPickCallback](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback)

Callback for a pick request.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [addLifecycleListener](#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener))`(`[`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")` lifecycleListener)`

Adds a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to this map view.

[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")

  [geoToViewCoordinates](#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` geoCoordinates)`

Converts geographical coordinates to view coordinates (in pixels).

[`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")

  [getCamera](#getCamera())`()`

Gets the camera to control the view for the map.

`int`

  [getFrameRate](#getFrameRate())`()`

Gets maximum render frame rate in frames per second.

[`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures")

  [getGestures](#getGestures())`()`

Gets the gestures control object.

[`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")

  [getHereMap](#getHereMap())`()`

Gets the [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") associated with this map view.

[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

  [getMapContext](#getMapContext())`()`

Gets the map context associated with this map view.

[`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview")

  [getMapScene](#getMapScene())`()`

Gets the map scene associated with this map view.

`double`

  [getPixelScale](#getPixelScale())`()`

Gets the pixel scale factor used by this `MapView`.

[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

  [getViewportSize](#getViewportSize())`()`

Gets the size of this map view in physical pixels.

[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

  [getWatermarkSize](#getWatermarkSize())`()`

Returns the watermark size in physical pixels.

`boolean`

  [isValid](#isValid())`()`

Returns `true` if this instance is valid, `false` otherwise.

`void`

  [pick](#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback))`(`[`MapScene.MapPickFilter`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview")` filter, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewArea, `[`MapViewBase.MapPickCallback`](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview")` callback)`

Returns all map content located inside the specified pick area.

`void`

  [removeLifecycleListener](#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener))`(`[`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")` lifecycleListener)`

Removes a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from this map view.

`void`

  [setFrameRate](#setFrameRate(int))`(int value)`

Sets maximum render frame rate in frames per second.

`void`

  [setWatermarkLocation](#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` anchor, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` offset)`

Sets the position of the HERE logo watermark within the map view.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [viewToGeoCoordinates](#viewToGeoCoordinates(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` viewCoordinates)`

Converts view coordinates (in pixels) to geographical coordinates.

## Method Details

### viewToGeoCoordinates

@Nullable [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") viewToGeoCoordinates(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") viewCoordinates)

    Converts view coordinates (in pixels) to geographical coordinates.

    An optional altitude component of the resulting geographical coordinate is not set.

    If the view coordinates specify a point above a horizon, then the result is geographical coordinates of the point on a horizon below the specified view coordinates.

    The fog effect is ignored for the calculation, meaning that for the view point within the area covered by the fog, the result is geographical coordinates that would be displayed at the specified point if the fog effect was not applied.

    If the render surface is not attached, it will return `null`.
Parameters:
    `viewCoordinates` -

    Point inside the view to convert.

    Returns:
    The geographical coordinates under specified view point or `null` if there is no render surface attached.

### geoToViewCoordinates

@Nullable [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") geoToViewCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") geoCoordinates)

    Converts geographical coordinates to view coordinates (in pixels).

    If specified, altitude of the input coordinates is interpreted as altitude above sea level. If not specified, the input coordinates are interpreted as being on ground elevation. The above distinction is only relevant when 3D terrain feature is enabled.

    The resulting view coordinates might be outside of current viewport, i.e. result might contain values less than zero or greater than view's dimensions.

    If the render surface is not attached, it will return `null`.
Parameters:
    `geoCoordinates` -

    Geographical coordinates to convert.

    Returns:
    The view coordinates of the specified geographical point or `null` if there is no render surface attached.

### setWatermarkLocation

void setWatermarkLocation(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchor, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") offset)

    Sets the position of the HERE logo watermark within the map view.

    By default, the watermark is aligned to the bottom-right corner of the view: Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2). It is recommended to change the default position only if necessary to avoid overlapping UI elements. The watermark should always be fully visible within the view. The anchor point on the watermark is its center (width/2, height/2), around which it will be placed in the map view. For map views smaller than 250 dip in both width and height, the watermark will not be shown.
Parameters:
    `anchor` -

    Anchor point in normalized view coordinates \[0, 1\]. Map view's origin at (0, 0) indicates a top-left corner of the map view. Out of boundary anchor point values will be clamped to the \[0, 1\] range.

    `offset` -

    A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that allows shifting the watermark from the anchor point position in one or the other direction. For the quadrant of values expressing visible part of the map view negative offset shifts the watermark to the direction of the origin, positive - away from it. For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to the bottom. If specified offset will result in watermark being completely or partially out-of-view the offset will be adjusted internally so that watermark is fully visible. Offset is not being scaled when the map view size changes.

### addLifecycleListener

void addLifecycleListener(@NonNull [MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)

    Adds a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to this map view. Adding the same object multiple times has no effect.
Parameters:
    `lifecycleListener` -

    An object to be notified of lifecycle events.

### removeLifecycleListener

void removeLifecycleListener(@NonNull [MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)

    Removes a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from this map view. Trying to remove an object that was not added or was removed before has no effect.
Parameters:
    `lifecycleListener` -

    An object to stop being notified of lifecycle events.

### pick

void pick(@Nullable [MapScene.MapPickFilter](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview") filter, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewArea, @NonNull [MapViewBase.MapPickCallback](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview") callback)

    Returns all map content located inside the specified pick area. Content to be picked is specified by a pick content filter. The pick area is defined by a rectangle in map view coordinates in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner of the map view.
Parameters:
    `filter` -

    Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.

    `viewArea` -

    The rectangular pixel area of the view inside which map content will be picked. View area is relative to the map view's origin at (0, 0) at the top-left corner of the map view.

    `callback` -

    Callback to call with the result. This will be called on a main thread when pick operation completes.

### isValid

boolean isValid()

    Returns `true` if this instance is valid, `false` otherwise. It will be made

    It will be made invalid when the corresponding `SDKNativeEngine` is destroyed.
Returns:
    Indicates whether this instance is valid.

### getCamera

@NonNull [MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview") getCamera()

    Gets the camera to control the view for the map.
Returns:
    The camera to control the view for the map.

### getGestures

@NonNull [Gestures](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") getGestures()

    Gets the gestures control object.
Returns:
    The gestures control object for setting up the capture of gestures.

### getMapScene

@NonNull [MapScene](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") getMapScene()

    Gets the map scene associated with this map view.
Returns:
    Map scene associated with this map view.

### getMapContext

@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") getMapContext()

    Gets the map context associated with this map view.
Returns:
    Map context associated with this map view.

### getHereMap

@NonNull [HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") getHereMap()

    Gets the [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") associated with this map view.
Returns:
    Here Map associated with this map view.

### getViewportSize

@NonNull [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") getViewportSize()

    Gets the size of this map view in physical pixels.

    If internally the map view's render surface is not attached yet (see: [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")), or after the map view has been destroyed then a `Size2D` with zero width and height is returned.
Returns:
    The size of this map view in physical pixels.

### getFrameRate

int getFrameRate()

    Gets maximum render frame rate in frames per second.
Returns:
    Maximum render frame rate in frames per second.

### setFrameRate

void setFrameRate(int value)

    Sets maximum render frame rate in frames per second. Setting to 0 disables automatic rendering for this view. Setting negative values has no effect. The default value is 60 frames per second.
Parameters:
    `value` -

    Maximum render frame rate in frames per second.

### getPixelScale

double getPixelScale()

    Gets the pixel scale factor used by this `MapView`.

    It is used to support screen resolution and size independence. This value is a derivative of the device's screen pixel density and is a direct analog of

    pixel density from DisplayMetrics.

    It can be used to translate between physical pixels and

    density-independent pixels

    according to the formula:

    dp = px / pixelScale.
Returns:
    The pixel scale factor used by this `MapView`.

    Pixel scale is 0.0 if the map view is not initialized.

### getWatermarkSize

@NonNull [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") getWatermarkSize()

    Returns the watermark size in physical pixels.
Returns:
    Provides the size of the watermark in physical pixels.
