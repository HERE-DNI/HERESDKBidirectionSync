---
title: "TrafficMergeWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">TrafficMergeWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive traffic merge warnings. Note: The traffic merge warner is a point warner, which means that for a traffic merge there will always be 2 warnings emitted, with the TrafficMergeWarning.distance_type set to DistanceType.AHEAD and DistanceType.PASSED which is given when the location of the traffic merge is reached. A TrafficMergeWarning will not be given until the previous warning of that type has been passed. For example, a route with TrafficMergeWarning 120 meters and TrafficMergeWarning 160 meters ahead, the first TrafficMergeWarning.distance_to_traffic_merge_in_meters is 120 meters and the next TrafficMergeWarning.distance_to_traffic_merge_in_meters is then 40 meters, since that is the distance between the first and second warnings.

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

      onTrafficMergeWarningUpdated ( TrafficMergeWarning trafficMergeWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new traffic merge warning is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onTrafficMergeWarningUpdated-com-here-sdk-navigation-TrafficMergeWarning" class="section detail">

    ### onTrafficMergeWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTrafficMergeWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a> trafficMergeWarning)</span>

    </div>

    <div class="block">

    Called whenever a new traffic merge warning is available.

    </div>

    Parameters:  
    `trafficMergeWarning` -

    The object that contains details on the traffic merge warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

