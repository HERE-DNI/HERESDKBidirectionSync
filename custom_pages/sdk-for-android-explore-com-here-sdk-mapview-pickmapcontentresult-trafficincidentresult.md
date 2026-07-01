---
title: "PickMapContentResult.TrafficIncidentResult (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult
→ com.here.NativeBase →
com.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
[`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

<!-- -->

Enclosing class:  
[PickMapContentResult](sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">PickMapContentResult.TrafficIncidentResult</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")
implements
[TrafficIncidentBase](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")</span>

</div>

<div class="block">

Carries the result of picking a Carto traffic incident object.
Description of incident is currently not present in our map data, so
TrafficIncidentBase.getDescription() always returns an empty string.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><pre><code>getCoordinates()</code></pre></td>
  <td><div class="block">
  Gets the geographic coordinates of the traffic incident.
  </div></td>
  </tr>
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getOriginalId()</code></pre></td>
  <td><div class="block">
  Gets the unique traffic event ID.
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

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="getOriginalId()" class="section detail">

    ### getOriginalId

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getOriginalId</span>()

    </div>

    <div class="block">

    Gets the unique traffic event ID. Can be referenced when checking
    for updated traffic information for the specified event.

    </div>

    Returns:  
    Unique traffic event ID.

    </div>

  - <div id="getCoordinates()" class="section detail">

    ### getCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getCoordinates</span>()

    </div>

    <div class="block">

    Gets the geographic coordinates of the traffic incident.

    </div>

    Returns:  
    The geographic coordinates of the traffic incident.

    </div>

  - <div id="getImpact()" class="section detail">

    ### getImpact

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TrafficIncidentImpact](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact "enum class in com.here.sdk.traffic")</span> <span class="element-name">getImpact</span>()

    </div>

    <div class="block">

    Gets the impact of the incident. The value is
    TrafficIncidentImpact.UNKNOWN if it hasn't been provided by the
    traffic incidents supplier.

    </div>

    Specified by:  
    [`getImpact`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getImpact()) in
    interface [`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

    Returns:  
    The impact of the incident.

    </div>

  - <div id="getType()" class="section detail">

    ### getType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TrafficIncidentType](sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype "enum class in com.here.sdk.traffic")</span> <span class="element-name">getType</span>()

    </div>

    <div class="block">

    Gets the category of the incident. The value is
    TrafficIncidentType.UNKNOWN if it hasn't been provided by the
    traffic incidents supplier.

    </div>

    Specified by:  
    [`getType`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getType()) in
    interface [`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

    Returns:  
    The category of the incident.

    </div>

  - <div id="getDescription()" class="section detail">

    ### getDescription

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LocalizedText](sdk-for-android-explore-com-here-sdk-core-localizedtext "class in com.here.sdk.core")</span> <span class="element-name">getDescription</span>()

    </div>

    <div class="block">

    Gets the human readable description of the incident, possibly with
    location information. The description is currently not present in
    our map data. Therefore, when accessing the data from a picked carto
    POI via TrafficIncidentResult , then always an empty string is
    returned. This does not apply when using the TrafficEngine .

    </div>

    Specified by:  
    [`getDescription`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getDescription()) in
    interface [`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

    Returns:  
    The human readable description of the incident, possibly with
    location information.

    </div>

  - <div id="getStartTime()" class="section detail">

    ### getStartTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getStartTime</span>()

    </div>

    <div class="block">

    Gets the time from which the incident is valid, before this time the
    incident should not be considered. The value is null if it hasn't
    been provided by the traffic incidents supplier.

    </div>

    Specified by:  
    [`getStartTime`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getStartTime()) in
    interface [`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

    Returns:  
    The time from which the incident is valid, before this time the
    incident should not be considered.

    </div>

  - <div id="getEndTime()" class="section detail">

    ### getEndTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getEndTime</span>()

    </div>

    <div class="block">

    Get the time until which the incident is valid, after this time the
    incident should not be considered. The value is null if it hasn't
    been provided by the traffic incidents supplier.

    </div>

    Specified by:  
    [`getEndTime`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getEndTime()) in
    interface [`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

    Returns:  
    The time until which the incident is valid, after this time the
    incident should not be considered.

    </div>

  </div>

</div>

