---
title: "MapIdleListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapidlelistener"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapIdleListener

------------------------------------------------------------------------
public interface MapIdleListener
Used to detect when the map becomes idle or busy.

Map is considered busy when its state changes (for example as a result of camera manipulation) and/or when it requires a redraw (for example, as a result of map data being downloaded).

Map is considered idle when current state is fully rendered and no further redraws are necessary.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onMapBusy](#onMapBusy())`()`

Called when map becomes invalidated and is about to be updated.

`void`

  [onMapIdle](#onMapIdle())`()`

Called when map finishes all state updates.

## Method Details

### onMapBusy

void onMapBusy()

    Called when map becomes invalidated and is about to be updated. One or more redraws will happen afterwards, until [`onMapIdle()`](#onMapIdle()) is called.

### onMapIdle

void onMapIdle()

    Called when map finishes all state updates. No state changes or redraws will happen aftrwards until [`onMapBusy()`](#onMapBusy()) is called.
