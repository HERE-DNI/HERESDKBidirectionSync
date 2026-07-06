---
title: "TileSource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

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
<div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

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

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion"
  class="type-name-link"
  title="class in com.here.sdk.mapview.datasource"><code>TileSource.DataVersion</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Tile data version.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static interface `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener"
  class="type-name-link"
  title="interface in com.here.sdk.mapview.datasource"><code>TileSource.Listener</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Listener of TileSource events.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle"
  class="type-name-link"
  title="interface in com.here.sdk.mapview.datasource"><code>TileSource.LoadTileRequestHandle</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Handle of a load request.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata"
  class="type-name-link"
  title="class in com.here.sdk.mapview.datasource"><code>TileSource.TileMetadata</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Tile metadata.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      addListener(TileSource.Listener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Adds a listener for receiving state notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TileSource.DataVersion`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getDataVersion(TileKey tileKey)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the current data version of a tile.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getStorageLevels()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the storage levels available for this data source.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TilingScheme`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTilingScheme()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the tiling scheme used by this source.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      removeListener(TileSource.Listener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Removes a listener from receiving state notifications.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-getDataVersion(com.here.sdk.mapview.datasource.TileKey)"
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
<div id="sdk-for-android-explore-addListener(com.here.sdk.mapview.datasource.TileSource.Listener)"
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
<div id="sdk-for-android-explore-removeListener(com.here.sdk.mapview.datasource.TileSource.Listener)"
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
<div id="sdk-for-android-explore-getTilingScheme()"
    class="section detail">

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
<div id="sdk-for-android-explore-getStorageLevels()"
    class="section detail">

    ### getStorageLevels

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
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

