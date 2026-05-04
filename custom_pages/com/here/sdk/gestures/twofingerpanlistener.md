---
title: "TwoFingerPanListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttwofingerpanlistener"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TwoFingerPanListener

------------------------------------------------------------------------
public interface TwoFingerPanListener
Interface for handling two finger pan gestures. Two finger pan gesture occurs when two fingers are on the screen and both of them are moving vertically.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTwoFingerPan](#onTwoFingerPan(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double))`(`[`GestureState`](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures")` state, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` translation, double velocity)`

Called when the two finger pan gesture occurs.

## Method Details

### onTwoFingerPan

void onTwoFingerPan(@NonNull [GestureState](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures") state, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") translation, double velocity)

    Called when the two finger pan gesture occurs.
Parameters:
    `state` -

    Determines in which state the gesture is.

    `origin` -

    Position halfway between two touch points relative to the MapView in pixels.

    `translation` -

    Translation offset since the last position in pixels.

    `velocity` -

    Velocity of panning in pixels per millisecond.
