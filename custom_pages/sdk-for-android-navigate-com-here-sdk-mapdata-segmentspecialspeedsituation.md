---
title: "SegmentSpecialSpeedSituation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SegmentSpecialSpeedSituation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.SegmentSpecialSpeedSituation</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SegmentSpecialSpeedSituation</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A special speed situation indicates a speed that exists under special circumstances. It can be used to further refine
 the estimation of traversal times, route calculation and calculation of route guidance timing.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation#appliesDuring">appliesDuring</a></code></div>
<div className="col-last even-row-color">
<div className="block">The times during which the condition applies.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-specialspeedtype" title="enum class in com.here.sdk.mapdata">SpecialSpeedType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation#specialSpeedType">specialSpeedType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Represents the speed situation type.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation#speedLimitInMetersPerSecond">speedLimitInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">Overrides normal speed limit for this situation.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation#%3Cinit%3E(com.here.sdk.mapdata.SpecialSpeedType,double,java.util.List)">SegmentSpecialSpeedSituation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapdata-specialspeedtype" title="enum class in com.here.sdk.mapdata">SpecialSpeedType</a> specialSpeedType,
 double speedLimitInMetersPerSecond,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a>&gt; appliesDuring)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance with default values.</div>
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
<section className="detail" id="specialSpeedType">
<h3>specialSpeedType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-specialspeedtype" title="enum class in com.here.sdk.mapdata">SpecialSpeedType</a></span> <span className="element-name">specialSpeedType</span></div>
<div className="block"><p>Represents the speed situation type.</p></div>
</section>
</li>
<li>
<section className="detail" id="speedLimitInMetersPerSecond">
<h3>speedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">speedLimitInMetersPerSecond</span></div>
<div className="block"><p>Overrides normal speed limit for this situation.
 May be 0 to indicate no special speed limit in the case of special_speed_type = SPEED_BUMPS_PRESENT
 and special_speed_type = LANE_DEPENDENT.
 Speed limit in meter per seconds.</p></div>
</section>
</li>
<li>
<section className="detail" id="appliesDuring">
<h3>appliesDuring</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a>&gt;</span> <span className="element-name">appliesDuring</span></div>
<div className="block"><p>The times during which the condition applies.
 May be empty for all special_speed_type values except <code>TIME_DEPENDENT</code> and <code>APPROXIMATE_SEASONAL_TIME</code>.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapdata.SpecialSpeedType,double,java.util.List)">
<h3>SegmentSpecialSpeedSituation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentSpecialSpeedSituation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-specialspeedtype" title="enum class in com.here.sdk.mapdata">SpecialSpeedType</a> specialSpeedType,
 double speedLimitInMetersPerSecond,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a>&gt; appliesDuring)</span></div>
<div className="block"><p>Creates a new instance with default values.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>specialSpeedType</code> - <p>Represents the speed situation type.</p></dd>
<dd><code>speedLimitInMetersPerSecond</code> - <p>Overrides normal speed limit for this situation.
 May be 0 to indicate no special speed limit in the case of special_speed_type = SPEED_BUMPS_PRESENT
 and special_speed_type = LANE_DEPENDENT.
 Speed limit in meter per seconds.</p></dd>
<dd><code>appliesDuring</code> - <p>The times during which the condition applies.
 May be empty for all special_speed_type values except <code>TIME_DEPENDENT</code> and <code>APPROXIMATE_SEASONAL_TIME</code>.</p></dd>
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
