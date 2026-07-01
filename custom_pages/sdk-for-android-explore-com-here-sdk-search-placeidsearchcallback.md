---
title: "PlaceIdSearchCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-placeidsearchcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div id="class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">PlaceIdSearchCallback</span>

</div>

<div class="block">

The method will be called on the main thread when a search by id call
has been completed.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onPlaceIdSearchCompleted(SearchError searchError,
   Place place)</code></pre></td>
  <td><div class="block">
  The method will be called on the main thread when a search by id call
  has been completed.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onPlaceIdSearchCompleted(com.here.sdk.search.SearchError,com.here.sdk.search.Place)"
    class="section detail">

    ### onPlaceIdSearchCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPlaceIdSearchCompleted</span><span class="parameters">(@Nullable
    [SearchError](sdk-for-android-explore-com-here-sdk-search-searcherror "enum class in com.here.sdk.search") searchError,
    @Nullable
    [Place](sdk-for-android-explore-com-here-sdk-search-place "class in com.here.sdk.search") place)</span>

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

    </div>

  </div>

</div>

