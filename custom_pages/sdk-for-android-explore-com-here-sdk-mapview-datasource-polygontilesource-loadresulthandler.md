---
title: "PolygonTileSource.LoadResultHandler (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource-loadresulthandler"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing interface:  
[PolygonTileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygontilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static interface
</span><span class="element-name type-name-label">PolygonTileSource.LoadResultHandler</span>

</div>

<div class="block">

Result handler of a load tile request.

</div>

</div>

<div class="section summary">

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
  <td><pre><code>failed(TileKey tileKey)</code></pre></td>
  <td><div class="block">
  Called upon failed load tile request.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>loaded(TileKey tileKey,
   List&lt;PolygonData&gt; data,
   TileSource.TileMetadata metadata)</code></pre></td>
  <td><div class="block">
  Called upon successful load tile request.
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

  - <div id="loaded(com.here.sdk.mapview.datasource.TileKey,java.util.List,com.here.sdk.mapview.datasource.TileSource.TileMetadata)"
    class="section detail">

    ### loaded

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">loaded</span><span class="parameters">(@NonNull
    [TileKey](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource") tileKey,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PolygonData](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata "class in com.here.sdk.mapview.datasource")> data,
    @NonNull
    [TileSource.TileMetadata](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata "class in com.here.sdk.mapview.datasource") metadata)</span>

    </div>

    <div class="block">

    Called upon successful load tile request.

    </div>

    Parameters:  
    `tileKey` -

    Loaded tile key.

    `data` -

    Loaded tile data.

    `metadata` -

    Loaded tile metadata.

    </div>

  - <div id="failed(com.here.sdk.mapview.datasource.TileKey)"
    class="section detail">

    ### failed

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">failed</span><span class="parameters">(@NonNull
    [TileKey](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource") tileKey)</span>

    </div>

    <div class="block">

    Called upon failed load tile request.

    </div>

    Parameters:  
    `tileKey` -

    Failed tile key.

    </div>

  </div>

</div>

