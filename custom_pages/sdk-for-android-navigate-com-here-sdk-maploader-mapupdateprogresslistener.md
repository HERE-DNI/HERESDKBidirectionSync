---
title: "MapUpdateProgressListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdateprogresslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">MapUpdateProgressListener</span>

</div>

<div class="block">

Interface to get notified on status updates when updating map data, previously downloaded by MapDownloader .

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

  Called after the update process for all regions has been completed.

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

  Called when update is paused.

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

  Called multiple times to indicate the update progress.

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

  Called when a paused map update is resumed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onProgress-com-here-sdk-maploader-RegionId-int" class="section detail">

    ### onProgress

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onProgress</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> region, int percentage)</span>

    </div>

    <div class="block">

    Called multiple times to indicate the update progress. Invoked on the main thread.

    </div>

    Parameters:  
    `region` -

    Represents an id of region status update is related to.

    `percentage` -

    Represents a percentage of map data which has been updated.

    </div>

  - <div id="sdk-for-android-navigate-onPause-com-here-sdk-maploader-MapLoaderError" class="section detail">

    ### onPause

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPause</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span>

    </div>

    <div class="block">

    Called when update is paused. Invoked on the main thread.

    </div>

    Parameters:  
    `error` -

    Populated when a retryable error is the reason for a pause. A retryable error can happen, when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection. In general, the HERE SDK will try a few times, before the update is paused. This error value gives a hint on the reason for the necessary retry operation. A paused download can be resumed by the user at a later time. It is 'null' when

        MapUpdateTask.pause(boolean)

    was called by the user.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-onComplete-com-here-sdk-maploader-MapLoaderError" class="section detail">

    ### onComplete

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onComplete</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span>

    </div>

    <div class="block">

    Called after the update process for all regions has been completed. Invoked on the main thread.

    </div>

    Parameters:  
    `error` -

    Represents an error in case of a failure. If an error occurs, the operation cannot be resumed later. It is `null` for an operation that succeeds.

    </div>

  - <div id="sdk-for-android-navigate-onResume" class="section detail">

    ### onResume

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onResume</span>()

    </div>

    <div class="block">

    Called when a paused map update is resumed.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

