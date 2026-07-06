---
title: "LocationListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-locationlistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">LocationListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications
about location updates.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

      onLocationUpdated(Location location)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called each time a new location is available.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-onLocationUpdated(com.here.sdk.core.Location)"
    class="section detail">

    ### onLocationUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><span class="parameters">(@NonNull
    [Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core") location)</span>

    </div>

    <div class="block">

    Called each time a new location is available. In a navigation
    context while using the Navigator or VisualNavigator , it's required
    to set the Location.time parameter for each Location object so that
    the HERE SDK can map-match the locations properly. If the
    Location.time parameter is missing, the location will be ignored.
    For navigation, it is also recommended to provide the bearing and
    speed parameters for each Location object. Invoked on the main
    thread.

    </div>

    Parameters:  
    `location` -

    Current location.

    </div>

  </div>

</div>

