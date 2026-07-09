---
title: "AvoidCorridorAreaOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AvoidCorridorAreaOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.AvoidCorridorAreaOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AvoidCorridorAreaOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Area of corridor shape which routes must not cross and exceptions for this area.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions#avoidCorridorArea">avoidCorridorArea</a></code></div>
<div className="col-last even-row-color">
<div className="block">Area of corridor shape which routes must not cross.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions#boundingBoxExceptionAreas">boundingBoxExceptionAreas</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Areas of rectangular shape to exclude from avoidance.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions#corridorExceptionAreas">corridorExceptionAreas</a></code></div>
<div className="col-last even-row-color">
<div className="block">Areas of corridor shape to exclude from avoidance.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions#polygonExceptionAreas">polygonExceptionAreas</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Areas of polygon shape to exclude from avoidance.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions#%3Cinit%3E(com.here.sdk.core.GeoCorridor)">AvoidCorridorAreaOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> avoidCorridorArea)</code></div>
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
<section className="detail" id="avoidCorridorArea">
<h3>avoidCorridorArea</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></span> <span className="element-name">avoidCorridorArea</span></div>
<div className="block"><p>Area of corridor shape which routes must not cross. Strictly enforced.
 Violations are reported as <a href="sdk-for-android-navigate-sectionnoticecode#VIOLATED_BLOCKED_ROAD"><code>SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code></a>.
 <strong>Note:</strong>
 This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
 Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
 Otherwise route calculation will fail with an [sdk.routing.RoutingError.INVALID_PARAMETER] error.</p></div>
</section>
</li>
<li>
<section className="detail" id="boundingBoxExceptionAreas">
<h3>boundingBoxExceptionAreas</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</span> <span className="element-name">boundingBoxExceptionAreas</span></div>
<div className="block"><p>Areas of rectangular shape to exclude from avoidance.</p></div>
</section>
</li>
<li>
<section className="detail" id="polygonExceptionAreas">
<h3>polygonExceptionAreas</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a>&gt;</span> <span className="element-name">polygonExceptionAreas</span></div>
<div className="block"><p>Areas of polygon shape to exclude from avoidance.</p></div>
</section>
</li>
<li>
<section className="detail" id="corridorExceptionAreas">
<h3>corridorExceptionAreas</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a>&gt;</span> <span className="element-name">corridorExceptionAreas</span></div>
<div className="block"><p>Areas of corridor shape to exclude from avoidance.
 <strong>Note:</strong>
 Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
 Otherwise route calculation will fail with an [sdk.routing.RoutingError.INVALID_PARAMETER] error.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCorridor)">
<h3>AvoidCorridorAreaOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AvoidCorridorAreaOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> avoidCorridorArea)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>avoidCorridorArea</code> - <p>Area of corridor shape which routes must not cross. Strictly enforced.
 Violations are reported as <a href="sdk-for-android-navigate-sectionnoticecode#VIOLATED_BLOCKED_ROAD"><code>SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code></a>.
 <strong>Note:</strong>
 This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
 Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
 Otherwise route calculation will fail with an [sdk.routing.RoutingError.INVALID_PARAMETER] error.</p></dd>
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
