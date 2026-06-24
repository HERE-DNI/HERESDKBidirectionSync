---
title: "TrafficBroadcastParameters (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcastparameters"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficBroadcastParameters.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.trafficbroadcast.TrafficBroadcastParameters</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficBroadcastParameters</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents the parameters needed to request the traffic broadcast.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcastparameters#location">location</a></code></div>
<div class="col-last even-row-color">
<div class="block">Current location to determine the country code and LTNs.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-tmcserviceinterface" title="interface in com.here.sdk.trafficbroadcast">TMCServiceInterface</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcastparameters#tmcService">tmcService</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains all outgoing dependencies to the client side.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcastparameters#%3Cinit%3E(com.here.sdk.trafficbroadcast.TMCServiceInterface,com.here.sdk.core.Location)">TrafficBroadcastParameters</a><wbr/>(<a href="sdk-for-android-navigate-tmcserviceinterface" title="interface in com.here.sdk.trafficbroadcast">TMCServiceInterface</a> tmcService,
 <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
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
<section class="detail" id="tmcService">
<h3>tmcService</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tmcserviceinterface" title="interface in com.here.sdk.trafficbroadcast">TMCServiceInterface</a></span> <span class="element-name">tmcService</span></div>
<div class="block"><p>Contains all outgoing dependencies to the client side.</p></div>
</section>
</li>
<li>
<section class="detail" id="location">
<h3>location</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a></span> <span class="element-name">location</span></div>
<div class="block"><p>Current location to determine the country code and LTNs.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.trafficbroadcast.TMCServiceInterface,com.here.sdk.core.Location)">
<h3>TrafficBroadcastParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TrafficBroadcastParameters</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-tmcserviceinterface" title="interface in com.here.sdk.trafficbroadcast">TMCServiceInterface</a> tmcService,
 @NonNull
 <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tmcService</code> - <p>Contains all outgoing dependencies to the client side.</p></dd>
<dd><code>location</code> - <p>Current location to determine the country code and LTNs.</p></dd>
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
