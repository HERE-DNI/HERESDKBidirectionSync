---
title: "PolygonDataSourceBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondatasourcebuilder"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PolygonDataSourceBuilder.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.PolygonDataSourceBuilder</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PolygonDataSourceBuilder</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Builder of the polygons data source.
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


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondatasourcebuilder#%3Cinit%3E(com.here.sdk.mapview.MapContext)">PolygonDataSourceBuilder</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a data source builder instance in the given context.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext)">
<h3>PolygonDataSourceBuilder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">PolygonDataSourceBuilder</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context)</span></div>
<div className="block"><p>Creates a data source builder instance in the given context.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>Map context to associate the data source with.</p></dd>
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
<section className="detail" id="withName(java.lang.String)">
<h3>withName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondatasourcebuilder" title="class in com.here.sdk.mapview.datasource">PolygonDataSourceBuilder</a></span> <span className="element-name">withName</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dataSourceName)</span></div>
<div className="block"><p>Configures the builder to use the given name for data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>dataSourceName</code> - <p>Name of the created data source. Must be unique.</p></dd>
<dt>Returns:</dt>
<dd><p>This data source builder instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withPolygon(com.here.sdk.mapview.datasource.PolygonData)">
<h3>withPolygon</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondatasourcebuilder" title="class in com.here.sdk.mapview.datasource">PolygonDataSourceBuilder</a></span> <span className="element-name">withPolygon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondata" title="class in com.here.sdk.mapview.datasource">PolygonData</a> polygon)</span></div>
<div className="block"><p>Configures the builder to insert the given polygon in the data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>polygon</code> - <p>The polygon to add.</p></dd>
<dt>Returns:</dt>
<dd><p>This data source builder instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withPolygons(java.util.List)">
<h3>withPolygons</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondatasourcebuilder" title="class in com.here.sdk.mapview.datasource">PolygonDataSourceBuilder</a></span> <span className="element-name">withPolygons</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondata" title="class in com.here.sdk.mapview.datasource">PolygonData</a>&gt; polygon)</span></div>
<div className="block"><p>Configures the builder to insert the given polygons in the data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>polygon</code> - <p>The polygons to add.</p></dd>
<dt>Returns:</dt>
<dd><p>This data source builder instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="build()">
<h3>build</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondatasource" title="class in com.here.sdk.mapview.datasource">PolygonDataSource</a></span> <span className="element-name">build</span>()</div>
<div className="block"><p>Builds a PolygonDataSource instance.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Instance of the data source created with given polygons and attributes.</p></dd>
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
