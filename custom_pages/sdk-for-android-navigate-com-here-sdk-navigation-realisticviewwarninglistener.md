---
title: "RealisticViewWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RealisticViewWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive realistic view warnings. A RealisticViewWarning will not be given until the previous warning of that type has been passed. For example, a route with RealisticViewWarning 120 meters and RealisticViewWarning 160 meters ahead, the first RealisticViewWarning.distanceToRealisticViewInMeters is 120 meters and the next RealisticViewWarning.distanceToRealisticViewInMeters is then 40 meters, since that is the distance between the first and second warnings.

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

      onRealisticViewWarningUpdated ( RealisticViewWarning realisticViewWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new realistic view warning is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onRealisticViewWarningUpdated-com-here-sdk-navigation-RealisticViewWarning" class="section detail">

    ### onRealisticViewWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRealisticViewWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation">RealisticViewWarning</a> realisticViewWarning)</span>

    </div>

    <div class="block">

    Called whenever a new realistic view warning is available.

    </div>

    Parameters:  
    `realisticViewWarning` -

    The object that contains details on the realistic view warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

