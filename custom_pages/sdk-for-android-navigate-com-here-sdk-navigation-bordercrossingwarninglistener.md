---
title: "BorderCrossingWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">BorderCrossingWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive border crossing warnings for country and state borders. Note: The border crossing warner is a point warner, which means that for a border crossing there will always be 2 warnings emitted, with the \[BorderCrossingWarning.distance_type\] set to DistanceType.AHEAD and DistanceType.PASSED which is given when the location of the border crossing is reached. A BorderCrossingWarning will not be given until the previous warning of that type has been passed. For example, a route with BorderCrossingWarning 120 meters and BorderCrossingWarning 160 meters ahead, the first \[BorderCrossingWarning.distance_to_border_crossing_in_meters\] is 120 meters and the next \[BorderCrossingWarning.distance_to_border_crossing_in_meters\] is then 40 meters, since that is the distance between the first and second warnings.

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

      onBorderCrossingWarningUpdated ( BorderCrossingWarning borderCrossingWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new border crossing warning is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onBorderCrossingWarningUpdated-com-here-sdk-navigation-BorderCrossingWarning" class="section detail">

    ### onBorderCrossingWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onBorderCrossingWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a> borderCrossingWarning)</span>

    </div>

    <div class="block">

    Called whenever a new border crossing warning is available.

    </div>

    Parameters:  
    `borderCrossingWarning` -

    The object that contains details on the border crossing warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

