---
title: "TrafficIncidentOnRoute (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.routing.TrafficIncidentOnRoute →
com.here.NativeBase → com.here.sdk.routing.TrafficIncidentOnRoute

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
[`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TrafficIncidentOnRoute</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")
implements
[TrafficIncidentBase](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")</span>

</div>

<div class="block">

Traffic incidents on a route. Use Section.getTrafficIncidents() to get a
list of incidents on a route section. Use
Span.getTrafficIncidentIndexes() to associate incidents with spans. Each
incident takes at least the whole geometry of matching spans. Also, an
incident can take some place out of the built route.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LocalizedText`](sdk-for-android-explore-com-here-sdk-core-localizedtext "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDescription()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the human readable description of the incident, possibly with
  location information.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEndTime()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Get the time until which the incident is valid, after this time the
  incident should not be considered.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getId()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the unique current identifier for a traffic incident.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TrafficIncidentImpact`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getImpact()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the impact of the incident.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStartTime()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the time from which the incident is valid, before this time the
  incident should not be considered.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TrafficIncidentType`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getType()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the category of the incident.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getId()" class="section detail">

    ### getId

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()

    </div>

    <div class="block">

    Gets the unique current identifier for a traffic incident. The
    identifier can be changed by the backend due to some events, e.g.
    changing of TrafficIncidentBase.getEndTime() . This field will be
    empty for OfflineRouting .

    </div>

    Returns:  
    The unique current identifier for a traffic incident.

    </div>

  - <div id="sdk-for-android-explore-getImpact()"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getType()" class="section detail">

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

  - <div id="sdk-for-android-explore-getDescription()"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getStartTime()"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getEndTime()"
    class="section detail">

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

