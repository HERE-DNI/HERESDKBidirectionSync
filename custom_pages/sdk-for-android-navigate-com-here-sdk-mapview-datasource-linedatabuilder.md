---
title: "LineDataBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatabuilder"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LineDataBuilder.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.LineDataBuilder</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LineDataBuilder</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Builder of <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedata" title="class in com.here.sdk.mapview.datasource"><code>LineData</code></a> instances.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatabuilder#%3Cinit%3E()">LineDataBuilder</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a builder instance.</div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>LineDataBuilder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LineDataBuilder</span>()</div>
<div className="block"><p>Creates a builder instance.</p></div>
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
<section className="detail" id="withGeometry(com.here.sdk.core.GeoPolyline)">
<h3>withGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatabuilder" title="class in com.here.sdk.mapview.datasource">LineDataBuilder</a></span> <span className="element-name">withGeometry</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry)</span></div>
<div className="block"><p>Configures the builder with geometry for line to be created.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>Geometry of the polyline. Each vertex defines two line segments: one
     with a previous vertex and one with a next vertex. First and last vertices don't have
     resp. previous and next vertices and thus belong to single line segments.
     Consecutive duplicate vertices are ignored.
     Altitude of polyline vertices is ignored.</p></dd>
<dt>Returns:</dt>
<dd><p>The builder.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withAttributes(com.here.sdk.mapview.datasource.DataAttributes)">
<h3>withAttributes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatabuilder" title="class in com.here.sdk.mapview.datasource">LineDataBuilder</a></span> <span className="element-name">withAttributes</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a> attributes)</span></div>
<div className="block"><p>Configures the builder with custom attributes for line to be created.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>attributes</code> - <p>Custom data attributes to be associated with the line.</p></dd>
<dt>Returns:</dt>
<dd><p>The builder.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="build()">
<h3>build</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a></span> <span className="element-name">build</span>()</div>
<div className="block"><p>Builds an instance of <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedata" title="class in com.here.sdk.mapview.datasource"><code>LineData</code></a> and resets the builder instance.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedata" title="class in com.here.sdk.mapview.datasource"><code>LineData</code></a> created with the configured parameters.</p></dd>
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
