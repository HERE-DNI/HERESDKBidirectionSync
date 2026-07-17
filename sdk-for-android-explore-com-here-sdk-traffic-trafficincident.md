---
title: "TrafficIncident (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincident"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-traffic-package-summary">com.here.sdk.traffic</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.traffic.TrafficIncident → com.here.NativeBase com.here.sdk.traffic.TrafficIncident → com.here.sdk.traffic.TrafficIncident

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">`TrafficIncidentBase`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficIncident</span> <span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></span>

</div>

<div class="block">

TrafficIncident provides details about a traffic incident.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" class="type-name-link" title="enum class in com.here.sdk.traffic"><code>TrafficIncident.RestrictedVehicleCategory</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The vehicle categories that can be restricted.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction" class="type-name-link" title="class in com.here.sdk.traffic"><code>TrafficIncident.VehicleRestriction</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The vehicle restriction representing a vehicle category and relevant restriction rules.

  </div>

  </div>

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCodes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEntryTime ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the time the incident was entered into the system.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getId ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the unique current identifier for a traffic incident.

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

  <a href="sdk-for-android-explore-com-here-sdk-traffic-junctionstraversability" title="enum class in com.here.sdk.traffic">`JunctionsTraversability`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getJunctionsTraversability ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the traversability of junctions along the affected road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficlocation" title="class in com.here.sdk.traffic">`TrafficLocation`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLocation ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the location of the incident.

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

  Gets the unique identifier of the first traffic incident.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getParentId ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the identifier of another incident to which this incident is linked.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStartTime ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the time from which the incident is valid, before this time the incident should not be considered.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSummary ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the human readable summary of the incident.

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

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">`TrafficIncident.RestrictedVehicleCategory`</a>, <wbr></wbr><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction" title="class in com.here.sdk.traffic">`TrafficIncident.VehicleRestriction`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVehicleRestrictions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map of restricted vehicle categories to restrictions.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isRoadClosed ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the flag indicating whether road is closed or not.

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

  - <div id="sdk-for-android-explore-getId" class="section detail">

    ### getId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()

    </div>

    <div class="block">

    Gets the unique current identifier for a traffic incident.

    </div>

    Returns:  
    The unique current identifier for a traffic incident.

    </div>

  - <div id="sdk-for-android-explore-getOriginalId" class="section detail">

    ### getOriginalId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getOriginalId</span>()

    </div>

    <div class="block">

    Gets the unique identifier of the first traffic incident. The original id remains the same whenever the traffic incident is updated and getId() is changed. Once an incident chain has been created, this value will never change. The traffic incident an be looked up by original id using TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback) .

    </div>

    Returns:  
    The unique identifier of the first traffic incident.

    </div>

  - <div id="sdk-for-android-explore-getParentId" class="section detail">

    ### getParentId

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getParentId</span>()

    </div>

    <div class="block">

    Gets the identifier of another incident to which this incident is linked. The value is null if the incident doesn't have a parent.

    </div>

    Returns:  
    The identifier of another incident to which this incident is linked.

    </div>

  - <div id="sdk-for-android-explore-getJunctionsTraversability" class="section detail">

    ### getJunctionsTraversability

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></span> <span class="element-name">getJunctionsTraversability</span>()

    </div>

    <div class="block">

    Gets the traversability of junctions along the affected road.

    </div>

    Returns:  
    The traversability of junctions along the affected road.

    </div>

  - <div id="sdk-for-android-explore-isRoadClosed" class="section detail">

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

  - <div id="sdk-for-android-explore-getCodes" class="section detail">

    ### getCodes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\></span> <span class="element-name">getCodes</span>()

    </div>

    <div class="block">

    Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category. Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.

    </div>

    Returns:  
    The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.

    </div>

  - <div id="sdk-for-android-explore-getSummary" class="section detail">

    ### getSummary

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">getSummary</span>()

    </div>

    <div class="block">

    Gets the human readable summary of the incident. The summary field provides a short version of the description containing no location information. The expected summary language can be managed via TrafficIncidentsQueryOptions.languageCode and TrafficIncidentLookupOptions.languageCode .

    </div>

    Returns:  
    The human readable summary of the incident.

    </div>

  - <div id="sdk-for-android-explore-getEntryTime" class="section detail">

    ### getEntryTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">getEntryTime</span>()

    </div>

    <div class="block">

    Gets the time the incident was entered into the system. The value is null if it hasn't been provided by the traffic incidents supplier.

    </div>

    Returns:  
    The time the incident was entered into the system.

    </div>

  - <div id="sdk-for-android-explore-getLocation" class="section detail">

    ### getLocation

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></span> <span class="element-name">getLocation</span>()

    </div>

    <div class="block">

    Gets the location of the incident.

    </div>

    Returns:  
    The location of the incident.

    </div>

  - <div id="sdk-for-android-explore-getVehicleRestrictions" class="section detail">

    ### getVehicleRestrictions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>,<wbr></wbr><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a>\></span> <span class="element-name">getVehicleRestrictions</span>()

    </div>

    <div class="block">

    Gets the map of restricted vehicle categories to restrictions. A vehicle is restricted if at least one restriction field is applicable for it. If the map is empty, there're no restricted vehicles for the incident.

    </div>

    Returns:  
    The map of restricted vehicle categories to restrictions.

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

