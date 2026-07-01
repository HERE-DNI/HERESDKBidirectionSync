---
title: "com.here.sdk.mapview.datasource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary"
---

<div class="package-signature">

package
<span class="element-name">com.here.sdk.mapview.datasource</span>

</div>

<div class="section summary">

- <div id="related-package-summary">

  <div class="caption">

  Related Packages

  </div>

  | Package | Description |
  |----|----|
  | [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary) |   |

  </div>

- <div id="class-summary">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes

  </div>

  <div id="class-summary.tabpanel" aria-labelledby="class-summary-tab0"
  role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes"
  title="class in com.here.sdk.mapview.datasource">DataAttributes</a></td>
  <td><div class="block">
  Data attributes collection.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesaccessor"
  title="class in com.here.sdk.mapview.datasource">DataAttributesAccessor</a></td>
  <td><div class="block">
  Accessor used for manipulating data attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbase"
  title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></td>
  <td><div class="block">
  Interface for a collection of data attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
  title="class in com.here.sdk.mapview.datasource">DataAttributesBuilder</a></td>
  <td><div class="block">
  Data attributes collection builder.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue"
  title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a></td>
  <td><div class="block">
  Encapsulates a data attribute value.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue-valuetype"
  title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></td>
  <td><div class="block">
  Supported types of the data attribute values.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedata"
  title="class in com.here.sdk.mapview.datasource">LineData</a></td>
  <td><div class="block">
  Represents a geodetic line with custom attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedataaccessor"
  title="class in com.here.sdk.mapview.datasource">LineDataAccessor</a></td>
  <td><div class="block">
  Line data accessor used for manipulating polylines that are part of a
  LineDataSource.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatabuilder"
  title="class in com.here.sdk.mapview.datasource">LineDataBuilder</a></td>
  <td><div class="block">
  Builder of LineData instances.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasource"
  title="class in com.here.sdk.mapview.datasource">LineDataSource</a></td>
  <td><div class="block">
  Polyline data source allows the rendering engine access to the user
  provided polylines geometry and their attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasource-linedataprocessor"
  title="interface in com.here.sdk.mapview.datasource">LineDataSource.LineDataProcessor</a></td>
  <td><div class="block">
  Called for each line, allowing inspection, removal or update of
  coordinates and attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder"
  title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></td>
  <td><div class="block">
  Builder of lines data source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linetiledatasource"
  title="class in com.here.sdk.mapview.datasource">LineTileDataSource</a></td>
  <td><div class="block">
  Line tile data source allows the rendering engine access to user managed
  data sets of geodetic lines and their attributes through a
  LineTileSource .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linetilesource"
  title="interface in com.here.sdk.mapview.datasource">LineTileSource</a></td>
  <td><div class="block">
  A source of geodetic line tiles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linetilesource-loadresulthandler"
  title="interface in com.here.sdk.mapview.datasource">LineTileSource.LoadResultHandler</a></td>
  <td><div class="block">
  Result handler of a load tile request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata"
  title="class in com.here.sdk.mapview.datasource">PointData</a></td>
  <td><div class="block">
  Represents a geodetic point with custom attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdataaccessor"
  title="class in com.here.sdk.mapview.datasource">PointDataAccessor</a></td>
  <td><div class="block">
  Point data accessor used for manipulating points that are part of a
  PointDataSource.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder"
  title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></td>
  <td><div class="block">
  Builder of PointData instances.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource"
  title="class in com.here.sdk.mapview.datasource">PointDataSource</a></td>
  <td><div class="block">
  Point data source allows the rendering engine access to the user
  provided geographical locations and their attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor"
  title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a></td>
  <td><div class="block">
  Called for each point, allowing inspection, removal or update of
  coordinates and attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasourcebuilder"
  title="class in com.here.sdk.mapview.datasource">PointDataSourceBuilder</a></td>
  <td><div class="block">
  Builder of points data source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointtiledatasource"
  title="class in com.here.sdk.mapview.datasource">PointTileDataSource</a></td>
  <td><div class="block">
  Point tile data source allows the rendering engine access to user
  managed data sets of geographical locations and their attributes through
  a PointTileSource .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointtilesource"
  title="interface in com.here.sdk.mapview.datasource">PointTileSource</a></td>
  <td><div class="block">
  A source of geodetic point tiles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointtilesource-loadresulthandler"
  title="interface in com.here.sdk.mapview.datasource">PointTileSource.LoadResultHandler</a></td>
  <td><div class="block">
  Result handler of a load tile request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata"
  title="class in com.here.sdk.mapview.datasource">PolygonData</a></td>
  <td><div class="block">
  Represents a geodetic polygon with custom attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondataaccessor"
  title="class in com.here.sdk.mapview.datasource">PolygonDataAccessor</a></td>
  <td><div class="block">
  Polygon data accessor used for manipulating polygons that are part of a
  PolygonDataSource.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatabuilder"
  title="class in com.here.sdk.mapview.datasource">PolygonDataBuilder</a></td>
  <td><div class="block">
  Builder of PolygonData instances.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource"
  title="class in com.here.sdk.mapview.datasource">PolygonDataSource</a></td>
  <td><div class="block">
  Polygon data source allows the rendering engine access to the user
  provided polygons geometry and their attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource-polygondataprocessor"
  title="interface in com.here.sdk.mapview.datasource">PolygonDataSource.PolygonDataProcessor</a></td>
  <td><div class="block">
  Called for each polygon, allowing inspection, removal or update of
  coordinates and attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder"
  title="class in com.here.sdk.mapview.datasource">PolygonDataSourceBuilder</a></td>
  <td><div class="block">
  Builder of the polygons data source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontiledatasource"
  title="class in com.here.sdk.mapview.datasource">PolygonTileDataSource</a></td>
  <td><div class="block">
  Polygon tile data source allows the rendering engine access to user
  managed data sets of geodetic polygons and their attributes through a
  PolygonTileSource .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource"
  title="interface in com.here.sdk.mapview.datasource">PolygonTileSource</a></td>
  <td><div class="block">
  A source of geodetic polygon tiles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource-loadresulthandler"
  title="interface in com.here.sdk.mapview.datasource">PolygonTileSource.LoadResultHandler</a></td>
  <td><div class="block">
  Result handler of a load tile request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasource"
  title="class in com.here.sdk.mapview.datasource">RasterDataSource</a></td>
  <td><div class="block">
  Data source to load map layers using a raster image format (jpg, png).
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration"
  title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a></td>
  <td><div class="block">
  Called on the main thread after fromJsonFile() method finishes loading
  the configuration.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache"
  title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a></td>
  <td><div class="block">
  Configuration of a local data cache.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider"
  title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a></td>
  <td><div class="block">
  Configuration of a data provider.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate"
  title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfigurationUpdate</a></td>
  <td><div class="block">
  Configuration update for a RasterDataSource.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceerror"
  title="enum class in com.here.sdk.mapview.datasource">RasterDataSourceError</a></td>
  <td><div class="block">
  Raster data source error codes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourcelistener"
  title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a></td>
  <td><div class="block">
  Listener for RasterDataSource events.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource"
  title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a></td>
  <td><div class="block">
  A source of raster tiles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource-loadresulthandler"
  title="interface in com.here.sdk.mapview.datasource">RasterTileSource.LoadResultHandler</a></td>
  <td><div class="block">
  Result handler of a load tile request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilegeoboundscalculator"
  title="class in com.here.sdk.mapview.datasource">TileGeoBoundsCalculator</a></td>
  <td><div class="block">
  A calculator of geodetic bounds for tiles identified by keys generated
  in a particular tiling scheme ( TilingScheme ).
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey"
  title="class in com.here.sdk.mapview.datasource">TileKey</a></td>
  <td><div class="block">
  Key of a data source tile.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource"
  title="interface in com.here.sdk.mapview.datasource">TileSource</a></td>
  <td><div class="block">
  A source of tiles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion"
  title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a></td>
  <td><div class="block">
  Tile data version.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener"
  title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a></td>
  <td><div class="block">
  Listener of TileSource events.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle"
  title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a></td>
  <td><div class="block">
  Handle of a load request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata"
  title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a></td>
  <td><div class="block">
  Tile metadata.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback"
  title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a></td>
  <td><div class="block">
  Provides the URL as String for the given tile coordinates and storage
  level.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlproviderfactory"
  title="class in com.here.sdk.mapview.datasource">TileUrlProviderFactory</a></td>
  <td><div class="block">
  Factory for generating a TileUrlProviderCallback utilized in creating a
  tile URL.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme"
  title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></td>
  <td><div class="block">
  List of available data tiling schemes.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

</div>

