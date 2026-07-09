---
title: "PickMapContentResult.TrafficIncidentResult (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult → com.here.NativeBase com.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult → com.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">`TrafficIncidentBase`</a>

<!-- -->

Enclosing class:  
<a href="sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult" title="class in com.here.sdk.mapview">PickMapContentResult</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">PickMapContentResult.TrafficIncidentResult</span> <span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></span>

</div>

<div class="block">

Carries the result of picking a Carto traffic incident object. Description of incident is currently not present in our map data, so TrafficIncidentBase.getDescription() always returns an empty string.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCoordinates ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the geographic coordinates of the traffic incident.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDescription ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the human readable description of the incident, possibly with location information.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEndTime ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Get the time until which the incident is valid, after this time the incident should not be considered.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact" title="enum class in com.here.sdk.traffic">`TrafficIncidentImpact`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getImpact ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the impact of the incident.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOriginalId ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the unique traffic event ID.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStartTime ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the time from which the incident is valid, before this time the incident should not be considered.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">`TrafficIncidentType`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getType ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the category of the incident.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-getOriginalId" class="section detail">

    ### getOriginalId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getOriginalId</span>()

    </div>

    <div class="block">

    Gets the unique traffic event ID. Can be referenced when checking for updated traffic information for the specified event.

    </div>

    Returns:  
    Unique traffic event ID.

    </div>

  - <div id="sdk-for-android-explore-getCoordinates" class="section detail">

    ### getCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCoordinates</span>()

    </div>

    <div class="block">

    Gets the geographic coordinates of the traffic incident.

    </div>

    Returns:  
    The geographic coordinates of the traffic incident.

    </div>

  - <div id="sdk-for-android-explore-getImpact" class="section detail">

    ### getImpact

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></span> <span class="element-name">getImpact</span>()

    </div>

    <div class="block">

    Gets the impact of the incident. The value is TrafficIncidentImpact.UNKNOWN if it hasn't been provided by the traffic incidents supplier.

    </div>

    Specified by:  
    <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getImpact(">`getImpact`</a>) in interface <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">`TrafficIncidentBase`</a>

    Returns:  
    The impact of the incident.

    </div>

  - <div id="sdk-for-android-explore-getType" class="section detail">

    ### getType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></span> <span class="element-name">getType</span>()

    </div>

    <div class="block">

    Gets the category of the incident. The value is TrafficIncidentType.UNKNOWN if it hasn't been provided by the traffic incidents supplier.

    </div>

    Specified by:  
    <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getType(">`getType`</a>) in interface <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">`TrafficIncidentBase`</a>

    Returns:  
    The category of the incident.

    </div>

  - <div id="sdk-for-android-explore-getDescription" class="section detail">

    ### getDescription

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">getDescription</span>()

    </div>

    <div class="block">

    Gets the human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via TrafficIncidentResult , then always an empty string is returned. This does not apply when using the TrafficEngine .

    </div>

    Specified by:  
    <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getDescription(">`getDescription`</a>) in interface <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">`TrafficIncidentBase`</a>

    Returns:  
    The human readable description of the incident, possibly with location information.

    </div>

  - <div id="sdk-for-android-explore-getStartTime" class="section detail">

    ### getStartTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getStartTime</span>()

    </div>

    <div class="block">

    Gets the time from which the incident is valid, before this time the incident should not be considered. The value is null if it hasn't been provided by the traffic incidents supplier.

    </div>

    Specified by:  
    <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getStartTime(">`getStartTime`</a>) in interface <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">`TrafficIncidentBase`</a>

    Returns:  
    The time from which the incident is valid, before this time the incident should not be considered.

    </div>

  - <div id="sdk-for-android-explore-getEndTime" class="section detail">

    ### getEndTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getEndTime</span>()

    </div>

    <div class="block">

    Get the time until which the incident is valid, after this time the incident should not be considered. The value is null if it hasn't been provided by the traffic incidents supplier.

    </div>

    Specified by:  
    <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase#getEndTime(">`getEndTime`</a>) in interface <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">`TrafficIncidentBase`</a>

    Returns:  
    The time until which the incident is valid, after this time the incident should not be considered.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

