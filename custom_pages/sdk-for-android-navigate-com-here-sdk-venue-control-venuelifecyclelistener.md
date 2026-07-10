---
title: "VenueLifecycleListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuelifecyclelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">VenueLifecycleListener</span>

</div>

<div class="block">

The interface for listeners for the Venue lifecycle events. Use the VenueMap to add and remove the VenueLifecycleListener .

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

      onVenueAdded ( Venue venue)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Indicates that a Venue was added to the VenueMap .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onVenueRemoved (int venueId)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Indicates that a Venue was removed from the VenueMap .

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onVenueAdded-com-here-sdk-venue-control-Venue" class="section detail">

    ### onVenueAdded

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onVenueAdded</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</span>

    </div>

    <div class="block">

    Indicates that a Venue was added to the VenueMap .

    </div>

    Parameters:  
    `venue` -

    The created <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">`Venue`</a>.

    </div>

  - <div id="sdk-for-android-navigate-onVenueRemoved-int" class="section detail">

    ### onVenueRemoved

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onVenueRemoved</span><wbr></wbr><span class="parameters">(int venueId)</span>

    </div>

    <div class="block">

    Indicates that a Venue was removed from the VenueMap .

    </div>

    Parameters:  
    `venueId` -

    The destroyed venue id, that can be obtained from the [](sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel#getId())

        VenueModel.getId()

    </a>.

    </p>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

