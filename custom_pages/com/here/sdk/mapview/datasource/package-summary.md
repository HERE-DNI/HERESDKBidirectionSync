---
title: "com.here.sdk.mapview.datasource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpackage-summary"
hidden: false
---

# Package com.here.sdk.mapview.datasource

------------------------------------------------------------------------
package com.here.sdk.mapview.datasource

Related Packages

Package

  Description

  [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes

  Class

  Description

  [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")

Data attributes collection.

[DataAttributesAccessor](sdk-for-android-explore-api-reference-latestdataattributesaccessor "class in com.here.sdk.mapview.datasource")

Accessor used for manipulating data attributes.

[DataAttributesBase](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

Interface for a collection of data attributes.

[DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")

Data attributes collection builder.

[DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")

Encapsulates a data attribute value.

[DataAttributeValue.ValueType](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource")

Supported types of the data attribute values.

[LineData](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")

Represents a geodetic line with custom attributes.

[LineDataAccessor](sdk-for-android-explore-api-reference-latestlinedataaccessor "class in com.here.sdk.mapview.datasource")

Line data accessor used for manipulating polylines that are part of a LineDataSource.

[LineDataBuilder](sdk-for-android-explore-api-reference-latestlinedatabuilder "class in com.here.sdk.mapview.datasource")

Builder of [`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") instances.

[LineDataSource](sdk-for-android-explore-api-reference-latestlinedatasource "class in com.here.sdk.mapview.datasource")

Polyline data source allows the rendering engine access to the user provided polylines geometry and their attributes.

[LineDataSource.LineDataProcessor](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor "interface in com.here.sdk.mapview.datasource")

Called for each line, allowing inspection, removal or update of coordinates and attributes.

[LineDataSourceBuilder](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource")

Builder of lines data source.

[LineTileDataSource](sdk-for-android-explore-api-reference-latestlinetiledatasource "class in com.here.sdk.mapview.datasource")

Line tile data source allows the rendering engine access to user managed data sets of geodetic lines and their attributes through a [`LineTileSource`](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource").

[LineTileSource](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource")

A source of geodetic line tiles.

[LineTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestlinetilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")

Result handler of a load tile request.

[PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")

Represents a geodetic point with custom attributes.

[PointDataAccessor](sdk-for-android-explore-api-reference-latestpointdataaccessor "class in com.here.sdk.mapview.datasource")

Point data accessor used for manipulating points that are part of a PointDataSource.

[PointDataBuilder](sdk-for-android-explore-api-reference-latestpointdatabuilder "class in com.here.sdk.mapview.datasource")

Builder of [`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") instances.

[PointDataSource](sdk-for-android-explore-api-reference-latestpointdatasource "class in com.here.sdk.mapview.datasource")

Point data source allows the rendering engine access to the user provided geographical locations and their attributes.

[PointDataSource.PointDataProcessor](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource")

Called for each point, allowing inspection, removal or update of coordinates and attributes.

[PointDataSourceBuilder](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource")

Builder of points data source.

[PointTileDataSource](sdk-for-android-explore-api-reference-latestpointtiledatasource "class in com.here.sdk.mapview.datasource")

Point tile data source allows the rendering engine access to user managed data sets of geographical locations and their attributes through a [`PointTileSource`](sdk-for-android-explore-api-reference-latestpointtilesource "interface in com.here.sdk.mapview.datasource").

[PointTileSource](sdk-for-android-explore-api-reference-latestpointtilesource "interface in com.here.sdk.mapview.datasource")

A source of geodetic point tiles.

[PointTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpointtilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")

Result handler of a load tile request.

[PolygonData](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")

Represents a geodetic polygon with custom attributes.

[PolygonDataAccessor](sdk-for-android-explore-api-reference-latestpolygondataaccessor "class in com.here.sdk.mapview.datasource")

Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.

[PolygonDataBuilder](sdk-for-android-explore-api-reference-latestpolygondatabuilder "class in com.here.sdk.mapview.datasource")

Builder of [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") instances.

[PolygonDataSource](sdk-for-android-explore-api-reference-latestpolygondatasource "class in com.here.sdk.mapview.datasource")

Polygon data source allows the rendering engine access to the user provided polygons geometry and their attributes.

[PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource")

Called for each polygon, allowing inspection, removal or update of coordinates and attributes.

[PolygonDataSourceBuilder](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource")

Builder of the polygons data source.

[PolygonTileDataSource](sdk-for-android-explore-api-reference-latestpolygontiledatasource "class in com.here.sdk.mapview.datasource")

Polygon tile data source allows the rendering engine access to user managed data sets of geodetic polygons and their attributes through a [`PolygonTileSource`](sdk-for-android-explore-api-reference-latestpolygontilesource "interface in com.here.sdk.mapview.datasource").

[PolygonTileSource](sdk-for-android-explore-api-reference-latestpolygontilesource "interface in com.here.sdk.mapview.datasource")

A source of geodetic polygon tiles.

[PolygonTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpolygontilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")

Result handler of a load tile request.

[RasterDataSource](sdk-for-android-explore-api-reference-latestrasterdatasource "class in com.here.sdk.mapview.datasource")

Data source to load map layers using a raster image format (jpg, png).

[RasterDataSourceConfiguration](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")

Called on the main thread after `fromJsonFile()` method finishes loading the configuration.

[RasterDataSourceConfiguration.Cache](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource")

Configuration of a local data cache.

[RasterDataSourceConfiguration.Provider](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource")

Configuration of a data provider.

[RasterDataSourceConfigurationUpdate](sdk-for-android-explore-api-reference-latestrasterdatasourceconfigurationupdate "class in com.here.sdk.mapview.datasource")

Configuration update for a RasterDataSource.

[RasterDataSourceError](sdk-for-android-explore-api-reference-latestrasterdatasourceerror "enum class in com.here.sdk.mapview.datasource")

Raster data source error codes.

[RasterDataSourceListener](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource")

Listener for RasterDataSource events.

[RasterTileSource](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource")

A source of raster tiles.

[RasterTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestrastertilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")

Result handler of a load tile request.

[TileGeoBoundsCalculator](sdk-for-android-explore-api-reference-latesttilegeoboundscalculator "class in com.here.sdk.mapview.datasource")

A calculator of geodetic bounds for tiles identified by keys generated in a particular tiling scheme ([`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")).

[TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")

Key of a data source tile.

[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

A source of tiles.

[TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource")

Tile data version.

[TileSource.Listener](sdk-for-android-explore-api-reference-latesttilesource-listener "interface in com.here.sdk.mapview.datasource")

Listener of [`TileSource`](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource") events.

[TileSource.LoadTileRequestHandle](sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource")

Handle of a load request.

[TileSource.TileMetadata](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata "class in com.here.sdk.mapview.datasource")

Tile metadata.

[TileUrlProviderCallback](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource")

Provides the URL as String for the given tile coordinates and storage level.

[TileUrlProviderFactory](sdk-for-android-explore-api-reference-latesttileurlproviderfactory "class in com.here.sdk.mapview.datasource")

Factory for generating a [`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") utilized in creating a tile URL.

[TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")

List of available data tiling schemes.
