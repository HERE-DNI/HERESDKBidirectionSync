---
title: "mapview.datasource library"
slug: "sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- mapview.datasource-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/mapview.datasource-library.html#classes">Classes</a></li>
<li><a href="mapview.datasource/DataAttributes-class.html">DataAttributes</a></li>
<li><a href="mapview.datasource/DataAttributesAccessor-class.html">DataAttributesAccessor</a></li>
<li><a href="mapview.datasource/DataAttributesBase-class.html">DataAttributesBase</a></li>
<li><a href="mapview.datasource/DataAttributesBuilder-class.html">DataAttributesBuilder</a></li>
<li><a href="mapview.datasource/DataAttributeValue-class.html">DataAttributeValue</a></li>
<li><a href="mapview.datasource/LineData-class.html">LineData</a></li>
<li><a href="mapview.datasource/LineDataAccessor-class.html">LineDataAccessor</a></li>
<li><a href="mapview.datasource/LineDataBuilder-class.html">LineDataBuilder</a></li>
<li><a href="mapview.datasource/LineDataSource-class.html">LineDataSource</a></li>
<li><a href="mapview.datasource/LineDataSourceBuilder-class.html">LineDataSourceBuilder</a></li>
<li><a href="mapview.datasource/LineTileDataSource-class.html">LineTileDataSource</a></li>
<li><a href="mapview.datasource/LineTileSource-class.html">LineTileSource</a></li>
<li><a href="mapview.datasource/LineTileSourceLoadResultHandler-class.html">LineTileSourceLoadResultHandler</a></li>
<li><a href="mapview.datasource/PointData-class.html">PointData</a></li>
<li><a href="mapview.datasource/PointDataAccessor-class.html">PointDataAccessor</a></li>
<li><a href="mapview.datasource/PointDataBuilder-class.html">PointDataBuilder</a></li>
<li><a href="mapview.datasource/PointDataSource-class.html">PointDataSource</a></li>
<li><a href="mapview.datasource/PointDataSourceBuilder-class.html">PointDataSourceBuilder</a></li>
<li><a href="mapview.datasource/PointTileDataSource-class.html">PointTileDataSource</a></li>
<li><a href="mapview.datasource/PointTileSource-class.html">PointTileSource</a></li>
<li><a href="mapview.datasource/PointTileSourceLoadResultHandler-class.html">PointTileSourceLoadResultHandler</a></li>
<li><a href="mapview.datasource/PolygonData-class.html">PolygonData</a></li>
<li><a href="mapview.datasource/PolygonDataAccessor-class.html">PolygonDataAccessor</a></li>
<li><a href="mapview.datasource/PolygonDataBuilder-class.html">PolygonDataBuilder</a></li>
<li><a href="mapview.datasource/PolygonDataSource-class.html">PolygonDataSource</a></li>
<li><a href="mapview.datasource/PolygonDataSourceBuilder-class.html">PolygonDataSourceBuilder</a></li>
<li><a href="mapview.datasource/PolygonTileDataSource-class.html">PolygonTileDataSource</a></li>
<li><a href="mapview.datasource/PolygonTileSource-class.html">PolygonTileSource</a></li>
<li><a href="mapview.datasource/PolygonTileSourceLoadResultHandler-class.html">PolygonTileSourceLoadResultHandler</a></li>
<li><a href="mapview.datasource/RasterDataSource-class.html">RasterDataSource</a></li>
<li><a href="mapview.datasource/RasterDataSourceCacheConfiguration-class.html">RasterDataSourceCacheConfiguration</a></li>
<li><a href="mapview.datasource/RasterDataSourceConfiguration-class.html">RasterDataSourceConfiguration</a></li>
<li><a href="mapview.datasource/RasterDataSourceConfigurationUpdate-class.html">RasterDataSourceConfigurationUpdate</a></li>
<li><a href="mapview.datasource/RasterDataSourceListener-class.html">RasterDataSourceListener</a></li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration-class.html">RasterDataSourceProviderConfiguration</a></li>
<li><a href="mapview.datasource/RasterTileSource-class.html">RasterTileSource</a></li>
<li><a href="mapview.datasource/RasterTileSourceLoadResultHandler-class.html">RasterTileSourceLoadResultHandler</a></li>
<li><a href="mapview.datasource/TileGeoBoundsCalculator-class.html">TileGeoBoundsCalculator</a></li>
<li><a href="mapview.datasource/TileKey-class.html">TileKey</a></li>
<li><a href="mapview.datasource/TileSource-class.html">TileSource</a></li>
<li><a href="mapview.datasource/TileSourceDataVersion-class.html">TileSourceDataVersion</a></li>
<li><a href="mapview.datasource/TileSourceListener-class.html">TileSourceListener</a></li>
<li><a href="mapview.datasource/TileSourceLoadTileRequestHandle-class.html">TileSourceLoadTileRequestHandle</a></li>
<li><a href="mapview.datasource/TileSourceTileMetadata-class.html">TileSourceTileMetadata</a></li>
<li><a href="mapview.datasource/TileUrlProviderFactory-class.html">TileUrlProviderFactory</a></li>
<li class="section-title"><a href="mapview.datasource/mapview.datasource-library.html#enums">Enums</a></li>
<li><a href="mapview.datasource/DataAttributeValueValueType.html">DataAttributeValueValueType</a></li>
<li><a href="mapview.datasource/RasterDataSourceError.html">RasterDataSourceError</a></li>
<li><a href="mapview.datasource/TilingScheme.html">TilingScheme</a></li>
<li class="section-title"><a href="mapview.datasource/mapview.datasource-library.html#typedefs">Typedefs</a></li>
<li><a href="mapview.datasource/LineDataSourceLineDataProcessor.html">LineDataSourceLineDataProcessor</a></li>
<li><a href="mapview.datasource/PointDataSourcePointDataProcessor.html">PointDataSourcePointDataProcessor</a></li>
<li><a href="mapview.datasource/PolygonDataSourcePolygonDataProcessor.html">PolygonDataSourcePolygonDataProcessor</a></li>
<li><a href="mapview.datasource/TileUrlProviderCallback.html">TileUrlProviderCallback</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li class="self-crumb">mapview.datasource.dart</li>
</ol>
<div class="self-name">mapview.datasource</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="" data-below-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>mapview.datasource library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="DataAttributes">
/sdk-for-flutter-explore-mapview-datasource-dataattributes-class
</dt>
<dd>
  Data attributes collection.
