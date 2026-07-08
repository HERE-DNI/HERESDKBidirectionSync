---
title: "RasterDataSourceListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourcelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RasterDataSourceListener</span>

</div>

<div class="block">

Listener for RasterDataSource events.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onRasterDataSourceError ( RasterDataSourceError dataSourceError)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The method to call on the listener when a data source error occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onRasterDataSourceReady ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The method to call on the listener when data source is ready to use.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-onRasterDataSourceReady" class="section detail">

    ### onRasterDataSourceReady

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRasterDataSourceReady</span>()

    </div>

    <div class="block">

    The method to call on the listener when data source is ready to use.

    </div>

    </div>

  - <div id="sdk-for-android-explore-onRasterDataSourceError-com-here-sdk-mapview-datasource-RasterDataSourceError" class="section detail">

    ### onRasterDataSourceError

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRasterDataSourceError</span><wbr></wbr><span class="parameters">(@NonNull [RasterDataSourceError](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceerror "enum class in com.here.sdk.mapview.datasource") dataSourceError)</span>

    </div>

    <div class="block">

    The method to call on the listener when a data source error occurs.

    </div>

    Parameters:  
    `dataSourceError` -

    a data source error.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

