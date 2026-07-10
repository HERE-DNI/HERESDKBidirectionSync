---
title: "LocationStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-location-package-summary">com.here.sdk.location</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">LocationStatusListener</span>

</div>

<div class="block">

Interface for listening the LocationEngine status updates.

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

      onFeaturesNotAvailable ( List < LocationFeature > features)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called after start() if any requested location feature is not available for the application.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onStatusChanged ( LocationEngineStatus locationEngineStatus)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called each time the status of the LocationEngine has changed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onStatusChanged-com-here-sdk-location-LocationEngineStatus" class="section detail">

    ### onStatusChanged

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onStatusChanged</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a> locationEngineStatus)</span>

    </div>

    <div class="block">

    Called each time the status of the LocationEngine has changed. Invoked on the main thread.

    </div>

    Parameters:  
    `locationEngineStatus` -

    The new status.

    </div>

  - <div id="sdk-for-android-navigate-onFeaturesNotAvailable-java-util-List" class="section detail">

    ### onFeaturesNotAvailable

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onFeaturesNotAvailable</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-location-locationfeature" title="enum class in com.here.sdk.location">LocationFeature</a>\> features)</span>

    </div>

    <div class="block">

    Called after start() if any requested location feature is not available for the application. Typically all features are enabled by default, but in certain variants some features may be disabled, e.g. to reduce binary size. If a feature that you need is not available, contact your HERE representative for more information.

    </div>

    Parameters:  
    `features` -

    List of unavailable location features.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

