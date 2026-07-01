---
title: "PolygonTileSource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

All Superinterfaces:  
[`TileSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">PolygonTileSource</span><span class="extends-implements">
extends
[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")</span>

</div>

<div class="block">

A source of geodetic polygon tiles. Polygons provided by an
implementation must be clipped to the boundaries of the requested tile.
The implementations must be thread-safe. Note: This is a beta release of
this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Interface</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource-loadresulthandler"
  class="type-name-link"
  title="interface in com.here.sdk.mapview.datasource"><code>PolygonTileSource.LoadResultHandler</code></a></td>
  <td><div class="block">
  Result handler of a load tile request.
  </div></td>
  </tr>
  </tbody>
  </table>

  <div class="inherited-list">

  [`TileSource.DataVersion`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion "class in com.here.sdk.mapview.datasource")`, `[`TileSource.Listener`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener "interface in com.here.sdk.mapview.datasource")`, `[`TileSource.LoadTileRequestHandle`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource")`, `[`TileSource.TileMetadata`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata "class in com.here.sdk.mapview.datasource")

  </div>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle"
  title="interface in com.here.sdk.mapview.datasource"><code>TileSource.LoadTileRequestHandle</code></a></td>
  <td><pre><code>loadTile(TileKey tileKey,
   PolygonTileSource.LoadResultHandler completionHandler)</code></pre></td>
  <td><div class="block">
  Load data of a tile.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from interface com.here.sdk.mapview.datasource.[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

  [`addListener`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#addListener(com.here.sdk.mapview.datasource.TileSource.Listener))`, `[`getDataVersion`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#getDataVersion(com.here.sdk.mapview.datasource.TileKey))`, `[`getStorageLevels`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#getStorageLevels())`, `[`getTilingScheme`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#getTilingScheme())`, `[`removeListener`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource#removeListener(com.here.sdk.mapview.datasource.TileSource.Listener))

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="loadTile(com.here.sdk.mapview.datasource.TileKey,com.here.sdk.mapview.datasource.PolygonTileSource.LoadResultHandler)"
    class="section detail">

    ### loadTile

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type">[TileSource.LoadTileRequestHandle](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource")</span> <span class="element-name">loadTile</span><span class="parameters">(@NonNull
    [TileKey](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource") tileKey,
    @NonNull
    [PolygonTileSource.LoadResultHandler](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource") completionHandler)</span>

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

</div>

