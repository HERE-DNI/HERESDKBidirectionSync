---
title: "TileSource.LoadTileRequestHandle (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing interface:  
[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static interface
</span><span class="element-name type-name-label">TileSource.LoadTileRequestHandle</span>

</div>

<div class="block">

Handle of a load request.

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
  <td><pre><code>cancel()</code></pre></td>
  <td><div class="block">
  Cancels the associated load tile request.
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

  - <div id="cancel()" class="section detail">

    ### cancel

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">cancel</span>()

    </div>

    <div class="block">

    Cancels the associated load tile request. Upon cancellation, the
    corresponding result handler must be informed.

    </div>

    </div>

  </div>

</div>

