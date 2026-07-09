---
title: "VenueListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-service-package-summary">com.here.sdk.venue.service</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">VenueListener</span>

</div>

<div class="block">

The interface for listeners for venue loading events in VenueService .

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

      onGetVenueCompleted (int venueId, VenueModel venueModel,
       boolean online, VenueStyle venueStyle)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when loading of a venue or its retrieval from the cache is completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onGetVenueCompleted-int-com-here-sdk-venue-data-VenueModel-boolean-com-here-sdk-venue-style-VenueStyle" class="section detail">

    ### onGetVenueCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onGetVenueCompleted</span><wbr></wbr><span class="parameters">(int venueId, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a> venueModel, boolean online, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a> venueStyle)</span>

    </div>

    <div class="block">

    Called when loading of a venue or its retrieval from the cache is completed.

    </div>

    Parameters:  
    `venueId` -

    The id of the venue.

    `venueModel` -

    The venue model.

    `online` -

    `True` if a new venue was loaded from the server and `false` otherwise.

    `venueStyle` -

    The style associated with the venue.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

