---
title: "TrafficIncidentBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-traffic-package-summary">com.here.sdk.traffic</a>

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Known Implementing Classes:  
<a href="sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult" title="class in com.here.sdk.mapview">`PickMapContentResult.TrafficIncidentResult`</a>, <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident" title="class in com.here.sdk.traffic">`TrafficIncident`</a>, <a href="sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute" title="class in com.here.sdk.routing">`TrafficIncidentOnRoute`</a>

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">TrafficIncidentBase</span>

</div>

<div class="block">

TrafficIncident provides details about a traffic incident.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

  <a href="sdk-for-android-explore-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getDescription ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the human readable description of the incident, possibly with location information.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getEndTime ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Get the time until which the incident is valid, after this time the incident should not be considered.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact" title="enum class in com.here.sdk.traffic">`TrafficIncidentImpact`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getImpact ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the impact of the incident.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getStartTime ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the time from which the incident is valid, before this time the incident should not be considered.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">`TrafficIncidentType`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getType ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the category of the incident.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-getImpact" class="section detail">

    ### getImpact

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></span> <span class="element-name">getImpact</span>()

    </div>

    <div class="block">

    Gets the impact of the incident. The value is TrafficIncidentImpact.UNKNOWN if it hasn't been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The impact of the incident.

    </div>

  - <div id="sdk-for-android-explore-getType" class="section detail">

    ### getType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></span> <span class="element-name">getType</span>()

    </div>

    <div class="block">

    Gets the category of the incident. The value is TrafficIncidentType.UNKNOWN if it hasn't been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The category of the incident.

    </div>

  - <div id="sdk-for-android-explore-getDescription" class="section detail">

    ### getDescription

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">getDescription</span>()

    </div>

    <div class="block">

    Gets the human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via TrafficIncidentResult , then always an empty string is returned. This does not apply when using the TrafficEngine .

    </div>

    Returns:  
    The human readable description of the incident, possibly with location information.

    </div>

  - <div id="sdk-for-android-explore-getStartTime" class="section detail">

    ### getStartTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getStartTime</span>()

    </div>

    <div class="block">

    Gets the time from which the incident is valid, before this time the incident should not be considered. The value is null if it hasn't been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The time from which the incident is valid, before this time the incident should not be considered.

    </div>

  - <div id="sdk-for-android-explore-getEndTime" class="section detail">

    ### getEndTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getEndTime</span>()

    </div>

    <div class="block">

    Get the time until which the incident is valid, after this time the incident should not be considered. The value is null if it hasn't been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The time until which the incident is valid, after this time the incident should not be considered.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

