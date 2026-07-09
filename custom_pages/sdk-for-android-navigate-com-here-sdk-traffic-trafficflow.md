---
title: "TrafficFlow (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficflow"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficFlow.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.traffic.TrafficFlow</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TrafficFlow</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></span></div>
<div className="block"><p>This class provides details about traffic flow along a <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core"><code>GeoCorridor</code></a>, inside a <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a> or a <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>, that represents particular path of the road network.<br/>
 Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
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
<section className="detail" id="getLocation()">
<h3>getLocation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></span> <span className="element-name">getLocation</span>()</div>
<div className="block"><p>Gets the location of the incident.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Defines the location affected by traffic flow.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpeedInMetersPerSecond()">
<h3>getSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getSpeedInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The expected speed in meters per second along the roadway; will not exceed the legal speed limit.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpeedUncappedInMetersPerSecond()">
<h3>getSpeedUncappedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getSpeedUncappedInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the expected speed in meters per second along the roadway.
 It is based on probe data (GPS coordinates sent by vehicles or mobile devices driving along that roadway).
 The calculated 'expected speed' may be over the legal speed limit for that roadway because people are driving over the speed limit.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The expected speed in meters per second that a car can drive along a roadway right now; may exceed the legal speed limit.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getJamTendency()">
<h3>getJamTendency</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" title="class or interface in java.lang">Short</a></span> <span className="element-name">getJamTendency</span>()</div>
<div className="block"><p>Gets the jam tendency field value which denotes whether the congestion is increasing, decreasing, or constant.
 The congestion tendency may take the following values:
 <ul>
<li>+2 - rapidly increasing congestion</li>
<li>+1 - increasing congestion</li>
<li>0 - constant congestion</li>
<li>-1 - decreasing congestion</li>
<li>-2 - rapidly decreasing congestion
 Default value of 0 can be assumed when this attribute is not present.</li>
</ul></p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The jamTendency field denotes whether the congestion is increasing, decreasing, or constant.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getConfidence()">
<h3>getConfidence</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getConfidence</span>()</div>
<div className="block"><p>Gets the confidence field value which is normalized value between 0.0 and 1.0.
 It is a normalized value between 0.0 and 1.0 with the following meaning:
 <ul>
<li>0.7 &lt; confidence &lt;= 1.0 indicates real time speeds</li>
<li>0.5 &lt; confidence &lt;= 0.7 indicates historical speeds</li>
<li>0.0 &lt; confidence &lt;= 0.5 indicates speed limit</li>
</ul>
This field can be used to identify whether the data for a location is derived from
 real-time probe sources or historical information only.
 All confidence data 0.71 and above is based on real-time information,
 where a confidence value of 0.75 or greater indicates high confidence real-time information.
 A confidence value equal to 0.70 or lower means that the data is derived from historical data only.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The confidence field indicates the proportion of real-time data included in the speed calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTraversability()">
<h3>getTraversability</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-traversability" title="enum class in com.here.sdk.traffic">Traversability</a></span> <span className="element-name">getTraversability</span>()</div>
<div className="block"><p>Gets the traversability of roadway.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The traversability of roadway.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getJunctionsTraversability()">
<h3>getJunctionsTraversability</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></span> <span className="element-name">getJunctionsTraversability</span>()</div>
<div className="block"><p>Gets the traversability of junctions along the affected road.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The traversability of junctions along the affected road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFreeFlowSpeedInMetersPerSecond()">
<h3>getFreeFlowSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getFreeFlowSpeedInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the reference speed in meters per second along the roadway when no traffic is present.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficflowbase#getFreeFlowSpeedInMetersPerSecond()">getFreeFlowSpeedInMetersPerSecond</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The reference speed in meters per second along the roadway when no traffic is present.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getJamFactor()">
<h3>getJamFactor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getJamFactor</span>()</div>
<div className="block"><p>Gets a value for the amount of traffic on the roadway.
 The value, between 0.0 and 10.0, indicate the expected quality of travel.
 A value of 0.0 indicates that there is no congestion on the roadway.
 As the value approaches 10.0, it indicates increasing congestion.
 A value of 10.0 is reserved to represent a blocked roadway (closure).</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficflowbase#getJamFactor()">getJamFactor</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></code></dd>
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
