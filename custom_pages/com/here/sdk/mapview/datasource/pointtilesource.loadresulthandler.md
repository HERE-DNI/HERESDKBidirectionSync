---
title: "PointTileSource.LoadResultHandler (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpointtilesource-loadresulthandler"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PointTileSource.LoadResultHandler

Enclosing interface:
[PointTileSource](sdk-for-android-explore-api-reference-latestpointtilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static interface PointTileSource.LoadResultHandler
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

  [loaded](#loaded(com.here.sdk.mapview.datasource.TileKey,java.util.List,com.here.sdk.mapview.datasource.TileSource.TileMetadata))`(`[`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")` tileKey, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")`> data, `[`TileSource.TileMetadata`](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata "class in com.here.sdk.mapview.datasource")` metadata)`

Called upon successful load tile request.

## Method Details

### loaded

void loaded(@NonNull [TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") tileKey, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")\> data, @NonNull [TileSource.TileMetadata](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata "class in com.here.sdk.mapview.datasource") metadata)

    Called upon successful load tile request.
Parameters:
    `tileKey` -

    Loaded tile key.

    `data` -

    Loaded tile data.

    `metadata` -

    Loaded tile metadata.

### failed

void failed(@NonNull [TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") tileKey)

    Called upon failed load tile request.
Parameters:
    `tileKey` -

    Failed tile key.
