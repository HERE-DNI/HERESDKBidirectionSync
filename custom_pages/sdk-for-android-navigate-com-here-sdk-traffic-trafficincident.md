---
title: "TrafficIncident (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficincident"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficIncident.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.traffic.TrafficIncident</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TrafficIncident</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></span></div>
<div className="block"><p>TrafficIncident provides details about a traffic incident.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></code></div>
<div className="col-last even-row-color">
<div className="block">The vehicle categories that can be restricted.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The vehicle restriction representing a vehicle category and relevant restriction rules.</div>
</div>
</div>
</section>
</li>
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
<section className="detail" id="getId()">
<h3>getId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getId</span>()</div>
<div className="block"><p>Gets the unique current identifier for a traffic incident.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The unique current identifier for a traffic incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOriginalId()">
<h3>getOriginalId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getOriginalId</span>()</div>
<div className="block"><p>Gets the unique identifier of the first traffic incident.
 The original id remains the same whenever the traffic incident is updated and <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident#getId()"><code>getId()</code></a> is changed.
 Once an incident chain has been created, this value will never change.
 The traffic incident an be looked up by original id using <a href="sdk-for-android-navigate-trafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)"><code>TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The unique identifier of the first traffic incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getParentId()">
<h3>getParentId</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getParentId</span>()</div>
<div className="block"><p>Gets the identifier of another incident to which this incident is linked.
 The value is <code>null</code> if the incident doesn't have a parent.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The identifier of another incident to which this incident is linked.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getJunctionsTraversability()">
<h3>getJunctionsTraversability</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></span> <span className="element-name">getJunctionsTraversability</span>()</div>
<div className="block"><p>Gets the traversability of junctions along the affected road.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The traversability of junctions along the affected road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isRoadClosed()">
<h3>isRoadClosed</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isRoadClosed</span>()</div>
<div className="block"><p>Gets the flag indicating whether road is closed or not.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The flag indicates whether road is closed or not.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCodes()">
<h3>getCodes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">getCodes</span>()</div>
<div className="block"><p>Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.
 Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSummary()">
<h3>getSummary</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">getSummary</span>()</div>
<div className="block"><p>Gets the human readable summary of the incident.
 The summary field provides a short version of the description containing no location information.
 The expected summary language can be managed
 via <a href="sdk-for-android-navigate-trafficincidentsqueryoptions#languageCode"><code>TrafficIncidentsQueryOptions.languageCode</code></a> and <a href="sdk-for-android-navigate-trafficincidentlookupoptions#languageCode"><code>TrafficIncidentLookupOptions.languageCode</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The human readable summary of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEntryTime()">
<h3>getEntryTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">getEntryTime</span>()</div>
<div className="block"><p>Gets the time the incident was entered into the system.
 The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The time the incident was entered into the system.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLocation()">
<h3>getLocation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></span> <span className="element-name">getLocation</span>()</div>
<div className="block"><p>Gets the location of the incident.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The location of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVehicleRestrictions()">
<h3>getVehicleRestrictions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>,<wbr/><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a>&gt;</span> <span className="element-name">getVehicleRestrictions</span>()</div>
<div className="block"><p>Gets the map of restricted vehicle categories to restrictions.
 A vehicle is restricted if at least one restriction field is applicable for it.
 If the map is empty, there're no restricted vehicles for the incident.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The map of restricted vehicle categories to restrictions.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getImpact()">
<h3>getImpact</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></span> <span className="element-name">getImpact</span>()</div>
<div className="block"><p>Gets the impact of the incident.
 The value is <a href="sdk-for-android-navigate-trafficincidentimpact#UNKNOWN"><code>TrafficIncidentImpact.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getImpact()">getImpact</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The impact of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getType()">
<h3>getType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></span> <span className="element-name">getType</span>()</div>
<div className="block"><p>Gets the category of the incident.
 The value is <a href="sdk-for-android-navigate-trafficincidenttype#UNKNOWN"><code>TrafficIncidentType.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getType()">getType</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The category of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDescription()">
<h3>getDescription</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">getDescription</span>()</div>
<div className="block"><p>Gets the human readable description of the incident, possibly with location information.
 The description is currently not present in our map data. Therefore, when
 accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
 always an empty string is returned. This does not apply when using the <code>TrafficEngine</code>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getDescription()">getDescription</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The human readable description of the incident, possibly with location information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStartTime()">
<h3>getStartTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">getStartTime</span>()</div>
<div className="block"><p>Gets the time from which the incident is valid, before this time the incident should not be considered.
 The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getStartTime()">getStartTime</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The time from which the incident is valid, before this time the incident should not be considered.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEndTime()">
<h3>getEndTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">getEndTime</span>()</div>
<div className="block"><p>Get the time until which the incident is valid, after this time the incident should not be considered.
 The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getEndTime()">getEndTime</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
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

</div>
</div>



</div>
`
}</HTMLBlock>
