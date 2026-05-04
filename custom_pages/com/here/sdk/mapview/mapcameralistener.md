---
title: "MapCameraListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcameralistener"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapCameraListener

------------------------------------------------------------------------
public interface MapCameraListener
Interface for objects that want to get updates whenever the map is redrawn after camera parameters change.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onMapCameraUpdated](#onMapCameraUpdated(com.here.sdk.mapview.MapCamera.State))`(`[`MapCamera.State`](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview")` cameraState)`

Called on the main thread after the map is drawn.

## Method Details

### onMapCameraUpdated

void onMapCameraUpdated(@NonNull [MapCamera.State](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview") cameraState)

    Called on the main thread after the map is drawn.
Parameters:
    `cameraState` -

    Camera parameters at the time the map was drawn.
