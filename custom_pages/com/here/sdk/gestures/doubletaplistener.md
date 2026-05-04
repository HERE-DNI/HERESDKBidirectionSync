---
title: "DoubleTapListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdoubletaplistener"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface DoubleTapListener

------------------------------------------------------------------------
public interface DoubleTapListener
Interface for handling double tap gestures. Double-tap gesture occurs after double-tapping on the screen.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onDoubleTap](#onDoubleTap(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Called when the double-tap gesture occurs.

## Method Details

### onDoubleTap

void onDoubleTap(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Called when the double-tap gesture occurs.
Parameters:
    `origin` -

    Position of the touch point relative to the MapView in pixels.
