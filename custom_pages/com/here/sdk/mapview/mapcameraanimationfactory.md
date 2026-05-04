---
title: "MapCameraAnimationFactory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcameraanimationfactory"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapCameraAnimationFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapCameraAnimationFactory
------------------------------------------------------------------------
public final class MapCameraAnimationFactory extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Factory for creating MapCameraAnimation objects to change map's camera over time.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

  [createAnimation](#createAnimation(com.here.sdk.mapview.MapCameraKeyframeTrack))`(`[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")` track)`

Creates a MapCameraAnimation for a movement defined by the supplied `track`.

`static `[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

  [createAnimation](#createAnimation(com.here.sdk.mapview.MapCameraUpdate,com.here.time.Duration,com.here.sdk.animation.Easing))`(`[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")` cameraUpdate, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing)`

Creates a [`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") to gradually update the camera properties within a specified duration from its current values to the ones defined in the `cameraUpdate`.

`static `[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

  [createAnimation](#createAnimation(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")`> tracks)`

Creates a MapCameraAnimation for a movement defined by the supplied list of `tracks`.

`static `[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

  [flyTo](#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,double,com.here.time.Duration))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, double bowFactor, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

`static `[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

  [flyTo](#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,double,com.here.time.Duration))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, double bowFactor, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

`static `[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

  [flyTo](#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` zoom, double bowFactor, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

`static `[`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

  [flyTo](#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` zoom, double bowFactor, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### createAnimation

@NonNull public static [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") createAnimation(@NonNull [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") cameraUpdate, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing)

    Creates a [`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") to gradually update the camera properties within a specified duration from its current values to the ones defined in the `cameraUpdate`. `MapCameraAnimation` instances created from [`MapCameraUpdateFactory.compositeUpdate(java.util.List<com.here.sdk.mapview.MapCameraUpdate>)`](sdk-for-android-explore-api-reference-latestmapcameraupdatefactory#compositeUpdate(java.util.List)) instances are not supported. An [`AnimationListener`](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation") will receive an [`AnimationState.CANCELLED`](sdk-for-android-explore-api-reference-latestanimationstate#CANCELLED) signal when trying to apply such animations.
Parameters:
    `cameraUpdate` -

    Update which should be applied to the map camera.

    `duration` -

    Duration of the animation. Negative duration results in no camera change when applied.

    `easing` -

    Easing to apply.

    Returns:
    MapCameraAnimation instance

### createAnimation

@NonNull public static [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") createAnimation(@NonNull [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") track)

    Creates a MapCameraAnimation for a movement defined by the supplied `track`.
Parameters:
    `track` -

    The track

    Returns:
    MapCameraAnimation instance

### createAnimation

@NonNull public static [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") createAnimation(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")\> tracks) throws [MapCameraAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationexception "class in com.here.sdk.mapview")

    Creates a MapCameraAnimation for a movement defined by the supplied list of `tracks`. Keyframe tracks specify how the map camera properties change during the animation. For the animation to be possible, no two different tracks can affect the same map camera property. The input tracks are validated with that in mind.

    However, the following cases can only be detected at the time when animation is started:

    - Changing altitude of camera position also changes camera look-at distance and at high altitudes, also camera look-at orientation.
    - Changing tilt of camera orientation also changes camera look-at distance and camera look-at target.
    - Changing bearing of camera orientation also changes camera look-at target if current tilt is not 0.
    - Changing tilt or bearing of camera look-at orientation also changes camera position.
    - Changing camera look-at orientation also changes camera look-at distance if tilt is not 0.
Parameters:
    `tracks` -

    The list of tracks

    Returns:
    MapCameraAnimation instance

    Throws:
    [`MapCameraAnimation.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### flyTo

@NonNull public static [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") flyTo(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, double bowFactor, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

    The beginning and end of the animation will use the current zoom.

    Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly.

    The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target.

    A bow factor of 0 does not change the camera's zoom over time.

    Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

    The bow factor is clamped to \[-1, +1\].

    Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value.

    Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:
    MapCameraAnimation instance

### flyTo

@NonNull public static [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") flyTo(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, double bowFactor, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

    The beginning and end of the animation will use the current zoom.

    Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `orientation` -

    The orientation at destination.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly.

    The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target.

    A bow factor of 0 does not change the camera's zoom over time.

    Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

    The bow factor is clamped to \[-1, +1\].

    Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value.

    Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:
    MapCameraAnimation instance

### flyTo

@NonNull public static [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") flyTo(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") zoom, double bowFactor, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

    The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.

    Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `zoom` -

    The zoom at the end of the animation.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly.

    The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target.

    A bow factor of 0 does not affect the camera's zoom over time.

    Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

    The bow factor is clamped to \[-1, +1\].

    Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value.

    Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:
    MapCameraAnimation instance

### flyTo

@NonNull public static [MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview") flyTo(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") zoom, double bowFactor, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

    The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.

    Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `orientation` -

    The orientation at destination.

    `zoom` -

    The zoom at the end of the animation.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly.

    The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target.

    A bow factor of 0 does not affect the camera's zoom over time.

    Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

    The bow factor is clamped to \[-1, +1\].

    Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value.

    Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:
    MapCameraAnimation instance
