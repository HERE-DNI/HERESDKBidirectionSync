---
title: "RasterTileSource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Superinterfaces:  
[`TileSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RasterTileSource</span><span class="extends-implements"> extends [TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")</span>

</div>

<div class="block">

A source of raster tiles. The implementations must be thread-safe. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Interface

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource-loadresulthandler" class="type-name-link" title="interface in com.here.sdk.mapview.datasource"><code>RasterTileSource.LoadResultHandler</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Result handler of a load tile request.

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from interface com.here.sdk.mapview.datasource.[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

  [`TileSource.DataVersion`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion "class in com.here.sdk.mapview.datasource"), [`TileSource.Listener`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener "interface in com.here.sdk.mapview.datasource"), [`TileSource.LoadTileRequestHandle`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource"), [`TileSource.TileMetadata`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata "class in com.here.sdk.mapview.datasource")

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TileSource.LoadTileRequestHandle`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      loadTile ( TileKey tileKey, RasterTileSource.LoadResultHandler completionHandler)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Load data of a tile.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from interface com.here.sdk.mapview.datasource.[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

  [`addListener`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#addListener(com.here.sdk.mapview.datasource.TileSource.Listener)), [`getDataVersion`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#getDataVersion(com.here.sdk.mapview.datasource.TileKey)), [`getStorageLevels`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#getStorageLevels()), [`getTilingScheme`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#getTilingScheme()), [`removeListener`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#removeListener(com.here.sdk.mapview.datasource.TileSource.Listener))

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-loadTile-com-here-sdk-mapview-datasource-TileKey-com-here-sdk-mapview-datasource-RasterTileSource-LoadResultHandler" class="section detail">

    ### loadTile

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type">[TileSource.LoadTileRequestHandle](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource")</span> <span class="element-name">loadTile</span><wbr></wbr><span class="parameters">(@NonNull [TileKey](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource") tileKey, @NonNull [RasterTileSource.LoadResultHandler](sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource") completionHandler)</span>

    </div>

    <div class="block">

    Load data of a tile. Upon completion, the handler gets informed.

    </div>

    Parameters:  
    `tileKey` -

    Key of the tile to load data for.

    `completionHandler` -

    Load result handler.

    Returns:  
    A handle to the created load request.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

