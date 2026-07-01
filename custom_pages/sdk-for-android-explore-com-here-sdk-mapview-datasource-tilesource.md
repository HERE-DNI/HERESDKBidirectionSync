---
title: "TileSource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

All Known Subinterfaces:  
[`LineTileSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-linetilesource "interface in com.here.sdk.mapview.datasource"),
[`PointTileSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointtilesource "interface in com.here.sdk.mapview.datasource"),
[`PolygonTileSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource "interface in com.here.sdk.mapview.datasource"),
[`RasterTileSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">TileSource</span>

</div>

<div class="block">

A source of tiles. The implementations must be thread-safe. Note: This
is a beta release of this feature, so there could be a few bugs and
unexpected behavior. Related APIs may change for new releases without a
deprecation process.

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
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion"
  class="type-name-link"
  title="class in com.here.sdk.mapview.datasource"><code>TileSource.DataVersion</code></a></td>
  <td><div class="block">
  Tile data version.
  </div></td>
  </tr>
  <tr>
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener"
  class="type-name-link"
  title="interface in com.here.sdk.mapview.datasource"><code>TileSource.Listener</code></a></td>
  <td><div class="block">
  Listener of TileSource events.
  </div></td>
  </tr>
  <tr>
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle"
  class="type-name-link"
  title="interface in com.here.sdk.mapview.datasource"><code>TileSource.LoadTileRequestHandle</code></a></td>
  <td><div class="block">
  Handle of a load request.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata"
  class="type-name-link"
  title="class in com.here.sdk.mapview.datasource"><code>TileSource.TileMetadata</code></a></td>
  <td><div class="block">
  Tile metadata.
  </div></td>
  </tr>
  </tbody>
  </table>

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
  <td><code>void</code></td>
  <td><pre><code>addListener(TileSource.Listener listener)</code></pre></td>
  <td><div class="block">
  Adds a listener for receiving state notifications.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion"
  title="class in com.here.sdk.mapview.datasource"><code>TileSource.DataVersion</code></a></td>
  <td><pre><code>getDataVersion(TileKey tileKey)</code></pre></td>
  <td><div class="block">
  Gets the current data version of a tile.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a><code>&gt;</code></td>
  <td><pre><code>getStorageLevels()</code></pre></td>
  <td><div class="block">
  Gets the storage levels available for this data source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme"
  title="enum class in com.here.sdk.mapview.datasource"><code>TilingScheme</code></a></td>
  <td><pre><code>getTilingScheme()</code></pre></td>
  <td><div class="block">
  Gets the tiling scheme used by this source.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeListener(TileSource.Listener listener)</code></pre></td>
  <td><div class="block">
  Removes a listener from receiving state notifications.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="getDataVersion(com.here.sdk.mapview.datasource.TileKey)"
    class="section detail">

    ### getDataVersion

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TileSource.DataVersion](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">getDataVersion</span><span class="parameters">(@NonNull
    [TileKey](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource") tileKey)</span>

    </div>

    <div class="block">

    Gets the current data version of a tile.

    </div>

    Parameters:  
    `tileKey` -

    Key of the tile for which to retrieve the version.

    Returns:  
    Data version for a tile.

    </div>

  - <div id="addListener(com.here.sdk.mapview.datasource.TileSource.Listener)"
    class="section detail">

    ### addListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">addListener</span><span class="parameters">(@NonNull
    [TileSource.Listener](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener "interface in com.here.sdk.mapview.datasource") listener)</span>

    </div>

    <div class="block">

    Adds a listener for receiving state notifications.

    </div>

    Parameters:  
    `listener` -

    The listener

    </div>

  - <div id="removeListener(com.here.sdk.mapview.datasource.TileSource.Listener)"
    class="section detail">

    ### removeListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">removeListener</span><span class="parameters">(@NonNull
    [TileSource.Listener](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener "interface in com.here.sdk.mapview.datasource") listener)</span>

    </div>

    <div class="block">

    Removes a listener from receiving state notifications.

    </div>

    Parameters:  
    `listener` -

    Listener to be removed from receiving state notifications.

    </div>

  - <div id="getTilingScheme()" class="section detail">

    ### getTilingScheme

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">getTilingScheme</span>()

    </div>

    <div class="block">

    Gets the tiling scheme used by this source.

    </div>

    Returns:  
    The tiling scheme used by this source.

    </div>

  - <div id="getStorageLevels()" class="section detail">

    ### getStorageLevels

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>></span> <span class="element-name">getStorageLevels</span>()

    </div>

    <div class="block">

    Gets the storage levels available for this data source. Supported
    range \[0, 31\]. At least one level must be available for this to be
    used as a source of data.

    </div>

    Returns:  
    The storage levels available for this data source. Supported range
    \[0, 31\].

    </div>

  </div>

</div>

