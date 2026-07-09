---
title: "ElectronicHorizonPosition (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ElectronicHorizonPosition.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonPosition</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ElectronicHorizonPosition</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Provides a position on an electronic horizon path with a reference to the current item in the <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizon" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizon</code></a>.
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



<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition#pathIndex">pathIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block">The index of the current path in the list of <a href="sdk-for-android-navigate-electronichorizon#paths"><code>ElectronicHorizon.paths</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition#pathSegmentIndex">pathSegmentIndex</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The index of the segment inside the <a href="sdk-for-android-navigate-electronichorizonpath#segments"><code>ElectronicHorizonPath.segments</code></a>.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition#pathSegmentOffsetInMeters">pathSegmentOffsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The offset from the start of the segment in meters.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition#%3Cinit%3E(int,int,double)">ElectronicHorizonPosition</a><wbr/>(int pathIndex,
 int pathSegmentIndex,
 double pathSegmentOffsetInMeters)</code></div>
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
<section className="detail" id="pathIndex">
<h3>pathIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">pathIndex</span></div>
<div className="block"><p>The index of the current path in the list of <a href="sdk-for-android-navigate-electronichorizon#paths"><code>ElectronicHorizon.paths</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="pathSegmentIndex">
<h3>pathSegmentIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">pathSegmentIndex</span></div>
<div className="block"><p>The index of the segment inside the <a href="sdk-for-android-navigate-electronichorizonpath#segments"><code>ElectronicHorizonPath.segments</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="pathSegmentOffsetInMeters">
<h3>pathSegmentOffsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">pathSegmentOffsetInMeters</span></div>
<div className="block"><p>The offset from the start of the segment in meters.</p></div>
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
<section className="detail" id="&lt;init&gt;(int,int,double)">
<h3>ElectronicHorizonPosition</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ElectronicHorizonPosition</span><wbr/><span className="parameters">(int pathIndex,
 int pathSegmentIndex,
 double pathSegmentOffsetInMeters)</span></div>
<div className="block"><p>Creates a new instance.
 Offline availability: This property is available online and offline.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>pathIndex</code> - <p>The index of the current path in the list of <a href="sdk-for-android-navigate-electronichorizon#paths"><code>ElectronicHorizon.paths</code></a>.</p></dd>
<dd><code>pathSegmentIndex</code> - <p>The index of the segment inside the <a href="sdk-for-android-navigate-electronichorizonpath#segments"><code>ElectronicHorizonPath.segments</code></a>.</p></dd>
<dd><code>pathSegmentOffsetInMeters</code> - <p>The offset from the start of the segment in meters.</p></dd>
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
