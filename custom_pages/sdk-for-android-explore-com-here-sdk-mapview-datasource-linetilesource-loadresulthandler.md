---
title: "LineTileSource.LoadResultHandler (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-linetilesource-loadresulthandler"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing interface:  
[LineTileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-linetilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static interface
</span><span class="element-name type-name-label">LineTileSource.LoadResultHandler</span>

</div>

<div class="block">

Result handler of a load tile request.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary"
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

      failed ( TileKey tileKey)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called upon failed load tile request.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      loaded ( TileKey tileKey, List < LineData > data, TileSource.TileMetadata metadata)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called upon successful load tile request.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-loaded-com-here-sdk-mapview-datasource-TileKey-java-util-List-com-here-sdk-mapview-datasource-TileSource-TileMetadata"
    class="section detail">

    ### loaded

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">loaded</span><span class="parameters">(@NonNull
    [TileKey](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource") tileKey,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[LineData](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedata "class in com.here.sdk.mapview.datasource")\> data,
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

  - <div id="sdk-for-android-explore-failed-com-here-sdk-mapview-datasource-TileKey"
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

