---
title: "LowSpeedZoneWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">LowSpeedZoneWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive low speed zone warnings. Note: This is currently available only for Japan. The low speed zone warner is a zone warner, which means that for a low speed zone there will always be 3 warnings emitted, with the LowSpeedZoneWarning.distance_type set to DistanceType.AHEAD , DistanceType.REACHED and lastly DistanceType.PASSED when the end of the low speed zone is passed.

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

      onLowSpeedZoneWarningUpdated ( LowSpeedZoneWarning lowSpeedZoneWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new low speed zone warning is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onLowSpeedZoneWarningUpdated-com-here-sdk-navigation-LowSpeedZoneWarning" class="section detail">

    ### onLowSpeedZoneWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onLowSpeedZoneWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a> lowSpeedZoneWarning)</span>

    </div>

    <div class="block">

    Called whenever a new low speed zone warning is available.

    </div>

    Parameters:  
    `lowSpeedZoneWarning` -

    The object that contains details on the low speed zone warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

