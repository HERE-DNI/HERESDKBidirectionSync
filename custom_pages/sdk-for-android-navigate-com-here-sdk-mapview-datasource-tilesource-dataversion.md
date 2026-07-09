---
title: "TileSource.DataVersion (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-dataversion"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TileSource.DataVersion.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.datasource.TileSource.DataVersion</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing interface:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource" title="interface in com.here.sdk.mapview.datasource">TileSource</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">TileSource.DataVersion</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Tile data version.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-dataversion#majorVersion">majorVersion</a></code></div>
<div className="col-last even-row-color">
<div className="block">Major version number.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-dataversion#minorVersion">minorVersion</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Minor version number.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilesource-dataversion#%3Cinit%3E(int,int)">DataVersion</a><wbr/>(int majorVersion,
 int minorVersion)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="majorVersion">
<h3>majorVersion</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">majorVersion</span></div>
<div className="block"><p>Major version number.
 Describes changes in underlying data that would require a complete reload
 (e.g. geometry changes).</p></div>
</section>
</li>
<li>
<section className="detail" id="minorVersion">
<h3>minorVersion</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">minorVersion</span></div>
<div className="block"><p>Minor version number.
 Describes changes in underlying data that would not require a complete reload
 (e.g. attributes changes).</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(int,int)">
<h3>DataVersion</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataVersion</span><wbr/><span className="parameters">(int majorVersion,
 int minorVersion)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>majorVersion</code> - <p>Major version number.
 Describes changes in underlying data that would require a complete reload
 (e.g. geometry changes).</p></dd>
<dd><code>minorVersion</code> - <p>Minor version number.
 Describes changes in underlying data that would not require a complete reload
 (e.g. attributes changes).</p></dd>
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
