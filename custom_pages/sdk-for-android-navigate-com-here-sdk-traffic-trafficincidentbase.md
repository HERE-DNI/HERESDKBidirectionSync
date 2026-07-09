---
title: "TrafficIncidentBase (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentbase"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficIncidentBase.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult" title="class in com.here.sdk.mapview">PickMapContentResult.TrafficIncidentResult</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-routing-trafficincidentonroute" title="class in com.here.sdk.routing">TrafficIncidentOnRoute</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TrafficIncidentBase</span></div>
<div className="block"><p>TrafficIncident provides details about a traffic incident.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="getImpact()">
<h3>getImpact</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></span> <span className="element-name">getImpact</span>()</div>
<div className="block"><p>Gets the impact of the incident.
 The value is <a href="sdk-for-android-navigate-trafficincidentimpact#UNKNOWN"><code>TrafficIncidentImpact.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The impact of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getType()">
<h3>getType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></span> <span className="element-name">getType</span>()</div>
<div className="block"><p>Gets the category of the incident.
 The value is <a href="sdk-for-android-navigate-trafficincidenttype#UNKNOWN"><code>TrafficIncidentType.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The category of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDescription()">
<h3>getDescription</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">getDescription</span>()</div>
<div className="block"><p>Gets the human readable description of the incident, possibly with location information.
 The description is currently not present in our map data. Therefore, when
 accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
 always an empty string is returned. This does not apply when using the <code>TrafficEngine</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The human readable description of the incident, possibly with location information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStartTime()">
<h3>getStartTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">getStartTime</span>()</div>
<div className="block"><p>Gets the time from which the incident is valid, before this time the incident should not be considered.
 The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The time from which the incident is valid, before this time the incident should not be considered.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEndTime()">
<h3>getEndTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">getEndTime</span>()</div>
<div className="block"><p>Get the time until which the incident is valid, after this time the incident should not be considered.
 The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl className="notes">
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