</dd>
<dt id="DataAttributesAccessor">
/sdk-for-flutter-explore-mapview-datasource-dataattributesaccessor-class
</dt>
<dd>
  Accessor used for manipulating data attributes.
</dd>
<dt id="DataAttributesBase">
/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-class
</dt>
<dd>
  Interface for a collection of data attributes.
</dd>
<dt id="DataAttributesBuilder">
/sdk-for-flutter-explore-mapview-datasource-dataattributesbuilder-class
</dt>
<dd>
  Data attributes collection builder.
</dd>
<dt id="DataAttributeValue">
/sdk-for-flutter-explore-mapview-datasource-dataattributevalue-class
</dt>
<dd>
  Encapsulates a data attribute value.
</dd>
<dt id="LineData">
/sdk-for-flutter-explore-mapview-datasource-linedata-class
</dt>
<dd>
  Represents a geodetic line with custom attributes.
</dd>
<dt id="LineDataAccessor">
/sdk-for-flutter-explore-mapview-datasource-linedataaccessor-class
</dt>
<dd>
  Line data accessor used for manipulating polylines that are part of a LineDataSource.
</dd>
<dt id="LineDataBuilder">
/sdk-for-flutter-explore-mapview-datasource-linedatabuilder-class
</dt>
<dd>
  Builder of /sdk-for-flutter-explore-mapview-datasource-linedata-class instances.
</dd>
<dt id="LineDataSource">
/sdk-for-flutter-explore-mapview-datasource-linedatasource-class
</dt>
<dd>
  Polyline data source allows the rendering engine access to the user provided
polylines geometry and their attributes.
</dd>
<dt id="LineDataSourceBuilder">
/sdk-for-flutter-explore-mapview-datasource-linedatasourcebuilder-class
</dt>
<dd>
  Builder of lines data source.
