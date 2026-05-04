---
title: "MapCamera.DryCameraUpdateCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcamera-drycameraupdatecallback"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapCamera.DryCameraUpdateCallback

Enclosing class:
[MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface MapCamera.DryCameraUpdateCallback
Used to report back results of dry update application to camera.

Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onDryApplyUpdateResult](#onDryApplyUpdateResult(com.here.sdk.mapview.MapCamera.State))`(`[`MapCamera.State`](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview")` cameraState)`

Used to report back results of dry update application to camera.

## Method Details

### onDryApplyUpdateResult

void onDryApplyUpdateResult(@Nullable [MapCamera.State](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview") cameraState)

    Used to report back results of dry update application to camera.

    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `cameraState` -

    Map camera state after dry application of update
