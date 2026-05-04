---
title: "MapMarkerAnimation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarkeranimation"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarkerAnimation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.animation.MapMarkerAnimation
------------------------------------------------------------------------
public final class MapMarkerAnimation extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
An animation that can be applied to the [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") object.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapMarkerAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarkeranimation-instantiationerrorcode)

Describes a reason for failing to create a [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation").

`static final class `

  [MapMarkerAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarkeranimation-instantiationexception)

Thrown when a problem occurs while trying to create a [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation").

## Constructor Summary

Constructors

Constructor

  Description

  [MapMarkerAnimation](#%3Cinit%3E(com.here.sdk.animation.MapItemKeyFrameTrack))`(`[`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation")` track)`

Creates an animation of [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") based on provided keyframe track.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.animation.MapItemKeyFrameTrack)" class="section detail">

### MapMarkerAnimation

public MapMarkerAnimation(@NonNull [MapItemKeyFrameTrack](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation") track) throws [MapMarkerAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarkeranimation-instantiationexception "class in com.here.sdk.animation")

    Creates an animation of [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") based on provided keyframe track.

    Supports tracks created with [`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation") 'moveTo\*' methods.

    For starting the animation see [`MapMarker.startAnimation(com.here.sdk.animation.MapMarkerAnimation, com.here.sdk.animation.AnimationListener)`](sdk-for-android-explore-api-reference-latestmapmarker#startAnimation(com.here.sdk.animation.MapMarkerAnimation,com.here.sdk.animation.AnimationListener)).
Parameters:
    `track` -

    The track holding the keyframes for the animation.

    Throws:
    [`MapMarkerAnimation.InstantiationException`](sdk-for-android-explore-api-reference-latestmapmarkeranimation-instantiationexception "class in com.here.sdk.animation") -

    If the specified keyframe track cannot be used to create animation of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").
