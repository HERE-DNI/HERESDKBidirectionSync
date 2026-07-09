---
title: "VenueSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venueselectionlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">VenueSelectionListener</span>

</div>

<div class="block">

The interface for listeners for the Venue selection event. Use the VenueMap to add and remove the VenueSelectionListener .

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

      onSelectedVenueChanged ( Venue deselectedVenue, Venue selectedVenue)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Indicates that the current selected Venue changed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onSelectedVenueChanged-com-here-sdk-venue-control-Venue-com-here-sdk-venue-control-Venue" class="section detail">

    ### onSelectedVenueChanged

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSelectedVenueChanged</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> deselectedVenue, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> selectedVenue)</span>

    </div>

    <div class="block">

    Indicates that the current selected Venue changed.

    </div>

    Parameters:  
    `deselectedVenue` -

    The <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">`Venue`</a> that was deselected or `null` if there was no selected venue before.

    `selectedVenue` -

    The <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">`Venue`</a> that was selected or `null` if there was no new selected venue.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

