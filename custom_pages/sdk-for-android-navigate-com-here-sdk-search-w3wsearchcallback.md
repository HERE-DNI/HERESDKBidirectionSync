---
title: "W3WSearchCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-w3wsearchcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-search-package-summary">com.here.sdk.search</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">W3WSearchCallback</span>

</div>

<div class="block">

The method that will be called on the main thread when a search operation in W3WSearchEngine has been completed.

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

      onW3WSearchCompleted ( W3WSearchError searchError, W3WSquare square)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The method that will be called on the main thread when a search operation in W3WSearchEngine has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onW3WSearchCompleted-com-here-sdk-search-W3WSearchError-com-here-sdk-search-W3WSquare" class="section detail">

    ### onW3WSearchCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onW3WSearchCompleted</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-search-w3wsearcherror" title="enum class in com.here.sdk.search">W3WSearchError</a> searchError, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-search-w3wsquare" title="class in com.here.sdk.search">W3WSquare</a> square)</span>

    </div>

    <div class="block">

    The method that will be called on the main thread when a search operation in W3WSearchEngine has been completed.

    </div>

    Parameters:  
    `searchError` -

    The w3w search error.

    `square` -

    The w3w square.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

