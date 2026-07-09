---
title: "TrafficFlowBase (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficFlowBase.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow" title="class in com.here.sdk.traffic">TrafficFlow</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TrafficFlowBase</span></div>
<div className="block"><p>This interface provides details about a traffic flow.<br/>
 For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<section className="detail" id="getFreeFlowSpeedInMetersPerSecond()">
<h3>getFreeFlowSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="return-type">double</span> <span className="element-name">getFreeFlowSpeedInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the reference speed in meters per second along the roadway when no traffic is present.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The reference speed in meters per second along the roadway when no traffic is present.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getJamFactor()">
<h3>getJamFactor</h3>
<div className="member-signature"><span className="return-type">double</span> <span className="element-name">getJamFactor</span>()</div>
<div className="block"><p>Gets a value for the amount of traffic on the roadway.
 The value, between 0.0 and 10.0, indicate the expected quality of travel.
 A value of 0.0 indicates that there is no congestion on the roadway.
 As the value approaches 10.0, it indicates increasing congestion.
 A value of 10.0 is reserved to represent a blocked roadway (closure).</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A value for the amount of traffic on the roadway.</p></dd>
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
