---
title: "Section (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-section"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.Section → com.here.NativeBase com.here.sdk.routing.Section → com.here.sdk.routing.Section

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">Section</span> <span class="extends-implements">extends [NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A section is a part of the route between two stopovers. A stopover is a location on the route where a stop is made. Note: A section contains a list of SectionNotice objects that describe potential issues after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

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

  [`LocationTime`](sdk-for-android-explore-com-here-sdk-core-locationtime "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getArrivalLocationTime ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the arrival location time of this section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`RoutePlace`](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getArrivalPlace ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the arrival place.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBoundingBox ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the closest rectangular area where this section fits in.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getConsumptionInKilowattHours ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LocationTime`](sdk-for-android-explore-com-here-sdk-core-locationtime "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDepartureLocationTime ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the departure location time of this section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`RoutePlace`](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDeparturePlace ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the departure place.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDuration ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the estimated time in seconds needed to travel along this section, including real-time traffic delays if available.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoPolyline`](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometry ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the GeoPolyline object representing the polyline of this section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`IndoorSectionDetails`](sdk-for-android-explore-com-here-sdk-routing-indoorsectiondetails "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIndoorSectionDetails ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets indoor routing section details.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLengthInMeters ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of this section in meters.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`Maneuver`](sdk-for-android-explore-com-here-sdk-routing-maneuver "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuvers ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the maneuvers for this section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`ViolatedRestriction`](sdk-for-android-explore-com-here-sdk-routing-violatedrestriction "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNoThroughRestrictions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  list of no through restriction.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`PassThroughWaypoint`](sdk-for-android-explore-com-here-sdk-routing-passthroughwaypoint "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPassthroughWaypoints ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of passthrough waypoints in this section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`PostAction`](sdk-for-android-explore-com-here-sdk-routing-postaction "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPostActions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the post actions that must be done after the arrival at the end of the section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`PreAction`](sdk-for-android-explore-com-here-sdk-routing-preaction "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPreActions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the preceding actions that must be done prior to departure at the beginning of the section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`SectionNotice`](sdk-for-android-explore-com-here-sdk-routing-sectionnotice "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSectionNotices ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the notices which explains the issues encountered during processing of this section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`SectionTransportMode`](sdk-for-android-explore-com-here-sdk-routing-sectiontransportmode "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSectionTransportMode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the transport mode of this section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`Span`](sdk-for-android-explore-com-here-sdk-routing-span "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpans ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the Span 's that constitute this section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`Toll`](sdk-for-android-explore-com-here-sdk-routing-toll "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTolls ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets all the tolls for this section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficDelay ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the estimated extra time in seconds spent due to traffic delays along this section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`TrafficIncidentOnRoute`](sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficIncidents ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  the list of traffic incidents that are found on the section.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TransitSectionDetails`](sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTransitDetails ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the details of a transit section.

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

  - <div id="sdk-for-android-explore-getGeometry" class="section detail">

    ### getGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core")</span> <span class="element-name">getGeometry</span>()

    </div>

    <div class="block">

    Gets the GeoPolyline object representing the polyline of this section.

    </div>

    Returns:  
    The [`GeoPolyline`](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core") object representing the polyline of this section.

    </div>

  - <div id="sdk-for-android-explore-getSpans" class="section detail">

    ### getSpans

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Span](sdk-for-android-explore-com-here-sdk-routing-span "class in com.here.sdk.routing")\></span> <span class="element-name">getSpans</span>()

    </div>

    <div class="block">

    Gets the Span 's that constitute this section.

    </div>

    Returns:  
    The [`Span`](sdk-for-android-explore-com-here-sdk-routing-span "class in com.here.sdk.routing")'s that constitute this section.

    </div>

  - <div id="sdk-for-android-explore-getManeuvers" class="section detail">

    ### getManeuvers

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Maneuver](sdk-for-android-explore-com-here-sdk-routing-maneuver "class in com.here.sdk.routing")\></span> <span class="element-name">getManeuvers</span>()

    </div>

    <div class="block">

    Gets the maneuvers for this section.

    </div>

    Returns:  
    The maneuvers for this section.

    </div>

  - <div id="sdk-for-android-explore-getBoundingBox" class="section detail">

    ### getBoundingBox

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">getBoundingBox</span>()

    </div>

    <div class="block">

    Gets the closest rectangular area where this section fits in.

    </div>

    Returns:  
    The closest rectangular area where this section fits in.

    </div>

  - <div id="sdk-for-android-explore-getLengthInMeters" class="section detail">

    ### getLengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()

    </div>

    <div class="block">

    Gets the length of this section in meters.

    </div>

    Returns:  
    The length of this section in meters.

    </div>

  - <div id="sdk-for-android-explore-getSectionTransportMode" class="section detail">

    ### getSectionTransportMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[SectionTransportMode](sdk-for-android-explore-com-here-sdk-routing-sectiontransportmode "enum class in com.here.sdk.routing")</span> <span class="element-name">getSectionTransportMode</span>()

    </div>

    <div class="block">

    Gets the transport mode of this section.

    </div>

    Returns:  
    The transport mode of this section.

    </div>

  - <div id="sdk-for-android-explore-getDeparturePlace" class="section detail">

    ### getDeparturePlace

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")</span> <span class="element-name">getDeparturePlace</span>()

    </div>

    <div class="block">

    Gets the departure place.

    </div>

    Returns:  
    Describes the departure place.

    </div>

  - <div id="sdk-for-android-explore-getArrivalPlace" class="section detail">

    ### getArrivalPlace

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")</span> <span class="element-name">getArrivalPlace</span>()

    </div>

    <div class="block">

    Gets the arrival place. Describes the arrival place.

    </div>

    Returns:  
    The arrival place.

    </div>

  - <div id="sdk-for-android-explore-getDepartureLocationTime" class="section detail">

    ### getDepartureLocationTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[LocationTime](sdk-for-android-explore-com-here-sdk-core-locationtime "class in com.here.sdk.core")</span> <span class="element-name">getDepartureLocationTime</span>()

    </div>

    <div class="block">

    Gets the departure location time of this section.

    </div>

    Returns:  
    The departure location time of this section.

    </div>

  - <div id="sdk-for-android-explore-getArrivalLocationTime" class="section detail">

    ### getArrivalLocationTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[LocationTime](sdk-for-android-explore-com-here-sdk-core-locationtime "class in com.here.sdk.core")</span> <span class="element-name">getArrivalLocationTime</span>()

    </div>

    <div class="block">

    Gets the arrival location time of this section.

    </div>

    Returns:  
    The arrival location time of this section.

    </div>

  - <div id="sdk-for-android-explore-getPreActions" class="section detail">

    ### getPreActions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[PreAction](sdk-for-android-explore-com-here-sdk-routing-preaction "class in com.here.sdk.routing")\></span> <span class="element-name">getPreActions</span>()

    </div>

    <div class="block">

    Gets the preceding actions that must be done prior to departure at the beginning of the section.

    </div>

    Returns:  
    The preceding actions that must be done prior to departure at the beginning of the section.

    </div>

  - <div id="sdk-for-android-explore-getPostActions" class="section detail">

    ### getPostActions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[PostAction](sdk-for-android-explore-com-here-sdk-routing-postaction "class in com.here.sdk.routing")\></span> <span class="element-name">getPostActions</span>()

    </div>

    <div class="block">

    Gets the post actions that must be done after the arrival at the end of the section.

    </div>

    Returns:  
    The post actions that must be done after the arrival at the end of the section.

    </div>

  - <div id="sdk-for-android-explore-getSectionNotices" class="section detail">

    ### getSectionNotices

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[SectionNotice](sdk-for-android-explore-com-here-sdk-routing-sectionnotice "class in com.here.sdk.routing")\></span> <span class="element-name">getSectionNotices</span>()

    </div>

    <div class="block">

    Gets the notices which explains the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding.

    </div>

    Returns:  
    The notices which explain the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding.

    </div>

  - <div id="sdk-for-android-explore-getIndoorSectionDetails" class="section detail">

    ### getIndoorSectionDetails

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[IndoorSectionDetails](sdk-for-android-explore-com-here-sdk-routing-indoorsectiondetails "class in com.here.sdk.routing")</span> <span class="element-name">getIndoorSectionDetails</span>()

    </div>

    <div class="block">

    Gets indoor routing section details.

    </div>

    Returns:  
    Indoor routing section information.

    </div>

  - <div id="sdk-for-android-explore-getConsumptionInKilowattHours" class="section detail">

    ### getConsumptionInKilowattHours

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConsumptionInKilowattHours</span>()

    </div>

    <div class="block">

    Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

    </div>

    Returns:  
    Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

    </div>

  - <div id="sdk-for-android-explore-getTransitDetails" class="section detail">

    ### getTransitDetails

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[TransitSectionDetails](sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails "class in com.here.sdk.routing")</span> <span class="element-name">getTransitDetails</span>()

    </div>

    <div class="block">

    Gets the details of a transit section.

    </div>

    Returns:  
    The transit details which are avilable for transit sections of a route.

    </div>

  - <div id="sdk-for-android-explore-getTolls" class="section detail">

    ### getTolls

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Toll](sdk-for-android-explore-com-here-sdk-routing-toll "class in com.here.sdk.routing")\></span> <span class="element-name">getTolls</span>()

    </div>

    <div class="block">

    Gets all the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too. Note : If you're using the OfflineRoutingEngine , be aware that this feature is currently in beta . As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the OfflineRoutingEngine is only available with the Navigate license. If you're using the RoutingEngine , this feature is considered to be stable.

    </div>

    Returns:  
    All the tolls for this section.

    </div>

  - <div id="sdk-for-android-explore-getTrafficIncidents" class="section detail">

    ### getTrafficIncidents

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[TrafficIncidentOnRoute](sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute "class in com.here.sdk.routing")\></span> <span class="element-name">getTrafficIncidents</span>()

    </div>

    <div class="block">

    the list of traffic incidents that are found on the section.

    </div>

    Returns:  
    The list of traffic incidents that are found on the section.

    </div>

  - <div id="sdk-for-android-explore-getDuration" class="section detail">

    ### getDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getDuration</span>()

    </div>

    <div class="block">

    Gets the estimated time in seconds needed to travel along this section, including real-time traffic delays if available.

    </div>

    Returns:  
    The estimated time in seconds needed to travel along this section, including real-time traffic delays if available.

    </div>

  - <div id="sdk-for-android-explore-getTrafficDelay" class="section detail">

    ### getTrafficDelay

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getTrafficDelay</span>()

    </div>

    <div class="block">

    Gets the estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual.

    </div>

    Returns:  
    The estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual.

    </div>

  - <div id="sdk-for-android-explore-getPassthroughWaypoints" class="section detail">

    ### getPassthroughWaypoints

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[PassThroughWaypoint](sdk-for-android-explore-com-here-sdk-routing-passthroughwaypoint "class in com.here.sdk.routing")\></span> <span class="element-name">getPassthroughWaypoints</span>()

    </div>

    <div class="block">

    Gets the list of passthrough waypoints in this section.

    </div>

    Returns:  
    The list of passthrough waypoints in this section.

    </div>

  - <div id="sdk-for-android-explore-getNoThroughRestrictions" class="section detail">

    ### getNoThroughRestrictions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[ViolatedRestriction](sdk-for-android-explore-com-here-sdk-routing-violatedrestriction "class in com.here.sdk.routing")\></span> <span class="element-name">getNoThroughRestrictions</span>()

    </div>

    <div class="block">

    list of no through restriction.

    </div>

    Returns:  
    The list of no through restriction The no through restriction area is part of the road network that do not allow through traffic. For example the `Resident only` sign indicates that vehicles are only allowed to enter this area if they are making a stop. This area will be set only if `origin, destination` or `via` waypoint will be requested within the area.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

