---
title: "RailwayCrossing (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RailwayCrossing.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.RailwayCrossing</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RailwayCrossing</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Identifies the presence and the location of railway corssings.
 Included in <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata"><code>SegmentData</code></a> only if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRailwayCrossings"><code>SegmentDataLoaderOptions.loadRailwayCrossings</code></a> is set to <code>true</code>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#endOffsetInMeters">endOffsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The end offset, in meters, from the beginning of the segment.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#railwayCrossingType">railwayCrossingType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The type of barrier presented by the railway crossing.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#startOffsetInMeters">startOffsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The start offset, in meters, from the beginning of the segment.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#%3Cinit%3E(com.here.sdk.mapdata.RailwayCrossingType)">RailwayCrossing</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a> railwayCrossingType)</code></div>
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
<section className="detail" id="startOffsetInMeters">
<h3>startOffsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">startOffsetInMeters</span></div>
<div className="block"><p>The start offset, in meters, from the beginning of the segment.
 If <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#endOffsetInMeters"><code>endOffsetInMeters</code></a> = 0, then <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#startOffsetInMeters"><code>startOffsetInMeters</code></a> approximately indicates a middle of a railway crossing.
 If <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#endOffsetInMeters"><code>endOffsetInMeters</code></a> &gt; 0, it means crossing consists of several rails, and
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#startOffsetInMeters"><code>startOffsetInMeters</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#endOffsetInMeters"><code>endOffsetInMeters</code></a> indicates starting and ending points of the crossing respectively.
 Default value is 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="endOffsetInMeters">
<h3>endOffsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">endOffsetInMeters</span></div>
<div className="block"><p>The end offset, in meters, from the beginning of the segment.
 Could be 0. See <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#startOffsetInMeters"><code>startOffsetInMeters</code></a> description.
 Default value is 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="railwayCrossingType">
<h3>railwayCrossingType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a></span> <span className="element-name">railwayCrossingType</span></div>
<div className="block"><p>The type of barrier presented by the railway crossing.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapdata.RailwayCrossingType)">
<h3>RailwayCrossing</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RailwayCrossing</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a> railwayCrossingType)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
