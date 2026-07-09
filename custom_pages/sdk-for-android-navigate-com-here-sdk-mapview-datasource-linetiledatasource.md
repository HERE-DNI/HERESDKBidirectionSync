---
title: "LineTileDataSource (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetiledatasource"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LineTileDataSource.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.LineTileDataSource</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LineTileDataSource</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Line tile data source allows the rendering engine access to user managed data sets of
 geodetic lines and their attributes through a <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetilesource" title="interface in com.here.sdk.mapview.datasource"><code>LineTileSource</code></a>.
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
<section className="detail" id="create(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.LineTileSource)">
<h3>create</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetiledatasource" title="class in com.here.sdk.mapview.datasource">LineTileDataSource</a></span> <span className="element-name">create</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetilesource" title="interface in com.here.sdk.mapview.datasource">LineTileSource</a> tileSource)</span></div>
<div className="block"><p>Creates a named <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetiledatasource" title="class in com.here.sdk.mapview.datasource"><code>LineTileDataSource</code></a> in the given context over a given <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetilesource" title="interface in com.here.sdk.mapview.datasource"><code>LineTileSource</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>Map context to associate the data source with.</p></dd>
<dd><code>name</code> - <p>Name of the data source to be created. Must be unique.</p></dd>
<dd><code>tileSource</code> - <p>The source of tile data.</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of the data source created with given name and tile source.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="destroy()">
<h3>destroy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">destroy</span>()</div>
<div className="block"><p>Frees all internally used resources. After calling this method, the object
 is not usable anymore.</p></div>
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
