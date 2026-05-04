---
title: "PolygonTileSource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolygontilesource"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PolygonTileSource

All Superinterfaces:
[`TileSource`](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public interface PolygonTileSource extends [TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")
A source of geodetic polygon tiles. Polygons provided by an implementation must be clipped to the boundaries of the requested tile. The implementations must be thread-safe.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Interface

  Description

  `static interface `

  [PolygonTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpolygontilesource-loadresulthandler)

Result handler of a load tile request.

## Nested classes/interfaces inherited from interface com.here.sdk.mapview.datasource.[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

  [`TileSource.DataVersion`](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource"), [`TileSource.Listener`](sdk-for-android-explore-api-reference-latesttilesource-listener "interface in com.here.sdk.mapview.datasource"), [`TileSource.LoadTileRequestHandle`](sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource"), [`TileSource.TileMetadata`](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata "class in com.here.sdk.mapview.datasource")

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [`TileSource.LoadTileRequestHandle`](sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource")

  [loadTile](#loadTile(com.here.sdk.mapview.datasource.TileKey,com.here.sdk.mapview.datasource.PolygonTileSource.LoadResultHandler))`(`[`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")` tileKey, `[`PolygonTileSource.LoadResultHandler`](sdk-for-android-explore-api-reference-latestpolygontilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")` completionHandler)`

Load data of a tile.

### Methods inherited from interface com.here.sdk.mapview.datasource.[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

  [`addListener`](sdk-for-android-explore-api-reference-latesttilesource#addListener(com.here.sdk.mapview.datasource.TileSource.Listener)), [`getDataVersion`](sdk-for-android-explore-api-reference-latesttilesource#getDataVersion(com.here.sdk.mapview.datasource.TileKey)), [`getStorageLevels`](sdk-for-android-explore-api-reference-latesttilesource#getStorageLevels()), [`getTilingScheme`](sdk-for-android-explore-api-reference-latesttilesource#getTilingScheme()), [`removeListener`](sdk-for-android-explore-api-reference-latesttilesource#removeListener(com.here.sdk.mapview.datasource.TileSource.Listener))

## Method Details

### loadTile

@Nullable [TileSource.LoadTileRequestHandle](sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource") loadTile(@NonNull [TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") tileKey, @NonNull [PolygonTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpolygontilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource") completionHandler)

    Load data of a tile. Upon completion, the handler gets informed.
Parameters:
    `tileKey` -

    Key of the tile to load data for.

    `completionHandler` -

    Load result handler.

    Returns:
    A handle to the created load request.
