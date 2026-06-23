---
title: "ElectronicHorizonSegment (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ElectronicHorizonSegment.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonSegment</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ElectronicHorizonSegment</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a segment in an <a href="sdk-for-android-navigate-electronichorizonpath" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonPath</code></a>.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#endOffsetInMeters">endOffsetInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The end offset from the beginning of the most preferred path in meters.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#parentPathIndex">parentPathIndex</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The index of the parent path.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#segmentId">segmentId</a></code></div>
<div class="col-last even-row-color">
<div class="block">The unique identifier of the segment.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#sidePathIndexes">sidePathIndexes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of indexes of the paths that branch off at the end of this segment.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#startOffsetInMeters">startOffsetInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The start offset from the beginning of the most preferred path in meters.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.electronichorizon.ElectronicHorizonSegmentId,int,double,double)">ElectronicHorizonSegment</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a> segmentId,
 int parentPathIndex,
 double startOffsetInMeters,
 double endOffsetInMeters)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="segmentId">
<h3>segmentId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a></span> <span class="element-name">segmentId</span></div>
<div class="block"><p>The unique identifier of the segment.</p></div>
</section>
</li>
<li>
<section class="detail" id="parentPathIndex">
<h3>parentPathIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">parentPathIndex</span></div>
<div class="block"><p>The index of the parent path.</p></div>
</section>
</li>
<li>
<section class="detail" id="startOffsetInMeters">
<h3>startOffsetInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">startOffsetInMeters</span></div>
<div class="block"><p>The start offset from the beginning of the most preferred path in meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="endOffsetInMeters">
<h3>endOffsetInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">endOffsetInMeters</span></div>
<div class="block"><p>The end offset from the beginning of the most preferred path in meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="sidePathIndexes">
<h3>sidePathIndexes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">sidePathIndexes</span></div>
<div class="block"><p>The list of indexes of the paths that branch off at the end of this segment.
 The list can be empty when no side paths branch off at this segment.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.electronichorizon.ElectronicHorizonSegmentId,int,double,double)">
<h3>ElectronicHorizonSegment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElectronicHorizonSegment</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a> segmentId,
 int parentPathIndex,
 double startOffsetInMeters,
 double endOffsetInMeters)</span></div>
<div class="block"><p>Creates a new instance.
 </p><p>Offline availability: This property is available online and offline.</p></div>
<dl class="notes">
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
