---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- mapview.datasource-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
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
/sdk-for-flutter-navigate-mapview-datasource-dataattributes-class
</dt>
<dd>
  Data attributes collection.
</dd>
<dt id="DataAttributesAccessor">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-class
</dt>
<dd>
  Accessor used for manipulating data attributes.
</dd>
<dt id="DataAttributesBase">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-class
</dt>
<dd>
  Interface for a collection of data attributes.
</dd>
<dt id="DataAttributesBuilder">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbuilder-class
</dt>
<dd>
  Data attributes collection builder.
</dd>
<dt id="DataAttributeValue">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class
</dt>
<dd>
  Encapsulates a data attribute value.
</dd>
<dt id="LineData">
/sdk-for-flutter-navigate-mapview-datasource-linedata-class
</dt>
<dd>
  Represents a geodetic line with custom attributes.
</dd>
<dt id="LineDataAccessor">
/sdk-for-flutter-navigate-mapview-datasource-linedataaccessor-class
</dt>
<dd>
  Line data accessor used for manipulating polylines that are part of a LineDataSource.
</dd>
<dt id="LineDataBuilder">
/sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-class
</dt>
<dd>
  Builder of /sdk-for-flutter-navigate-mapview-datasource-linedata-class instances.
</dd>
<dt id="LineDataSource">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-class
</dt>
<dd>
  Polyline data source allows the rendering engine access to the user provided
polylines geometry and their attributes.
</dd>
<dt id="LineDataSourceBuilder">
/sdk-for-flutter-navigate-mapview-datasource-linedatasourcebuilder-class
</dt>
<dd>
  Builder of lines data source.
</dd>
<dt id="LineTileDataSource">
/sdk-for-flutter-navigate-mapview-datasource-linetiledatasource-class
</dt>
<dd>
  Line tile data source allows the rendering engine access to user managed data sets of
geodetic lines and their attributes through a /sdk-for-flutter-navigate-mapview-datasource-linetilesource-class.
</dd>
<dt id="LineTileSource">
/sdk-for-flutter-navigate-mapview-datasource-linetilesource-class
</dt>
<dd>
  A source of geodetic line tiles.
</dd>
<dt id="LineTileSourceLoadResultHandler">
/sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="PointData">
/sdk-for-flutter-navigate-mapview-datasource-pointdata-class
</dt>
<dd>
  Represents a geodetic point with custom attributes.
</dd>
<dt id="PointDataAccessor">
/sdk-for-flutter-navigate-mapview-datasource-pointdataaccessor-class
</dt>
<dd>
  Point data accessor used for manipulating points that are part of a PointDataSource.
</dd>
<dt id="PointDataBuilder">
/sdk-for-flutter-navigate-mapview-datasource-pointdatabuilder-class
</dt>
<dd>
  Builder of /sdk-for-flutter-navigate-mapview-datasource-pointdata-class instances.
</dd>
<dt id="PointDataSource">
/sdk-for-flutter-navigate-mapview-datasource-pointdatasource-class
</dt>
<dd>
  Point data source allows the rendering engine access to the user provided
geographical locations and their attributes.
</dd>
<dt id="PointDataSourceBuilder">
/sdk-for-flutter-navigate-mapview-datasource-pointdatasourcebuilder-class
</dt>
<dd>
  Builder of points data source.
</dd>
<dt id="PointTileDataSource">
/sdk-for-flutter-navigate-mapview-datasource-pointtiledatasource-class
</dt>
<dd>
  Point tile data source allows the rendering engine access to user managed data sets of
geographical locations and their attributes through a /sdk-for-flutter-navigate-mapview-datasource-pointtilesource-class.
</dd>
<dt id="PointTileSource">
/sdk-for-flutter-navigate-mapview-datasource-pointtilesource-class
</dt>
<dd>
  A source of geodetic point tiles.
</dd>
<dt id="PointTileSourceLoadResultHandler">
/sdk-for-flutter-navigate-mapview-datasource-pointtilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="PolygonData">
/sdk-for-flutter-navigate-mapview-datasource-polygondata-class
</dt>
<dd>
  Represents a geodetic polygon with custom attributes.
</dd>
<dt id="PolygonDataAccessor">
/sdk-for-flutter-navigate-mapview-datasource-polygondataaccessor-class
</dt>
<dd>
  Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.
</dd>
<dt id="PolygonDataBuilder">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-class
</dt>
<dd>
  Builder of /sdk-for-flutter-navigate-mapview-datasource-polygondata-class instances.
</dd>
<dt id="PolygonDataSource">
/sdk-for-flutter-navigate-mapview-datasource-polygondatasource-class
</dt>
<dd>
  Polygon data source allows the rendering engine access to the user provided
polygons geometry and their attributes.
</dd>
<dt id="PolygonDataSourceBuilder">
/sdk-for-flutter-navigate-mapview-datasource-polygondatasourcebuilder-class
</dt>
<dd>
  Builder of the polygons data source.
</dd>
<dt id="PolygonTileDataSource">
/sdk-for-flutter-navigate-mapview-datasource-polygontiledatasource-class
</dt>
<dd>
  Polygon tile data source allows the rendering engine access to user managed data sets of
