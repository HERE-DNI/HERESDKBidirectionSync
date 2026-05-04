---
title: "PanListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpanlistener"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PanListener

------------------------------------------------------------------------
public interface PanListener
Interface for handling pan gestures. Pan gesture occurs when a finger is moving on the screen.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onPan](#onPan(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double))`(`[`GestureState`](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures")` state, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` translation, double velocity)`

Called when the pan gesture occurs.

## Method Details

### onPan

void onPan(@NonNull [GestureState](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures") state, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") translation, double velocity)

    Called when the pan gesture occurs.
Parameters:
    `state` -

    Determines in which state the gesture is.

    `origin` -

    Position of the touch point relative to the MapView in pixels.

    `translation` -

    Translation offset since the last position in pixels.

    `velocity` -

    Velocity of panning in pixels per millisecond.
