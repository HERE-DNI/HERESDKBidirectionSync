---
title: "MapCamera.State (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcamera-state"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapCamera.State

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapCamera.State
Enclosing class:
[MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapCamera.State extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Encapsulates state of the camera.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [distanceToTargetInMeters](#distanceToTargetInMeters)

Distance from the camera to the target point in meters.

[`GeoOrientation`](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core")

  [orientationAtTarget](#orientationAtTarget)

Camera's orientation at target point.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [targetCoordinates](#targetCoordinates)

Camera's 'LookAt' target position in geodetic space.

`double`

  [zoomLevel](#zoomLevel)

Zoom level corresponding to the current distance to target.

## Constructor Summary

Constructors

Constructor

  Description

  [State](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` targetCoordinates, `[`GeoOrientation`](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core")` orientationAtTarget, double distanceToTargetInMeters, double zoomLevel)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### targetCoordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") targetCoordinates

    Camera's 'LookAt' target position in geodetic space.

    Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

### orientationAtTarget

@NonNull public [GeoOrientation](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core") orientationAtTarget

    Camera's orientation at target point.

### distanceToTargetInMeters

public double distanceToTargetInMeters

    Distance from the camera to the target point in meters.

### zoomLevel

public double zoomLevel

    Zoom level corresponding to the current distance to target.

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double)" class="section detail">

### State

public State(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") targetCoordinates, @NonNull [GeoOrientation](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core") orientationAtTarget, double distanceToTargetInMeters, double zoomLevel)

    Creates a new instance.
Parameters:
    `targetCoordinates` -

    Camera's 'LookAt' target position in geodetic space.

    Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `orientationAtTarget` -

    Camera's orientation at target point.

    `distanceToTargetInMeters` -

    Distance from the camera to the target point in meters.

    `zoomLevel` -

    Zoom level corresponding to the current distance to target.
