---
title: "TwoFingerTapListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttwofingertaplistener"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TwoFingerTapListener

------------------------------------------------------------------------
public interface TwoFingerTapListener
Interface for handling two finger tap gestures. Two finger tap gesture occurs after tapping on the screen with two fingers.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTwoFingerTap](#onTwoFingerTap(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Called when the double-tap gesture occurs.

## Method Details

### onTwoFingerTap

void onTwoFingerTap(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Called when the double-tap gesture occurs.
Parameters:
    `origin` -

    Position halfway between two touch points relative to the MapView in pixels.
