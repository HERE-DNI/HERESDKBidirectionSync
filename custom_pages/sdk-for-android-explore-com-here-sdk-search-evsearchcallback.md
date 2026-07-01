---
title: "EVSearchCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evsearchcallback"
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
</span><span class="element-name type-name-label">EVSearchCallback</span>

</div>

<div class="block">

The method that will be called on the main thread when a search
operation in EVSearchEngine has been completed. Note: This is a beta
release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a
deprecation process.

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
  <td><pre><code>onEVCP3SearchCompleted(EVSearchError error,
   List&lt;EVChargingLocation&gt; chargingLocations)</code></pre></td>
  <td><div class="block">
  The method that will be called on the main thread when a search
  operation in EVSearchEngine has been completed.
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

  - <div id="onEVCP3SearchCompleted(com.here.sdk.search.EVSearchError,java.util.List)"
    class="section detail">

    ### onEVCP3SearchCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onEVCP3SearchCompleted</span><span class="parameters">(@Nullable
    [EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search") error,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[EVChargingLocation](sdk-for-android-explore-com-here-sdk-search-evcharginglocation "class in com.here.sdk.search")> chargingLocations)</span>

    </div>

    <div class="block">

    The method that will be called on the main thread when a search
    operation in EVSearchEngine has been completed. Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    Parameters:  
    `error` -

    The ev search error.

    `chargingLocations` -

    The ev charging locations.

    </div>

  </div>

</div>

