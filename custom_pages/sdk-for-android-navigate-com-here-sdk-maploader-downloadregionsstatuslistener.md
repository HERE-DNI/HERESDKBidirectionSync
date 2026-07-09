---
title: "DownloadRegionsStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">DownloadRegionsStatusListener</span>

</div>

<div class="block">

Interface to get notified on status updates when downloading map regions.

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

      onDownloadRegionsComplete ( MapLoaderError error, List < RegionId > regions)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called after the download for all requested regions has been completed with success or failure.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onPause ( MapLoaderError error)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when download is paused.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onProgress ( RegionId region,
       int percentage)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called multiple times to indicate the download progress for each requested region individually.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onResume ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when paused download is resumed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onDownloadRegionsComplete-com-here-sdk-maploader-MapLoaderError-java-util-List" class="section detail">

    ### onDownloadRegionsComplete

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDownloadRegionsComplete</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a>\> regions)</span>

    </div>

    <div class="block">

    Called after the download for all requested regions has been completed with success or failure. In this callback, failure represents non-retryable error (eg. authentication failure because of invalid credentials and similars). Temporary failures (eg. network errors) are notified through onPause(com.here.sdk.maploader.MapLoaderError) and downloads will be in paused state so they can be resumed later. Invoked on the main thread.

    </div>

    Parameters:  
    `error` -

    Represents an error in case of a failure. It is `null` for an operation that succeeds.

    `regions` -

    Represents a list of regions which has been downloaded. It is `null` in case of an error.

    </div>

  - <div id="sdk-for-android-navigate-onProgress-com-here-sdk-maploader-RegionId-int" class="section detail">

    ### onProgress

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onProgress</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> region, int percentage)</span>

    </div>

    <div class="block">

    Called multiple times to indicate the download progress for each requested region individually. Invoked on the main thread.

    </div>

    Parameters:  
    `region` -

    Represents an id of region status update is related to.

    `percentage` -

    Represents a percentage of data which has been downloaded for particular region.

    </div>

  - <div id="sdk-for-android-navigate-onPause-com-here-sdk-maploader-MapLoaderError" class="section detail">

    ### onPause

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPause</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span>

    </div>

    <div class="block">

    Called when download is paused.

    </div>

    Parameters:  
    `error` -

    Populated when retryable error is a reason of a pause. It is 'null' when pause is called by the user.

    </div>

  - <div id="sdk-for-android-navigate-onResume" class="section detail">

    ### onResume

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onResume</span>()

    </div>

    <div class="block">

    Called when paused download is resumed.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

