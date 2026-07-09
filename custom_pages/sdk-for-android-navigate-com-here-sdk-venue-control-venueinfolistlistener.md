---
title: "VenueInfoListListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venueinfolistlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">VenueInfoListListener</span>

</div>

<div class="block">

The interface for listeners for the list of VenueInfo load event. Use VenueMap to add and remove the VenueInfoListListener .

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

      onVenueInfoListLoad ( List < VenueInfo > venueInfoList)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Indicates that VenueInfo list is loaded.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onVenueInfoListLoad-java-util-List" class="section detail">

    ### onVenueInfoListLoad

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onVenueInfoListLoad</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>\> venueInfoList)</span>

    </div>

    <div class="block">

    Indicates that VenueInfo list is loaded.

    </div>

    Parameters:  
    `venueInfoList` -

    The <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control">`VenueMap`</a> where the loaded list of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">`VenueInfo`</a>.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

