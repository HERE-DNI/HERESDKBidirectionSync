---
title: "PointTileSource.LoadResultHandler (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointtilesource-loadresulthandler"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PointTileSource.LoadResultHandler.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing interface:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointtilesource" title="interface in com.here.sdk.mapview.datasource">PointTileSource</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static interface </span><span className="element-name type-name-label">PointTileSource.LoadResultHandler</span></div>
<div className="block"><p>Result handler of a load tile request.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<section className="detail" id="loaded(com.here.sdk.mapview.datasource.TileKey,java.util.List,com.here.sdk.mapview.datasource.TileSource.TileMetadata)">
<h3>loaded</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">loaded</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a>&gt; data,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-tilemetadata" title="class in com.here.sdk.mapview.datasource">TileSource.TileMetadata</a> metadata)</span></div>
<div className="block"><p>Called upon successful load tile request.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tileKey</code> - <p>Loaded tile key.</p></dd>
<dd><code>data</code> - <p>Loaded tile data.</p></dd>
<dd><code>metadata</code> - <p>Loaded tile metadata.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="failed(com.here.sdk.mapview.datasource.TileKey)">
<h3>failed</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">failed</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey)</span></div>
<div className="block"><p>Called upon failed load tile request.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
