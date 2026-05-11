---
title: "PolygonTileSource (API Reference)"
slug: "sdk-for-android-explore-polygontilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PolygonTileSource.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.mapview.datasource</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="TileSource.html" title="interface in com.here.sdk.mapview.datasource">TileSource</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">PolygonTileSource</span><span class="extends-implements">
extends <a href="TileSource.html" title="interface in com.here.sdk.mapview.datasource">TileSource</a></span></div>
<div class="block"><p>A source of geodetic polygon tiles.
 Polygons provided by an implementation must be clipped to the boundaries of the requested tile.
 The implementations must be thread-safe.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="PolygonTileSource.LoadResultHandler.html" title="interface in com.here.sdk.mapview.datasource">PolygonTileSource.LoadResultHandler</a></code></div>
<div class="col-last even-row-color">
<div class="block">Result handler of a load tile request.</div>
</div>
</div>
<div class="inherited-list">

<code><a href="TileSource.DataVersion.html" title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a>, <a href="TileSource.Listener.html" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a>, <a href="TileSource.LoadTileRequestHandle.html" title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a>, <a href="TileSource.TileMetadata.html" title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a></code></div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TileSource.LoadTileRequestHandle.html" title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#loadTile(com.here.sdk.mapview.datasource.TileKey,com.here.sdk.mapview.datasource.PolygonTileSource.LoadResultHandler)">loadTile</a><wbr/>(<a href="TileKey.html" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey,
 <a href="PolygonTileSource.LoadResultHandler.html" title="interface in com.here.sdk.mapview.datasource">PolygonTileSource.LoadResultHandler</a> completionHandler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Load data of a tile.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.here.sdk.mapview.datasource.TileSource">Methods inherited from interface com.here.sdk.mapview.datasource.<a href="TileSource.html" title="interface in com.here.sdk.mapview.datasource">TileSource</a></h3>
<code><a href="TileSource.html#addListener(com.here.sdk.mapview.datasource.TileSource.Listener)">addListener</a>, <a href="TileSource.html#getDataVersion(com.here.sdk.mapview.datasource.TileKey)">getDataVersion</a>, <a href="TileSource.html#getStorageLevels()">getStorageLevels</a>, <a href="TileSource.html#getTilingScheme()">getTilingScheme</a>, <a href="TileSource.html#removeListener(com.here.sdk.mapview.datasource.TileSource.Listener)">removeListener</a></code></div>
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
<section class="detail" id="loadTile(com.here.sdk.mapview.datasource.TileKey,com.here.sdk.mapview.datasource.PolygonTileSource.LoadResultHandler)">
<h3>loadTile</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="TileSource.LoadTileRequestHandle.html" title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a></span> <span class="element-name">loadTile</span><wbr/><span class="parameters">(@NonNull
 <a href="TileKey.html" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey,
 @NonNull
 <a href="PolygonTileSource.LoadResultHandler.html" title="interface in com.here.sdk.mapview.datasource">PolygonTileSource.LoadResultHandler</a> completionHandler)</span></div>
<div class="block"><p>Load data of a tile.
 Upon completion, the handler gets informed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tileKey</code> - <p>Key of the tile to load data for.</p></dd>
<dd><code>completionHandler</code> - <p>Load result handler.</p></dd>
<dt>Returns:</dt>
<dd><p>A handle to the created load request.</p></dd>
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
