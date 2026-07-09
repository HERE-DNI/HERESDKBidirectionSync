---
title: "SafetyCameraWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">SafetyCameraWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications on safety cameras. A SafetyCameraWarning will not be given until the previous warning of that type has been passed. For example, a route with SafetyCameraWarning 120 meters and SafetyCameraWarning 160 meters ahead, the first SafetyCameraWarning.distance_to_camera_in_meters is 120 meters and the next SafetyCameraWarning.distance_to_camera_in_meters is then 40 meters, since that is the distance between the first and second warnings. When SafetyCameraWarningListener is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled. The updates for the same safety camera appear in order of the initial DistanceType.AHEAD event. That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.

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

      onSafetyCameraWarningUpdated ( SafetyCameraWarning safetyCameraWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new SafetyCameraWarning is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onSafetyCameraWarningUpdated-com-here-sdk-navigation-SafetyCameraWarning" class="section detail">

    ### onSafetyCameraWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSafetyCameraWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a> safetyCameraWarning)</span>

    </div>

    <div class="block">

    Called whenever a new SafetyCameraWarning is available.

    </div>

    Parameters:  
    `safetyCameraWarning` -

    The object that contains details on the safety camera warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

