---
title: "ElectronicHorizonSegment (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ElectronicHorizonSegment.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonSegment</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ElectronicHorizonSegment</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a segment in an <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonpath" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonPath</code></a>.
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



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment#endOffsetInMeters">endOffsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The end offset from the beginning of the most preferred path in meters.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment#parentPathIndex">parentPathIndex</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The index of the parent path.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment#segmentId">segmentId</a></code></div>
<div className="col-last even-row-color">
<div className="block">The unique identifier of the segment.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment#sidePathIndexes">sidePathIndexes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of indexes of the paths that branch off at the end of this segment.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment#startOffsetInMeters">startOffsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The start offset from the beginning of the most preferred path in meters.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment#%3Cinit%3E(com.here.sdk.electronichorizon.ElectronicHorizonSegmentId,int,double,double)">ElectronicHorizonSegment</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a> segmentId,
 int parentPathIndex,
 double startOffsetInMeters,
 double endOffsetInMeters)</code></div>
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
<section className="detail" id="segmentId">
<h3>segmentId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a></span> <span className="element-name">segmentId</span></div>
<div className="block"><p>The unique identifier of the segment.</p></div>
</section>
</li>
<li>
<section className="detail" id="parentPathIndex">
<h3>parentPathIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">parentPathIndex</span></div>
<div className="block"><p>The index of the parent path.</p></div>
</section>
</li>
<li>
<section className="detail" id="startOffsetInMeters">
<h3>startOffsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">startOffsetInMeters</span></div>
<div className="block"><p>The start offset from the beginning of the most preferred path in meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="endOffsetInMeters">
<h3>endOffsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">endOffsetInMeters</span></div>
<div className="block"><p>The end offset from the beginning of the most preferred path in meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="sidePathIndexes">
<h3>sidePathIndexes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">sidePathIndexes</span></div>
<div className="block"><p>The list of indexes of the paths that branch off at the end of this segment.
 The list can be empty when no side paths branch off at this segment.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.electronichorizon.ElectronicHorizonSegmentId,int,double,double)">
<h3>ElectronicHorizonSegment</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ElectronicHorizonSegment</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a> segmentId,
 int parentPathIndex,
 double startOffsetInMeters,
 double endOffsetInMeters)</span></div>
<div className="block"><p>Creates a new instance.
 Offline availability: This property is available online and offline.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>The unique identifier of the segment.</p></dd>
<dd><code>parentPathIndex</code> - <p>The index of the parent path.</p></dd>
<dd><code>startOffsetInMeters</code> - <p>The start offset from the beginning of the most preferred path in meters.</p></dd>
<dd><code>endOffsetInMeters</code> - <p>The end offset from the beginning of the most preferred path in meters.</p></dd>
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
