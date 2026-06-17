---
title: "RailwayCrossing (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RailwayCrossing.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapdata.RailwayCrossing</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RailwayCrossing</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Identifies the presence and the location of railway corssings.
 Included in <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentdata" title="class in com.here.sdk.mapdata"><code>SegmentData</code></a> only if <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentdataloaderoptions#loadRailwayCrossings"><code>SegmentDataLoaderOptions.loadRailwayCrossings</code></a> is set to <code>true</code>.</p></div>
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
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#endOffsetInMeters">endOffsetInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The end offset, in meters, from the beginning of the segment.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#railwayCrossingType">railwayCrossingType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The type of barrier presented by the railway crossing.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#startOffsetInMeters">startOffsetInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The start offset, in meters, from the beginning of the segment.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.mapdata.RailwayCrossingType)">RailwayCrossing</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a> railwayCrossingType)</code></div>
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
<section class="detail" id="startOffsetInMeters">
<h3>startOffsetInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">startOffsetInMeters</span></div>
<div class="block"><p>The start offset, in meters, from the beginning of the segment.
 </p><p>If <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#endOffsetInMeters"><code>endOffsetInMeters</code></a> = 0, then <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#startOffsetInMeters"><code>startOffsetInMeters</code></a> approximately indicates a middle of a railway crossing.
 If <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#endOffsetInMeters"><code>endOffsetInMeters</code></a> &gt; 0, it means crossing consists of several rails, and
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#startOffsetInMeters"><code>startOffsetInMeters</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#endOffsetInMeters"><code>endOffsetInMeters</code></a> indicates starting and ending points of the crossing respectively.
 Default value is 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="endOffsetInMeters">
<h3>endOffsetInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">endOffsetInMeters</span></div>
<div class="block"><p>The end offset, in meters, from the beginning of the segment.
 Could be 0. See <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#startOffsetInMeters"><code>startOffsetInMeters</code></a> description.
 Default value is 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="railwayCrossingType">
<h3>railwayCrossingType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a></span> <span class="element-name">railwayCrossingType</span></div>
<div class="block"><p>The type of barrier presented by the railway crossing.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapdata.RailwayCrossingType)">
<h3>RailwayCrossing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RailwayCrossing</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a> railwayCrossingType)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>railwayCrossingType</code> - <p>The type of barrier presented by the railway crossing.</p></dd>
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
