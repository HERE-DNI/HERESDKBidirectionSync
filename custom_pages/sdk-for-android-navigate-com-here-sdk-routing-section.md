---
title: "Section (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-section"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Section.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.Section</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Section</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A section is a part of the route between two stopovers.
 A stopover is a location on the route where a stop is made.
 </p><p><strong>Note:</strong> A section contains a list of <a href="sdk-for-android-navigate-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a> objects that describe
 <em>potential issues</em> after the route was calculated. If the list is non-empty, it
 is recommended to evaluate possible violations against the requested route options
 and reject the route if deemed necessary.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationtime" title="class in com.here.sdk.core">LocationTime</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getArrivalLocationTime()">getArrivalLocationTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the arrival location time of this section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-routeplace" title="class in com.here.sdk.routing">RoutePlace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getArrivalPlace()">getArrivalPlace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the arrival place.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getBoundingBox()">getBoundingBox</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the closest rectangular area where this section fits in.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getConsumptionInKilowattHours()">getConsumptionInKilowattHours</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
 is an electric vehicle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationtime" title="class in com.here.sdk.core">LocationTime</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDepartureLocationTime()">getDepartureLocationTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the departure location time of this section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-routeplace" title="class in com.here.sdk.routing">RoutePlace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDeparturePlace()">getDeparturePlace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the departure place.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDuration()">getDuration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the estimated time in seconds needed to travel along this section, including
 real-time traffic delays if available.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getGeometry()">getGeometry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this section.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-indoorsectiondetails" title="class in com.here.sdk.routing">IndoorSectionDetails</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getIndoorSectionDetails()">getIndoorSectionDetails</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets indoor routing section details.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getLengthInMeters()">getLengthInMeters</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the length of this section in meters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-maneuver" title="class in com.here.sdk.routing">Maneuver</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getManeuvers()">getManeuvers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the maneuvers for this section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getNoThroughRestrictions()">getNoThroughRestrictions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">list of no through restriction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-passthroughwaypoint" title="class in com.here.sdk.routing">PassThroughWaypoint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPassthroughWaypoints()">getPassthroughWaypoints</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of passthrough waypoints in this section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-postaction" title="class in com.here.sdk.routing">PostAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPostActions()">getPostActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the post actions that must be done after the arrival at the end of the section.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-preaction" title="class in com.here.sdk.routing">PreAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPreActions()">getPreActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the preceding actions that must be done prior to departure at the beginning of the section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-sectionnotice" title="class in com.here.sdk.routing">SectionNotice</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSectionNotices()">getSectionNotices</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the notices which explains the issues encountered during processing of this section.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSectionTransportMode()">getSectionTransportMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the transport mode of this section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-span" title="class in com.here.sdk.routing">Span</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSpans()">getSpans</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-span" title="class in com.here.sdk.routing"><code>Span</code></a>'s that constitute this section.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-toll" title="class in com.here.sdk.routing">Toll</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTolls()">getTolls</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets all the tolls for this section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrafficDelay()">getTrafficDelay</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the estimated extra time in seconds spent due to traffic delays along this section.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-trafficincidentonroute" title="class in com.here.sdk.routing">TrafficIncidentOnRoute</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrafficIncidents()">getTrafficIncidents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">the list of traffic incidents that are found on the section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-transitsectiondetails" title="class in com.here.sdk.routing">TransitSectionDetails</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTransitDetails()">getTransitDetails</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the details of a transit section.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span class="element-name">getGeometry</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpans()">
<h3>getSpans</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-span" title="class in com.here.sdk.routing">Span</a>&gt;</span> <span class="element-name">getSpans</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-span" title="class in com.here.sdk.routing"><code>Span</code></a>'s that constitute this section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-span" title="class in com.here.sdk.routing"><code>Span</code></a>'s that constitute this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuvers()">
<h3>getManeuvers</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-maneuver" title="class in com.here.sdk.routing">Maneuver</a>&gt;</span> <span class="element-name">getManeuvers</span>()</div>
<div class="block"><p>Gets the maneuvers for this section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The maneuvers for this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">getBoundingBox</span>()</div>
<div class="block"><p>Gets the closest rectangular area where this section fits in.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The closest rectangular area where this section fits in.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()</div>
<div class="block"><p>Gets the length of this section in meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The length of this section in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSectionTransportMode()">
<h3>getSectionTransportMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a></span> <span class="element-name">getSectionTransportMode</span>()</div>
<div class="block"><p>Gets the transport mode of this section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The transport mode of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeparturePlace()">
<h3>getDeparturePlace</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routeplace" title="class in com.here.sdk.routing">RoutePlace</a></span> <span class="element-name">getDeparturePlace</span>()</div>
<div class="block"><p>Gets the departure place.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Describes the departure place.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getArrivalPlace()">
<h3>getArrivalPlace</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routeplace" title="class in com.here.sdk.routing">RoutePlace</a></span> <span class="element-name">getArrivalPlace</span>()</div>
<div class="block"><p>Gets the arrival place.
 </p><p>Describes the arrival place.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The arrival place.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDepartureLocationTime()">
