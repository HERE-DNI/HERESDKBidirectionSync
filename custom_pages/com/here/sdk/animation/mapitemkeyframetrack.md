---
title: "MapItemKeyFrameTrack (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapitemkeyframetrack"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapItemKeyFrameTrack

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.animation.MapItemKeyFrameTrack
------------------------------------------------------------------------
public final class MapItemKeyFrameTrack extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Stores keyframes for interpolation of a map item property using a specific easing function and interpolation mode.

The keyframe track object is used to create animations, see [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation") and [`MapPolylineAnimation`](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation").

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapItemKeyFrameTrack.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationerrorcode)

Describes a reason for failing to create a [`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation").

`static final class `

  [MapItemKeyFrameTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationexception)

Thrown when a problem occurs while trying to create [`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation").

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation")

  [moveTo](#moveTo(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinatesKeyframe`](sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a map item position keyframe track.

`static `[`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation")

  [polylineProgress](#polylineProgress(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ScalarKeyframe`](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")`> keyframes, `[`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")` easing, `[`KeyframeInterpolationMode`](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")` interpolationMode)`

Creates a keyframe track used to animate the progress of a polyline.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### moveTo

@NonNull public static [MapItemKeyFrameTrack](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation") moveTo(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinatesKeyframe](sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapItemKeyFrameTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation")

    Creates a map item position keyframe track. It enables animations over the geographical coordinates where the map item is positioned.
Parameters:
    `keyframes` -

    The list of keyframes that specify how the map item position changes over time.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    MapItemKeyFrameTrack instance.

    Throws:
    [`MapItemKeyFrameTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation") -

    If the supplied keyframe list is empty or first keyframe duration is not 0.

### polylineProgress

@NonNull public static [MapItemKeyFrameTrack](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation") polylineProgress(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ScalarKeyframe](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")\> keyframes, @NonNull [Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation") easing, @NonNull [KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode) throws [MapItemKeyFrameTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation")

    Creates a keyframe track used to animate the progress of a polyline.

    Each scalar keyframe specifies the progress property (as passed to [`MapPolyline.setProgress(double)`](sdk-for-android-explore-api-reference-latestmappolyline#setProgress(double))) at key points of the animation.
Parameters:
    `keyframes` -

    The list of keyframes that specify how the polyline progress changes over time.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:
    MapItemKeyFrameTrack instance.

    Throws:
    [`MapItemKeyFrameTrack.InstantiationException`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation") -

    If the supplied keyframe list is empty or first keyframe duration is not 0.
