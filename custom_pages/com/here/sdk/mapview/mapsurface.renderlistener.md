---
title: "MapSurface.RenderListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapsurface-renderlistener"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapSurface.RenderListener

Enclosing class:
[MapSurface](sdk-for-android-explore-api-reference-latestmapsurface "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static interface MapSurface.RenderListener
Listener of MapSurface render events. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onFramePrepared](#onFramePrepared())`()`

Called after each frame is prepared for rendering, before presenting it, from inside the render loop.

`void`

  [onRenderTargetReleased](#onRenderTargetReleased())`()`

Called after the render target has been released.

## Method Details

### onFramePrepared

void onFramePrepared()

    Called after each frame is prepared for rendering, before presenting it, from inside the render loop. Inside, custom rendering can be performed. It is recommended that the execution to be kept to a minimum as this can adversely affect the frame rendering time.

### onRenderTargetReleased

void onRenderTargetReleased()

    Called after the render target has been released. Inside, resources associated with any custom rendering can be released.
