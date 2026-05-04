---
title: "AnimationListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestanimationlistener"
hidden: false
---

Package [com.here.sdk.animation](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface AnimationListener

------------------------------------------------------------------------
public interface AnimationListener
A listener for animation events.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onAnimationStateChanged](#onAnimationStateChanged(com.here.sdk.animation.AnimationState))`(`[`AnimationState`](sdk-for-android-explore-api-reference-latestanimationstate "enum class in com.here.sdk.animation")` state)`

Called after the state of an animation changes.

## Method Details

### onAnimationStateChanged

void onAnimationStateChanged(@NonNull [AnimationState](sdk-for-android-explore-api-reference-latestanimationstate "enum class in com.here.sdk.animation") state)

    Called after the state of an animation changes.
Parameters:
    `state` -

    The animation changed to this state.
