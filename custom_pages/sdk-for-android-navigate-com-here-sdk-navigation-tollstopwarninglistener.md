---
title: "TollStopWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">TollStopWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive information on the upcoming toll booth structure. The warner might also warn about gates/checkpoints for vignette, border checkpoints and similar structures on the street. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. A TollStop will not be given until the previous warning of that type has been passed. For example, a route with TollStop 120 meters and TollStop 160 meters ahead, the first TollStop.distance_to_toll_stop_in_meters is 120 meters and the next TollStop.distance_to_toll_stop_in_meters is then 40 meters, since that is the distance between the first and second warnings.

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

      onTollStopWarning ( TollStop tollStop)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new TollStop is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onTollStopWarning-com-here-sdk-navigation-TollStop" class="section detail">

    ### onTollStopWarning

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTollStopWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstop" title="class in com.here.sdk.navigation">TollStop</a> tollStop)</span>

    </div>

    <div class="block">

    Called whenever a new TollStop is available.

    </div>

    Parameters:  
    `tollStop` -

    The upcoming toll stop.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

