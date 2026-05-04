---
title: "TileSource.LoadTileRequestHandle (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TileSource.LoadTileRequestHandle

Enclosing interface:
[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static interface TileSource.LoadTileRequestHandle
Handle of a load request.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [cancel](#cancel())`()`

Cancels the associated load tile request.

## Method Details

### cancel

void cancel()

    Cancels the associated load tile request. Upon cancellation, the corresponding result handler must be informed.
