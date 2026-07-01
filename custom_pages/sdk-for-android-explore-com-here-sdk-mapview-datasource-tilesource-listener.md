---
title: "TileSource.Listener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-listener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing interface:  
[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static interface
</span><span class="element-name type-name-label">TileSource.Listener</span>

</div>

<div class="block">

Listener of TileSource events.

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
  <td><pre><code>onDataVersionChanged(TileSource.DataVersion dataVersion)</code></pre></td>
  <td><div class="block">
  Called when tile source data version changes.
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

  - <div id="onDataVersionChanged(com.here.sdk.mapview.datasource.TileSource.DataVersion)"
    class="section detail">

    ### onDataVersionChanged

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDataVersionChanged</span><span class="parameters">(@NonNull
    [TileSource.DataVersion](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion "class in com.here.sdk.mapview.datasource") dataVersion)</span>

    </div>

    <div class="block">

    Called when tile source data version changes.

    </div>

    Parameters:  
    `dataVersion` -

    New tile data version.

    </div>

  </div>

</div>

