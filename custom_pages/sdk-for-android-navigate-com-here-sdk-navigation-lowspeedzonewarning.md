---
title: "LowSpeedZoneWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LowSpeedZoneWarning.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.LowSpeedZoneWarning</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LowSpeedZoneWarning</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class that provides low speed zone. The main field describing the low speed zone is <code>LowSpeedZoneWarning.speed_limit_in_meters_per_second</code>
 specifying the speed limit of the low speed zone.
 Use <code>LowSpeedZoneWarningListener</code> to get notifications about upcoming low speed zones.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning#distanceToLowSpeedZoneInMeters">distanceToLowSpeedZoneInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Distance to the low speed warning in meters.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning#distanceType">distanceType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The distance type for the warning, e.g.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning#id">id</a></code></div>
<div className="col-last even-row-color">
<div className="block">Unique identifier for this specific low speed zone warning instance.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning#segmentReference">segmentReference</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The reference to the segment where the low speed zone is located.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning#speedLimitInMetersPerSecond">speedLimitInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">Speed limit of the low speed zone.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning#%3Cinit%3E(double,double,com.here.sdk.navigation.DistanceType,com.here.sdk.routing.SegmentReference)">LowSpeedZoneWarning</a><wbr/>(double distanceToLowSpeedZoneInMeters,
 double speedLimitInMetersPerSecond,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> segmentReference)</code></div>
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
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">id</span></div>
<div className="block"><p>Unique identifier for this specific low speed zone warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceToLowSpeedZoneInMeters">
<h3>distanceToLowSpeedZoneInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceToLowSpeedZoneInMeters</span></div>
<div className="block"><p>Distance to the low speed warning in meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="speedLimitInMetersPerSecond">
<h3>speedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">speedLimitInMetersPerSecond</span></div>
<div className="block"><p>Speed limit of the low speed zone.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceType">
<h3>distanceType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span className="element-name">distanceType</span></div>
<div className="block"><p>The distance type for the warning, e.g. a warning for a new low speed zone ahead or a warning
 for passing a low speed zone.</p></div>
</section>
</li>
<li>
<section className="detail" id="segmentReference">
<h3>segmentReference</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span className="element-name">segmentReference</span></div>
<div className="block"><p>The reference to the segment where the low speed zone is located. It can be used to identify the
 location.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,double,com.here.sdk.navigation.DistanceType,com.here.sdk.routing.SegmentReference)">
<h3>LowSpeedZoneWarning</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LowSpeedZoneWarning</span><wbr/><span className="parameters">(double distanceToLowSpeedZoneInMeters,
 double speedLimitInMetersPerSecond,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> segmentReference)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>distanceToLowSpeedZoneInMeters</code> - <p>Distance to the low speed warning in meters.</p></dd>
<dd><code>speedLimitInMetersPerSecond</code> - <p>Speed limit of the low speed zone.</p></dd>
<dd><code>distanceType</code> - <p>The distance type for the warning, e.g. a warning for a new low speed zone ahead or a warning
 for passing a low speed zone.</p></dd>
<dd><code>segmentReference</code> - <p>The reference to the segment where the low speed zone is located. It can be used to identify the
 location.</p></dd>
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