geodetic polygons and their attributes through a /sdk-for-flutter-navigate-mapview-datasource-polygontilesource-class.
</dd>
<dt id="PolygonTileSource">
/sdk-for-flutter-navigate-mapview-datasource-polygontilesource-class
</dt>
<dd>
  A source of geodetic polygon tiles.
</dd>
<dt id="PolygonTileSourceLoadResultHandler">
/sdk-for-flutter-navigate-mapview-datasource-polygontilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="RasterDataSource">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-class
</dt>
<dd>
  Data source to load map layers using a raster image format (jpg, png).
</dd>
<dt id="RasterDataSourceCacheConfiguration">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-class
</dt>
<dd>
  Configuration of a local data cache.
</dd>
<dt id="RasterDataSourceConfiguration">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfiguration-class
</dt>
<dd>
  Called on the main thread after <code>fromJsonFile()</code> method finishes loading
the configuration.
</dd>
<dt id="RasterDataSourceConfigurationUpdate">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfigurationupdate-class
</dt>
<dd>
  Configuration update for a RasterDataSource.
</dd>
<dt id="RasterDataSourceListener">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class
</dt>
<dd>
  Listener for RasterDataSource events.
</dd>
<dt id="RasterDataSourceProviderConfiguration">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceproviderconfiguration-class
</dt>
<dd>
  Configuration of a data provider.
</dd>
<dt id="RasterTileSource">
/sdk-for-flutter-navigate-mapview-datasource-rastertilesource-class
</dt>
<dd>
  A source of raster tiles.
</dd>
<dt id="RasterTileSourceLoadResultHandler">
/sdk-for-flutter-navigate-mapview-datasource-rastertilesourceloadresulthandler-class
</dt>
<dd>
  Result handler of a load tile request.
</dd>
<dt id="TileGeoBoundsCalculator">
/sdk-for-flutter-navigate-mapview-datasource-tilegeoboundscalculator-class
</dt>
<dd>
  A calculator of geodetic bounds for tiles identified by keys generated
in a particular tiling scheme (/sdk-for-flutter-navigate-mapview-datasource-tilingscheme).
</dd>
<dt id="TileKey">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-class
</dt>
<dd>
  Key of a data source tile.
</dd>
<dt id="TileSource">
/sdk-for-flutter-navigate-mapview-datasource-tilesource-class
</dt>
<dd>
  A source of tiles.
</dd>
<dt id="TileSourceDataVersion">
/sdk-for-flutter-navigate-mapview-datasource-tilesourcedataversion-class
</dt>
<dd>
  Tile data version.
</dd>
<dt id="TileSourceListener">
/sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-class
</dt>
<dd>
  Listener of /sdk-for-flutter-navigate-mapview-datasource-tilesource-class events.
</dd>
<dt id="TileSourceLoadTileRequestHandle">
/sdk-for-flutter-navigate-mapview-datasource-tilesourceloadtilerequesthandle-class
</dt>
<dd>
  Handle of a load request.
</dd>
<dt id="TileSourceTileMetadata">
/sdk-for-flutter-navigate-mapview-datasource-tilesourcetilemetadata-class
</dt>
<dd>
  Tile metadata.
</dd>
<dt id="TileUrlProviderFactory">
/sdk-for-flutter-navigate-mapview-datasource-tileurlproviderfactory-class
</dt>
<dd>
  Factory for generating a /sdk-for-flutter-navigate-mapview-datasource-tileurlprovidercallback utilized in creating a tile URL.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="DataAttributeValueValueType">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevaluevaluetype
</dt>
<dd>
  Supported types of the data attribute values.
</dd>
<dt id="RasterDataSourceError">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceerror
</dt>
<dd>
  Raster data source error codes.
</dd>
<dt id="TilingScheme">
/sdk-for-flutter-navigate-mapview-datasource-tilingscheme
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
/sdk-for-flutter-navigate-mapview-datasource-linedatasourcelinedataprocessor
= bool Function(/sdk-for-flutter-navigate-mapview-datasource-linedataaccessor-class lineAccessor)

</dt>
<dd>
    Called for each line, allowing inspection, removal or update of coordinates and attributes.
    

  </dd>
<dt class="callable" id="PointDataSourcePointDataProcessor">
/sdk-for-flutter-navigate-mapview-datasource-pointdatasourcepointdataprocessor
= bool Function(/sdk-for-flutter-navigate-mapview-datasource-pointdataaccessor-class pointAccessor)

</dt>
<dd>
    Called for each point, allowing inspection, removal or update of coordinates and attributes.
    

  </dd>
<dt class="callable" id="PolygonDataSourcePolygonDataProcessor">
/sdk-for-flutter-navigate-mapview-datasource-polygondatasourcepolygondataprocessor
= bool Function(/sdk-for-flutter-navigate-mapview-datasource-polygondataaccessor-class polygonAccessor)

</dt>
<dd>
    Called for each polygon, allowing inspection, removal or update of coordinates and attributes.
    

  </dd>
<dt class="callable" id="TileUrlProviderCallback">
/sdk-for-flutter-navigate-mapview-datasource-tileurlprovidercallback
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
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">mapview.datasource.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-navigate-animation-animation-library</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-navigate-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-ev-ev-library</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-style-venue-style-library</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
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



</div>
`
}</HTMLBlock>
