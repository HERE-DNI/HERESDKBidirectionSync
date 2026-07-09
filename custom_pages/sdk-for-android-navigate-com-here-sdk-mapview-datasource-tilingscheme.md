---
title: "TilingScheme (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TilingScheme.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a>&gt;
<div className="inheritance">com.here.sdk.mapview.datasource.TilingScheme</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">TilingScheme</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a>&gt;</span></div>
<div className="block"><p>List of available data tiling schemes.
 X axis has the origin at -180 longitude and is increasing in east direction.
 Y axis has the origin at max latitude and is increasing in south direction.
 For half quad tree schemes, only the uppper half of the tree is used.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section className="constants-summary" id="enum-constant-summary">

<div className="caption"><span>Enum Constants</span></div>
<div className="summary-table two-column-summary">


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme#HALF_QUAD_TREE_EQUIRECTANGULAR">HALF_QUAD_TREE_EQUIRECTANGULAR</a></code></div>
<div className="col-last even-row-color">
<div className="block">A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme#HALF_QUAD_TREE_IDENTITY">HALF_QUAD_TREE_IDENTITY</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme#HALF_QUAD_TREE_MERCATOR">HALF_QUAD_TREE_MERCATOR</a></code></div>
<div className="col-last even-row-color">
<div className="block">A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme#QUAD_TREE_EQUIRECTANGULAR">QUAD_TREE_EQUIRECTANGULAR</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A tiling scheme that splits each level tile into 4 equal-sized subtiles.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme#QUAD_TREE_IDENTITY">QUAD_TREE_IDENTITY</a></code></div>
<div className="col-last even-row-color">
<div className="block">A tiling scheme that splits each level tile into 4 equal-sized subtiles.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme#QUAD_TREE_MERCATOR">QUAD_TREE_MERCATOR</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A tiling scheme that splits each level tile into 4 equal-sized subtiles.</div>
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
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section className="constant-details" id="enum-constant-detail">

<ul className="member-list">
<li>
<section className="detail" id="HALF_QUAD_TREE_IDENTITY">
<h3>HALF_QUAD_TREE_IDENTITY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">HALF_QUAD_TREE_IDENTITY</span></div>
<div className="block"><p>A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.</p></div>
</section>
</li>
<li>
<section className="detail" id="HALF_QUAD_TREE_MERCATOR">
<h3>HALF_QUAD_TREE_MERCATOR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">HALF_QUAD_TREE_MERCATOR</span></div>
<div className="block"><p>A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.
 The coordinates of the tile's corners are transformed through the web-mercator projection.</p></div>
</section>
</li>
<li>
<section className="detail" id="HALF_QUAD_TREE_EQUIRECTANGULAR">
<h3>HALF_QUAD_TREE_EQUIRECTANGULAR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">HALF_QUAD_TREE_EQUIRECTANGULAR</span></div>
<div className="block"><p>A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.
 The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.</p></div>
</section>
</li>
<li>
<section className="detail" id="QUAD_TREE_IDENTITY">
<h3>QUAD_TREE_IDENTITY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">QUAD_TREE_IDENTITY</span></div>
<div className="block"><p>A tiling scheme that splits each level tile into 4 equal-sized subtiles.</p></div>
</section>
</li>
<li>
<section className="detail" id="QUAD_TREE_MERCATOR">
<h3>QUAD_TREE_MERCATOR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">QUAD_TREE_MERCATOR</span></div>
<div className="block"><p>A tiling scheme that splits each level tile into 4 equal-sized subtiles.
 The coordinates of the tile's corners are transformed through the web-mercator projection.</p></div>
</section>
</li>
<li>
<section className="detail" id="QUAD_TREE_EQUIRECTANGULAR">
<h3>QUAD_TREE_EQUIRECTANGULAR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">QUAD_TREE_EQUIRECTANGULAR</span></div>
<div className="block"><p>A tiling scheme that splits each level tile into 4 equal-sized subtiles.
 The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.</p></div>
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
<section className="detail" id="values()">
<h3>values</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a>[]</span> <span className="element-name">values</span>()</div>
<div className="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
