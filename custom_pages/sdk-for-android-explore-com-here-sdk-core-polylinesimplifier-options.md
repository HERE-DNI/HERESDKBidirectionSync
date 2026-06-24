---
title: "PolylineSimplifier.Options (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PolylineSimplifier.Options.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.PolylineSimplifier.Options</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-polylinesimplifier" title="class in com.here.sdk.core">PolylineSimplifier</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">PolylineSimplifier.Options</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Controls the strategy of <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>
 when reducing a size of polyline.</p></div>
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
<div class="col-first even-row-color"><code>long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints">maxPoints</a></code></div>
<div class="col-last even-row-color">
<div class="block">Sets the upper limit on the resulting collection for
 the <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Value for simplification tolerance for 14 zoom level without significant artifacts.</div>
</div>
<div class="col-first even-row-color"><code>long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters">simplificationToleranceInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Sets the accuracy limit for the <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>:
 
 higher tolerance results in more simplification (fewer points);
 lower tolerance keeps the line closer to its original shape.
 </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#%3Cinit%3E()">Options</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates default options with <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> equal to 0 and
 <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a> equal to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#%3Cinit%3E(long,long)">Options</a><wbr/>(long maxPoints,
 long simplificationToleranceInMeters)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates options with explicitly specified <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> and <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</div>
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
<section class="detail" id="SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">
<h3>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">long</span> <span class="element-name">SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</span></div>
<div class="block"><p>Value for simplification tolerance for 14 zoom level without significant artifacts.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.core.PolylineSimplifier.Options.SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="maxPoints">
<h3>maxPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">maxPoints</span></div>
<div class="block"><p>Sets the upper limit on the resulting collection for
 the <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>. Lower
 value results in the lower accuracy of the resulting
 polyline. If <code>maxPoints</code> is less than <code>2</code>
 then resulting polyline will not have an upper limit
 on the size and only <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>
 will be considered. When <code>maxPoints</code> is greater than
 size of the passed polyline then simplification algorithm
 will take into account only <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="simplificationToleranceInMeters">
<h3>simplificationToleranceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">simplificationToleranceInMeters</span></div>
<div class="block"><p>Sets the accuracy limit for the <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>:
 <ul>
<li>higher tolerance results in more simplification (fewer points);</li>
<li>lower tolerance keeps the line closer to its original shape.</li>
</ul>
</p><p>If removing a point produces polyline, which deviates from the
 original one more than <code>simplificationToleranceInMeters</code>, then
 this point is left in the collection.
 </p><p>If specified tolerance will not allow to create a polyline
 conforming to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a>, then <code>simplificationToleranceInMeters</code>
 is ignored.
 </p><p>Default value is equal to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</p></div>
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
<h3>Options</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Options</span>()</div>
<div class="block"><p>Creates default options with <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> equal to 0 and
 <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a> equal to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(long,long)">
<h3>Options</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Options</span><wbr/><span class="parameters">(long maxPoints,
 long simplificationToleranceInMeters)</span></div>
<div class="block"><p>Creates options with explicitly specified <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> and <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>maxPoints</code> - <p>Sets the upper limit on the resulting collection for
 the <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>. Lower
 value results in the lower accuracy of the resulting
 polyline. If <code>maxPoints</code> is less than <code>2</code>
 then resulting polyline will not have an upper limit
 on the size and only <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>
 will be considered. When <code>maxPoints</code> is greater than
 size of the passed polyline then simplification algorithm
 will take into account only <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</p></dd>
<dd><code>simplificationToleranceInMeters</code> - <p>Sets the accuracy limit for the <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>:
 <ul>
<li>higher tolerance results in more simplification (fewer points);</li>
<li>lower tolerance keeps the line closer to its original shape.</li>
</ul>
</p><p>If removing a point produces polyline, which deviates from the
 original one more than <code>simplificationToleranceInMeters</code>, then
 this point is left in the collection.
 </p><p>If specified tolerance will not allow to create a polyline
 conforming to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a>, then <code>simplificationToleranceInMeters</code>
 is ignored.
 </p><p>Default value is equal to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</p></dd>
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
