---
title: "DownloadableRegionsCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-downloadableregionscallback"
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

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">DownloadableRegionsCallback</span>

</div>

<div class="block">

A method which is called on the main thread when MapDownloader.getDownloadableRegions(LanguageCode, DownloadableRegionsCallback) has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be null at the same time - or not null at the same time.

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

      onCompleted ( MapLoaderError maploaderError, List < Region > regions)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  A method which is called on the main thread when MapDownloader.getDownloadableRegions(LanguageCode, DownloadableRegionsCallback) has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onCompleted-com-here-sdk-maploader-MapLoaderError-java-util-List" class="section detail">

    ### onCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onCompleted</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> maploaderError, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader">Region</a>\> regions)</span>

    </div>

    <div class="block">

    A method which is called on the main thread when MapDownloader.getDownloadableRegions(LanguageCode, DownloadableRegionsCallback) has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be null at the same time - or not null at the same time.

    </div>

    Parameters:  
    `maploaderError` -

    Represents an error in case of a failure. It is `null` for an operation that succeeds.

    `regions` -

    Represents a list of downloadable regions. It is `null` in case of an error. Each region can contain child regions that can contain child regions and so on. Usually, the top-level regions represent continents that contain countries as children.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