</dd>
<dt id="LineTileDataSource">
/sdk-for-flutter-explore-mapview-datasource-linetiledatasource-class
</dt>
<dd>
  Line tile data source allows the rendering engine access to user managed data sets of
geodetic lines and their attributes through a /sdk-for-flutter-explore-mapview-datasource-linetilesource-class.
</dd>
<dt id="LineTileSource">
/sdk-for-flutter-explore-mapview-datasource-linetilesource-class
</dt>
<dd>
  A source of geodetic line tiles.
</dd>
<dt id="LineTileSourceLoadResultHandler">
/sdk-for-flutter-explore-mapview-datasource-linetilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="PointData">
/sdk-for-flutter-explore-mapview-datasource-pointdata-class
</dt>
<dd>
  Represents a geodetic point with custom attributes.
</dd>
<dt id="PointDataAccessor">
/sdk-for-flutter-explore-mapview-datasource-pointdataaccessor-class
</dt>
<dd>
  Point data accessor used for manipulating points that are part of a PointDataSource.
</dd>
<dt id="PointDataBuilder">
/sdk-for-flutter-explore-mapview-datasource-pointdatabuilder-class
</dt>
<dd>
  Builder of /sdk-for-flutter-explore-mapview-datasource-pointdata-class instances.
</dd>
<dt id="PointDataSource">
/sdk-for-flutter-explore-mapview-datasource-pointdatasource-class
</dt>
<dd>
  Point data source allows the rendering engine access to the user provided
geographical locations and their attributes.
</dd>
<dt id="PointDataSourceBuilder">
/sdk-for-flutter-explore-mapview-datasource-pointdatasourcebuilder-class
</dt>
<dd>
  Builder of points data source.
</dd>
<dt id="PointTileDataSource">
/sdk-for-flutter-explore-mapview-datasource-pointtiledatasource-class
</dt>
<dd>
  Point tile data source allows the rendering engine access to user managed data sets of
geographical locations and their attributes through a /sdk-for-flutter-explore-mapview-datasource-pointtilesource-class.
</dd>
<dt id="PointTileSource">
/sdk-for-flutter-explore-mapview-datasource-pointtilesource-class
</dt>
<dd>
  A source of geodetic point tiles.
</dd>
<dt id="PointTileSourceLoadResultHandler">
/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="PolygonData">
/sdk-for-flutter-explore-mapview-datasource-polygondata-class
</dt>
<dd>
  Represents a geodetic polygon with custom attributes.
</dd>
<dt id="PolygonDataAccessor">
/sdk-for-flutter-explore-mapview-datasource-polygondataaccessor-class
</dt>
<dd>
  Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.
</dd>
<dt id="PolygonDataBuilder">
/sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-class
</dt>
<dd>
  Builder of /sdk-for-flutter-explore-mapview-datasource-polygondata-class instances.
</dd>
<dt id="PolygonDataSource">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-class
</dt>
<dd>
  Polygon data source allows the rendering engine access to the user provided
polygons geometry and their attributes.
</dd>
<dt id="PolygonDataSourceBuilder">
/sdk-for-flutter-explore-mapview-datasource-polygondatasourcebuilder-class
</dt>
<dd>
  Builder of the polygons data source.
</dd>
<dt id="PolygonTileDataSource">
/sdk-for-flutter-explore-mapview-datasource-polygontiledatasource-class
</dt>
<dd>
  Polygon tile data source allows the rendering engine access to user managed data sets of
geodetic polygons and their attributes through a /sdk-for-flutter-explore-mapview-datasource-polygontilesource-class.
</dd>
<dt id="PolygonTileSource">
/sdk-for-flutter-explore-mapview-datasource-polygontilesource-class
</dt>
<dd>
  A source of geodetic polygon tiles.
</dd>
<dt id="PolygonTileSourceLoadResultHandler">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="RasterDataSource">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-class
</dt>
<dd>
  Data source to load map layers using a raster image format (jpg, png).
</dd>
<dt id="RasterDataSourceCacheConfiguration">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class
</dt>
<dd>
  Configuration of a local data cache.
</dd>
<dt id="RasterDataSourceConfiguration">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-class
</dt>
<dd>
  Called on the main thread after <code>fromJsonFile()</code> method finishes loading
