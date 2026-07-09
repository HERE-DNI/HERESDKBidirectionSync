---
title: "TileUrlProviderCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-tileurlprovidercallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TileUrlProviderCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">TileUrlProviderCallback</span></div>
<div className="block"><p>Provides the URL as String for the given tile coordinates and storage level.
 The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1.
 The third parameter indicates the level of the tile.</p></div>
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
<section className="detail" id="onTileUrlRequest(int,int,int)">
<h3>onTileUrlRequest</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">onTileUrlRequest</span><wbr/><span className="parameters">(int x,
 int y,
 int level)</span></div>
<div className="block"><p>Provides the URL as String for the given tile coordinates and storage level.
 The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1.
 The third parameter indicates the level of the tile.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - <p>X coordinate of the tile. This ranges from 0 to 2^level − 1.</p></dd>
<dd><code>y</code> - <p>Y coordinate of the tile. This ranges from 0 to 2^level − 1.</p></dd>
<dd><code>level</code> - <p>Level of the tile.</p></dd>
<dt>Returns:</dt>
<dd><p>the URL.</p></dd>
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
