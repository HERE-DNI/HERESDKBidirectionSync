---
title: "TileSource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttilesource"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TileSource

All Known Subinterfaces:
[`LineTileSource`](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource"), [`PointTileSource`](sdk-for-android-explore-api-reference-latestpointtilesource "interface in com.here.sdk.mapview.datasource"), [`PolygonTileSource`](sdk-for-android-explore-api-reference-latestpolygontilesource "interface in com.here.sdk.mapview.datasource"), [`RasterTileSource`](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public interface TileSource
A source of tiles. The implementations must be thread-safe.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Interface

  Description

  `static final class `

  [TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion)

Tile data version.

`static interface `

  [TileSource.Listener](sdk-for-android-explore-api-reference-latesttilesource-listener)

Listener of [`TileSource`](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource") events.

`static interface `

  [TileSource.LoadTileRequestHandle](sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle)

Handle of a load request.

`static final class `

  [TileSource.TileMetadata](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata)

Tile metadata.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [addListener](#addListener(com.here.sdk.mapview.datasource.TileSource.Listener))`(`[`TileSource.Listener`](sdk-for-android-explore-api-reference-latesttilesource-listener "interface in com.here.sdk.mapview.datasource")` listener)`

Adds a listener for receiving state notifications.

[`TileSource.DataVersion`](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource")

  [getDataVersion](#getDataVersion(com.here.sdk.mapview.datasource.TileKey))`(`[`TileKey`](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")` tileKey)`

Gets the current data version of a tile.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [getStorageLevels](#getStorageLevels())`()`

Gets the storage levels available for this data source.

[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")

  [getTilingScheme](#getTilingScheme())`()`

Gets the tiling scheme used by this source.

`void`

  [removeListener](#removeListener(com.here.sdk.mapview.datasource.TileSource.Listener))`(`[`TileSource.Listener`](sdk-for-android-explore-api-reference-latesttilesource-listener "interface in com.here.sdk.mapview.datasource")` listener)`

Removes a listener from receiving state notifications.

## Method Details

### getDataVersion

@NonNull [TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource") getDataVersion(@NonNull [TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource") tileKey)

    Gets the current data version of a tile.
Parameters:
    `tileKey` -

    Key of the tile for which to retrieve the version.

    Returns:
    Data version for a tile.

### addListener

void addListener(@NonNull [TileSource.Listener](sdk-for-android-explore-api-reference-latesttilesource-listener "interface in com.here.sdk.mapview.datasource") listener)

    Adds a listener for receiving state notifications.
Parameters:
    `listener` -

    The listener

### removeListener

void removeListener(@NonNull [TileSource.Listener](sdk-for-android-explore-api-reference-latesttilesource-listener "interface in com.here.sdk.mapview.datasource") listener)

    Removes a listener from receiving state notifications.
Parameters:
    `listener` -

    Listener to be removed from receiving state notifications.

### getTilingScheme

@NonNull [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") getTilingScheme()

    Gets the tiling scheme used by this source.
Returns:
    The tiling scheme used by this source.

### getStorageLevels

@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> getStorageLevels()

    Gets the storage levels available for this data source. Supported range \[0, 31\].

    At least one level must be available for this to be used as a source of data.
Returns:
    The storage levels available for this data source. Supported range \[0, 31\].
