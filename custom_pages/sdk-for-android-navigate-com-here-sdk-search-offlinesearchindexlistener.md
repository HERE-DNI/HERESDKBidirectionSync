---
title: "OfflineSearchIndexListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-offlinesearchindexlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-search-package-summary">com.here.sdk.search</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">OfflineSearchIndexListener</span>

</div>

<div class="block">

Interface to get updates about progress of creating persistent map index. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      onComplete ( OfflineSearchIndex.Error error)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called after index creation or deletion has been completed.

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

  Called multiple times to indicate the progress of index creation or deletion.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onStarted ( OfflineSearchIndex.Operation operation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called each time that the indexing has started.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onStarted-com-here-sdk-search-OfflineSearchIndex-Operation" class="section detail">

    ### onStarted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onStarted</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindex-operation" title="enum class in com.here.sdk.search">OfflineSearchIndex.Operation</a> operation)</span>

    </div>

    <div class="block">

    Called each time that the indexing has started. It is triggered by changes to persistent map or by calling OfflineSearchEngine.setIndexOptions . If a valid index was previously created for the installed regions, no additional indexing is performed, so no notifications are sent. In this context, a valid index is the one that contains data for the exact versions of the installed map regions. When any of them is updated or new regions are downloaded or deleted, the index becomes invalid and is automatically rebuilt, as long as indexing has been enabled previously. Invoked on the main thread.

    </div>

    Parameters:  
    `operation` -

    Shows whether the index is being created or removed.

    </div>

  - <div id="sdk-for-android-navigate-onProgress-int" class="section detail">

    ### onProgress

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onProgress</span><wbr></wbr><span class="parameters">(int percentage)</span>

    </div>

    <div class="block">

    Called multiple times to indicate the progress of index creation or deletion. Invoked on the main thread.

    </div>

    Parameters:  
    `percentage` -

    Represents a percentage of work done.

    </div>

  - <div id="sdk-for-android-navigate-onComplete-com-here-sdk-search-OfflineSearchIndex-Error" class="section detail">

    ### onComplete

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onComplete</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindex-error" title="enum class in com.here.sdk.search">OfflineSearchIndex.Error</a> error)</span>

    </div>

    <div class="block">

    Called after index creation or deletion has been completed. Invoked on the main thread.

    </div>

    Parameters:  
    `error` -

    Represents an error in case of a failure. It is `null` for an operation that succeeds.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

