---
title: "SatellitePositioningOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SatellitePositioningOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.location.SatellitePositioningOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SatellitePositioningOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>GNSS positioning options.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions#enabled">enabled</a></code></div>
<div className="col-last even-row-color">
<div className="block">Controls GNSS positioning.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions#hdEnabled">hdEnabled</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Controls HD GNSS positioning.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions#%3Cinit%3E()">SatellitePositioningOptions</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<section className="detail" id="enabled">
<h3>enabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enabled</span></div>
<div className="block"><p>Controls GNSS positioning. If false, GNSS positioning is disabled.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="hdEnabled">
<h3>hdEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">hdEnabled</span></div>
<div className="block"><p>Controls HD GNSS positioning. If false, HD GNSS positioning is disabled.
 VDR (Vehicle Dead Reckoning) is used if HD GNSS is enabled and sensors are used for positioning.
 This feature requires Android 12 or later and dual frequency GNSS receiver and raw GNSS measurements.
 This feature is disabled by default: <a href="https://www.here.com/platform/positioning">Contact us</a> to enable it.
 If it is not enabled or the OS/device requirements are not met, fallback to other positioning technologies may occur and desired accuracy level may not be reached.
 Defaults to <code>false</code>.</p></div>
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
<h3>SatellitePositioningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SatellitePositioningOptions</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
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
