---
title: "LocationListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocationlistener"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface LocationListener

------------------------------------------------------------------------
public interface LocationListener
This interface should be implemented in order to receive notifications about location updates.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onLocationUpdated](#onLocationUpdated(com.here.sdk.core.Location))`(`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")` location)`

Called each time a new location is available.

## Method Details

### onLocationUpdated

void onLocationUpdated(@NonNull [Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core") location)

    Called each time a new location is available. In a navigation context while using the `Navigator` or `VisualNavigator`, it's required to set the `Location.time` parameter for each `Location` object so that the HERE SDK can map-match the locations properly. If the `Location.time` parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each `Location` object. Invoked on the main thread.
Parameters:
    `location` -

    Current location.
