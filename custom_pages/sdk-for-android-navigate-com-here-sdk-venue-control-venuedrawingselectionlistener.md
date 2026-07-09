---
title: "VenueDrawingSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">VenueDrawingSelectionListener</span>

</div>

<div class="block">

The interface for listeners for the VenueDrawing selection event. Use the VenueMap to add and remove the VenueDrawingSelectionListener .

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

      onDrawingSelected ( Venue venue, VenueDrawing deselectedDrawing, VenueDrawing selectedDrawing)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Indicates that new VenueDrawing has been selected.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onDrawingSelected-com-here-sdk-venue-control-Venue-com-here-sdk-venue-data-VenueDrawing-com-here-sdk-venue-data-VenueDrawing" class="section detail">

    ### onDrawingSelected

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDrawingSelected</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> deselectedDrawing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> selectedDrawing)</span>

    </div>

    <div class="block">

    Indicates that new VenueDrawing has been selected.

    </div>

    Parameters:  
    `venue` -

    The <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">`Venue`</a> where a selected drawing was changed.

    `deselectedDrawing` -

    The previously selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a> object or `null` if there was no selected drawing before.

    `selectedDrawing` -

    The new selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a> object.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

