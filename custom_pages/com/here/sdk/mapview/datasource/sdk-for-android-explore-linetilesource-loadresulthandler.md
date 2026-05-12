---
title: "LineTileSource.LoadResultHandler (API Reference)"
slug: "sdk-for-android-explore-linetilesource-loadresulthandler"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LineTileSource.LoadResultHandler.html -->
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
<li><a href="../../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../../index-all.html">Index</a></li>
<li><a href="../../../../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.mapview.datasource</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing interface:</dt>
<dd><a href="LineTileSource.html" title="interface in com.here.sdk.mapview.datasource">LineTileSource</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">LineTileSource.LoadResultHandler</span></div>
<div class="block"><p>Result handler of a load tile request.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#failed(com.here.sdk.mapview.datasource.TileKey)">failed</a><wbr/>(<a href="TileKey.html" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called upon failed load tile request.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#loaded(com.here.sdk.mapview.datasource.TileKey,java.util.List,com.here.sdk.mapview.datasource.TileSource.TileMetadata)">loaded</a><wbr/>(<a href="TileKey.html" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="LineData.html" title="class in com.here.sdk.mapview.datasource">LineData</a>&gt; data,
 <a href="TileSource.TileMetadata.html" title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a> metadata)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called upon successful load tile request.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="loaded(com.here.sdk.mapview.datasource.TileKey,java.util.List,com.here.sdk.mapview.datasource.TileSource.TileMetadata)">
<h3>loaded</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">loaded</span><wbr/><span class="parameters">(@NonNull
 <a href="TileKey.html" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="LineData.html" title="class in com.here.sdk.mapview.datasource">LineData</a>&gt; data,
 @NonNull
 <a href="TileSource.TileMetadata.html" title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a> metadata)</span></div>
<div class="block"><p>Called upon successful load tile request.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tileKey</code> - <p>Loaded tile key.</p></dd>
<dd><code>data</code> - <p>Loaded tile data.</p></dd>
<dd><code>metadata</code> - <p>Loaded tile metadata.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="failed(com.here.sdk.mapview.datasource.TileKey)">
<h3>failed</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">failed</span><wbr/><span class="parameters">(@NonNull
 <a href="TileKey.html" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey)</span></div>
<div class="block"><p>Called upon failed load tile request.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tileKey</code> - <p>Failed tile key.</p></dd>
</dl>
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
