---
title: "RouteOffset (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routeoffset"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RouteOffset.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.RouteOffset</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RouteOffset</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a specific location along the route.
 A <code>RouteOffset</code> is a location on the route defined by the section index and the distance in meters from the start of that section to the specified location on the route.
 An offset in meters indicates the distance that needs to be traveled to reach a specific location along the route, such as a railway crossing.
 For the latter case, the location of a railway crossing can be retrieved from <code>RouteRailwayCrossing.coordinates</code>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoffset#offsetInMeters">offsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Offset from the start of the indexed <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> to the specified location along the route.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoffset#sectionIndex">sectionIndex</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Index of the corresponding route <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoffset#%3Cinit%3E(int,double)">RouteOffset</a><wbr/>(int sectionIndex,
 double offsetInMeters)</code></div>
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
<section className="detail" id="sectionIndex">
<h3>sectionIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">sectionIndex</span></div>
<div className="block"><p>Index of the corresponding route <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>. The start of the section indicates the start of the offset.</p></div>
</section>
</li>
<li>
<section className="detail" id="offsetInMeters">
<h3>offsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">offsetInMeters</span></div>
<div className="block"><p>Offset from the start of the indexed <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> to the specified location along the route.
 The maximum possible offset is limited by the length of the section and cannot exceed it.</p></div>
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
<section className="detail" id="&lt;init&gt;(int,double)">
<h3>RouteOffset</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOffset</span><wbr/><span className="parameters">(int sectionIndex,
 double offsetInMeters)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sectionIndex</code> - <p>Index of the corresponding route <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>. The start of the section indicates the start of the offset.</p></dd>
<dd><code>offsetInMeters</code> - <p>Offset from the start of the indexed <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> to the specified location along the route.
 The maximum possible offset is limited by the length of the section and cannot exceed it.</p></dd>
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
