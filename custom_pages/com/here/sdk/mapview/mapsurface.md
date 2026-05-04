---
title: "MapSurface (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapsurface"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapSurface

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapSurface
All Implemented Interfaces:
[`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

------------------------------------------------------------------------
public class MapSurface extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) implements [MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")
Provides the ability to render a map into a provided rendering surface. This enables the possibility to render a map into external displays like Android Auto. If you want to use the map for a regular use case please use the [`MapView`](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview") instead.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [MapSurface.RenderListener](sdk-for-android-explore-api-reference-latestmapsurface-renderlistener)

Listener of MapSurface render events.

## Nested classes/interfaces inherited from interface com.here.sdk.mapview.[MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

  [`MapViewBase.MapPickCallback`](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview")

## Constructor Summary

Constructors

Constructor

  Description

  [MapSurface](#%3Cinit%3E())`()`

Creates a new instance.

[MapSurface](#%3Cinit%3E(android.content.Context))`(android.content.Context context)`

Creates a new instance.

[MapSurface](#%3Cinit%3E(android.content.Context,com.here.sdk.mapview.MapViewOptions))`(android.content.Context context, `[`MapViewOptions`](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview")` options)`

Creates a new instance.

[MapSurface](#%3Cinit%3E(com.here.sdk.mapview.MapViewOptions))`(`[`MapViewOptions`](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview")` options)`

Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods
  Deprecated Methods

  Modifier and Type

  Method

  Description

  `void`

  [addLifecycleListener](#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener))`(`[`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")` lifecycleListener)`

Adds a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to this map view.

`void`

  [attachSurface](#attachSurface(android.content.Context,android.view.Surface,int,int))`(android.content.Context context, android.view.Surface surface, int width, int height)`

Sets the surface on which the map will be rendered.

`void`

  [attachSurface](#attachSurface(android.content.Context,android.view.Surface,int,int,com.here.sdk.mapview.MapSurface.RenderListener))`(android.content.Context context, android.view.Surface surface, int width, int height, `[`MapSurface.RenderListener`](sdk-for-android-explore-api-reference-latestmapsurface-renderlistener "interface in com.here.sdk.mapview")` renderListener)`

Sets the surface on which the map will be rendered.

`void`

  [destroy](#destroy())`()`

Destroys the map renderer and render surface, making this `MapSurface` invalid.

`void`

  [destroySurface](#destroySurface())`()`

Destroys the rendering surface.

[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")

  [geoToViewCoordinates](#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` geoCoordinates)`

Converts geographical coordinates to view coordinates (in pixels).

[`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")

  [getCamera](#getCamera())`()`

Returns the camera control object for the map

`int`

  [getFrameRate](#getFrameRate())`()`

Gets maximum render frame rate in frames per second.

[`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures")

  [getGestures](#getGestures())`()`

Returns the gestures control object.

[`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")

  [getHereMap](#getHereMap())`()`

Gets the HereMap associated with this map view.

[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

  [getMapContext](#getMapContext())`()`

Gets the map context associated with this map view.

[`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview")

  [getMapScene](#getMapScene())`()`

Gets the map scene associated with this map view.

`double`

  [getPixelScale](#getPixelScale())`()`

Gets the pixel scale factor used by this MapView.

`static `[`ShadowQuality`](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview")

  [getShadowQuality](#getShadowQuality())`()`

Gets the currently set shadow quality.

[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

  [getViewportSize](#getViewportSize())`()`

Returns the viewport size of this MapView in physical pixels.

[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

  [getWatermarkSize](#getWatermarkSize())`()`

Returns the watermark size in physical pixels.

`boolean`

  [isValid](#isValid())`()`

Returns whether this `MapSurface` is valid.

`void`

  [onPause](#onPause())`()`

Call this method in the onPause() method of the lifecycle owner.

`void`

  [onResume](#onResume())`()`

Call this method in the onResume() method of the lifecycle owner.

`void`

  [pick](#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback))`(`[`MapScene.MapPickFilter`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview")` filter, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewArea, `[`MapViewBase.MapPickCallback`](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview")` callback)`

Returns all map content located inside the specified pick area.

`void`

  [redraw](#redraw(java.lang.Runnable))`(`[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)` redrawFinished)`

Redraws the map and reports back on completion.

`void`

  [removeLifecycleListener](#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener))`(`[`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")` lifecycleListener)`

Removes a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from this map view.

`void`

  [setFrameRate](#setFrameRate(int))`(int value)`

Sets maximum render frame rate in frames per second.

`void`

  [setOnReadyListener](#setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener))`(`[`MapView.OnReadyListener`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")` readyListener)`

Sets the OnReadyListener, which will be notified once MapView initialization has been finished.

`static void`

  [setShadowQuality](#setShadowQuality(com.here.sdk.mapview.ShadowQuality))`(`[`ShadowQuality`](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview")` shadowQuality)`

Set desired shadow quality for all instances of MapSurface/MapView.

`void`

  [setSurface](#setSurface(android.content.Context,android.view.Surface,int,int))`(android.content.Context context, android.view.Surface surface, int width, int height)`

Deprecated.
Will be removed in v4.26.0.

  `void`

  [setSurface](#setSurface(android.content.Context,android.view.Surface,int,int,com.here.sdk.mapview.MapSurface.RenderListener))`(android.content.Context context, android.view.Surface surface, int width, int height, `[`MapSurface.RenderListener`](sdk-for-android-explore-api-reference-latestmapsurface-renderlistener "interface in com.here.sdk.mapview")` renderListener)`

Deprecated.
Will be removed in v4.26.0.

  `void`

  [setWatermarkLocation](#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` anchor, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` offset)`

Sets the position of the HERE logo watermark within the map view.

`void`

  [takeScreenshot](#takeScreenshot(com.here.sdk.mapview.MapView.TakeScreenshotCallback))`(`[`MapView.TakeScreenshotCallback`](sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback "interface in com.here.sdk.mapview")` callback)`

Asynchronously retrieves screenshot of current map view

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [viewToGeoCoordinates](#viewToGeoCoordinates(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` viewCoordinates)`

Converts view coordinates to geographical coordinates.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### MapSurface

public MapSurface()

    Creates a new instance.

  - (com.here.sdk.mapview.MapViewOptions)" class="section detail">

### MapSurface

public MapSurface([MapViewOptions](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview") options)

    Creates a new instance.
Parameters:
    `options` - The options
- (android.content.Context)" class="section detail">

### MapSurface

public MapSurface(android.content.Context context)

    Creates a new instance.
Parameters:
    `context` - The Application context
- (android.content.Context,com.here.sdk.mapview.MapViewOptions)" class="section detail">

### MapSurface

public MapSurface(android.content.Context context, [MapViewOptions](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview") options)

    Creates a new instance.
Parameters:
    `options` - The options

    `context` - The Application context

## Method Details

### isValid

public boolean isValid()

    Returns whether this `MapSurface` is valid. An invalid `MapSurface` is non-functional. A `MapSurface` is considered valid only after [`setSurface(Context, Surface, int, int)`](#setSurface(android.content.Context,android.view.Surface,int,int)) and before [`destroy()`](#destroy()) is called. ` MapSurface` is also invalidated when the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") it is using is destroyed.
Specified by:
    [`isValid`](sdk-for-android-explore-api-reference-latestmapviewbase#isValid()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    `true` if this `MapSurface` is valid, `false` otherwise.

### destroy

public void destroy()

    Destroys the map renderer and render surface, making this `MapSurface` invalid. Call this method only when the render surface will no longer be used. [`isValid()`](#isValid()) will return @{code false} after this is called. It can be made valid again by setting render surface using [`setSurface(Context, Surface, int, int)`](#setSurface(android.content.Context,android.view.Surface,int,int)).

### setOnReadyListener

public void setOnReadyListener([MapView.OnReadyListener](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview") readyListener)

    Sets the OnReadyListener, which will be notified once MapView initialization has been finished. It is highly recommended to put code that accesses map view related functionality inside [`MapView.OnReadyListener.onMapViewReady()`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener#onMapViewReady()) instead of directly in `Activity`'s `onResume()`.
Parameters:
    `readyListener` - The listener to be registered, or `null` to unregister any previously register listener.

### setSurface

public void setSurface(android.content.Context context, android.view.Surface surface, int width, int height)

    Deprecated.
Will be removed in v4.26.0. Please use attachSurface.

Sets the surface on which the map will be rendered. This method needs to be called before any other methods in this class.
Parameters:
    `context` - The Application context

    `surface` - The surface to render to.

    `width` - The width of the render surface in pixels.

    `height` - The height of the render surface in pixels.

### attachSurface

public void attachSurface(android.content.Context context, android.view.Surface surface, int width, int height)

    Sets the surface on which the map will be rendered. Throws exception if the surface cannot be used by HERESDK.
Parameters:
    `context` - The Application context

    `surface` - The surface to render to.

    `width` - The width of the render surface in pixels.

    `height` - The height of the render surface in pixels.

    Throws:
    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if surface is invalid and cannot be used.

### setSurface

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public void setSurface(android.content.Context context, android.view.Surface surface, int width, int height, @NonNull [MapSurface.RenderListener](sdk-for-android-explore-api-reference-latestmapsurface-renderlistener "interface in com.here.sdk.mapview") renderListener)

    Deprecated.
Will be removed in v4.26.0. Please use attachSurface.

Sets the surface on which the map will be rendered. This method needs to be called before any other methods in this class. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `context` - The Application context

    `surface` - The surface to render to.

    `width` - The width of the render surface in pixels.

    `height` - The height of the render surface in pixels.

    `renderListener` - A listener for render events. The listener will be released once [`destroySurface()`](#destroySurface()) gets called.

### attachSurface

public void attachSurface(android.content.Context context, android.view.Surface surface, int width, int height, @NonNull [MapSurface.RenderListener](sdk-for-android-explore-api-reference-latestmapsurface-renderlistener "interface in com.here.sdk.mapview") renderListener)

    Sets the surface on which the map will be rendered. Throws exception if the surface cannot be used by HERESDK. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `context` - The Application context

    `surface` - The surface to render to.

    `width` - The width of the render surface in pixels.

    `height` - The height of the render surface in pixels.

    `renderListener` - A listener for render events. The listener will be released once [`destroySurface()`](#destroySurface()) gets called.

    Throws:
    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if surface is invalid and cannot be used.

### destroySurface

public void destroySurface()

    Destroys the rendering surface.

### redraw

public void redraw([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) redrawFinished)

    Redraws the map and reports back on completion.
Parameters:
    `redrawFinished` -

    The runnable to be executed after completion.

### pick

public void pick(@Nullable [MapScene.MapPickFilter](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview") filter, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewArea, @NonNull [MapViewBase.MapPickCallback](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview") callback)

    Returns all map content located inside the specified pick area. Content to be picked is specified by a pick content filter. The pick area is defined by a rectangle in map view coordinates in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner of the map view.
Specified by:
    [`pick`](sdk-for-android-explore-api-reference-latestmapviewbase#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `filter` -

    Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.

    `viewArea` -

    The rectangular pixel area of the view inside which map content will be picked. View area is relative to the map view's origin at (0, 0) at the top-left corner of the map view.

    `callback` -

    Callback to call with the result. This will be called on a main thread when pick operation completes.

### geoToViewCoordinates

@Nullable public [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") geoToViewCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") geoCoordinates)

    Converts geographical coordinates to view coordinates (in pixels).
    If specified, altitude of the input coordinates is interpreted as altitude above sea level. If not specified, the input coordinates are interpreted as being on ground elevation. The above distinction is only relevant when 3D terrain feature is enabled.

    The resulting view coordinates might be outside of current viewport, i.e. result might contain values less than zero or greater than view's dimensions.

    If the render surface is not attached, it will return `null`.
Specified by:
    [`geoToViewCoordinates`](sdk-for-android-explore-api-reference-latestmapviewbase#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `geoCoordinates` -

    Geographical coordinates to convert.

    Returns:
    The view coordinates of the specified geographical point or `null` if there is no render surface attached.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

    See Also:
    - [`MapView.OnReadyListener`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")

### addLifecycleListener

public void addLifecycleListener(@NonNull [MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)

    Adds a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to this map view. Adding the same object multiple times has no effect.
Specified by:
    [`addLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewbase#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `lifecycleListener` -

    An object to be notified of lifecycle events.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### removeLifecycleListener

public void removeLifecycleListener(@NonNull [MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)

    Removes a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from this map view. Trying to remove an object that was not added or was removed before has no effect.
Specified by:
    [`removeLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewbase#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `lifecycleListener` -

    An object to stop being notified of lifecycle events.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### onResume

public void onResume()

    Call this method in the onResume() method of the lifecycle owner.

### onPause

public void onPause()

    Call this method in the onPause() method of the lifecycle owner.

### viewToGeoCoordinates

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") viewToGeoCoordinates(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") viewCoordinates)

    Converts view coordinates to geographical coordinates.
    An optional altitude component of the resulting geographical coordinate is not set.

    If the view coordinates specify a point above a horizon, then the result is geographical coordinates of the point on a horizon below the specified view coordinates.

    The fog effect is ignored for the calculation, meaning that for the view point within the area covered by the fog, the result is geographical coordinates that would be displayed at the specified point if the fog effect was not applied.

    If the render surface is not attached, it will return `null`.
Specified by:
    [`viewToGeoCoordinates`](sdk-for-android-explore-api-reference-latestmapviewbase#viewToGeoCoordinates(com.here.sdk.core.Point2D)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `viewCoordinates` -

    Point inside the view to convert.

    Returns:
    The geographical coordinates under specified view point or `null` if there is no render surface attached.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

    See Also:
    - [`MapView.OnReadyListener`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")

### getGestures

@NonNull public [Gestures](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") getGestures()

    Returns the gestures control object. Please note that there is no gesture support for the MapSurface at this point.
Specified by:
    [`getGestures`](sdk-for-android-explore-api-reference-latestmapviewbase#getGestures()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") control object

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getPixelScale

public double getPixelScale()

    Gets the pixel scale factor used by this MapView. It is used to support screen resolution and size independence. This value is a derivative of the device's screen pixel density and is a direct analog of pixel density from DisplayMetrics. It can be used to translate between physical pixels and density independent pixels according to formula:

    dp = px / pixel_scale.
Specified by:
    [`getPixelScale`](sdk-for-android-explore-api-reference-latestmapviewbase#getPixelScale()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    current pixel scale factor, or 0.0 if MapView is not initialized

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getViewportSize

public [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") getViewportSize()

    Returns the viewport size of this MapView in physical pixels.
Specified by:
    [`getViewportSize`](sdk-for-android-explore-api-reference-latestmapviewbase#getViewportSize()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    The viewport size in physical pixels

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getFrameRate

public int getFrameRate()

    Gets maximum render frame rate in frames per second. The default value is 60 frames per second.
Specified by:
    [`getFrameRate`](sdk-for-android-explore-api-reference-latestmapviewbase#getFrameRate()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    Actual maximal render frame rate

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### setFrameRate

public void setFrameRate(int value)

    Sets maximum render frame rate in frames per second.
Specified by:
    [`setFrameRate`](sdk-for-android-explore-api-reference-latestmapviewbase#setFrameRate(int)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `value` - Maximum render frame rate in frames per second. Setting to 0 disables automatic rendering for this view. Setting negative values has no effect.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### takeScreenshot

public void takeScreenshot([MapView.TakeScreenshotCallback](sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback "interface in com.here.sdk.mapview") callback)

    Asynchronously retrieves screenshot of current map view
Parameters:
    `callback` - Completion handler called when the screenshot is completed

### setWatermarkLocation

public void setWatermarkLocation(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchor, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") offset)

    Sets the position of the HERE logo watermark within the map view. By default, the watermark is aligned to the bottom-right corner of the view: Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2). It is recommended to change the default position only if necessary to avoid overlapping UI elements. The watermark should always be fully visible within the view. The anchor point on the watermark is its center (width/2, height/2), around which it will be placed in the map view. For map views smaller than 250 dip in both width and height, the watermark will not be shown.
Specified by:
    [`setWatermarkLocation`](sdk-for-android-explore-api-reference-latestmapviewbase#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `anchor` -

    Anchor point in normalized view coordinates \[0, 1\]. Map view's origin at (0, 0) indicates a top-left corner of the map view. Out of boundary anchor point values will be clamped to the \[0, 1\] range.

    `offset` -

    A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that allows shifting the watermark from the anchor point position in one or the other direction. For the quadrant of values expressing visible part of the map view negative offset shifts the watermark to the direction of the origin, positive - away from it. For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to the bottom. If specified offset will result in watermark being completely or partially out-of-view the offset will be adjusted internally so that watermark is fully visible. Offset is not being scaled when the map view size changes.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getWatermarkSize

@NonNull public [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") getWatermarkSize()

    Returns the watermark size in physical pixels.
Specified by:
    [`getWatermarkSize`](sdk-for-android-explore-api-reference-latestmapviewbase#getWatermarkSize()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    Provides the size of the watermark in physical pixels.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### setShadowQuality

public static void setShadowQuality([ShadowQuality](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview") shadowQuality)

    Set desired shadow quality for all instances of MapSurface/MapView. The quality controls the size of the shadow maps and the cascade count. The default shadow quality is `ShadowQuality.MEDIUM`. MapSurfaces can request to render shadows by feature. Enabling shadows has a performance impact and should be considered only for devices with sufficient performance. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
Parameters:
    `shadowQuality` - The shadow quality.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getShadowQuality

public static [ShadowQuality](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview") getShadowQuality()

    Gets the currently set shadow quality. The default shadow quality is `ShadowQuality.MEDIUM`. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
Returns:
    The currently set shadow quality.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getCamera

@NonNull public [MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview") getCamera()

    Returns the camera control object for the map
Specified by:
    [`getCamera`](sdk-for-android-explore-api-reference-latestmapviewbase#getCamera()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview") object for the map

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getMapScene

@NonNull public [MapScene](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") getMapScene()

    Gets the map scene associated with this map view. This can be used to request different map schemes to be displayed in the map view, and to add and remove map items from the map.
Specified by:
    [`getMapScene`](sdk-for-android-explore-api-reference-latestmapviewbase#getMapScene()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") associated with this map view.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getMapContext

@NonNull public [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") getMapContext()

    Gets the map context associated with this map view.
Specified by:
    [`getMapContext`](sdk-for-android-explore-api-reference-latestmapviewbase#getMapContext()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") associated with this map view.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.

### getHereMap

@NonNull public [HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") getHereMap()

    Gets the HereMap associated with this map view.
Specified by:
    [`getHereMap`](sdk-for-android-explore-api-reference-latestmapviewbase#getHereMap()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") associated with this map view.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if MapSurface object is not valid.
