---
title: "com.here.sdk.mapview.datasource Class Hierarchy (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpackage-tree"
hidden: false
---

# Hierarchy For Package com.here.sdk.mapview.datasource

Package Hierarchies:

- [All Packages](sdk-for-android-explore-api-reference-latestoverview-tree)

## Class Hierarchy

- java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
  - com.here.[NativeBase](sdk-for-android-explore-api-reference-latestnativebase)
    - com.here.sdk.mapview.datasource.[DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes) (implements com.here.sdk.mapview.datasource.[DataAttributesBase](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource"))
    - com.here.sdk.mapview.datasource.[DataAttributesAccessor](sdk-for-android-explore-api-reference-latestdataattributesaccessor) (implements com.here.sdk.mapview.datasource.[DataAttributesBase](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource"))
    - com.here.sdk.mapview.datasource.[DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder)
    - com.here.sdk.mapview.datasource.[DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue)
    - com.here.sdk.mapview.datasource.[LineData](sdk-for-android-explore-api-reference-latestlinedata)
    - com.here.sdk.mapview.datasource.[LineDataAccessor](sdk-for-android-explore-api-reference-latestlinedataaccessor)
    - com.here.sdk.mapview.datasource.[LineDataBuilder](sdk-for-android-explore-api-reference-latestlinedatabuilder)
    - com.here.sdk.mapview.datasource.[LineDataSource](sdk-for-android-explore-api-reference-latestlinedatasource)
    - com.here.sdk.mapview.datasource.[LineDataSourceBuilder](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder)
    - com.here.sdk.mapview.datasource.[LineTileDataSource](sdk-for-android-explore-api-reference-latestlinetiledatasource)
    - com.here.sdk.mapview.datasource.[PointData](sdk-for-android-explore-api-reference-latestpointdata)
    - com.here.sdk.mapview.datasource.[PointDataAccessor](sdk-for-android-explore-api-reference-latestpointdataaccessor)
    - com.here.sdk.mapview.datasource.[PointDataBuilder](sdk-for-android-explore-api-reference-latestpointdatabuilder)
    - com.here.sdk.mapview.datasource.[PointDataSource](sdk-for-android-explore-api-reference-latestpointdatasource)
    - com.here.sdk.mapview.datasource.[PointDataSourceBuilder](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder)
    - com.here.sdk.mapview.datasource.[PointTileDataSource](sdk-for-android-explore-api-reference-latestpointtiledatasource)
    - com.here.sdk.mapview.datasource.[PolygonData](sdk-for-android-explore-api-reference-latestpolygondata)
    - com.here.sdk.mapview.datasource.[PolygonDataAccessor](sdk-for-android-explore-api-reference-latestpolygondataaccessor)
    - com.here.sdk.mapview.datasource.[PolygonDataBuilder](sdk-for-android-explore-api-reference-latestpolygondatabuilder)
    - com.here.sdk.mapview.datasource.[PolygonDataSource](sdk-for-android-explore-api-reference-latestpolygondatasource)
    - com.here.sdk.mapview.datasource.[PolygonDataSourceBuilder](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder)
    - com.here.sdk.mapview.datasource.[PolygonTileDataSource](sdk-for-android-explore-api-reference-latestpolygontiledatasource)
    - com.here.sdk.mapview.datasource.[RasterDataSource](sdk-for-android-explore-api-reference-latestrasterdatasource)
    - com.here.sdk.mapview.datasource.[TileGeoBoundsCalculator](sdk-for-android-explore-api-reference-latesttilegeoboundscalculator)
    - com.here.sdk.mapview.datasource.[TileUrlProviderFactory](sdk-for-android-explore-api-reference-latesttileurlproviderfactory)
  - com.here.sdk.mapview.datasource.[RasterDataSourceConfiguration](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration)
  - com.here.sdk.mapview.datasource.[RasterDataSourceConfiguration.Cache](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache)
  - com.here.sdk.mapview.datasource.[RasterDataSourceConfiguration.Provider](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider)
  - com.here.sdk.mapview.datasource.[RasterDataSourceConfigurationUpdate](sdk-for-android-explore-api-reference-latestrasterdatasourceconfigurationupdate)
  - com.here.sdk.mapview.datasource.[TileKey](sdk-for-android-explore-api-reference-latesttilekey)
  - com.here.sdk.mapview.datasource.[TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion)
  - com.here.sdk.mapview.datasource.[TileSource.TileMetadata](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata)

## Interface Hierarchy

- com.here.sdk.mapview.datasource.[DataAttributesBase](sdk-for-android-explore-api-reference-latestdataattributesbase)
- com.here.sdk.mapview.datasource.[LineDataSource.LineDataProcessor](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor)
- com.here.sdk.mapview.datasource.[LineTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestlinetilesource-loadresulthandler)
- com.here.sdk.mapview.datasource.[PointDataSource.PointDataProcessor](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor)
- com.here.sdk.mapview.datasource.[PointTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpointtilesource-loadresulthandler)
- com.here.sdk.mapview.datasource.[PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor)
- com.here.sdk.mapview.datasource.[PolygonTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpolygontilesource-loadresulthandler)
- com.here.sdk.mapview.datasource.[RasterDataSourceListener](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener)
- com.here.sdk.mapview.datasource.[RasterTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestrastertilesource-loadresulthandler)
- com.here.sdk.mapview.datasource.[TileSource](sdk-for-android-explore-api-reference-latesttilesource)
  - com.here.sdk.mapview.datasource.[LineTileSource](sdk-for-android-explore-api-reference-latestlinetilesource)
  - com.here.sdk.mapview.datasource.[PointTileSource](sdk-for-android-explore-api-reference-latestpointtilesource)
  - com.here.sdk.mapview.datasource.[PolygonTileSource](sdk-for-android-explore-api-reference-latestpolygontilesource)
  - com.here.sdk.mapview.datasource.[RasterTileSource](sdk-for-android-explore-api-reference-latestrastertilesource)
- com.here.sdk.mapview.datasource.[TileSource.Listener](sdk-for-android-explore-api-reference-latesttilesource-listener)
- com.here.sdk.mapview.datasource.[TileSource.LoadTileRequestHandle](sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle)
- com.here.sdk.mapview.datasource.[TileUrlProviderCallback](sdk-for-android-explore-api-reference-latesttileurlprovidercallback)

## Enum Class Hierarchy

- java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
  - java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<E\> (implements java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)\<T\>, java.lang.constant.[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html), java.io.[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html))
    - com.here.sdk.mapview.datasource.[DataAttributeValue.ValueType](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype)
    - com.here.sdk.mapview.datasource.[RasterDataSourceError](sdk-for-android-explore-api-reference-latestrasterdatasourceerror)
    - com.here.sdk.mapview.datasource.[TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme)
