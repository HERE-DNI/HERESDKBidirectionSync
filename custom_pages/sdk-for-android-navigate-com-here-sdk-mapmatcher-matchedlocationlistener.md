---
title: "MatchedLocationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-package-summary">com.here.sdk.mapmatcher</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">MatchedLocationListener</span>

</div>

<div class="block">

This interface should be implemented to receive notifications about the current location from MapMatchedLocation . Note: This is a beta release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.

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

      onMatchedLocationUpdated ( MatchedLocation matchedLocation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever the current map-matched location has been updated.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onMatchedLocationUpdated-com-here-sdk-mapmatcher-MatchedLocation" class="section detail">

    ### onMatchedLocationUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMatchedLocationUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocation" title="class in com.here.sdk.mapmatcher">MatchedLocation</a> matchedLocation)</span>

    </div>

    <div class="block">

    Called whenever the current map-matched location has been updated.

    </div>

    Parameters:  
    `matchedLocation` -

    The current matched location update.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

