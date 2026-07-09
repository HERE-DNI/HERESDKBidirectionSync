---
title: "SpeedWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">SpeedWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Note: The warnings issued by this interface don't take into account any temporary special speed limits. See SpeedLimitListener .

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

      onSpeedWarningStatusChanged ( SpeedWarningStatus status)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new SpeedWarningStatus is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onSpeedWarningStatusChanged-com-here-sdk-navigation-SpeedWarningStatus" class="section detail">

    ### onSpeedWarningStatusChanged

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSpeedWarningStatusChanged</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningstatus" title="enum class in com.here.sdk.navigation">SpeedWarningStatus</a> status)</span>

    </div>

    <div class="block">

    Called whenever a new SpeedWarningStatus is available.

    </div>

    Parameters:  
    `status` -

    The new status of the speed warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

