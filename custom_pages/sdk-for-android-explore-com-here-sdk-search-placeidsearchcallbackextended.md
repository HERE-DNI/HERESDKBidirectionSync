---
title: "PlaceIdSearchCallbackExtended (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-placeidsearchcallbackextended"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">PlaceIdSearchCallbackExtended</span>

</div>

<div class="block">

The method will be called on the main thread when a search by id call
has been completed.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

      onPlaceIdSearchExtendedCompleted(SearchError searchError,
       Place place,
       ResponseDetails responseDetails)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The method will be called on the main thread when a search by id call
  has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-onPlaceIdSearchExtendedCompleted(com.here.sdk.search.SearchError,com.here.sdk.search.Place,com.here.sdk.search.ResponseDetails)"
    class="section detail">

    ### onPlaceIdSearchExtendedCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPlaceIdSearchExtendedCompleted</span><span class="parameters">(@Nullable
    [SearchError](sdk-for-android-explore-com-here-sdk-search-searcherror "enum class in com.here.sdk.search") searchError,
    @Nullable
    [Place](sdk-for-android-explore-com-here-sdk-search-place "class in com.here.sdk.search") place,
    @Nullable
    [ResponseDetails](sdk-for-android-explore-com-here-sdk-search-responsedetails "class in com.here.sdk.search") responseDetails)</span>

    </div>

    <div class="block">

    The method will be called on the main thread when a search by id
    call has been completed.

    </div>

    Parameters:  
    `searchError` -

    The search error.

    `place` -

    The place.

    `responseDetails` -

    The response details.

    </div>

  </div>

</div>

