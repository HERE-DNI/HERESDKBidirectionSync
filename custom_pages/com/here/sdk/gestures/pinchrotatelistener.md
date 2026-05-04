---
title: "PinchRotateListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpinchrotatelistener"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PinchRotateListener

------------------------------------------------------------------------
public interface PinchRotateListener
Interface for handling pinch rotate gestures. Pinch rotate gesture occurs when two fingers are on the screen and at least one of them moves.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onPinchRotate](#onPinchRotate(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double,com.here.sdk.core.Angle))`(`[`GestureState`](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures")` state, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` pinchOrigin, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` rotationOrigin, double twoFingerDistance, `[`Angle`](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core")` rotation)`

Called when the pinch rotate gesture occurs.

## Method Details

### onPinchRotate

void onPinchRotate(@NonNull [GestureState](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures") state, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") pinchOrigin, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") rotationOrigin, double twoFingerDistance, @NonNull [Angle](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core") rotation)

    Called when the pinch rotate gesture occurs.
Parameters:
    `state` -

    Determines in which state the gesture is.

    `pinchOrigin` -

    Position where the pinch happened relative to the MapView in pixels.

    `rotationOrigin` -

    Position where the rotation happened relative to the MapView in pixels.

    `twoFingerDistance` -

    Distance between the two fingers in pixels.

    `rotation` -

    Fingers rotation angle delta. Indicates how much the fingers rotation angle has changed since the previous gesture update. Clockwise finger rotation gives positive deltas, counter clockwise finger rotation gives negative deltas.
