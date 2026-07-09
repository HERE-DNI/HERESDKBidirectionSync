---
title: "PolylineSimplifier.Options (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PolylineSimplifier.Options.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.PolylineSimplifier.Options</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier" title="class in com.here.sdk.core">PolylineSimplifier</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">PolylineSimplifier.Options</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Controls the strategy of <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>
 when reducing a size of polyline.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>long</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#maxPoints">maxPoints</a></code></div>
<div className="col-last even-row-color">
<div className="block">Sets the upper limit on the resulting collection for
 the <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Value for simplification tolerance for 14 zoom level without significant artifacts.</div>
</div>
<div className="col-first even-row-color"><code>long</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters">simplificationToleranceInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Sets the accuracy limit for the <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>:
 
 higher tolerance results in more simplification (fewer points);
 lower tolerance keeps the line closer to its original shape.
 </div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#%3Cinit%3E()">Options</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates default options with <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> equal to 0 and
 <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a> equal to <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#%3Cinit%3E(long,long)">Options</a><wbr/>(long maxPoints,
 long simplificationToleranceInMeters)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates options with explicitly specified <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</div>
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
<section className="detail" id="SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">
<h3>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type">long</span> <span className="element-name">SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</span></div>
<div className="block"><p>Value for simplification tolerance for 14 zoom level without significant artifacts.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.core.PolylineSimplifier.Options.SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="maxPoints">
<h3>maxPoints</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">maxPoints</span></div>
<div className="block"><p>Sets the upper limit on the resulting collection for
 the <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>. Lower
 value results in the lower accuracy of the resulting
 polyline. If <code>maxPoints</code> is less than <code>2</code>
 then resulting polyline will not have an upper limit
 on the size and only <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>
 will be considered. When <code>maxPoints</code> is greater than
 size of the passed polyline then simplification algorithm
 will take into account only <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="simplificationToleranceInMeters">
<h3>simplificationToleranceInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">simplificationToleranceInMeters</span></div>
<div className="block"><p>Sets the accuracy limit for the <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>:
 <ul>
<li>higher tolerance results in more simplification (fewer points);</li>
<li>lower tolerance keeps the line closer to its original shape.</li>
</ul>
If removing a point produces polyline, which deviates from the
 original one more than <code>simplificationToleranceInMeters</code>, then
 this point is left in the collection.
 If specified tolerance will not allow to create a polyline
 conforming to <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a>, then <code>simplificationToleranceInMeters</code>
 is ignored.
 Default value is equal to <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</p></div>
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
<h3>Options</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Options</span>()</div>
<div className="block"><p>Creates default options with <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> equal to 0 and
 <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a> equal to <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(long,long)">
<h3>Options</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Options</span><wbr/><span className="parameters">(long maxPoints,
 long simplificationToleranceInMeters)</span></div>
<div className="block"><p>Creates options with explicitly specified <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>maxPoints</code> - <p>Sets the upper limit on the resulting collection for
 the <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>. Lower
 value results in the lower accuracy of the resulting
 polyline. If <code>maxPoints</code> is less than <code>2</code>
 then resulting polyline will not have an upper limit
 on the size and only <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>
 will be considered. When <code>maxPoints</code> is greater than
 size of the passed polyline then simplification algorithm
 will take into account only <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters"><code>simplificationToleranceInMeters</code></a>.</p></dd>
<dd><code>simplificationToleranceInMeters</code> - <p>Sets the accuracy limit for the <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>:
 <ul>
<li>higher tolerance results in more simplification (fewer points);</li>
<li>lower tolerance keeps the line closer to its original shape.</li>
</ul>
If removing a point produces polyline, which deviates from the
 original one more than <code>simplificationToleranceInMeters</code>, then
 this point is left in the collection.
 If specified tolerance will not allow to create a polyline
 conforming to <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#maxPoints"><code>maxPoints</code></a>, then <code>simplificationToleranceInMeters</code>
 is ignored.
 Default value is equal to <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>.</p></dd>
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
