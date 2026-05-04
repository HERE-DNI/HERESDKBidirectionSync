---
title: "RasterTileSource.LoadResultHandler (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrastertilesource-loadresulthandler"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface RasterTileSource.LoadResultHandler

Enclosing interface:
[RasterTileSource](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static interface RasterTileSource.LoadResultHandler
Result handler of a load tile request.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [failed](#failed(com.here.sdk.mapview.datasource.TileKey))`(`[`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")` tileKey)`

Called upon failed load tile request.

`void`

  [loaded](#loaded(com.here.sdk.mapview.datasource.TileKey,byte%5B%5D,com.here.sdk.mapview.datasource.TileSource.TileMetadata))`(`[`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")` tileKey, byte[] data, `[`TileSource.TileMetadata`](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata "class in com.here.sdk.mapview.datasource")` metadata)`

Called upon successful load tile request.

## Method Details

### loaded

void loaded(@NonNull [TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") tileKey, @NonNull byte\[\] data, @NonNull [TileSource.TileMetadata](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata "class in com.here.sdk.mapview.datasource") metadata)

    Called upon successful load tile request.
Parameters:
    `tileKey` -

    Loaded tile key.

    `data` -

    Loaded tile data. Supported are images in PNG or JPEG format.

    `metadata` -

    Loaded tile metadata.

### failed

void failed(@NonNull [TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") tileKey)

    Called upon failed load tile request.
Parameters:
    `tileKey` -

    Failed tile key.
