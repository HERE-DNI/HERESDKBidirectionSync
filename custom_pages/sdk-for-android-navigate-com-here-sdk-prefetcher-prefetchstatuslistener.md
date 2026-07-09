---
title: "PrefetchStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-package-summary">com.here.sdk.prefetcher</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">PrefetchStatusListener</span>

</div>

<div class="block">

Interface to get notified on status updates when prefetching map data.

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

      onComplete ( MapLoaderError error)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called after the geo-corridor data downloads has been completed either with success or with error.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onProgress (int percentage)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called multiple times to indicate the update progress.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onProgress-int" class="section detail">

    ### onProgress

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onProgress</span><wbr></wbr><span class="parameters">(int percentage)</span>

    </div>

    <div class="block">

    Called multiple times to indicate the update progress. Invoked on the main thread.

    </div>

    Parameters:  
    `percentage` -

    Represents a percentage of corridor data which has been downloaded.

    </div>

  - <div id="sdk-for-android-navigate-onComplete-com-here-sdk-maploader-MapLoaderError" class="section detail">

    ### onComplete

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onComplete</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span>

    </div>

    <div class="block">

    Called after the geo-corridor data downloads has been completed either with success or with error. Invoked on the main thread.

    </div>

    Parameters:  
    `error` -

    Represents an error in case of a failure. If an error occurs, to resume operation, please download geo-corridor again. It is `null` for an operation that succeeds.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

