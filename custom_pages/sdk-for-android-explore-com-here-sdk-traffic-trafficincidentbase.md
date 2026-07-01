---
title: "TrafficIncidentBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

<div id="class-description" class="section class-description">

All Known Implementing Classes:  
[`PickMapContentResult.TrafficIncidentResult`](sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult "class in com.here.sdk.mapview"),
[`TrafficIncident`](sdk-for-android-explore-com-here-sdk-traffic-trafficincident "class in com.here.sdk.traffic"),
[`TrafficIncidentOnRoute`](sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute "class in com.here.sdk.routing")

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">TrafficIncidentBase</span>

</div>

<div class="block">

TrafficIncident provides details about a traffic incident.

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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-localizedtext"
  title="class in com.here.sdk.core"><code>LocalizedText</code></a></td>
  <td><pre><code>getDescription()</code></pre></td>
  <td><div class="block">
  Gets the human readable description of the incident, possibly with
  location information.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a></td>
  <td><pre><code>getEndTime()</code></pre></td>
  <td><div class="block">
  Get the time until which the incident is valid, after this time the
  incident should not be considered.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact"
  title="enum class in com.here.sdk.traffic"><code>TrafficIncidentImpact</code></a></td>
  <td><pre><code>getImpact()</code></pre></td>
  <td><div class="block">
  Gets the impact of the incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a></td>
  <td><pre><code>getStartTime()</code></pre></td>
  <td><div class="block">
  Gets the time from which the incident is valid, before this time the
  incident should not be considered.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype"
  title="enum class in com.here.sdk.traffic"><code>TrafficIncidentType</code></a></td>
  <td><pre><code>getType()</code></pre></td>
  <td><div class="block">
  Gets the category of the incident.
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

  - <div id="getImpact()" class="section detail">

    ### getImpact

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TrafficIncidentImpact](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact "enum class in com.here.sdk.traffic")</span> <span class="element-name">getImpact</span>()

    </div>

    <div class="block">

    Gets the impact of the incident. The value is
    TrafficIncidentImpact.UNKNOWN if it hasn't been provided by the
    traffic incidents supplier.

    </div>

    Returns:  
    The impact of the incident.

    </div>

  - <div id="getType()" class="section detail">

    ### getType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TrafficIncidentType](sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype "enum class in com.here.sdk.traffic")</span> <span class="element-name">getType</span>()

    </div>

    <div class="block">

    Gets the category of the incident. The value is
    TrafficIncidentType.UNKNOWN if it hasn't been provided by the
    traffic incidents supplier.

    </div>

    Returns:  
    The category of the incident.

    </div>

  - <div id="getDescription()" class="section detail">

    ### getDescription

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[LocalizedText](sdk-for-android-explore-com-here-sdk-core-localizedtext "class in com.here.sdk.core")</span> <span class="element-name">getDescription</span>()

    </div>

    <div class="block">

    Gets the human readable description of the incident, possibly with
    location information. The description is currently not present in
    our map data. Therefore, when accessing the data from a picked carto
    POI via TrafficIncidentResult , then always an empty string is
    returned. This does not apply when using the TrafficEngine .

    </div>

    Returns:  
    The human readable description of the incident, possibly with
    location information.

    </div>

  - <div id="getStartTime()" class="section detail">

    ### getStartTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getStartTime</span>()

    </div>

    <div class="block">

    Gets the time from which the incident is valid, before this time the
    incident should not be considered. The value is null if it hasn't
    been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The time from which the incident is valid, before this time the
    incident should not be considered.

    </div>

  - <div id="getEndTime()" class="section detail">

    ### getEndTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getEndTime</span>()

    </div>

    <div class="block">

    Get the time until which the incident is valid, after this time the
    incident should not be considered. The value is null if it hasn't
    been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The time until which the incident is valid, after this time the
    incident should not be considered.

    </div>

  </div>

</div>

