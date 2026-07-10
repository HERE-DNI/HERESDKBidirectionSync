---
title: "VenueLevelSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuelevelselectionlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">VenueLevelSelectionListener</span>

</div>

<div class="block">

The interface for listeners for the VenueLevel selection event. Use the VenueMap to add and remove the VenueLevelSelectionListener .

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

      onLevelSelected ( Venue venue, VenueDrawing drawing, VenueLevel deselectedLevel, VenueLevel selectedLevel)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Indicates that the selected VenueLevel of a venue changed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onLevelSelected-com-here-sdk-venue-control-Venue-com-here-sdk-venue-data-VenueDrawing-com-here-sdk-venue-data-VenueLevel-com-here-sdk-venue-data-VenueLevel" class="section detail">

    ### onLevelSelected

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onLevelSelected</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> drawing, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> deselectedLevel, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> selectedLevel)</span>

    </div>

    <div class="block">

    Indicates that the selected VenueLevel of a venue changed.

    </div>

    Parameters:  
    `venue` -

    The <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">`Venue`</a> where the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a> changed.

    `drawing` -

    The <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a> where the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a> changed.

    `deselectedLevel` -

    The previously selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a> or `null` if there was no selected level before.

    `selectedLevel` -

    The new selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a>.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

