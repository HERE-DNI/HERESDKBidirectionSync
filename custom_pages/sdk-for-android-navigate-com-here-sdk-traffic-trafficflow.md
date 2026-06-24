---
title: "TrafficFlow (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficflow"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficFlow.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.traffic.TrafficFlow</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficFlow</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></span></div>
<div class="block"><p>This class provides details about traffic flow along a <a href="sdk-for-android-navigate-geocorridor" title="class in com.here.sdk.core"><code>GeoCorridor</code></a>, inside a <a href="sdk-for-android-navigate-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a> or a <a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>, that represents particular path of the road network.<br/>
 Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
 For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getConfidence()">getConfidence</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the confidence field value which is normalized value between 0.0 and 1.0.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getFreeFlowSpeedInMetersPerSecond()">getFreeFlowSpeedInMetersPerSecond</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the reference speed in meters per second along the roadway when no traffic is present.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getJamFactor()">getJamFactor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a value for the amount of traffic on the roadway.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" title="class or interface in java.lang">Short</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getJamTendency()">getJamTendency</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the jam tendency field value which denotes whether the congestion is increasing, decreasing, or constant.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getJunctionsTraversability()">getJunctionsTraversability</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the traversability of junctions along the affected road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getLocation()">getLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the location of the incident.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getSpeedInMetersPerSecond()">getSpeedInMetersPerSecond</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getSpeedUncappedInMetersPerSecond()">getSpeedUncappedInMetersPerSecond</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the expected speed in meters per second along the roadway.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-traversability" title="enum class in com.here.sdk.traffic">Traversability</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflow#getTraversability()">getTraversability</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the traversability of roadway.</div>
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
<section class="detail" id="getLocation()">
<h3>getLocation</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></span> <span class="element-name">getLocation</span>()</div>
<div class="block"><p>Gets the location of the incident.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Defines the location affected by traffic flow.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedInMetersPerSecond()">
<h3>getSpeedInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getSpeedInMetersPerSecond</span>()</div>
<div class="block"><p>Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The expected speed in meters per second along the roadway; will not exceed the legal speed limit.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedUncappedInMetersPerSecond()">
<h3>getSpeedUncappedInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getSpeedUncappedInMetersPerSecond</span>()</div>
<div class="block"><p>Gets the expected speed in meters per second along the roadway.
 </p><p>It is based on probe data (GPS coordinates sent by vehicles or mobile devices driving along that roadway).
 The calculated 'expected speed' may be over the legal speed limit for that roadway because people are driving over the speed limit.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The expected speed in meters per second that a car can drive along a roadway right now; may exceed the legal speed limit.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJamTendency()">
<h3>getJamTendency</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" title="class or interface in java.lang">Short</a></span> <span class="element-name">getJamTendency</span>()</div>
<div class="block"><p>Gets the jam tendency field value which denotes whether the congestion is increasing, decreasing, or constant.
 </p><p>The congestion tendency may take the following values:
 <ul>
<li>+2 - rapidly increasing congestion</li>
<li>+1 - increasing congestion</li>
<li>0 - constant congestion</li>
<li>-1 - decreasing congestion</li>
<li>-2 - rapidly decreasing congestion
 Default value of 0 can be assumed when this attribute is not present.</li>
</ul></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The jamTendency field denotes whether the congestion is increasing, decreasing, or constant.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConfidence()">
<h3>getConfidence</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConfidence</span>()</div>
<div class="block"><p>Gets the confidence field value which is normalized value between 0.0 and 1.0.
 </p><p>It is a normalized value between 0.0 and 1.0 with the following meaning:
 <ul>
<li>0.7 &lt; confidence &lt;= 1.0 indicates real time speeds</li>
<li>0.5 &lt; confidence &lt;= 0.7 indicates historical speeds</li>
<li>0.0 &lt; confidence &lt;= 0.5 indicates speed limit</li>
</ul>
</p><p>This field can be used to identify whether the data for a location is derived from
 real-time probe sources or historical information only.
 All confidence data 0.71 and above is based on real-time information,
 where a confidence value of 0.75 or greater indicates high confidence real-time information.
 A confidence value equal to 0.70 or lower means that the data is derived from historical data only.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The confidence field indicates the proportion of real-time data included in the speed calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTraversability()">
<h3>getTraversability</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-traversability" title="enum class in com.here.sdk.traffic">Traversability</a></span> <span class="element-name">getTraversability</span>()</div>
<div class="block"><p>Gets the traversability of roadway.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The traversability of roadway.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJunctionsTraversability()">
<h3>getJunctionsTraversability</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></span> <span class="element-name">getJunctionsTraversability</span>()</div>
<div class="block"><p>Gets the traversability of junctions along the affected road.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The traversability of junctions along the affected road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFreeFlowSpeedInMetersPerSecond()">
<h3>getFreeFlowSpeedInMetersPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getFreeFlowSpeedInMetersPerSecond</span>()</div>
<div class="block"><p>Gets the reference speed in meters per second along the roadway when no traffic is present.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficflowbase#getFreeFlowSpeedInMetersPerSecond()">getFreeFlowSpeedInMetersPerSecond</a></code> in interface <code><a href="sdk-for-android-navigate-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The reference speed in meters per second along the roadway when no traffic is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJamFactor()">
<h3>getJamFactor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getJamFactor</span>()</div>
<div class="block"><p>Gets a value for the amount of traffic on the roadway.
 </p><p>The value, between 0.0 and 10.0, indicate the expected quality of travel.
 A value of 0.0 indicates that there is no congestion on the roadway.
 As the value approaches 10.0, it indicates increasing congestion.
 A value of 10.0 is reserved to represent a blocked roadway (closure).</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-trafficflowbase#getJamFactor()">getJamFactor</a></code> in interface <code><a href="sdk-for-android-navigate-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></code></dd>
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
`
}</HTMLBlock>
