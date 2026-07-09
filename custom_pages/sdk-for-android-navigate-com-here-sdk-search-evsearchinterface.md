---
title: "EVSearchInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evsearchinterface"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-search-package-summary">com.here.sdk.search</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Known Implementing Classes:  
<a href="sdk-for-android-navigate-com-here-sdk-search-evsearchengine" title="class in com.here.sdk.search">`EVSearchEngine`</a>

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">EVSearchInterface</span>

</div>

<div class="block">

Provides the interface for the EVSearchEngine . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      search ( List < String > ids, EVSearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous request for EVChargingLocation instances with given Place IDs.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-search-java-util-List-com-here-sdk-search-EVSearchCallback" class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\> ids, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-evsearchcallback" title="interface in com.here.sdk.search">EVSearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request for EVChargingLocation instances with given Place IDs.

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

<!-- ========= END OF CLASS DATA ========= -->

