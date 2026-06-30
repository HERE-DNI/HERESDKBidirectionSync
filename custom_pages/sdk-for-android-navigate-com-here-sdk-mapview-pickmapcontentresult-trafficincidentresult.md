---
title: "PickMapContentResult.TrafficIncidentResult (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PickMapContentResult.TrafficIncidentResult.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-pickmapcontentresult" title="class in com.here.sdk.mapview">PickMapContentResult</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">PickMapContentResult.TrafficIncidentResult</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></span></div>
<div class="block"><p>Carries the result of picking a Carto traffic incident object.
 Description of incident is currently not present in our map data, so
 <a href="sdk-for-android-navigate-trafficincidentbase#getDescription()"><code>TrafficIncidentBase.getDescription()</code></a> always returns an empty string.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult#getCoordinates()">getCoordinates</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geographic coordinates of the traffic incident.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the human readable description of the incident, possibly with location information.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult#getEndTime()">getEndTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the time until which the incident is valid, after this time the incident should not be considered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult#getImpact()">getImpact</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the impact of the incident.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult#getOriginalId()">getOriginalId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the unique traffic event ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult#getStartTime()">getStartTime</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the time from which the incident is valid, before this time the incident should not be considered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the category of the incident.</div>
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
<section class="detail" id="getOriginalId()">
<h3>getOriginalId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOriginalId</span>()</div>
<div class="block"><p>Gets the unique traffic event ID.
 Can be referenced when checking for updated traffic information
 for the specified event.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Unique traffic event ID.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCoordinates()">
<h3>getCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCoordinates</span>()</div>
<div class="block"><p>Gets the geographic coordinates of the traffic incident.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the traffic incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImpact()">
<h3>getImpact</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></span> <span class="element-name">getImpact</span>()</div>
<div class="block"><p>Gets the impact of the incident.
 The value is <a href="sdk-for-android-navigate-trafficincidentimpact#UNKNOWN"><code>TrafficIncidentImpact.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getImpact()">getImpact</a></code> in interface <code><a href="sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The impact of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></span> <span class="element-name">getType</span>()</div>
<div class="block"><p>Gets the category of the incident.
 The value is <a href="sdk-for-android-navigate-trafficincidenttype#UNKNOWN"><code>TrafficIncidentType.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getType()">getType</a></code> in interface <code><a href="sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The category of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block"><p>Gets the human readable description of the incident, possibly with location information.
 The description is currently not present in our map data. Therefore, when
 accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
 always an empty string is returned. This does not apply when using the <code>TrafficEngine</code>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getDescription()">getDescription</a></code> in interface <code><a href="sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
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
 The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getStartTime()">getStartTime</a></code> in interface <code><a href="sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
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
 The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficincidentbase#getEndTime()">getEndTime</a></code> in interface <code><a href="sdk-for-android-navigate-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
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
`
}</HTMLBlock>
