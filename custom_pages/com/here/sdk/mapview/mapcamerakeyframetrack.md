---
title: "MapCameraKeyframeTrack (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapCameraKeyframeTrack

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapCameraKeyframeTrack
------------------------------------------------------------------------
public final class MapCameraKeyframeTrack extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode. Can only hold keyframes of a single type.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapCameraKeyframeTrack.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationerrorcode)

Describes a reason for failing to create a MapCameraKeyframeTrack.

`static final class `

  [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception)

Thrown when a problem occurs while trying to create [`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview").

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods
  Deprecated Methods

  Modifier and Type

  Method

  Description

  `static `[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

  [fieldOfView](#fieldOfView(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ScalarKeyframe`](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a map camera field-of-view keyframe track.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Anchor2DKeyframe`](sdk-for-android-explore-api-reference-latestanchor2dkeyframe "class in com.here.sdk.animation")`>`

  [getAnchor2DKeyframes](#getAnchor2DKeyframes())`()`

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinatesKeyframe`](sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe "class in com.here.sdk.animation")`>`

  [getGeoCoordinatesKeyframes](#getGeoCoordinatesKeyframes())`()`

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoOrientationKeyframe`](sdk-for-android-explore-api-reference-latestgeoorientationkeyframe "class in com.here.sdk.animation")`>`

  [getGeoOrientationKeyframes](#getGeoOrientationKeyframes())`()`

  [`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")

  [getInterpolationMode](#getInterpolationMode())`()`

Gets the interpolation mode for the between key frames in the track.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Point2DKeyframe`](sdk-for-android-explore-api-reference-latestpoint2dkeyframe "class in com.here.sdk.animation")`>`

  [getPoint2DKeyframes](#getPoint2DKeyframes())`()`

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ScalarKeyframe`](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")`>`

  [getScalarKeyframes](#getScalarKeyframes())`()`

  `static `[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

  [lookAtDistance](#lookAtDistance(com.here.sdk.mapview.MapMeasure.Kind,java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[`MapMeasure.Kind`](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview")` distanceKind, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ScalarKeyframe`](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a map camera look-at distance keyframe track.

`static `[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

  [lookAtDistance](#lookAtDistance(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ScalarKeyframe`](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Deprecated.
Will be removed in v4.27.0.

  `static `[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

  [lookAtOrientation](#lookAtOrientation(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoOrientationKeyframe`](sdk-for-android-explore-api-reference-latestgeoorientationkeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a map camera look-at orientation keyframe track.

`static `[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

  [lookAtTarget](#lookAtTarget(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinatesKeyframe`](sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a map camera look-at target keyframe track.

`static `[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

  [normalizedPrincipalPoint](#normalizedPrincipalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Anchor2DKeyframe`](sdk-for-android-explore-api-reference-latestanchor2dkeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a map camera principal point keyframe track.

`static `[`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

  [principalPoint](#principalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Point2DKeyframe`](sdk-for-android-explore-api-reference-latestpoint2dkeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a map camera principal point keyframe track.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getScalarKeyframes

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ScalarKeyframe](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")\> getScalarKeyframes()
Returns:
    a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.

### getPoint2DKeyframes

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Point2DKeyframe](sdk-for-android-explore-api-reference-latestpoint2dkeyframe "class in com.here.sdk.animation")\> getPoint2DKeyframes()
Returns:
    a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.

### getAnchor2DKeyframes

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Anchor2DKeyframe](sdk-for-android-explore-api-reference-latestanchor2dkeyframe "class in com.here.sdk.animation")\> getAnchor2DKeyframes()
Returns:
    a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.

### getGeoCoordinatesKeyframes

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinatesKeyframe](sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe "class in com.here.sdk.animation")\> getGeoCoordinatesKeyframes()
Returns:
    a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.

### getGeoOrientationKeyframes

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoOrientationKeyframe](sdk-for-android-explore-api-reference-latestgeoorientationkeyframe "class in com.here.sdk.animation")\> getGeoOrientationKeyframes()
Returns:
    a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.

### lookAtDistance

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public static [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") lookAtDistance(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ScalarKeyframe](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

    Deprecated.
Will be removed in v4.27.0. Use , Easing, KeyframeInterpolationMode) instead.

Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at in meters. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.
Parameters:
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    A keyframe track over the distance from the map camera to its target.

    Throws:
    [`MapCameraKeyframeTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### lookAtDistance

@NonNull public static [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") lookAtDistance(@NonNull [MapMeasure.Kind](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview") distanceKind, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ScalarKeyframe](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

    Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at. The measure kind of that distance can be specified. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.
Parameters:
    `distanceKind` -

    The kind of measure of distance between camera and target point.

    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    A keyframe track over the distance from the map camera to its target.

    Throws:
    [`MapCameraKeyframeTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### lookAtTarget

@NonNull public static [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") lookAtTarget(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinatesKeyframe](sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

    Creates a map camera look-at target keyframe track. It enables animations over the geographical coordinates of the target point that the map camera is looking at. Altitude components of coordinates are ignored.
Parameters:
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    A keyframe track over the map camera target coordinates.

    Throws:
    [`MapCameraKeyframeTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### lookAtOrientation

@NonNull public static [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") lookAtOrientation(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoOrientationKeyframe](sdk-for-android-explore-api-reference-latestgeoorientationkeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

    Creates a map camera look-at orientation keyframe track. It enables animations over the orientation of the map camera target (bearing and tilt).
Parameters:
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    A keyframe track over the map camera target orientation.

    Throws:
    [`MapCameraKeyframeTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### principalPoint

@NonNull public static [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") principalPoint(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Point2DKeyframe](sdk-for-android-explore-api-reference-latestpoint2dkeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

    Creates a map camera principal point keyframe track. It enables animations on the pixel point where the map camera's target is placed in view coordinates. (0,0) is top left of the viewport, (viewport width, viewport height) is bottom right.
Parameters:
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Point values must be in screen (pixel) coordinates with origin (0,0) in the top left of the viewport. Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    A keyframe track over the principal point.

    Throws:
    [`MapCameraKeyframeTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### normalizedPrincipalPoint

@NonNull public static [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") normalizedPrincipalPoint(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Anchor2DKeyframe](sdk-for-android-explore-api-reference-latestanchor2dkeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

    Creates a map camera principal point keyframe track. It enables animations on the point where the map camera's target is placed in normalized view coordinates. (0,0) is top left of the viewport, (1, 1) is bottom right.
Parameters:
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport. Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    A keyframe track over the principal point.

    Throws:
    [`MapCameraKeyframeTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### fieldOfView

@NonNull public static [MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview") fieldOfView(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ScalarKeyframe](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

    Creates a map camera field-of-view keyframe track. It enables animations over the angle of the field of view captured by the map camera in degrees. Values will be clamped to a range from 1 to 150.
Parameters:
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    A keyframe track over the map camera field-of-view.

    Throws:
    [`MapCameraKeyframeTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.

### getInterpolationMode

@NonNull public [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") getInterpolationMode()

    Gets the interpolation mode for the between key frames in the track.
Returns:
    Interpolation mode affects the shape of the spline going through all keyframes.
