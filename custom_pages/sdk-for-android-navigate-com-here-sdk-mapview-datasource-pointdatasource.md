---
title: "PointDataSource (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PointDataSource.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.datasource.PointDataSource</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">PointDataSource</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Point data source allows the rendering engine access to the user provided
 geographical locations and their attributes.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-pointdatasource.pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a></code></div>
<div class="col-last even-row-color">
<div class="block">Called for each point, allowing inspection, removal or update of coordinates and attributes.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource#add(com.here.sdk.mapview.datasource.PointData)">add</a><wbr/>(<a href="sdk-for-android-navigate-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a> point)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new point to the data source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource#add(java.util.List)">add</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a>&gt; points)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new points to the data source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Frees all internally used resources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource#forEach(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)">forEach</a><wbr/>(<a href="sdk-for-android-navigate-pointdatasource.pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a> processor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Iterates through all the points from the data source and passes them to the
 given processor, one by one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource#removeAll()">removeAll</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all points from the data source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource#removeIf(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)">removeIf</a><wbr/>(<a href="sdk-for-android-navigate-pointdatasource.pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a> processor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Iterates through all the points from the data source and passes them to the
 given inspector, one by one.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="add(com.here.sdk.mapview.datasource.PointData)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a> point)</span></div>
<div class="block"><p>Adds a new point to the data source.
 Altitude of the point coordinates is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - <p>Point to be added.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(java.util.List)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a>&gt; points)</span></div>
<div class="block"><p>Adds new points to the data source.
 Altitude of the points coordinates is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - <p>Point positions.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAll()">
<h3>removeAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAll</span>()</div>
<div class="block"><p>Removes all points from the data source.</p></div>
</section>
</li>
<li>
<section class="detail" id="forEach(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)">
<h3>forEach</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEach</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-pointdatasource.pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a> processor)</span></div>
<div class="block"><p>Iterates through all the points from the data source and passes them to the
 given processor, one by one. The processor can update the point data.
 The iteration stops after all points have been processed or the processor returns false
 from the process call.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>processor</code> - <p>Point data processor.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIf(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)">
<h3>removeIf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIf</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-pointdatasource.pointdataprocessor" title="interface in com.here.sdk.mapview.datasource">PointDataSource.PointDataProcessor</a> processor)</span></div>
<div class="block"><p>Iterates through all the points from the data source and passes them to the
 given inspector, one by one. All points for which the inspector returns <code>true</code> get removed from the data source.
 The inspector cannot update the point data.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>processor</code> - <p>Point data processor.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block"><p>Frees all internally used resources. After calling this method, the object
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
`
}</HTMLBlock>
