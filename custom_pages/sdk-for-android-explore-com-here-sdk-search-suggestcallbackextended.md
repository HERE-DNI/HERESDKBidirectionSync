---
title: "SuggestCallbackExtended (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-suggestcallbackextended"
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
</span><span class="element-name type-name-label">SuggestCallbackExtended</span>

</div>

<div class="block">

The method will be called on the main thread when a suggest call has
been completed. The first argument indicates an error in case of a
failure. The second argument contains the results. Both arguments cannot
be null at the same time - or not null at the same time. This API is not
supported by offline search.

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
  <td><pre><code>onSuggestExtendedCompleted(SearchError searchError,
   List&lt;Suggestion&gt; suggestions,
   ResponseDetails responseDetails)</code></pre></td>
  <td><div class="block">
  The method will be called on the main thread when a suggest call has
  been completed.
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

  - <div id="onSuggestExtendedCompleted(com.here.sdk.search.SearchError,java.util.List,com.here.sdk.search.ResponseDetails)"
    class="section detail">

    ### onSuggestExtendedCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSuggestExtendedCompleted</span><span class="parameters">(@Nullable
    [SearchError](sdk-for-android-explore-com-here-sdk-search-searcherror "enum class in com.here.sdk.search") searchError,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[Suggestion](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")> suggestions,
    @Nullable
    [ResponseDetails](sdk-for-android-explore-com-here-sdk-search-responsedetails "class in com.here.sdk.search") responseDetails)</span>

    </div>

    <div class="block">

    The method will be called on the main thread when a suggest call has
    been completed. The first argument indicates an error in case of a
    failure. The second argument contains the results. Both arguments
    cannot be null at the same time - or not null at the same time. This
    API is not supported by offline search.

    </div>

    Parameters:  
    `searchError` -

    An error enum indicating what went wrong. It is `null` for an
    operation that succeeds.

    `suggestions` -

    The list of suggestion results. It is `null` in case of an error.

    `responseDetails` -

    Additional information provided with response. It is `null` in case
    of an error.

    </div>

  </div>

</div>

