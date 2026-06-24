---
title: "LineDataSourceBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatasourcebuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LineDataSourceBuilder.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.datasource.LineDataSourceBuilder</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LineDataSourceBuilder</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Builder of lines data source.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatasourcebuilder#%3Cinit%3E(com.here.sdk.mapview.MapContext)">LineDataSourceBuilder</a><wbr/>(<a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a data source builder instance in the given context.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-linedatasource" title="class in com.here.sdk.mapview.datasource">LineDataSource</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatasourcebuilder#build()">build</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Builds instance of LineDataSource.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-linedatasourcebuilder" title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatasourcebuilder#withName(java.lang.String)">withName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dataSourceName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to use the given name for data source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-linedatasourcebuilder" title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatasourcebuilder#withPolyline(com.here.sdk.mapview.datasource.LineData)">withPolyline</a><wbr/>(<a href="sdk-for-android-navigate-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a> polyline)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to insert the given polyline in the data source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-linedatasourcebuilder" title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatasourcebuilder#withPolylines(java.util.List)">withPolylines</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a>&gt; polylines)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to insert the given polylines in the data source.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext)">
<h3>LineDataSourceBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LineDataSourceBuilder</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context)</span></div>
<div class="block"><p>Creates a data source builder instance in the given context.</p></div>
<dl class="notes">
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="withName(java.lang.String)">
<h3>withName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-linedatasourcebuilder" title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></span> <span class="element-name">withName</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dataSourceName)</span></div>
<div class="block"><p>Configures the builder to use the given name for data source.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataSourceName</code> - <p>Name of the created data source. Must be unique.</p></dd>
<dt>Returns:</dt>
<dd><p>This data source builder instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withPolyline(com.here.sdk.mapview.datasource.LineData)">
<h3>withPolyline</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-linedatasourcebuilder" title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></span> <span class="element-name">withPolyline</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a> polyline)</span></div>
<div class="block"><p>Configures the builder to insert the given polyline in the data source.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>polyline</code> - <p>Polyline to add.</p></dd>
<dt>Returns:</dt>
<dd><p>This data source builder instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withPolylines(java.util.List)">
<h3>withPolylines</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-linedatasourcebuilder" title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></span> <span class="element-name">withPolylines</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a>&gt; polylines)</span></div>
<div class="block"><p>Configures the builder to insert the given polylines in the data source.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>polylines</code> - <p>Polylines to add.</p></dd>
<dt>Returns:</dt>
<dd><p>This data source builder instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="build()">
<h3>build</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-linedatasource" title="class in com.here.sdk.mapview.datasource">LineDataSource</a></span> <span class="element-name">build</span>()</div>
<div class="block"><p>Builds instance of LineDataSource.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Instance of the data source created with given polylines and attributes.</p></dd>
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
`
}</HTMLBlock>
