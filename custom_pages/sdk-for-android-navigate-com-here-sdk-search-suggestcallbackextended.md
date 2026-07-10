---
title: "SuggestCallbackExtended (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-suggestcallbackextended"
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

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">SuggestCallbackExtended</span>

</div>

<div class="block">

The method will be called on the main thread when a suggest call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be null at the same time - or not null at the same time. This API is not supported by offline search.

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

      onSuggestExtendedCompleted ( SearchError searchError, List < Suggestion > suggestions, ResponseDetails responseDetails)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The method will be called on the main thread when a suggest call has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onSuggestExtendedCompleted-com-here-sdk-search-SearchError-java-util-List-com-here-sdk-search-ResponseDetails" class="section detail">

    ### onSuggestExtendedCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSuggestExtendedCompleted</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-search-searcherror" title="enum class in com.here.sdk.search">SearchError</a> searchError, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search">Suggestion</a>\> suggestions, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-search-responsedetails" title="class in com.here.sdk.search">ResponseDetails</a> responseDetails)</span>

    </div>

    <div class="block">

    The method will be called on the main thread when a suggest call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be null at the same time - or not null at the same time. This API is not supported by offline search.

    </div>

    Parameters:  
    `searchError` -

    An error enum indicating what went wrong. It is `null` for an operation that succeeds.

    `suggestions` -

    The list of suggestion results. It is `null` in case of an error.

    `responseDetails` -

    Additional information provided with response. It is `null` in case of an error.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

