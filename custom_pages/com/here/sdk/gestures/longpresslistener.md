---
title: "LongPressListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlongpresslistener"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface LongPressListener

------------------------------------------------------------------------
public interface LongPressListener
Interface for handling long-press gestures. Long-press gesture occurs after tapping and holding the finger for a long time on the screen.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onLongPress](#onLongPress(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D))`(`[`GestureState`](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures")` state, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Called when the double long press gesture occurs.

## Method Details

### onLongPress

void onLongPress(@NonNull [GestureState](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures") state, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Called when the double long press gesture occurs.
Parameters:
    `state` -

    Determines in which state the gesture is.

    `origin` -

    Position of the touch point relative to the MapView in pixels.
