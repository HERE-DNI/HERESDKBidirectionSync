---
title: "PickMapContentResult.TrafficIncidentResult (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PickMapContentResult.TrafficIncidentResult.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></code></dd>
</dl>
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult" title="class in com.here.sdk.mapview">PickMapContentResult</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">PickMapContentResult.TrafficIncidentResult</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></span></div>
<div className="block"><p>Carries the result of picking a Carto traffic incident object.
 Description of incident is currently not present in our map data, so
 <a href="sdk-for-android-navigate-trafficincidentbase#getDescription()"><code>TrafficIncidentBase.getDescription()</code></a> always returns an empty string.</p></div>
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
<section className="detail" id="getOriginalId()">
<h3>getOriginalId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getOriginalId</span>()</div>
<div className="block"><p>Gets the unique traffic event ID.
 Can be referenced when checking for updated traffic information
 for the specified event.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Unique traffic event ID.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCoordinates()">
<h3>getCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCoordinates</span>()</div>
<div className="block"><p>Gets the geographic coordinates of the traffic incident.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the traffic incident.</p></dd>
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
