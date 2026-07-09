---
title: "PolygonDataAccessor (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondataaccessor"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PolygonDataAccessor.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.PolygonDataAccessor</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PolygonDataAccessor</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a></span> <span className="element-name">getGeometry</span>()</div>
<div className="block"><p>Gets polygon geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The polygon geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAttributes()">
<h3>getAttributes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesaccessor" title="class in com.here.sdk.mapview.datasource">DataAttributesAccessor</a></span> <span className="element-name">getAttributes</span>()</div>
<div className="block"><p>Gets polygon attributes accessor.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The polygon attributes accessor.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setGeometry(com.here.sdk.core.GeoPolygon)">
<h3>setGeometry</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setGeometry</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry)</span></div>
<div className="block"><p>Replaces polygon geometry.
 The outer boundary has to be ordered clockwise and closed.
 Altitude of the vertices is ignored.
 The visual behaviour for self-intersecting outer boundary is undefined.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>Geometry of the polygon. The outer boundary has to be ordered clockwise and closed.
     Altitude of the vertices is ignored.
     The visual behaviour for self-intersecting outer boundary is undefined.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setAttributes(com.here.sdk.mapview.datasource.DataAttributes)">
<h3>setAttributes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setAttributes</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a> attributes)</span></div>
<div className="block"><p>Replaces polygon attributes.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>attributes</code> - <p>The attributes.</p></dd>
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
