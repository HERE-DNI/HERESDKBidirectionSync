---
title: "PointDataSource (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PointDataSource.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.PointDataSource</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PointDataSource</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Point data source allows the rendering engine access to the user provided
 geographical locations and their attributes.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a></code></div>
<div className="col-last even-row-color">
<div className="block">Called for each point, allowing inspection, removal or update of coordinates and attributes.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="add(com.here.sdk.mapview.datasource.PointData)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a> point)</span></div>
<div className="block"><p>Adds a new point to the data source.
 Altitude of the point coordinates is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - <p>Point to be added.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(java.util.List)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a>&gt; points)</span></div>
<div className="block"><p>Adds new points to the data source.
 Altitude of the points coordinates is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - <p>Point positions.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAll()">
<h3>removeAll</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAll</span>()</div>
<div className="block"><p>Removes all points from the data source.</p></div>
</section>
</li>
<li>
<section className="detail" id="forEach(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)">
<h3>forEach</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">forEach</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a> processor)</span></div>
<div className="block"><p>Iterates through all the points from the data source and passes them to the
 given processor, one by one. The processor can update the point data.
 The iteration stops after all points have been processed or the processor returns false
 from the process call.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>processor</code> - <p>Point data processor.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeIf(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)">
<h3>removeIf</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeIf</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a> processor)</span></div>
<div className="block"><p>Iterates through all the points from the data source and passes them to the
 given inspector, one by one. All points for which the inspector returns <code>true</code> get removed from the data source.
 The inspector cannot update the point data.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>processor</code> - <p>Point data processor.</p></dd>
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
