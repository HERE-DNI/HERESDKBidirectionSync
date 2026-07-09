---
title: "LineTileSource (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetilesource"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LineTileSource.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource" title="interface in com.here.sdk.mapview.datasource">TileSource</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">LineTileSource</span><span className="extends-implements">
extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource" title="interface in com.here.sdk.mapview.datasource">TileSource</a></span></div>
<div className="block"><p>A source of geodetic line tiles.
 Lines provided by an implementation must be clipped to the boundaries of the requested tile.
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



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetilesource-loadresulthandler" title="interface in com.here.sdk.mapview.datasource">LineTileSource.LoadResultHandler</a></code></div>
<div className="col-last even-row-color">
<div className="block">Result handler of a load tile request.</div>
</div>
</div>
<div className="inherited-list">

<code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-dataversion" title="class in com.here.sdk.mapview.datasource">TileSource.DataVersion</a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-listener" title="interface in com.here.sdk.mapview.datasource">TileSource.Listener</a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle" title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-tilemetadata" title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-com.here.sdk.mapview.datasource.TileSource">Methods inherited from interface com.here.sdk.mapview.datasource.<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource" title="interface in com.here.sdk.mapview.datasource">TileSource</a></h3>
<code><a href="sdk-for-android-navigate-tilesource#addListener(com.here.sdk.mapview.datasource.TileSource.Listener)">addListener</a>, <a href="sdk-for-android-navigate-tilesource#getDataVersion(com.here.sdk.mapview.datasource.TileKey)">getDataVersion</a>, <a href="sdk-for-android-navigate-tilesource#getStorageLevels()">getStorageLevels</a>, <a href="sdk-for-android-navigate-tilesource#getTilingScheme()">getTilingScheme</a>, <a href="sdk-for-android-navigate-tilesource#removeListener(com.here.sdk.mapview.datasource.TileSource.Listener)">removeListener</a></code></div>
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
<section className="detail" id="loadTile(com.here.sdk.mapview.datasource.TileKey,com.here.sdk.mapview.datasource.LineTileSource.LoadResultHandler)">
<h3>loadTile</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-loadtilerequesthandle" title="interface in com.here.sdk.mapview.datasource">TileSource.LoadTileRequestHandle</a></span> <span className="element-name">loadTile</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linetilesource-loadresulthandler" title="interface in com.here.sdk.mapview.datasource">LineTileSource.LoadResultHandler</a> completionHandler)</span></div>
<div className="block"><p>Load data of a tile.
 Upon completion, the handler gets informed.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
