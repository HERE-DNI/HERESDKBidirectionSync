---
title: "TrafficIncidentBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficIncidentBase.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.traffic</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-pickmapcontentresult.trafficincidentresult" title="class in com.here.sdk.mapview">PickMapContentResult.TrafficIncidentResult</a></code>, <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a></code>, <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincidentonroute" title="class in com.here.sdk.routing">TrafficIncidentOnRoute</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TrafficIncidentBase</span></div>
<div class="block"><p>TrafficIncident provides details about a traffic incident.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getDescription()">getDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the human readable description of the incident, possibly with location information.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getEndTime()">getEndTime</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get the time until which the incident is valid, after this time the incident should not be considered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getImpact()">getImpact</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the impact of the incident.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getStartTime()">getStartTime</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the time from which the incident is valid, before this time the incident should not be considered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the category of the incident.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="getImpact()">
<h3>getImpact</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></span> <span class="element-name">getImpact</span>()</div>
<div class="block"><p>Gets the impact of the incident.
 </p><p>The value is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincidentimpact#UNKNOWN"><code>TrafficIncidentImpact.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The impact of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></span> <span class="element-name">getType</span>()</div>
<div class="block"><p>Gets the category of the incident.
 </p><p>The value is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-trafficincidenttype#UNKNOWN"><code>TrafficIncidentType.UNKNOWN</code></a> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The category of the incident.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block"><p>Gets the human readable description of the incident, possibly with location information.
 </p><p>The description is currently not present in our map data. Therefore, when
 accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
 always an empty string is returned. This does not apply when using the <code>TrafficEngine</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The human readable description of the incident, possibly with location information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStartTime()">
<h3>getStartTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">getStartTime</span>()</div>
<div class="block"><p>Gets the time from which the incident is valid, before this time the incident should not be considered.
 </p><p>The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The time from which the incident is valid, before this time the incident should not be considered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndTime()">
<h3>getEndTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">getEndTime</span>()</div>
<div class="block"><p>Get the time until which the incident is valid, after this time the incident should not be considered.
 </p><p>The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.</p></div>
<dl class="notes">
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
