---
title: "TrafficFlowBase (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-traffic-package-summary">com.here.sdk.traffic</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Known Implementing Classes:  
<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow" title="class in com.here.sdk.traffic">`TrafficFlow`</a>

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">TrafficFlowBase</span>

</div>

<div class="block">

This interface provides details about a traffic flow. For additional information about fields, refer to Traffic API v7 API Reference: Traffic API v7 . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getFreeFlowSpeedInMetersPerSecond ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the reference speed in meters per second along the roadway when no traffic is present.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getJamFactor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets a value for the amount of traffic on the roadway.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getFreeFlowSpeedInMetersPerSecond" class="section detail">

    ### getFreeFlowSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="return-type">double</span> <span class="element-name">getFreeFlowSpeedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the reference speed in meters per second along the roadway when no traffic is present.

    </div>

    Returns:  
    The reference speed in meters per second along the roadway when no traffic is present.

    </div>

  - <div id="sdk-for-android-navigate-getJamFactor" class="section detail">

    ### getJamFactor

    <div class="member-signature">

    <span class="return-type">double</span> <span class="element-name">getJamFactor</span>()

    </div>

    <div class="block">

    Gets a value for the amount of traffic on the roadway. The value, between 0.0 and 10.0, indicate the expected quality of travel. A value of 0.0 indicates that there is no congestion on the roadway. As the value approaches 10.0, it indicates increasing congestion. A value of 10.0 is reserved to represent a blocked roadway (closure).

    </div>

    Returns:  
    A value for the amount of traffic on the roadway.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

