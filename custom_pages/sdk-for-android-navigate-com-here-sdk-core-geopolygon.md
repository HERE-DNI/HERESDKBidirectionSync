---
title: "GeoPolygon (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geopolygon"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GeoPolygon.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.GeoPolygon</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GeoPolygon</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a <code>GeoPolygon</code> area as a series of geographic coordinates, and optionally,
 a list of inner boundaries (also known as holes).
 An instance of this class, initialized with appropriate vertices.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#innerBoundaries">innerBoundaries</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.</div>
</div>
<div className="col-first odd-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#vertices">vertices</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of geographic coordinates representing the outer boundary vertices of polygon.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#%3Cinit%3E(com.here.sdk.core.GeoBox)">GeoPolygon</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#%3Cinit%3E(com.here.sdk.core.GeoCircle)">GeoPolygon</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> geoCircle)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#%3Cinit%3E(java.util.List)">GeoPolygon</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs an instance of this class from the provided vertices.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#%3Cinit%3E(java.util.List,java.util.List)">GeoPolygon</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt; innerBoundaries)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs an instance of this class from the provided vertices and inner boundaries (holes).</div>
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
<div className="block"><p>The list of geographic coordinates representing the outer boundary vertices of polygon.</p></div>
</section>
</li>
<li>
<section className="detail" id="innerBoundaries">
<h3>innerBoundaries</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt;</span> <span className="element-name">innerBoundaries</span></div>
<div className="block"><p>The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.</p></div>
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
<h3>GeoPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoPolygon</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</span>
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Constructs an instance of this class from the provided vertices.
 Throws InstantiationError if the number of vertices is less than three.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>vertices</code> - <p>List of vertices representing the polygon outer boundary in clockwise order.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List)">
<h3>GeoPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoPolygon</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt; innerBoundaries)</span>
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Constructs an instance of this class from the provided vertices and inner boundaries (holes).
 Throws InstantiationError if the number of vertices is less than three.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>vertices</code> - <p>List of vertices representing the polygon outer boundary in clockwise order.</p></dd>
<dd><code>innerBoundaries</code> - <p>List of polygon inner boundaries (holes), each in counterclockwise order.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCircle)">
<h3>GeoPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoPolygon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> geoCircle)</span></div>
<div className="block"><p>Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoCircle</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a> to be converted into <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoBox)">
<h3>GeoPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoPolygon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div className="block"><p>Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A rectangle defined by the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> to be converted into <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.
     The corner coordinates defined by the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> will define the outer boundary verticies of the <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.</p></dd>
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
