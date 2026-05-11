---
title: "Untitled"
slug: "sdk-for-android-explore-tilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TileSource.html -->
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
<h1 class="title" title="Interface TileSource">Interface TileSource</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="sdk-for-android-explore-linetilesource" title="interface in com.here.sdk.mapview.datasource">LineTileSource</a></code>, <code><a href="sdk-for-android-explore-pointtilesource" title="interface in com.here.sdk.mapview.datasource">PointTileSource</a></code>, <code><a href="sdk-for-android-explore-polygontilesource" title="interface in com.here.sdk.mapview.datasource">PolygonTileSource</a></code>, <code><a href="sdk-for-android-explore-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TileSource</span></div>
<div class="block"><p>A source of tiles.
 The implementations must be thread-safe.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-tilesource-dataversion" title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a></code></div>
<div class="col-last even-row-color">
<div class="block">Tile data version.</div>
</div>
<div class="col-first odd-row-color"><code>static interface </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listener of <a href="sdk-for-android-explore-tilesource" title="interface in com.here.sdk.mapview.datasource"><code>TileSource</code></a> events.</div>
</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-tilesource-loadtilerequesthandle" title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a></code></div>
<div class="col-last even-row-color">
<div class="block">Handle of a load request.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-tilesource-tilemetadata" title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Tile metadata.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addListener(com.here.sdk.mapview.datasource.TileSource.Listener)">addListener</a><wbr/>(<a href="sdk-for-android-explore-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a listener for receiving state notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-tilesource-dataversion" title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDataVersion(com.here.sdk.mapview.datasource.TileKey)">getDataVersion</a><wbr/>(<a href="sdk-for-android-explore-tilekey" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the current data version of a tile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStorageLevels()">getStorageLevels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the storage levels available for this data source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTilingScheme()">getTilingScheme</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the tiling scheme used by this source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeListener(com.here.sdk.mapview.datasource.TileSource.Listener)">removeListener</a><wbr/>(<a href="sdk-for-android-explore-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes a listener from receiving state notifications.</div>
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
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getDataVersion(com.here.sdk.mapview.datasource.TileKey)">
<h3>getDataVersion</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-tilesource-dataversion" title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a></span> <span class="element-name">getDataVersion</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-tilekey" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey)</span></div>
<div class="block"><p>Gets the current data version of a tile.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tileKey</code> - <p>Key of the tile for which to retrieve the version.</p></dd>
<dt>Returns:</dt>
<dd><p>Data version for a tile.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addListener(com.here.sdk.mapview.datasource.TileSource.Listener)">
<h3>addListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a> listener)</span></div>
<div class="block"><p>Adds a listener for receiving state notifications.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeListener(com.here.sdk.mapview.datasource.TileSource.Listener)">
<h3>removeListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a> listener)</span></div>
<div class="block"><p>Removes a listener from receiving state notifications.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>Listener to be removed from receiving state notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTilingScheme()">
<h3>getTilingScheme</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span class="element-name">getTilingScheme</span>()</div>
<div class="block"><p>Gets the tiling scheme used by this source.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The tiling scheme used by this source.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStorageLevels()">
<h3>getStorageLevels</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">getStorageLevels</span>()</div>
<div class="block"><p>Gets the storage levels available for this data source. Supported range [0, 31].
 <p>At least one level must be available for this to be used as a source of data.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The storage levels available for this data source. Supported range [0, 31].</p></dd>
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
