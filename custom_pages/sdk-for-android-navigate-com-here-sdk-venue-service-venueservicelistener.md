---
title: "VenueServiceListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-service-venueservicelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-service-package-summary">com.here.sdk.venue.service</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">VenueServiceListener</span>

</div>

<div class="block">

The interface for listeners for lifecycle events in VenueService .

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

      onInitializationCompleted ( VenueServiceInitStatus result)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when a service initialization has been completed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onVenueServiceStopped ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when the venue service stops.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onInitializationCompleted-com-here-sdk-venue-service-VenueServiceInitStatus" class="section detail">

    ### onInitializationCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onInitializationCompleted</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueserviceinitstatus" title="enum class in com.here.sdk.venue.service">VenueServiceInitStatus</a> result)</span>

    </div>

    <div class="block">

    Called when a service initialization has been completed.

    </div>

    Parameters:  
    `result` -

    The initialization status.

    </div>

  - <div id="sdk-for-android-navigate-onVenueServiceStopped" class="section detail">

    ### onVenueServiceStopped

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onVenueServiceStopped</span>()

    </div>

    <div class="block">

    Called when the venue service stops.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

