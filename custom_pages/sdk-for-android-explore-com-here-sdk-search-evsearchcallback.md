---
title: "EVSearchCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evsearchcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">EVSearchCallback</span>

</div>

<div class="block">

The method that will be called on the main thread when a search operation in EVSearchEngine has been completed. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      onEVCP3SearchCompleted ( EVSearchError error, List < EVChargingLocation > chargingLocations)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The method that will be called on the main thread when a search operation in EVSearchEngine has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-onEVCP3SearchCompleted-com-here-sdk-search-EVSearchError-java-util-List" class="section detail">

    ### onEVCP3SearchCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onEVCP3SearchCompleted</span><wbr></wbr><span class="parameters">(@Nullable [EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search") error, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[EVChargingLocation](sdk-for-android-explore-com-here-sdk-search-evcharginglocation "class in com.here.sdk.search")\> chargingLocations)</span>

    </div>

    <div class="block">

    The method that will be called on the main thread when a search operation in EVSearchEngine has been completed. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `error` -

    The ev search error.

    `chargingLocations` -

    The ev charging locations.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

