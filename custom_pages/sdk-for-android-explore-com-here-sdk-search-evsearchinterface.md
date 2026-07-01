---
title: "EVSearchInterface (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evsearchinterface"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div id="class-description" class="section class-description">

All Known Implementing Classes:  
[`EVSearchEngine`](sdk-for-android-explore-com-here-sdk-search-evsearchengine "class in com.here.sdk.search")

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">EVSearchInterface</span>

</div>

<div class="block">

Provides the interface for the EVSearchEngine . Note: This is a beta
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
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-threading-taskhandle"
  title="interface in com.here.sdk.core.threading"><code>TaskHandle</code></a></td>
  <td><pre><code>search(List&lt;String&gt; ids,
   EVSearchCallback callback)</code></pre></td>
  <td><div class="block">
  Performs an asynchronous request for EVChargingLocation instances with
  given Place IDs.
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

  - <div id="search(java.util.List,com.here.sdk.search.EVSearchCallback)"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> ids,
    @NonNull
    [EVSearchCallback](sdk-for-android-explore-com-here-sdk-search-evsearchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request for EVChargingLocation instances
    with given Place IDs.

    </div>

    Parameters:  
    `ids` -

    List of charging location identifiers.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  </div>

</div>

