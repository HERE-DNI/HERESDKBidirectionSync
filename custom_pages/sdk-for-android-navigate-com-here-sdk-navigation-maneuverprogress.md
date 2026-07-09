---
title: "ManeuverProgress (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ManeuverProgress.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.ManeuverProgress</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ManeuverProgress</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Indicates a user's progress to a <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress#maneuverIndex">maneuverIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block">Index of the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> being traversed along the route.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress#remainingDistanceInMeters">remainingDistanceInMeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The distance in meters from current location until the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a>.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress#remainingDuration">remainingDuration</a></code></div>
<div className="col-last even-row-color">
<div className="block">The estimated time in seconds for traversing the <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>
 from current location until the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> is reached,
 including traffic delays if available.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress#%3Cinit%3E()">ManeuverProgress</a>()</code></div>
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
<section className="detail" id="maneuverIndex">
<h3>maneuverIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">maneuverIndex</span></div>
<div className="block"><p>Index of the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> being traversed along the route.
 Defaults to 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="remainingDistanceInMeters">
<h3>remainingDistanceInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">remainingDistanceInMeters</span></div>
<div className="block"><p>The distance in meters from current location until the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a>.
 Defaults to 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="remainingDuration">
<h3>remainingDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">remainingDuration</span></div>
<div className="block"><p>The estimated time in seconds for traversing the <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>
 from current location until the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> is reached,
 including traffic delays if available.
 Defaults to 0 seconds.</p></div>
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
<h3>ManeuverProgress</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ManeuverProgress</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
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
