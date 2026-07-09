---
title: "GeoPolyline (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geopolyline"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GeoPolyline.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.GeoPolyline</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GeoPolyline</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A list of geographic coordinates representing the vertices of a polyline.
 An instance of this class, initialized with appropriate vertices.
 Represents a <code>GeoPolyline</code> as a series of geographic coordinates.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#vertices">vertices</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of vertices representing the polyline.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#%3Cinit%3E(com.here.sdk.core.GeoBox)">GeoPolyline</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#%3Cinit%3E(java.util.List)">GeoPolyline</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a GeoPolyline from the provided vertices.</div>
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
<section className="detail" id="vertices">
<h3>vertices</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</span> <span className="element-name">vertices</span></div>
<div className="block"><p>The list of vertices representing the polyline.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.util.List)">
<h3>GeoPolyline</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoPolyline</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</span>
            throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Constructs a GeoPolyline from the provided vertices.
 Throws an InstantiationError if the number of vertices is less than two.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>vertices</code> - <p>List of vertices representing the polyline.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoBox)">
<h3>GeoPolyline</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoPolyline</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div className="block"><p>Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A rectangle defined by the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> to be converted into <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a>.
     The corner coordinates of the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> will define the points of the resulting <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a>.</p></dd>
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
<li>
<section className="detail" id="getNearestIndexTo(com.here.sdk.core.GeoCoordinates)">
<h3>getNearestIndexTo</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">getNearestIndexTo</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> point)</span></div>
<div className="block"><p>Returns the index of the nearest vertex to the given point.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - <p>Coordinates of the point.</p></dd>
<dt>Returns:</dt>
<dd><p>Index of the closest vertex of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="coordinatesAtOffsetInMeters(double,com.here.sdk.core.GeoPolylineDirection)">
<h3>coordinatesAtOffsetInMeters</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">coordinatesAtOffsetInMeters</span><wbr/><span className="parameters">(double offsetInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolylinedirection" title="enum class in com.here.sdk.core">GeoPolylineDirection</a> direction)</span></div>
<div className="block"><p>Returns the coordinates at the given distance along the polyline. When the polyline is
 traversed from the beginning, the distance is calculated from the start of the
 polyline; while a direction from the end indicates a distance from the last vertex.
 The offset is expected to be non-negative and smaller than the length of the polyline.
 When the offset is negative, the function returns the starting end point of the polyline,
 i.e. the first vertex in positive direction and the last vertex in the negative direction.
 Similarly, when the offset is larger than the length of the polyline, then the function
 returns the opposite end point of the polyline.
 The distance between two consecutive vertices is calculated using the
 <a href="sdk-for-android-navigate-geocoordinates#distanceTo(com.here.sdk.core.GeoCoordinates)"><code>GeoCoordinates.distanceTo(com.here.sdk.core.GeoCoordinates)</code></a> function. Therefore, it computes the distance (in meters) along
 the great circle between the two vertices. Similarly, the full length of the polyline is the
 sum of the distances between its vertices. The interpolation coordinates between two vertices
 is calculated using the <a href="sdk-for-android-navigate-geocoordinates#interpolate(com.here.sdk.core.GeoCoordinates,double)"><code>GeoCoordinates.interpolate(com.here.sdk.core.GeoCoordinates, double)</code></a> function.
 Note: the result may different from the analogue result from other matching components since
 they may adapt the result to the length of the underlying object described by the polyline.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>offsetInMeters</code> - <p>The distance along the polyline in meters</p></dd>
<dd><code>direction</code> - <p>The direction in which the polyline is traversed.</p></dd>
<dt>Returns:</dt>
<dd><p>The coordinates of the point at the given distance</p></dd>
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
