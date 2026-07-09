---
title: "TileSource (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TileSource.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetilesource" title="interface in com.here.sdk.mapview.datasource">LineTileSource</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointtilesource" title="interface in com.here.sdk.mapview.datasource">PointTileSource</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygontilesource" title="interface in com.here.sdk.mapview.datasource">PolygonTileSource</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TileSource</span></div>
<div className="block"><p>A source of tiles.
 The implementations must be thread-safe.
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



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-dataversion" title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a></code></div>
<div className="col-last even-row-color">
<div className="block">Tile data version.</div>
</div>
<div className="col-first odd-row-color"><code>static interface </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Listener of <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource" title="interface in com.here.sdk.mapview.datasource"><code>TileSource</code></a> events.</div>
</div>
<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle" title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a></code></div>
<div className="col-last even-row-color">
<div className="block">Handle of a load request.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-tilemetadata" title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Tile metadata.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="getDataVersion(com.here.sdk.mapview.datasource.TileKey)">
<h3>getDataVersion</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-dataversion" title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a></span> <span className="element-name">getDataVersion</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey)</span></div>
<div className="block"><p>Gets the current data version of a tile.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tileKey</code> - <p>Key of the tile for which to retrieve the version.</p></dd>
<dt>Returns:</dt>
<dd><p>Data version for a tile.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addListener(com.here.sdk.mapview.datasource.TileSource.Listener)">
<h3>addListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">addListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a> listener)</span></div>
<div className="block"><p>Adds a listener for receiving state notifications.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeListener(com.here.sdk.mapview.datasource.TileSource.Listener)">
<h3>removeListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">removeListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a> listener)</span></div>
<div className="block"><p>Removes a listener from receiving state notifications.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>Listener to be removed from receiving state notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTilingScheme()">
<h3>getTilingScheme</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">getTilingScheme</span>()</div>
<div className="block"><p>Gets the tiling scheme used by this source.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The tiling scheme used by this source.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStorageLevels()">
<h3>getStorageLevels</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">getStorageLevels</span>()</div>
<div className="block"><p>Gets the storage levels available for this data source. Supported range [0, 31].
 At least one level must be available for this to be used as a source of data.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
