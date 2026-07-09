---
title: "Isoline (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-isoline"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Isoline.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.routing.Isoline</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Isoline</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents an isoline polygon around a center point. Any possible route between
 the center and any point on the edges of the polygon can be travelled within the
 given range restriction. The edges of the polygon are not guaranteed to be on the road as
 all reachable road endpoints are smoothened to fit into one polygon shape. This
 process can be influenced by setting <a href="sdk-for-android-navigate-isolineoptions-calculation#maxPoints"><code>IsolineOptions.Calculation.maxPoints</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isoline#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,double,com.here.sdk.routing.MapMatchedCoordinates,java.util.List)">Isoline</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 double rangeValue,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-mapmatchedcoordinates" title="class in com.here.sdk.routing">MapMatchedCoordinates</a> center,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a>&gt; polygons)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs an isoline instance.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,double,com.here.sdk.routing.MapMatchedCoordinates,java.util.List)">
<h3>Isoline</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Isoline</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 double rangeValue,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-mapmatchedcoordinates" title="class in com.here.sdk.routing">MapMatchedCoordinates</a> center,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a>&gt; polygons)</span></div>
<div className="block"><p>Constructs an isoline instance. This instance is provided by the
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateisolinecallback" title="interface in com.here.sdk.routing"><code>CalculateIsolineCallback</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>Specifies the range type of the provided <code>rangeValue</code> list.</p></dd>
<dd><code>rangeValue</code> - <p>A list of range values. At least one value must be set.</p></dd>
<dd><code>center</code> - <p>The center of the isoline.</p></dd>
<dd><code>polygons</code> - <p>A list of polygons that belong to this isoline. At least one value must be set.</p></dd>
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
<section className="detail" id="getRangeType()">
<h3>getRangeType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a></span> <span className="element-name">getRangeType</span>()</div>
<div className="block"><p>Gets the type of the restriction that was used to calculate this isoline.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Specifies the type of the restriction that was used to calculate this isoline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRangeValue()">
<h3>getRangeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getRangeValue</span>()</div>
<div className="block"><p>Gets the numerical value of the restriction that was used to calculate this isoline.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Specifies the numerical value of the restriction that was used to calculate this isoline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCenter()">
<h3>getCenter</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-mapmatchedcoordinates" title="class in com.here.sdk.routing">MapMatchedCoordinates</a></span> <span className="element-name">getCenter</span>()</div>
<div className="block"><p>Gets the center point that was used to calculate this isoline.
 Specifies the center point that was used to calculate this isoline.
 This includes the original center that was passed to the RoutingEngine.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The center point that was used to calculate this isoline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPolygons()">
<h3>getPolygons</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a>&gt;</span> <span className="element-name">getPolygons</span>()</div>
<div className="block"><p>Gets a list of polygons that belong to this isoline. An isoline can consist of multiple
 polygons. For example, islands that can be reached by a ferry are included.
 Each island is then represented as a separate polygon. However, in most cases
 only a single polygon is included.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A list of polygons that belong to this isoline. An isoline can consist of multiple
     polygons. For example, islands that can be reached by a ferry are included.
     Each island is then represented as a separate polygon. However, in most cases
     only a single polygon is included.</p></dd>
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
