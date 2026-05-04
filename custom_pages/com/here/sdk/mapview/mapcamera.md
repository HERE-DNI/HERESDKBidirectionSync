---
title: "MapCamera (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcamera"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapCamera

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapCamera
------------------------------------------------------------------------
public final class MapCamera extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents the camera looking onto the map view.

Each map instance has exactly one camera that is used to manipulate the way the map is displayed.

Any updates to the state of the camera will be applied while drawing the next map view frame and the current state of the camera reflects what is currently drawn inside the map view.

Note: The camera can be configured and positioned even before a map scene is loaded for the first time. This allows for pre-setting the desired camera position, orientation, and zoom level, which will be applied once the map scene becomes available.

**Camera Model**

*Camera Concepts and Units*

By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around two axes - bearing (also known as head) and tilt (also known as pitch).

The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed so that it looks at a specific geo-coordinates (placed at the `principal point`) from a given orientation and distance.

- the look-at target in geo-coordinates (latitude, longitude) in degrees and an `altitude` in meters above MSL (mean sea level) at the `principal point`
- the `orientation` at the look-at target
- the distance of the camera from the look-at target, given as `distance` in meters or as `zoom-level`

*Getting the current camera state*

The current camera state can be obtained by the [`getState()`](#getState()) call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space. The values are returned for the current `principal point`. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point, e.g. when using [`MapCameraUpdateFactory.lookAt(GeoBox)`](sdk-for-android-explore-api-reference-latestmapcameraupdatefactory#lookAt(com.here.sdk.core.GeoBox)) with a view rectangle, whose center does not coincide with the `principal point`. In this case, the geo-coordinates of the look-at target will differ from the center of the geo-box used in the `lookAt` call.

*Geo coordinates*

Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.

*Altitude*

When `altitude` is specified, it is always in meters above mean sea level (MSL). If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map. This is especially interesting in cases where terrain elevation is used within the map display.

*Distance vs zoom-level vs scale*

Map camera `distance`, `zoom-level` and `scale` determine how much of the world is visible on the HERE map. `Distance`, `zoom-level` and `scale` are directly connected and changing one will automatically change the others as well (except for `distance`/`scale` changes that map to `zoom-level` values \< 0 or \> 23).

- `distance`: the distance from the camera to the look-at target on the surface of the Earth, in meters
- `zoom-level`: the map zoom level, in the range \[0, 3\]. The relation between the width of the equator in logical pixels `w` and the zoom level `z` is: `w = 256 * 2^(z)`
- `scale`: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.

The following mapping represents the `zoom-level` values:

| zoom-level | ~ scale on screen (130dpi) | width of the equator in logical pixels | what can be seen |
|------------|:--------------------------:|:--------------------------------------:|:----------------:|
| 0          |       1:800 million        |                  256                   |      Earth       |
| 1          |       1:400 million        |                  512                   |                  |
| 2          |       1:200 million        |                  1024                  |                  |
| 3          |       1:100 million        |                  2048                  |                  |
| 4          |        1:50 million        |                  4096                  |   A continent    |
| 5          |        1:25 million        |                  8192                  |   Large roads    |
| 6          |        1:12 million        |                 16384                  |   Large rivers   |
| 7          |        1:6 million         |                 32768                  |    A country     |
| 8          |        1:3 million         |                 65536                  |                  |
| 9          |        1:1 million         |                 131072                 |                  |
| 10         |       1:780 thousand       |                 262144                 |                  |
| 11         |       1:390 thousand       |                 524288                 |                  |
| 12         |       1:195 thousand       |                1048576                 |                  |
| 13         |       1:100 thousand       |                2097152                 |                  |
| 14         |       1:50 thousand        |                4194304                 |      A city      |
| 15         |       1:25 thousand        |                8388608                 |                  |
| 16         |       1:12 thousand        |                16777216                |    Buildings     |
| 17         |        1:6 thousand        |                33554432                |    Landmarks     |
| 18         |        1:3 thousand        |                67108864                |                  |
| 19         |        1:1 thousand        |               134217728                |                  |
| 20         |        1:7 hundred         |               268435456                |     Streets      |
| 21         |        1:3 hundred         |               536870912                |                  |
| 22         |        1:1 hundred         |               1073741824               |                  |
| 23         |            1:95            |               2147483648               |                  |

*Orientation*

The camera `orientation` is composed of two parts:

- `bearing`: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west
- `tilt`: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.

*Changing the Camera*

All changes to the camera are encapsulated in camera updates that are created using the methods in the [`MapCameraUpdateFactory`](sdk-for-android-explore-api-reference-latestmapcameraupdatefactory "class in com.here.sdk.mapview") class.

These updates can then be applied to the [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") using [`applyUpdate(com.here.sdk.mapview.MapCameraUpdate)`](#applyUpdate(com.here.sdk.mapview.MapCameraUpdate)).

Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.

*Animating the Camera*

Camera updates can be animated by first creating a camera animation using the methods in the [`MapCameraAnimationFactory`](sdk-for-android-explore-api-reference-latestmapcameraanimationfactory "class in com.here.sdk.mapview") class and then applying this animation to the [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") using [`startAnimation(MapCameraAnimation, AnimationListener)`](#startAnimation(com.here.sdk.mapview.MapCameraAnimation,com.here.sdk.animation.AnimationListener)).

Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started. The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (`target pose` and `distance/zoom level/scale`) and camera projection (`field of view`, `focal length` and `principal point`).

The running animations can also be canceled using [`cancelAnimations()`](#cancelAnimations()) or individual ones using [`cancelAnimation(com.here.sdk.mapview.MapCameraAnimation)`](#cancelAnimation(com.here.sdk.mapview.MapCameraAnimation)).

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [MapCamera.DryCameraUpdateCallback](sdk-for-android-explore-api-reference-latestmapcamera-drycameraupdatecallback)

Used to report back results of dry update application to camera.

`static final class `

  [MapCamera.FarPlaneConfiguration](sdk-for-android-explore-api-reference-latestmapcamera-farplaneconfiguration)

Far plane distance configuration for a zoom level.

`static final class `

  [MapCamera.State](sdk-for-android-explore-api-reference-latestmapcamera-state)

Encapsulates state of the camera.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [addListener](#addListener(com.here.sdk.mapview.MapCameraListener))`(`[`MapCameraListener`](sdk-for-android-explore-api-reference-latestmapcameralistener "interface in com.here.sdk.mapview")` listener)`

Adds a listener to this camera that will be notified on the main thread every time the map is redrawn with new camera parameters.

`void`

  [applyUpdate](#applyUpdate(com.here.sdk.mapview.MapCameraUpdate))`(`[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")` cameraUpdate)`

Applies camera update to the map camera.

`void`

  [cancelAnimation](#cancelAnimation(com.here.sdk.mapview.MapCameraAnimation))`(`[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")` cameraAnimation)`

Cancels an ongoing camera animation.

`void`

  [cancelAnimations](#cancelAnimations())`()`

Cancels any ongoing camera animation.

`void`

  [dryApplyUpdate](#dryApplyUpdate(com.here.sdk.mapview.MapCameraUpdate,com.here.sdk.mapview.MapCamera.DryCameraUpdateCallback))`(`[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")` cameraUpdate, `[`MapCamera.DryCameraUpdateCallback`](sdk-for-android-explore-api-reference-latestmapcamera-drycameraupdatecallback "interface in com.here.sdk.mapview")` callback)`

Computes result of applying camera update without changing state of the map camera.

[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [getBoundingBox](#getBoundingBox())`()`

Gets the current visible map area encompassed in a GeoBox.

[`MapCameraLimits`](sdk-for-android-explore-api-reference-latestmapcameralimits "class in com.here.sdk.mapview")

  [getLimits](#getLimits())`()`

Gets a MapCameraLimits instance that controls limits for the camera settings.

[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")

  [getPrincipalPoint](#getPrincipalPoint())`()`

Gets the pixel point that determines where the target is placed within the map view.

[`MapCamera.State`](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview")

  [getState](#getState())`()`

Gets state of the camera that reflects what is currently drawn inside the map view.

`void`

  [lookAt](#lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation)`

Makes the camera look at the specified geodetic area.

`void`

  [lookAt](#lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Rectangle2D))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewRectangle)`

Makes the camera look at the specified geodetic area and pass a rectangle which specifies where the area should appear inside of the map view.

`void`

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` target)`

Makes the camera look at a new geodetic target, while preserving the current orientation and distance to the target.

`void`

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` zoom)`

Makes the camera look at the geodetic target with the given zoom and orientation.

`void`

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMeasure))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` target, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` zoom)`

Makes the camera look at the geodetic target with the given zoom.

`void`

  [orbitBy](#orbitBy(com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Point2D))`(`[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` delta, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Orbits the camera around a specified view point by increasing tilt and bearing by specified delta values.

`void`

  [removeListener](#removeListener(com.here.sdk.mapview.MapCameraListener))`(`[`MapCameraListener`](sdk-for-android-explore-api-reference-latestmapcameralistener "interface in com.here.sdk.mapview")` observer)`

Removes the listener from the camera.

`void`

  [removeListeners](#removeListeners())`()`

Removes all registered listeners.

`void`

  [setDistanceToTarget](#setDistanceToTarget(double))`(double distanceInMeters)`

Makes the camera look at current target from certain distance

`void`

  [setFarPlaneConfiguration](#setFarPlaneConfiguration(java.util.Map))`(`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html), [`MapCamera.FarPlaneConfiguration`](sdk-for-android-explore-api-reference-latestmapcamera-farplaneconfiguration "class in com.here.sdk.mapview")`> configs)`

Sets far plane distance configs per zoom level.

`void`

  [setOrientationAtTarget](#setOrientationAtTarget(com.here.sdk.core.GeoOrientationUpdate))`(`[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation)`

Changes camera orientation in relation to target location.

`void`

  [setPrincipalPoint](#setPrincipalPoint(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` value)`

Sets the pixel point that determines where the target appears within the map view.

`void`

  [startAnimation](#startAnimation(com.here.sdk.mapview.MapCameraAnimation))`(`[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")` cameraAnimation)`

Starts a given camera animation.

`void`

  [startAnimation](#startAnimation(com.here.sdk.mapview.MapCameraAnimation,com.here.sdk.animation.AnimationListener))`(`[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")` cameraAnimation, `[`AnimationListener`](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation")` animationListener)`

Starts a given camera animation.

`void`

  [zoomBy](#zoomBy(double,com.here.sdk.core.Point2D))`(double factor, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Zooms in or out by a specified factor.

`void`

  [zoomTo](#zoomTo(double))`(double zoomLevel)`

Zooms to the specified zoom level.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### setFarPlaneConfiguration

public void setFarPlaneConfiguration(@NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html),[MapCamera.FarPlaneConfiguration](sdk-for-android-explore-api-reference-latestmapcamera-farplaneconfiguration "class in com.here.sdk.mapview")\> configs)

    Sets far plane distance configs per zoom level.

    Values are linearly interpolated between provided zoom levels. For z between z0 and z1: t = (z - z0) / (z1 - z0) distanceFactor(z) = lerp(distanceFactor0, distanceFactor1, t) minDistance(z) = lerp(minDistance0, minDistance1, t)

    Effective far plane for the current frame is: farPlaneInMeters = max( minDistance(z), distanceToTargetInMeters \* distanceFactor(z) )

    Sample Configuration (balanced quality/performance, tune per zoom level): 14.4 -\> FarPlaneConfiguration(1.3) 18.34 -\> FarPlaneConfiguration(2.0) 19.60 -\> FarPlaneConfiguration(1.3) minDistanceInMeters remains default in this case. Passing an empty map clears the per-zoom override and restores the default behavior. Non-finite zoom levels or values are ignored. Distance factors are clamped to 0.1 to 10.0. The minimum distance is clamped to a range of \[100, 3000\] meters.
Parameters:
    `configs` -

    Per-zoom override mapping from zoom level to distance configuration.

### addListener

public void addListener(@NonNull [MapCameraListener](sdk-for-android-explore-api-reference-latestmapcameralistener "interface in com.here.sdk.mapview") listener)

    Adds a listener to this camera that will be notified on the main thread every time the map is redrawn with new camera parameters.

    Adding the same listener multiple times has no effect.
Parameters:
    `listener` -

    The listener to add.

### removeListener

public void removeListener(@NonNull [MapCameraListener](sdk-for-android-explore-api-reference-latestmapcameralistener "interface in com.here.sdk.mapview") observer)

    Removes the listener from the camera.

    Trying to remove a listener that is not currently registered has no effect.
Parameters:
    `observer` -

    Listener to be removed from receiving state notifications.

### removeListeners

public void removeListeners()

    Removes all registered listeners.

### applyUpdate

public void applyUpdate(@NonNull [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") cameraUpdate)

    Applies camera update to the map camera.

    Any ongoing camera animations will be cancelled and the corresponding camera animation listener will be notified.
Parameters:
    `cameraUpdate` -

    The update that gets applied to camera.

### dryApplyUpdate

public void dryApplyUpdate(@NonNull [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") cameraUpdate, @NonNull [MapCamera.DryCameraUpdateCallback](sdk-for-android-explore-api-reference-latestmapcamera-drycameraupdatecallback "interface in com.here.sdk.mapview") callback)

    Computes result of applying camera update without changing state of the map camera.

    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `cameraUpdate` -

    The update that gets dryly applied to camera.

    `callback` -

    Called upon completion with computed map state.

    callback is called on the main thread.

### startAnimation

public void startAnimation(@NonNull [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") cameraAnimation)

    Starts a given camera animation.

    Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties, like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length). The corresponding listener of an ongoing animation will be notified about the cancellation in these cases.
Parameters:
    `cameraAnimation` -

    The animation to be started.

### startAnimation

public void startAnimation(@NonNull [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") cameraAnimation, @NonNull [AnimationListener](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation") animationListener)

    Starts a given camera animation. The state of the animation can be tracked with the provided listener.

    Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties, like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length). The corresponding listener of an ongoing animation will be notified about the cancellation in these cases.
Parameters:
    `cameraAnimation` -

    The animation to be started.

    `animationListener` -

    Animation listener. A strong reference is kept internally up until the animation gets cancelled or completed.

### cancelAnimation

public void cancelAnimation(@NonNull [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") cameraAnimation)

    Cancels an ongoing camera animation.

    Upon cancellation, the corresponding listener will be notified.
Parameters:
    `cameraAnimation` -

    The animation to be cancelled.

### cancelAnimations

public void cancelAnimations()

    Cancels any ongoing camera animation.

    Upon cancellation, the corresponding listener of any cancelled animation will be notified.

### orbitBy

public void orbitBy(@NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") delta, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Orbits the camera around a specified view point by increasing tilt and bearing by specified delta values.
Parameters:
    `delta` -

    Camera orientation change, containing tilt and bearing angle deltas.

    `origin` -

    Pixel point in view coordinates around which orbiting occurs.

### zoomBy

public void zoomBy(double factor, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Zooms in or out by a specified factor.

    This effectively changes the distance from the camera to the [`MapCamera.State.targetCoordinates`](sdk-for-android-explore-api-reference-latestmapcamera-state#targetCoordinates) by the specified factor, which changes [`MapCamera.State.zoomLevel`](sdk-for-android-explore-api-reference-latestmapcamera-state#zoomLevel) as well.

    Values above 1.0 will zoom in and values below will zoom out.

    The relation with [`MapCamera.State.distanceToTargetInMeters`](sdk-for-android-explore-api-reference-latestmapcamera-state#distanceToTargetInMeters) is inversely linear, meaning that zooming by 4 will decrease distance to target by 4 while zooming by 0.5 will increase distance to target by 2.

    The relation with zoom level is logarithmic. Meaning that zooming by a factor of 4 will increase zoom level by 2 (because log2(4) == 2). So to zoom in by X zoom levels, the zoom factor needs to be 2^X. To zoom out by X zoom levels, zoom factor needs to be 1/(2^X).

    The zooming occurs around the specified origin inside the view.
Parameters:
    `factor` -

    The zoom factor. Values above 1.0 will zoom in and values below will zoom out.

    `origin` -

    Pixel point in view coordinates around which zooming occurs.

### zoomTo

public void zoomTo(double zoomLevel)

    Zooms to the specified zoom level. The supplied value will be clamped to the range of \[0, 22\], where 0 is a view of whole globe and 22 is street level.

    This effectively changes the distance from the camera to the target. The zooming occurs around the current target point.
Parameters:
    `zoomLevel` -

    The zoom level to set, clamped to the range of \[0, 22\].

### lookAt

public void lookAt(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") target)

    Makes the camera look at a new geodetic target, while preserving the current orientation and distance to the target.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    Geodetic coordinates at which the camera will point.

### lookAt

public void lookAt(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") target, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") zoom)

    Makes the camera look at the geodetic target with the given zoom.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    Geodetic coordinates at which the camera will point.

    `zoom` -

    The zoom level which can be provided as distance to the target point, scale or zoom level.

### lookAt

public void lookAt(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") zoom)

    Makes the camera look at the geodetic target with the given zoom and orientation.

    The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    Geodetic coordinates at which the camera will point.

    `orientation` -

    Desired orientation of the camera.

    `zoom` -

    The zoom level which can be provided as distance to the target point, scale or zoom level.

### lookAt

public void lookAt(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation)

    Makes the camera look at the specified geodetic area.

    The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method.

    The altitude of the target points is ignored.
Parameters:
    `target` -

    Geodetic area at which the camera will point

    `orientation` -

    Desired orientation of the camera

### lookAt

public void lookAt(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewRectangle)

    Makes the camera look at the specified geodetic area and pass a rectangle which specifies where the area should appear inside of the map view.

    The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method. Please note that the resulting orientation might deviate from the provided orientation. This is particularly the case if a large geobox on world level and a view rectangle which is relatively small was passed to the method.

    The altitude of the target points is ignored.
Parameters:
    `target` -

    Geodetic area which will be shown in the viewRectangle.

    `orientation` -

    Desired orientation of the camera.

    `viewRectangle` -

    The view rectangle in viewport pixel coordinates inside which the geographical target area is displayed.

### setDistanceToTarget

public void setDistanceToTarget(double distanceInMeters)

    Makes the camera look at current target from certain distance

    This function neither modifies target coordinates nor target orientation.
Parameters:
    `distanceInMeters` -

    Distance in meters to the target point. Minimal distance value is clamped to 100 meters.

### setOrientationAtTarget

public void setOrientationAtTarget(@NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation)

    Changes camera orientation in relation to target location.
Parameters:
    `orientation` -

    Desired orientation of the camera.

### getState

@NonNull public [MapCamera.State](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview") getState()

    Gets state of the camera that reflects what is currently drawn inside the map view.
Returns:
    Current state of the camera that reflects what is currently drawn by the map view.

### getPrincipalPoint

@NonNull public [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") getPrincipalPoint()

    Gets the pixel point that determines where the target is placed within the map view. By default, the principal point is located at the center of the map view.

    The value of the principal point is adjusted when the dimensions of the map view change, so that it stays in the same point relative to width and height. Meaning that when a principal point it set to bottom middle of the map view, it will stay in the bottom middle regardless of the changes to dimensions and orientation of the view.
Returns:
    Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point.

### setPrincipalPoint

public void setPrincipalPoint(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") value)

    Sets the pixel point that determines where the target appears within the map view. This instantly moves the map to render the current target coordinates at the new principal point.

    By default, the principal point is located at the center of the map view. It is set in pixels relative to the map view's origin top-left (0, 0). Values outside the map view's dimensions (x \< 0 \|\| x \> width, y \< 0 \|\| y \> height) will be rejected silently and the current principal point is kept.

    The value of the principal point is adjusted when the dimensions of the map view change, so that it stays in the same point relative to width and height. Meaning that when a principal point it set to bottom middle of the map view, it will stay in the bottom middle regardless of the changes to dimensions and orientation of the view.

    Note: The principal point affects all programmatical map transformations (rotate, orbit, tilt and zoom) and the two-finger-pan gesture to tilt the map. Other gestures, like pinch-rotate, are not affected.
Parameters:
    `value` -

    Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point.

### getBoundingBox

@Nullable public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") getBoundingBox()

    Gets the current visible map area encompassed in a GeoBox.

    Note that this bounding box is always rectangular, and its sides are always parallel to the latitude and longitude. If the camera is rotated, the returned bounding box will be a circumscribed rectangle that is larger than the visible map area. Similarly, when the map is tilted (for example, if the map is tilted by 45 degrees), the visible map area represents a trapezoidal area in the world. Resulting value will then be a larger circumscribed rectangle that contains this trapezoid area. Because on this, corners of the resulting bounding box may be located outside of the currently visible area.

    When the map area does not fully fill the viewport, `null` is returned.
Returns:
    Currently visible map area encompassed in a GeoBox.

### getLimits

@NonNull public [MapCameraLimits](sdk-for-android-explore-api-reference-latestmapcameralimits "class in com.here.sdk.mapview") getLimits()

    Gets a MapCameraLimits instance that controls limits for the camera settings.
Returns:
    Controls limits for the camera settings.
