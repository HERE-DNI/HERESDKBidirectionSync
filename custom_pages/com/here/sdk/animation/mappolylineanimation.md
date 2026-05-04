---
title: "MapPolylineAnimation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappolylineanimation"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPolylineAnimation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.animation.MapPolylineAnimation
------------------------------------------------------------------------
public final class MapPolylineAnimation extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
An animation that can be applied to the [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview") object.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapPolylineAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmappolylineanimation-instantiationerrorcode)

Describes a reason for failing to create a [`MapPolylineAnimation`](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation").

`static final class `

  [MapPolylineAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolylineanimation-instantiationexception)

Thrown when a problem occurs while trying to create a [`MapPolylineAnimation`](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation").

## Constructor Summary

Constructors

Constructor

  Description

  [MapPolylineAnimation](#%3Cinit%3E(com.here.sdk.animation.MapItemKeyFrameTrack))`(`[`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation")` track)`

Creates an animation of [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview") based on provided keyframe track.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.animation.MapItemKeyFrameTrack)" class="section detail">

### MapPolylineAnimation

public MapPolylineAnimation(@NonNull [MapItemKeyFrameTrack](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation") track) throws [MapPolylineAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolylineanimation-instantiationexception "class in com.here.sdk.animation")

    Creates an animation of [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview") based on provided keyframe track. Supports tracks created with [`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation") 'polylineProgress\*' methods. For starting the animation, see [`MapPolyline.startAnimation(com.here.sdk.animation.MapPolylineAnimation, com.here.sdk.animation.AnimationListener)`](sdk-for-android-explore-api-reference-latestmappolyline#startAnimation(com.here.sdk.animation.MapPolylineAnimation,com.here.sdk.animation.AnimationListener)).
Parameters:
    `track` -

    The track holding the keyframes for the animation.

    Throws:
    [`MapPolylineAnimation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolylineanimation-instantiationexception "class in com.here.sdk.animation") -

    If the specified keyframe track cannot be used to create animation of a [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview").