<h3>getDepartureLocationTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationtime" title="class in com.here.sdk.core">LocationTime</a></span> <span class="element-name">getDepartureLocationTime</span>()</div>
<div class="block"><p>Gets the departure location time of this section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The departure location time of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getArrivalLocationTime()">
<h3>getArrivalLocationTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationtime" title="class in com.here.sdk.core">LocationTime</a></span> <span class="element-name">getArrivalLocationTime</span>()</div>
<div class="block"><p>Gets the arrival location time of this section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The arrival location time of this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreActions()">
<h3>getPreActions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-preaction" title="class in com.here.sdk.routing">PreAction</a>&gt;</span> <span class="element-name">getPreActions</span>()</div>
<div class="block"><p>Gets the preceding actions that must be done prior to departure at the beginning of the section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The preceding actions that must be done prior to departure at the beginning of the section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPostActions()">
<h3>getPostActions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-postaction" title="class in com.here.sdk.routing">PostAction</a>&gt;</span> <span class="element-name">getPostActions</span>()</div>
<div class="block"><p>Gets the post actions that must be done after the arrival at the end of the section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The post actions that must be done after the arrival at the end of the section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSectionNotices()">
<h3>getSectionNotices</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-sectionnotice" title="class in com.here.sdk.routing">SectionNotice</a>&gt;</span> <span class="element-name">getSectionNotices</span>()</div>
<div class="block"><p>Gets the notices which explains the issues encountered during processing of this section.
 For example, while the scooter transport mode is selected, if no reasonable alternative route is
 possible except violating controlled-access to highway rule for the section, one notice is generated
 for the violation. The user must judge all the notices carefully before proceeding.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The notices which explain the issues encountered during processing of this section.
     For example, while the scooter transport mode is selected, if no reasonable alternative route is
     possible except violating controlled-access to highway rule for the section, one notice is generated
     for the violation. The user must judge all the notices carefully before proceeding.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndoorSectionDetails()">
<h3>getIndoorSectionDetails</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-indoorsectiondetails" title="class in com.here.sdk.routing">IndoorSectionDetails</a></span> <span class="element-name">getIndoorSectionDetails</span>()</div>
<div class="block"><p>Gets indoor routing section details.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Indoor routing section information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConsumptionInKilowattHours()">
<h3>getConsumptionInKilowattHours</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConsumptionInKilowattHours</span>()</div>
<div class="block"><p>Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
 is an electric vehicle. Note that it can be negative due to energy recuperation.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Estimated net energy consumption (in kWh) if the transportation mode used for this route
     is an electric vehicle. Note that it can be negative due to energy recuperation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransitDetails()">
<h3>getTransitDetails</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-transitsectiondetails" title="class in com.here.sdk.routing">TransitSectionDetails</a></span> <span class="element-name">getTransitDetails</span>()</div>
<div class="block"><p>Gets the details of a transit section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The transit details which are avilable for transit sections of a route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTolls()">
<h3>getTolls</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-toll" title="class in com.here.sdk.routing">Toll</a>&gt;</span> <span class="element-name">getTolls</span>()</div>
<div class="block"><p>Gets all the tolls for this section. Note that tolls are found depending on the
 transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls.
 Indoor route sections have no tolls, too.
 </p><p>Note that tolls are found depending on the transport mode.
 For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor
 route sections have no tolls, too.
 <strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
 currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
 Additionally, this feature and related APIs may be updated in future releases
 without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
 is only available with the Navigate license. If you're using the
 <code>RoutingEngine</code>, this feature is considered to be stable.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>All the tolls for this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficIncidents()">
<h3>getTrafficIncidents</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-trafficincidentonroute" title="class in com.here.sdk.routing">TrafficIncidentOnRoute</a>&gt;</span> <span class="element-name">getTrafficIncidents</span>()</div>
<div class="block"><p>the list of traffic incidents that are found on the section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of traffic incidents that are found on the section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDuration()">
<h3>getDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getDuration</span>()</div>
<div class="block"><p>Gets the estimated time in seconds needed to travel along this section, including
 real-time traffic delays if available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds needed to travel along this section, including
     real-time traffic delays if available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficDelay()">
<h3>getTrafficDelay</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getTrafficDelay</span>()</div>
<div class="block"><p>Gets the estimated extra time in seconds spent due to traffic delays along this section.
 Negative values indicate that the route can be traversed faster than usual.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The estimated extra time in seconds spent due to traffic delays along this section. Negative values
     indicate that the route can be traversed faster than usual.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPassthroughWaypoints()">
<h3>getPassthroughWaypoints</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-passthroughwaypoint" title="class in com.here.sdk.routing">PassThroughWaypoint</a>&gt;</span> <span class="element-name">getPassthroughWaypoints</span>()</div>
<div class="block"><p>Gets the list of passthrough waypoints in this section.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of passthrough waypoints in this section.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNoThroughRestrictions()">
<h3>getNoThroughRestrictions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a>&gt;</span> <span class="element-name">getNoThroughRestrictions</span>()</div>
<div class="block"><p>list of no through restriction.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>
