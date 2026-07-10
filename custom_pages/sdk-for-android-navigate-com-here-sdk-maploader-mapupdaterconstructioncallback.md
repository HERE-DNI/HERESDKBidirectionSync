---
title: "MapUpdaterConstructionCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdaterconstructioncallback"
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

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">MapUpdaterConstructionCallback</span>

</div>

<div class="block">

A method which is called on the main thread when MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback) has been completed. Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread. When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.

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

      onMapUpdaterConstructe ( MapUpdater mapUpdater)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  A method which is called on the main thread when MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback) has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onMapUpdaterConstructe-com-here-sdk-maploader-MapUpdater" class="section detail">

    ### onMapUpdaterConstructe

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapUpdaterConstructe</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater" title="class in com.here.sdk.maploader">MapUpdater</a> mapUpdater)</span>

    </div>

    <div class="block">

    A method which is called on the main thread when MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback) has been completed. Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread. When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.

    </div>

    Parameters:  
    `mapUpdater` -

    Represents a constructed `MapUpdater` object.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

