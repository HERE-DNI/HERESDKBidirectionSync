---
title: "TrafficOnSpan (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-trafficonspan"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficOnSpan.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.TrafficOnSpan</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TrafficOnSpan</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Traffic information of a span along a route.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#baseSpeedInMetersPerSecond">baseSpeedInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">The speed, in meters per second, without taking traffic into consideration.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#consumptionInKilowattHours">consumptionInKilowattHours</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The power consumption in kilowatt-hours (kWh) necessary to traverse the span.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#duration">duration</a></code></div>
<div className="col-last even-row-color">
<div className="block">The time duration necessary to traverse the traffic span.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#incidentIndices">incidentIndices</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The indices of traffic incidents from the field <a href="sdk-for-android-navigate-trafficonsection#trafficIncidents"><code>TrafficOnSection.trafficIncidents</code></a>.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#jamFactor">jamFactor</a></code></div>
<div className="col-last even-row-color">
<div className="block">The traffic jam factor shows the traffic condition in a numeric way.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#lengthInMeters">lengthInMeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Length of the traffic span, in meters.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#trafficDelay">trafficDelay</a></code></div>
<div className="col-last even-row-color">
<div className="block">The estimated extra time in seconds spent due to traffic delays along this traffic span.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#trafficSectionPolylineOffset">trafficSectionPolylineOffset</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Index over <a href="sdk-for-android-navigate-trafficonsection#geometry"><code>TrafficOnSection.geometry</code></a> where this span starts.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#trafficSpeedInMetersPerSecond">trafficSpeedInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">The speed, in meters per second, considering traffic.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-trafficonspan#%3Cinit%3E()">TrafficOnSpan</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="trafficSectionPolylineOffset">
<h3>trafficSectionPolylineOffset</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">trafficSectionPolylineOffset</span></div>
<div className="block"><p>Index over <a href="sdk-for-android-navigate-trafficonsection#geometry"><code>TrafficOnSection.geometry</code></a> where this span starts.</p></div>
</section>
</li>
<li>
<section className="detail" id="lengthInMeters">
<h3>lengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">lengthInMeters</span></div>
<div className="block"><p>Length of the traffic span, in meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="duration">
<h3>duration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">duration</span></div>
<div className="block"><p>The time duration necessary to traverse the traffic span. This duration takes also into
 consideration the delays caused by the traffic.</p></div>
</section>
</li>
<li>
<section className="detail" id="trafficDelay">
<h3>trafficDelay</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">trafficDelay</span></div>
<div className="block"><p>The estimated extra time in seconds spent due to traffic delays along this traffic span.
 Negative values indicate that the traffic span can be traversed faster than usual.</p></div>
</section>
</li>
<li>
<section className="detail" id="baseSpeedInMetersPerSecond">
<h3>baseSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">baseSpeedInMetersPerSecond</span></div>
<div className="block"><p>The speed, in meters per second, without taking traffic into consideration.</p></div>
</section>
</li>
<li>
<section className="detail" id="trafficSpeedInMetersPerSecond">
<h3>trafficSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">trafficSpeedInMetersPerSecond</span></div>
<div className="block"><p>The speed, in meters per second, considering traffic.</p></div>
</section>
</li>
<li>
<section className="detail" id="jamFactor">
<h3>jamFactor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">jamFactor</span></div>
<div className="block"><p>The traffic jam factor shows the traffic condition in a numeric way. It is a
 value in the range [0.0, 10.0]. A large jamFactor value means more traffic jam
 in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.</p></div>
</section>
</li>
<li>
<section className="detail" id="incidentIndices">
<h3>incidentIndices</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">incidentIndices</span></div>
<div className="block"><p>The indices of traffic incidents from the field <a href="sdk-for-android-navigate-trafficonsection#trafficIncidents"><code>TrafficOnSection.trafficIncidents</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="consumptionInKilowattHours">
<h3>consumptionInKilowattHours</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">consumptionInKilowattHours</span></div>
<div className="block"><p>The power consumption in kilowatt-hours (kWh) necessary to traverse the span.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>TrafficOnSpan</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TrafficOnSpan</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
