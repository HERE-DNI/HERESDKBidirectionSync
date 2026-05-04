---
title: "TapListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttaplistener"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TapListener

------------------------------------------------------------------------
public interface TapListener
Interface for handling tap gestures. Tap gesture occurs after tapping on the screen.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTap](#onTap(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Called when the tap gesture occurs.

## Method Details

### onTap

void onTap(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Called when the tap gesture occurs.
Parameters:
    `origin` -

    Position of the touch point relative to the MapView in pixels.