the configuration.
</dd>
<dt id="RasterDataSourceConfigurationUpdate">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfigurationupdate-class
</dt>
<dd>
  Configuration update for a RasterDataSource.
</dd>
<dt id="RasterDataSourceListener">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class
</dt>
<dd>
  Listener for RasterDataSource events.
</dd>
<dt id="RasterDataSourceProviderConfiguration">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class
</dt>
<dd>
  Configuration of a data provider.
</dd>
<dt id="RasterTileSource">
/sdk-for-flutter-explore-mapview-datasource-rastertilesource-class
</dt>
<dd>
  A source of raster tiles.
</dd>
<dt id="RasterTileSourceLoadResultHandler">
/sdk-for-flutter-explore-mapview-datasource-rastertilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="TileGeoBoundsCalculator">
/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-class
</dt>
<dd>
  A calculator of geodetic bounds for tiles identified by keys generated
in a particular tiling scheme (/sdk-for-flutter-explore-mapview-datasource-tilingscheme).
</dd>
<dt id="TileKey">
/sdk-for-flutter-explore-mapview-datasource-tilekey-class
</dt>
<dd>
  Key of a data source tile.
</dd>
<dt id="TileSource">
/sdk-for-flutter-explore-mapview-datasource-tilesource-class
</dt>
<dd>
  A source of tiles.
</dd>
<dt id="TileSourceDataVersion">
/sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class
</dt>
<dd>
  Tile data version.
</dd>
<dt id="TileSourceListener">
/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class
</dt>
<dd>
  Listener of /sdk-for-flutter-explore-mapview-datasource-tilesource-class events.
</dd>
<dt id="TileSourceLoadTileRequestHandle">
/sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class
</dt>
<dd>
  Handle of a load request.
</dd>
<dt id="TileSourceTileMetadata">
/sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class
</dt>
<dd>
  Tile metadata.
</dd>
<dt id="TileUrlProviderFactory">
/sdk-for-flutter-explore-mapview-datasource-tileurlproviderfactory-class
</dt>
<dd>
  Factory for generating a /sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback utilized in creating a tile URL.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="DataAttributeValueValueType">
/sdk-for-flutter-explore-mapview-datasource-dataattributevaluevaluetype
</dt>
<dd>
  Supported types of the data attribute values.
</dd>
<dt id="RasterDataSourceError">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceerror
</dt>
<dd>
  Raster data source error codes.
</dd>
<dt id="TilingScheme">
/sdk-for-flutter-explore-mapview-datasource-tilingscheme
</dt>
<dd>
  List of available data tiling schemes.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="LineDataSourceLineDataProcessor">
/sdk-for-flutter-explore-mapview-datasource-linedatasourcelinedataprocessor
= bool Function(/sdk-for-flutter-explore-mapview-datasource-linedataaccessor-class lineAccessor)

</dt>
<dd>
    Called for each line, allowing inspection, removal or update of coordinates and attributes.
    

  </dd>
<dt class="callable" id="PointDataSourcePointDataProcessor">
/sdk-for-flutter-explore-mapview-datasource-pointdatasourcepointdataprocessor
= bool Function(/sdk-for-flutter-explore-mapview-datasource-pointdataaccessor-class pointAccessor)

</dt>
<dd>
    Called for each point, allowing inspection, removal or update of coordinates and attributes.
    

  </dd>
<dt class="callable" id="PolygonDataSourcePolygonDataProcessor">
/sdk-for-flutter-explore-mapview-datasource-polygondatasourcepolygondataprocessor
= bool Function(/sdk-for-flutter-explore-mapview-datasource-polygondataaccessor-class polygonAccessor)

</dt>
<dd>
    Called for each polygon, allowing inspection, removal or update of coordinates and attributes.
    

  </dd>
<dt class="callable" id="TileUrlProviderCallback">
/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback
= String Function(int x, int y, int level)

</dt>
<dd>
    Provides the URL as String for the given tile coordinates and storage level.
    

  </dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li class="self-crumb">mapview.datasource.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-explore-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-explore-ev-ev-library</li>
<li>/sdk-for-flutter-explore-gestures-gestures-library</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-transport-transport-library</li>
</ol>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
<h5>mapview.datasource library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
