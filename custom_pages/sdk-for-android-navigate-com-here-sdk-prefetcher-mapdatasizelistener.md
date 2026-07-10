---
title: "MapDataSizeListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-mapdatasizelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-package-summary">com.here.sdk.prefetcher</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">MapDataSizeListener</span>

</div>

<div class="block">

Interface to get the result of map data size estimation.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

      onSizeEstimated ( MapLoaderError error, MapDataSize dataSize)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called after map data size estimation has been completed either with success or with error.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onSizeEstimated-com-here-sdk-maploader-MapLoaderError-com-here-sdk-prefetcher-MapDataSize" class="section detail">

    ### onSizeEstimated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSizeEstimated</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-mapdatasize" title="class in com.here.sdk.prefetcher">MapDataSize</a> dataSize)</span>

    </div>

    <div class="block">

    Called after map data size estimation has been completed either with success or with error. Invoked on the main thread.

    </div>

    Parameters:  
    `error` -

    Represents an error in case of a failure. If the operation was successful, `null` is returned.

    `dataSize` -

    Represents the map data size. In case of failure, `null` is returned.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

