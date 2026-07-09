---
title: "Section (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-section"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Section.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.routing.Section</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Section</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A section is a part of the route between two stopovers.
 A stopover is a location on the route where a stop is made.
 <strong>Note:</strong> A section contains a list of <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a> objects that describe
 <em>potential issues</em> after the route was calculated. If the list is non-empty, it
 is recommended to evaluate possible violations against the requested route options
 and reject the route if deemed necessary.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span className="element-name">getGeometry</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpans()">
<h3>getSpans</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-span" title="class in com.here.sdk.routing">Span</a>&gt;</span> <span className="element-name">getSpans</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-routing-span" title="class in com.here.sdk.routing"><code>Span</code></a>'s that constitute this section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-routing-span" title="class in com.here.sdk.routing"><code>Span</code></a>'s that constitute this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getManeuvers()">
<h3>getManeuvers</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a>&gt;</span> <span className="element-name">getManeuvers</span>()</div>
<div className="block"><p>Gets the maneuvers for this section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The maneuvers for this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets the closest rectangular area where this section fits in.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The closest rectangular area where this section fits in.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getLengthInMeters</span>()</div>
<div className="block"><p>Gets the length of this section in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The length of this section in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSectionTransportMode()">
<h3>getSectionTransportMode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a></span> <span className="element-name">getSectionTransportMode</span>()</div>
<div className="block"><p>Gets the transport mode of this section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The transport mode of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDeparturePlace()">
<h3>getDeparturePlace</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing">RoutePlace</a></span> <span className="element-name">getDeparturePlace</span>()</div>
<div className="block"><p>Gets the departure place.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Describes the departure place.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getArrivalPlace()">
<h3>getArrivalPlace</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing">RoutePlace</a></span> <span className="element-name">getArrivalPlace</span>()</div>
<div className="block"><p>Gets the arrival place.
 Describes the arrival place.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The arrival place.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDepartureLocationTime()">
<h3>getDepartureLocationTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-locationtime" title="class in com.here.sdk.core">LocationTime</a></span> <span className="element-name">getDepartureLocationTime</span>()</div>
<div className="block"><p>Gets the departure location time of this section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The departure location time of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getArrivalLocationTime()">
<h3>getArrivalLocationTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-locationtime" title="class in com.here.sdk.core">LocationTime</a></span> <span className="element-name">getArrivalLocationTime</span>()</div>
<div className="block"><p>Gets the arrival location time of this section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The arrival location time of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPreActions()">
<h3>getPreActions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-preaction" title="class in com.here.sdk.routing">PreAction</a>&gt;</span> <span className="element-name">getPreActions</span>()</div>
<div className="block"><p>Gets the preceding actions that must be done prior to departure at the beginning of the section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The preceding actions that must be done prior to departure at the beginning of the section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPostActions()">
<h3>getPostActions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-postaction" title="class in com.here.sdk.routing">PostAction</a>&gt;</span> <span className="element-name">getPostActions</span>()</div>
<div className="block"><p>Gets the post actions that must be done after the arrival at the end of the section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The post actions that must be done after the arrival at the end of the section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSectionNotices()">
<h3>getSectionNotices</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing">SectionNotice</a>&gt;</span> <span className="element-name">getSectionNotices</span>()</div>
<div className="block"><p>Gets the notices which explains the issues encountered during processing of this section.
 For example, while the scooter transport mode is selected, if no reasonable alternative route is
 possible except violating controlled-access to highway rule for the section, one notice is generated
 for the violation. The user must judge all the notices carefully before proceeding.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The notices which explain the issues encountered during processing of this section.
     For example, while the scooter transport mode is selected, if no reasonable alternative route is
     possible except violating controlled-access to highway rule for the section, one notice is generated
     for the violation. The user must judge all the notices carefully before proceeding.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIndoorSectionDetails()">
<h3>getIndoorSectionDetails</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-indoorsectiondetails" title="class in com.here.sdk.routing">IndoorSectionDetails</a></span> <span className="element-name">getIndoorSectionDetails</span>()</div>
<div className="block"><p>Gets indoor routing section details.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Indoor routing section information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getConsumptionInKilowattHours()">
<h3>getConsumptionInKilowattHours</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getConsumptionInKilowattHours</span>()</div>
<div className="block"><p>Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
 is an electric vehicle. Note that it can be negative due to energy recuperation.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Estimated net energy consumption (in kWh) if the transportation mode used for this route
     is an electric vehicle. Note that it can be negative due to energy recuperation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTransitDetails()">
<h3>getTransitDetails</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-transitsectiondetails" title="class in com.here.sdk.routing">TransitSectionDetails</a></span> <span className="element-name">getTransitDetails</span>()</div>
<div className="block"><p>Gets the details of a transit section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The transit details which are avilable for transit sections of a route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTolls()">
<h3>getTolls</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-toll" title="class in com.here.sdk.routing">Toll</a>&gt;</span> <span className="element-name">getTolls</span>()</div>
<div className="block"><p>Gets all the tolls for this section. Note that tolls are found depending on the
 transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls.
 Indoor route sections have no tolls, too.
 Note that tolls are found depending on the transport mode.
 For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor
 route sections have no tolls, too.
 <strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
 currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
 Additionally, this feature and related APIs may be updated in future releases
 without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
 is only available with the Navigate license. If you're using the
 <code>RoutingEngine</code>, this feature is considered to be stable.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>All the tolls for this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficIncidents()">
<h3>getTrafficIncidents</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-trafficincidentonroute" title="class in com.here.sdk.routing">TrafficIncidentOnRoute</a>&gt;</span> <span className="element-name">getTrafficIncidents</span>()</div>
<div className="block"><p>the list of traffic incidents that are found on the section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of traffic incidents that are found on the section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDuration()">
<h3>getDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getDuration</span>()</div>
<div className="block"><p>Gets the estimated time in seconds needed to travel along this section, including
 real-time traffic delays if available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds needed to travel along this section, including
     real-time traffic delays if available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficDelay()">
<h3>getTrafficDelay</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getTrafficDelay</span>()</div>
<div className="block"><p>Gets the estimated extra time in seconds spent due to traffic delays along this section.
 Negative values indicate that the route can be traversed faster than usual.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The estimated extra time in seconds spent due to traffic delays along this section. Negative values
     indicate that the route can be traversed faster than usual.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPassthroughWaypoints()">
<h3>getPassthroughWaypoints</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-passthroughwaypoint" title="class in com.here.sdk.routing">PassThroughWaypoint</a>&gt;</span> <span className="element-name">getPassthroughWaypoints</span>()</div>
<div className="block"><p>Gets the list of passthrough waypoints in this section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of passthrough waypoints in this section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNoThroughRestrictions()">
<h3>getNoThroughRestrictions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a>&gt;</span> <span className="element-name">getNoThroughRestrictions</span>()</div>
<div className="block"><p>list of no through restriction.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of no through restriction
     The no through restriction area is part of the road network that do not allow through traffic.
     For example the <code>Resident only</code> sign indicates that vehicles are only allowed to enter this area if they are making a stop.
     This area will be set only if <code>origin</code>, <code>destination</code> or <code>via</code> waypoint will be requested within the area.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
