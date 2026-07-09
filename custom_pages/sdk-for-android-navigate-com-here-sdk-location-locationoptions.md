---
title: "LocationOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.location.LocationOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LocationOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Location options that combine notification, sensor, cellular positioning, GNSS positioning and WiFi positioning options.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-location-cellularpositioningoptions" title="class in com.here.sdk.location">CellularPositioningOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#cellularPositioningOptions">cellularPositioningOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">Cellular network positioning options.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-location-notificationoptions" title="class in com.here.sdk.location">NotificationOptions</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#notificationOptions">notificationOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Positioning notification options.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions" title="class in com.here.sdk.location">SatellitePositioningOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#satellitePositioningOptions">satellitePositioningOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">GNSS positioning options.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-location-sensoroptions" title="class in com.here.sdk.location">SensorOptions</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#sensorOptions">sensorOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Positioning sensor options.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-location-wifipositioningoptions" title="class in com.here.sdk.location">WifiPositioningOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#wifiPositioningOptions">wifiPositioningOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">WiFi network positioning options.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#%3Cinit%3E()">LocationOptions</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs LocationOptions from default options.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#%3Cinit%3E(com.here.sdk.location.LocationAccuracy)">LocationOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs LocationOptions from LocationAccuracy.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="notificationOptions">
<h3>notificationOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-notificationoptions" title="class in com.here.sdk.location">NotificationOptions</a></span> <span className="element-name">notificationOptions</span></div>
<div className="block"><p>Positioning notification options.</p></div>
</section>
</li>
<li>
<section className="detail" id="sensorOptions">
<h3>sensorOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-sensoroptions" title="class in com.here.sdk.location">SensorOptions</a></span> <span className="element-name">sensorOptions</span></div>
<div className="block"><p>Positioning sensor options.</p></div>
</section>
</li>
<li>
<section className="detail" id="cellularPositioningOptions">
<h3>cellularPositioningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-cellularpositioningoptions" title="class in com.here.sdk.location">CellularPositioningOptions</a></span> <span className="element-name">cellularPositioningOptions</span></div>
<div className="block"><p>Cellular network positioning options.</p></div>
</section>
</li>
<li>
<section className="detail" id="satellitePositioningOptions">
<h3>satellitePositioningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions" title="class in com.here.sdk.location">SatellitePositioningOptions</a></span> <span className="element-name">satellitePositioningOptions</span></div>
<div className="block"><p>GNSS positioning options.</p></div>
</section>
</li>
<li>
<section className="detail" id="wifiPositioningOptions">
<h3>wifiPositioningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-wifipositioningoptions" title="class in com.here.sdk.location">WifiPositioningOptions</a></span> <span className="element-name">wifiPositioningOptions</span></div>
<div className="block"><p>WiFi network positioning options.</p></div>
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
<h3>LocationOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LocationOptions</span>()</div>
<div className="block"><p>Constructs LocationOptions from default options.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.location.LocationAccuracy)">
<h3>LocationOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LocationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div className="block"><p>Constructs LocationOptions from LocationAccuracy. Returned LocationOptions
 instance has default options for given LocationAccuracy set.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
