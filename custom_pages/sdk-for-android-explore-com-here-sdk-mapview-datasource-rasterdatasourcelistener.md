---
title: "RasterDataSourceListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourcelistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">RasterDataSourceListener</span>

</div>

<div class="block">

Listener for RasterDataSource events.

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
  <td><pre><code>onRasterDataSourceError(RasterDataSourceError dataSourceError)</code></pre></td>
  <td><div class="block">
  The method to call on the listener when a data source error occurs.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onRasterDataSourceReady()</code></pre></td>
  <td><div class="block">
  The method to call on the listener when data source is ready to use.
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

  - <div id="onRasterDataSourceReady()" class="section detail">

    ### onRasterDataSourceReady

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRasterDataSourceReady</span>()

    </div>

    <div class="block">

    The method to call on the listener when data source is ready to use.

    </div>

    </div>

  - <div id="onRasterDataSourceError(com.here.sdk.mapview.datasource.RasterDataSourceError)"
    class="section detail">

    ### onRasterDataSourceError

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRasterDataSourceError</span><span class="parameters">(@NonNull
    [RasterDataSourceError](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceerror "enum class in com.here.sdk.mapview.datasource") dataSourceError)</span>

    </div>

    <div class="block">

    The method to call on the listener when a data source error occurs.

    </div>

    Parameters:  
    `dataSourceError` -

    a data source error.

    </div>

  </div>

</div>

