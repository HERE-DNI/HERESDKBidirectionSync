---
title: "LineDataSource (API Reference)"
slug: "sdk-for-android-explore-linedatasource"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LineDataSource.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.datasource.LineDataSource</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LineDataSource</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Polyline data source allows the rendering engine access to the user provided
 polylines geometry and their attributes.
 <p>Polyline segments are rendered following the shortest path between their end vertices.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></p></p></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-linedatasource.linedataprocessor" title="interface in com.here.sdk.mapview.datasource">LineDataSource.LineDataProcessor</a></code></div>
<div class="col-last even-row-color">
<div class="block">Called for each line, allowing inspection, removal or update of coordinates and attributes.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.mapview.datasource.LineData)">add</a><wbr/>(<a href="sdk-for-android-explore-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a> line)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new line to the data source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(java.util.List)">add</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a>&gt; lines)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new lines to the data source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Frees all internally used resources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forEach(com.here.sdk.mapview.datasource.LineDataSource.LineDataProcessor)">forEach</a><wbr/>(<a href="sdk-for-android-explore-linedatasource.linedataprocessor" title="interface in com.here.sdk.mapview.datasource">LineDataSource.LineDataProcessor</a> processor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Iterates through all the lines from the data source and passes them to the
 given processor, one by one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAll()">removeAll</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all lines from the data source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeIf(com.here.sdk.mapview.datasource.LineDataSource.LineDataProcessor)">removeIf</a><wbr/>(<a href="sdk-for-android-explore-linedatasource.linedataprocessor" title="interface in com.here.sdk.mapview.datasource">LineDataSource.LineDataProcessor</a> inspector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Iterates through all the lines from the data source and passes them to the
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
<section class="detail" id="add(com.here.sdk.mapview.datasource.LineData)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a> line)</span></div>
<div class="block"><p>Adds a new line to the data source.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>line</code> - <p>Line to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(java.util.List)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-linedata" title="class in com.here.sdk.mapview.datasource">LineData</a>&gt; lines)</span></div>
<div class="block"><p>Adds new lines to the data source.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lines</code> - <p>Lines to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAll()">
<h3>removeAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAll</span>()</div>
<div class="block"><p>Removes all lines from the data source.</p></div>
</section>
</li>
<li>
<section class="detail" id="forEach(com.here.sdk.mapview.datasource.LineDataSource.LineDataProcessor)">
<h3>forEach</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEach</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-linedatasource.linedataprocessor" title="interface in com.here.sdk.mapview.datasource">LineDataSource.LineDataProcessor</a> processor)</span></div>
<div class="block"><p>Iterates through all the lines from the data source and passes them to the
 given processor, one by one. The processor can update the line data.
 The iteration stops after all lines have been processed or the processor returns false
 from the process call.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>processor</code> - <p>Line processor.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIf(com.here.sdk.mapview.datasource.LineDataSource.LineDataProcessor)">
<h3>removeIf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIf</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-linedatasource.linedataprocessor" title="interface in com.here.sdk.mapview.datasource">LineDataSource.LineDataProcessor</a> inspector)</span></div>
<div class="block"><p>Iterates through all the lines from the data source and passes them to the
 given inspector, one by one. All lines for which the inspector returns <code>true</code> get removed from the data source.
 The inspector cannot update the line data.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inspector</code> - <p>Line data processor.</p></dd>
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
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
