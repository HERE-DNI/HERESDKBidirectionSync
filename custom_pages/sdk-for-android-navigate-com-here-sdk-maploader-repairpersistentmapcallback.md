---
title: "RepairPersistentMapCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-repairpersistentmapcallback"
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

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">RepairPersistentMapCallback</span>

</div>

<div class="block">

A method which is called on the main thread when MapDownloader.repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback) has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be null at the same time - or not null at the same time.

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

      onCompleted ( PersistentMapRepairError persistentMapRepairError)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  A method which is called on the main thread when MapDownloader.repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback) has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onCompleted-com-here-sdk-maploader-PersistentMapRepairError" class="section detail">

    ### onCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onCompleted</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a> persistentMapRepairError)</span>

    </div>

    <div class="block">

    A method which is called on the main thread when MapDownloader.repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback) has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be null at the same time - or not null at the same time.

    </div>

    Parameters:  
    `persistentMapRepairError` -

    Represents an error in case of a failure. It is `null` for an operation that succeeds.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

