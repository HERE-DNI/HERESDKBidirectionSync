---
title: "TrafficFlowBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficflowbase"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

<div id="class-description" class="section class-description">

All Known Implementing Classes:  
[`TrafficFlow`](sdk-for-android-explore-com-here-sdk-traffic-trafficflow "class in com.here.sdk.traffic")

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">TrafficFlowBase</span>

</div>

<div class="block">

This interface provides details about a traffic flow. For additional
information about fields, refer to Traffic API v7 API Reference: Traffic
API v7 . Note: This is a beta release of this feature, so there could be
a few bugs and unexpected behaviors. Related APIs may change for new
releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>double</code></td>
  <td><pre><code>getFreeFlowSpeedInMetersPerSecond()</code></pre></td>
  <td><div class="block">
  Gets the reference speed in meters per second along the roadway when no
  traffic is present.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><pre><code>getJamFactor()</code></pre></td>
  <td><div class="block">
  Gets a value for the amount of traffic on the roadway.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="getFreeFlowSpeedInMetersPerSecond()"
    class="section detail">

    ### getFreeFlowSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="return-type">double</span> <span class="element-name">getFreeFlowSpeedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the reference speed in meters per second along the roadway when
    no traffic is present.

    </div>

    Returns:  
    The reference speed in meters per second along the roadway when no
    traffic is present.

    </div>

  - <div id="getJamFactor()" class="section detail">

    ### getJamFactor

    <div class="member-signature">

    <span class="return-type">double</span> <span class="element-name">getJamFactor</span>()

    </div>

    <div class="block">

    Gets a value for the amount of traffic on the roadway. The value,
    between 0.0 and 10.0, indicate the expected quality of travel. A
    value of 0.0 indicates that there is no congestion on the roadway.
    As the value approaches 10.0, it indicates increasing congestion. A
    value of 10.0 is reserved to represent a blocked roadway (closure).

    </div>

    Returns:  
    A value for the amount of traffic on the roadway.

    </div>

  </div>

</div>

