---
title: "MapDownloaderConstructionCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapdownloaderconstructioncallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">MapDownloaderConstructionCallback</span>

</div>

<div class="block">

A method which is called on the main thread when MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback) has been completed. The MapDownloader instance is created on a background thread to not block the calling thread. During construction an online connection is established to fetch configuration data for internal use. If no online connection is available, cached or default values will be used. This is only for internal reasons and has no effect on the operability of the resulting instance. When configuration data is available from the cache, construction can still take a reasonable amount of time. Applications should consider to show a loading indicator.

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

      onMapDownloaderConstructedCompleted ( MapDownloader mapDownloader)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  A method which is called on the main thread when MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback) has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onMapDownloaderConstructedCompleted-com-here-sdk-maploader-MapDownloader" class="section detail">

    ### onMapDownloaderConstructedCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapDownloaderConstructedCompleted</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader" title="class in com.here.sdk.maploader">MapDownloader</a> mapDownloader)</span>

    </div>

    <div class="block">

    A method which is called on the main thread when MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback) has been completed. The MapDownloader instance is created on a background thread to not block the calling thread. During construction an online connection is established to fetch configuration data for internal use. If no online connection is available, cached or default values will be used. This is only for internal reasons and has no effect on the operability of the resulting instance. When configuration data is available from the cache, construction can still take a reasonable amount of time. Applications should consider to show a loading indicator.

    </div>

    Parameters:  
    `mapDownloader` -

    Represents a constructed MapDownloader object.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

