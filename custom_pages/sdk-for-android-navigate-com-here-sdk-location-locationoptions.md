---
title: "LocationOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationOptions.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.location.LocationOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LocationOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Location options that combine notification, sensor, cellular positioning, GNSS positioning and WiFi positioning options.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-cellularpositioningoptions" title="class in com.here.sdk.location">CellularPositioningOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#cellularPositioningOptions">cellularPositioningOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Cellular network positioning options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationoptions" title="class in com.here.sdk.location">NotificationOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#notificationOptions">notificationOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Positioning notification options.</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-satellitepositioningoptions" title="class in com.here.sdk.location">SatellitePositioningOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#satellitePositioningOptions">satellitePositioningOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">GNSS positioning options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sensoroptions" title="class in com.here.sdk.location">SensorOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#sensorOptions">sensorOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Positioning sensor options.</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-wifipositioningoptions" title="class in com.here.sdk.location">WifiPositioningOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#wifiPositioningOptions">wifiPositioningOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">WiFi network positioning options.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E()">LocationOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs LocationOptions from default options.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.location.LocationAccuracy)">LocationOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs LocationOptions from LocationAccuracy.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="notificationOptions">
<h3>notificationOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationoptions" title="class in com.here.sdk.location">NotificationOptions</a></span> <span class="element-name">notificationOptions</span></div>
<div class="block"><p>Positioning notification options.</p></div>
</section>
</li>
<li>
<section class="detail" id="sensorOptions">
<h3>sensorOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sensoroptions" title="class in com.here.sdk.location">SensorOptions</a></span> <span class="element-name">sensorOptions</span></div>
<div class="block"><p>Positioning sensor options.</p></div>
</section>
</li>
<li>
<section class="detail" id="cellularPositioningOptions">
<h3>cellularPositioningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-cellularpositioningoptions" title="class in com.here.sdk.location">CellularPositioningOptions</a></span> <span class="element-name">cellularPositioningOptions</span></div>
<div class="block"><p>Cellular network positioning options.</p></div>
</section>
</li>
<li>
<section class="detail" id="satellitePositioningOptions">
<h3>satellitePositioningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-satellitepositioningoptions" title="class in com.here.sdk.location">SatellitePositioningOptions</a></span> <span class="element-name">satellitePositioningOptions</span></div>
<div class="block"><p>GNSS positioning options.</p></div>
</section>
</li>
<li>
<section class="detail" id="wifiPositioningOptions">
<h3>wifiPositioningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-wifipositioningoptions" title="class in com.here.sdk.location">WifiPositioningOptions</a></span> <span class="element-name">wifiPositioningOptions</span></div>
<div class="block"><p>WiFi network positioning options.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>LocationOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationOptions</span>()</div>
<div class="block"><p>Constructs LocationOptions from default options.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.location.LocationAccuracy)">
<h3>LocationOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div class="block"><p>Constructs LocationOptions from LocationAccuracy. Returned LocationOptions
 instance has default options for given LocationAccuracy set.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - <p>LocationAccuracy to define the LocationOptions.</p></dd>
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
