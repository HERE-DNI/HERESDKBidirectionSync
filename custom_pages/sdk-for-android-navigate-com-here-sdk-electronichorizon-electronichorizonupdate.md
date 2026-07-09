---
title: "ElectronicHorizonUpdate (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ElectronicHorizonUpdate.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonUpdate</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ElectronicHorizonUpdate</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class representing a full update delivered via <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> notifications.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizon" title="class in com.here.sdk.electronichorizon">ElectronicHorizon</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate#electronicHorizon">electronicHorizon</a></code></div>
<div className="col-last even-row-color">
<div className="block">The full electronic horizon recomputed for the current vehicle state.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPosition</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate#position">position</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The vehicle’s updated position relative to the electronic horizon.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentchanges" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentChanges</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate#segmentChanges">segmentChanges</a></code></div>
<div className="col-last even-row-color">
<div className="block">The difference between the previously emitted horizon and the newly computed one.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate#%3Cinit%3E(com.here.sdk.electronichorizon.ElectronicHorizonPosition)">ElectronicHorizonUpdate</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPosition</a> position)</code></div>
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
<section className="detail" id="electronicHorizon">
<h3>electronicHorizon</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizon" title="class in com.here.sdk.electronichorizon">ElectronicHorizon</a></span> <span className="element-name">electronicHorizon</span></div>
<div className="block"><p>The full electronic horizon recomputed for the current vehicle state.
 May be <code>null</code> if there is no update.
 Contains the complete set of preferred paths.</p></div>
</section>
</li>
<li>
<section className="detail" id="segmentChanges">
<h3>segmentChanges</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentchanges" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentChanges</a></span> <span className="element-name">segmentChanges</span></div>
<div className="block"><p>The difference between the previously emitted horizon and the newly computed one.
 Contains added and removed segments.
 May be <code>null</code> if there is no update.</p></div>
</section>
</li>
<li>
<section className="detail" id="position">
<h3>position</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPosition</a></span> <span className="element-name">position</span></div>
<div className="block"><p>The vehicle’s updated position relative to the electronic horizon.
 Always present. If no <code>electronic_horizon</code> is available, the position
 refers to the most recently known horizon.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.electronichorizon.ElectronicHorizonPosition)">
<h3>ElectronicHorizonUpdate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ElectronicHorizonUpdate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPosition</a> position)</span></div>
<div className="block"><p>Creates a new instance.
 Offline availability: This property is available online and offline.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>The vehicle’s updated position relative to the electronic horizon.
 Always present. If no <code>electronic_horizon</code> is available, the position
 refers to the most recently known horizon.</p></dd>
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
