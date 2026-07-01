---
title: "TrafficIncident (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincident"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.traffic.TrafficIncident →
com.here.NativeBase → com.here.sdk.traffic.TrafficIncident

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
[`TrafficIncidentBase`](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TrafficIncident</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")
implements
[TrafficIncidentBase](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")</span>

</div>

<div class="block">

TrafficIncident provides details about a traffic incident.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory"
  class="type-name-link"
  title="enum class in com.here.sdk.traffic"><code>TrafficIncident.RestrictedVehicleCategory</code></a></td>
  <td><div class="block">
  The vehicle categories that can be restricted.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction"
  class="type-name-link"
  title="class in com.here.sdk.traffic"><code>TrafficIncident.VehicleRestriction</code></a></td>
  <td><div class="block">
  The vehicle restriction representing a vehicle category and relevant
  restriction rules.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a><code>&gt;</code></td>
  <td><pre><code>getCodes()</code></pre></td>
  <td><div class="block">
  Gets the list of standardized codes as categorized in ISO 14819-2:2013
  standard for this incident category.
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a></td>
  <td><pre><code>getEntryTime()</code></pre></td>
  <td><div class="block">
  Gets the time the incident was entered into the system.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getId()</code></pre></td>
  <td><div class="block">
  Gets the unique current identifier for a traffic incident.
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
  href="sdk-for-android-explore-com-here-sdk-traffic-junctionstraversability"
  title="enum class in com.here.sdk.traffic"><code>JunctionsTraversability</code></a></td>
  <td><pre><code>getJunctionsTraversability()</code></pre></td>
  <td><div class="block">
  Gets the traversability of junctions along the affected road.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficlocation"
  title="class in com.here.sdk.traffic"><code>TrafficLocation</code></a></td>
  <td><pre><code>getLocation()</code></pre></td>
  <td><div class="block">
  Gets the location of the incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getOriginalId()</code></pre></td>
  <td><div class="block">
  Gets the unique identifier of the first traffic incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getParentId()</code></pre></td>
  <td><div class="block">
  Gets the identifier of another incident to which this incident is
  linked.
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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-localizedtext"
  title="class in com.here.sdk.core"><code>LocalizedText</code></a></td>
  <td><pre><code>getSummary()</code></pre></td>
  <td><div class="block">
  Gets the human readable summary of the incident.
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
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory"
  title="enum class in com.here.sdk.traffic"><code>TrafficIncident.RestrictedVehicleCategory</code></a><code>,</code><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction"
  title="class in com.here.sdk.traffic"><code>TrafficIncident.VehicleRestriction</code></a><code>&gt;</code></td>
  <td><pre><code>getVehicleRestrictions()</code></pre></td>
  <td><div class="block">
  Gets the map of restricted vehicle categories to restrictions.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isRoadClosed()</code></pre></td>
  <td><div class="block">
  Gets the flag indicating whether road is closed or not.
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

  - <div id="getId()" class="section detail">

    ### getId

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()

    </div>

    <div class="block">

    Gets the unique current identifier for a traffic incident.

    </div>

    Returns:  
    The unique current identifier for a traffic incident.

    </div>

  - <div id="getOriginalId()" class="section detail">

    ### getOriginalId

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getOriginalId</span>()

    </div>

    <div class="block">

    Gets the unique identifier of the first traffic incident. The
    original id remains the same whenever the traffic incident is
    updated and getId() is changed. Once an incident chain has been
    created, this value will never change. The traffic incident an be
    looked up by original id using
    TrafficEngine.lookupIncident(java.lang.String,
    com.here.sdk.traffic.TrafficIncidentLookupOptions,
    com.here.sdk.traffic.TrafficIncidentLookupCallback) .

    </div>

    Returns:  
    The unique identifier of the first traffic incident.

    </div>

  - <div id="getParentId()" class="section detail">

    ### getParentId

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getParentId</span>()

    </div>

    <div class="block">

    Gets the identifier of another incident to which this incident is
    linked. The value is null if the incident doesn't have a parent.

    </div>

    Returns:  
    The identifier of another incident to which this incident is linked.

    </div>

  - <div id="getJunctionsTraversability()" class="section detail">

    ### getJunctionsTraversability

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[JunctionsTraversability](sdk-for-android-explore-com-here-sdk-traffic-junctionstraversability "enum class in com.here.sdk.traffic")</span> <span class="element-name">getJunctionsTraversability</span>()

    </div>

    <div class="block">

    Gets the traversability of junctions along the affected road.

    </div>

    Returns:  
    The traversability of junctions along the affected road.

    </div>

  - <div id="isRoadClosed()" class="section detail">

    ### isRoadClosed

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRoadClosed</span>()

    </div>

    <div class="block">

    Gets the flag indicating whether road is closed or not.

    </div>

    Returns:  
    The flag indicates whether road is closed or not.

    </div>

  - <div id="getCodes()" class="section detail">

    ### getCodes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>></span> <span class="element-name">getCodes</span>()

    </div>

    <div class="block">

    Gets the list of standardized codes as categorized in ISO
    14819-2:2013 standard for this incident category. Codes are given in
    order of importance, so the first item in the list is considered the
    primary cause of the incident.

    </div>

    Returns:  
    The list of standardized codes as categorized in ISO 14819-2:2013
    standard for this incident category.

    </div>

  - <div id="getSummary()" class="section detail">

    ### getSummary

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LocalizedText](sdk-for-android-explore-com-here-sdk-core-localizedtext "class in com.here.sdk.core")</span> <span class="element-name">getSummary</span>()

    </div>

    <div class="block">

    Gets the human readable summary of the incident. The summary field
    provides a short version of the description containing no location
    information. The expected summary language can be managed via
    TrafficIncidentsQueryOptions.languageCode and
    TrafficIncidentLookupOptions.languageCode .

    </div>

    Returns:  
    The human readable summary of the incident.

    </div>

  - <div id="getEntryTime()" class="section detail">

    ### getEntryTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getEntryTime</span>()

    </div>

    <div class="block">

    Gets the time the incident was entered into the system. The value is
    null if it hasn't been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The time the incident was entered into the system.

    </div>

  - <div id="getLocation()" class="section detail">

    ### getLocation

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TrafficLocation](sdk-for-android-explore-com-here-sdk-traffic-trafficlocation "class in com.here.sdk.traffic")</span> <span class="element-name">getLocation</span>()

    </div>

    <div class="block">

    Gets the location of the incident.

    </div>

    Returns:  
    The location of the incident.

    </div>

  - <div id="getVehicleRestrictions()" class="section detail">

    ### getVehicleRestrictions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic"),[TrafficIncident.VehicleRestriction](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction "class in com.here.sdk.traffic")></span> <span class="element-name">getVehicleRestrictions</span>()

    </div>

    <div class="block">

    Gets the map of restricted vehicle categories to restrictions. A
    vehicle is restricted if at least one restriction field is
    applicable for it. If the map is empty, there're no restricted
    vehicles for the incident.

    </div>

    Returns:  
    The map of restricted vehicle categories to restrictions.

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

