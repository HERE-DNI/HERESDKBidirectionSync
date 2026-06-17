---
title: "TrafficIncident (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficincident"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficIncident.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.traffic.TrafficIncident</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficIncident</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></span></div>
<div class="block"><p>TrafficIncident provides details about a traffic incident.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></code></div>
<div class="col-last even-row-color">
<div class="block">The vehicle categories that can be restricted.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincident.vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The vehicle restriction representing a vehicle category and relevant restriction rules.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getCodes()">getCodes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the human readable description of the incident, possibly with location information.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getEndTime()">getEndTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the time until which the incident is valid, after this time the incident should not be considered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getEntryTime()">getEntryTime</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the time the incident was entered into the system.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getId()">getId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the unique current identifier for a traffic incident.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getImpact()">getImpact</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the impact of the incident.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getJunctionsTraversability()">getJunctionsTraversability</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the traversability of junctions along the affected road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getLocation()">getLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the location of the incident.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getOriginalId()">getOriginalId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the unique identifier of the first traffic incident.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getParentId()">getParentId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the identifier of another incident to which this incident is linked.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getStartTime()">getStartTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the time from which the incident is valid, before this time the incident should not be considered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getSummary()">getSummary</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the human readable summary of the incident.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the category of the incident.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>,<wbr/><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincident.vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getVehicleRestrictions()">getVehicleRestrictions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map of restricted vehicle categories to restrictions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isRoadClosed()">isRoadClosed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the flag indicating whether road is closed or not.</div>
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
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block"><p>Gets the unique current identifier for a traffic incident.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The unique current identifier for a traffic incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalId()">
<h3>getOriginalId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOriginalId</span>()</div>
<div class="block"><p>Gets the unique identifier of the first traffic incident.
 </p><p>The original id remains the same whenever the traffic incident is updated and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getId()"><code>getId()</code></a> is changed.
 Once an incident chain has been created, this value will never change.
 The traffic incident an be looked up by original id using <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)"><code>TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The unique identifier of the first traffic incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentId()">
<h3>getParentId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getParentId</span>()</div>
<div class="block"><p>Gets the identifier of another incident to which this incident is linked.
 </p><p>The value is <code>null</code> if the incident doesn't have a parent.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The identifier of another incident to which this incident is linked.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJunctionsTraversability()">
<h3>getJunctionsTraversability</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></span> <span class="element-name">getJunctionsTraversability</span>()</div>
<div class="block"><p>Gets the traversability of junctions along the affected road.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The traversability of junctions along the affected road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRoadClosed()">
<h3>isRoadClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRoadClosed</span>()</div>
<div class="block"><p>Gets the flag indicating whether road is closed or not.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The flag indicates whether road is closed or not.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCodes()">
<h3>getCodes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">getCodes</span>()</div>
<div class="block"><p>Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.
 </p><p>Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSummary()">
<h3>getSummary</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">getSummary</span>()</div>
<div class="block"><p>Gets the human readable summary of the incident.
 </p><p>The summary field provides a short version of the description containing no location information.
 The expected summary language can be managed
 via <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentsqueryoptions#languageCode"><code>TrafficIncidentsQueryOptions.languageCode</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentlookupoptions#languageCode"><code>TrafficIncidentLookupOptions.languageCode</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The human readable summary of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEntryTime()">
<h3>getEntryTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">getEntryTime</span>()</div>
<div class="block"><p>Gets the time the incident was entered into the system.
 </p><p>The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The time the incident was entered into the system.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocation()">
<h3>getLocation</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></span> <span class="element-name">getLocation</span>()</div>
<div class="block"><p>Gets the location of the incident.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The location of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVehicleRestrictions()">
<h3>getVehicleRestrictions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>,<wbr/><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincident.vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a>&gt;</span> <span class="element-name">getVehicleRestrictions</span>()</div>
<div class="block"><p>Gets the map of restricted vehicle categories to restrictions.
 </p><p>A vehicle is restricted if at least one restriction field is applicable for it.
 If the map is empty, there're no restricted vehicles for the incident.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The map of restricted vehicle categories to restrictions.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImpact()">
<h3>getImpact</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></span> <span class="element-name">getImpact</span>()</div>
<div class="block"><p>Gets the impact of the incident.
 </p><p>The value is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentimpact#UNKNOWN"><code>TrafficIncidentImpact.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase#getImpact()">getImpact</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The impact of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></span> <span class="element-name">getType</span>()</div>
<div class="block"><p>Gets the category of the incident.
 </p><p>The value is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidenttype#UNKNOWN"><code>TrafficIncidentType.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase#getType()">getType</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The category of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block"><p>Gets the human readable description of the incident, possibly with location information.
 </p><p>The description is currently not present in our map data. Therefore, when
 accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
 always an empty string is returned. This does not apply when using the <code>TrafficEngine</code>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase#getDescription()">getDescription</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The human readable description of the incident, possibly with location information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStartTime()">
<h3>getStartTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">getStartTime</span>()</div>
<div class="block"><p>Gets the time from which the incident is valid, before this time the incident should not be considered.
 </p><p>The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase#getStartTime()">getStartTime</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The time from which the incident is valid, before this time the incident should not be considered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndTime()">
<h3>getEndTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">getEndTime</span>()</div>
<div class="block"><p>Get the time until which the incident is valid, after this time the incident should not be considered.
 </p><p>The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase#getEndTime()">getEndTime</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The time until which the incident is valid, after this time the incident should not be considered.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
