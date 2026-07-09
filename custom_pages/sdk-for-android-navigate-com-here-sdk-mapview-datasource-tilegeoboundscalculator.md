---
title: "TileGeoBoundsCalculator (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilegeoboundscalculator"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TileGeoBoundsCalculator.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.TileGeoBoundsCalculator</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TileGeoBoundsCalculator</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A calculator of geodetic bounds for tiles identified by keys generated
 in a particular tiling scheme (<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource"><code>TilingScheme</code></a>).
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilegeoboundscalculator#%3Cinit%3E(com.here.sdk.mapview.datasource.TilingScheme)">TileGeoBoundsCalculator</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilegeoboundscalculator" title="class in com.here.sdk.mapview.datasource"><code>TileGeoBoundsCalculator</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.datasource.TilingScheme)">
<h3>TileGeoBoundsCalculator</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TileGeoBoundsCalculator</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme)</span></div>
<div className="block"><p>Creates an instance of <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilegeoboundscalculator" title="class in com.here.sdk.mapview.datasource"><code>TileGeoBoundsCalculator</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tilingScheme</code> - <p>The tiling scheme used for generating the tile keys that are to be supported by this instance.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="boundsOf(com.here.sdk.mapview.datasource.TileKey)">
<h3>boundsOf</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">boundsOf</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource">TileKey</a> tileKey)</span></div>
<div className="block"><p>Computes the geodetic bounds (as <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>) for a tile identified by <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource"><code>TileKey</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tileKey</code> - <p><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource"><code>TileKey</code></a> to compute geodetic bounds for.
     The geodetic bounds would be calculated relative to the tiling scheme
     provided at this <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilegeoboundscalculator" title="class in com.here.sdk.mapview.datasource"><code>TileGeoBoundsCalculator</code></a> instance creation.</p></dd>
<dt>Returns:</dt>
<dd><p>The geodetic bounds of tile identified by given <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilekey" title="class in com.here.sdk.mapview.datasource"><code>TileKey</code></a>.</p></dd>
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
