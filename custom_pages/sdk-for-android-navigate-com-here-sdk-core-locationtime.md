---
title: "LocationTime (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-locationtime"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationTime.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.LocationTime</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LocationTime</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>This struct presents all the time data tied to a location, like an arrival or departure time.
 The time data is originally specified in RFC 3339, section 5.6 format. For example,
 "2022-03-23T16:07:31+01:00" in Cracow, Poland, i.e. a Central European Time (CET) location.
 Note that this struct doesn't give any data on the tied location. The location should be derived
 from the context.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-locationtime#localTime">localTime</a></code></div>
<div className="col-last even-row-color">
<div className="block">The time as observed in the tied location.</div>
</div>
<div className="col-first odd-row-color"><code>final <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-locationtime#utcOffset">utcOffset</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC)
 in seconds.</div>
</div>
<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-locationtime#utcTime">utcTime</a></code></div>
<div className="col-last even-row-color">
<div className="block">The time as Coordinated Universal Time (UTC).</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-locationtime#%3Cinit%3E(java.util.Date,java.util.Date,com.here.time.Duration)">LocationTime</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> localTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> utcTime,
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> utcOffset)</code></div>
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
<section className="detail" id="localTime">
<h3>localTime</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">localTime</span></div>
<div className="block"><p>The time as observed in the tied location. For example, if a route is requested in Cracow,
 Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.</p></div>
</section>
</li>
<li>
<section className="detail" id="utcTime">
<h3>utcTime</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">utcTime</span></div>
<div className="block"><p>The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland,
 the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.</p></div>
</section>
</li>
<li>
<section className="detail" id="utcOffset">
<h3>utcOffset</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">utcOffset</span></div>
<div className="block"><p>The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC)
 in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is
 UTC-05:00, it is -18000.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.util.Date,java.util.Date,com.here.time.Duration)">
<h3>LocationTime</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LocationTime</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> localTime,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> utcTime,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> utcOffset)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>localTime</code> - <p>The time as observed in the tied location. For example, if a route is requested in Cracow,
 Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.</p></dd>
<dd><code>utcTime</code> - <p>The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland,
 the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.</p></dd>
<dd><code>utcOffset</code> - <p>The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC)
 in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is
 UTC-05:00, it is -18000.</p></dd>
</dl>
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
