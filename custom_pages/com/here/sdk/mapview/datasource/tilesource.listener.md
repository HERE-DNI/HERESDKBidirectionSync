---
title: "TileSource.Listener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttilesource-listener"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TileSource.Listener

Enclosing interface:
[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static interface TileSource.Listener
Listener of [`TileSource`](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource") events.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onDataVersionChanged](#onDataVersionChanged(com.here.sdk.mapview.datasource.TileSource.DataVersion))`(`[`TileSource.DataVersion`](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource")` dataVersion)`

Called when tile source data version changes.

## Method Details

### onDataVersionChanged

void onDataVersionChanged(@NonNull [TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource") dataVersion)

    Called when tile source data version changes.
Parameters:
    `dataVersion` -

    New tile data version.
