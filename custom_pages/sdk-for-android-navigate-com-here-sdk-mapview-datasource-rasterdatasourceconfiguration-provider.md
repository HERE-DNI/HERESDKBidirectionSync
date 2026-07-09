---
title: "RasterDataSourceConfiguration.Provider (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RasterDataSourceConfiguration.Provider.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">RasterDataSourceConfiguration.Provider</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Configuration of a data provider.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#hasAlphaChannel">hasAlphaChannel</a></code></div>
<div className="col-last even-row-color">
<div className="block">A flag indicating whether the image content contains an alpha channel for transparency.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#headers">headers</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The optional name-value pairs specifying HTTP headers that are passed with each tile request.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#storageLevels">storageLevels</a></code></div>
<div className="col-last even-row-color">
<div className="block">The storage levels available for this data source.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#tilingScheme">tilingScheme</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The tiling scheme used by this source.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#urlProvider">urlProvider</a></code></div>
<div className="col-last even-row-color">
<div className="block">Provides a function that generates URLs based on tile coordinates and storage level.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#%3Cinit%3E(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List)">Provider</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#%3Cinit%3E(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List,boolean,java.util.Map)">Provider</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels,
 boolean hasAlphaChannel,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; headers)</code></div>
<div className="col-last odd-row-color">
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
<section className="detail" id="urlProvider">
<h3>urlProvider</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a></span> <span className="element-name">urlProvider</span></div>
<div className="block"><p>Provides a function that generates URLs based on tile coordinates and storage level.</p></div>
</section>
</li>
<li>
<section className="detail" id="tilingScheme">
<h3>tilingScheme</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span className="element-name">tilingScheme</span></div>
<div className="block"><p>The tiling scheme used by this source.</p></div>
</section>
</li>
<li>
<section className="detail" id="storageLevels">
<h3>storageLevels</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">storageLevels</span></div>
<div className="block"><p>The storage levels available for this data source. Supported range [0, 31].
 At least one level must be available for this provider to be used as a source of data.
 At storage level zero, the whole world is represented by one tile. At storage level 1
 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme).
 The tiling process continues in this fashion until sufficient granularity has been
 achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds
 to the storage level.
 Depending on the available storage levels and the given camera zoom level, the
 appropriate z value of the tile key will be determined.</p></div>
</section>
</li>
<li>
<section className="detail" id="hasAlphaChannel">
<h3>hasAlphaChannel</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">hasAlphaChannel</span></div>
<div className="block"><p>A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="headers">
<h3>headers</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">headers</span></div>
<div className="block"><p>The optional name-value pairs specifying HTTP headers that are passed with each tile request.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List,boolean,java.util.Map)">
<h3>Provider</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Provider</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels,
 boolean hasAlphaChannel,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; headers)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>urlProvider</code> - <p>Provides a function that generates URLs based on tile coordinates and storage level.</p></dd>
<dd><code>tilingScheme</code> - <p>The tiling scheme used by this source.</p></dd>
<dd><code>storageLevels</code> - <p>The storage levels available for this data source. Supported range [0, 31].
 At least one level must be available for this provider to be used as a source of data.
 At storage level zero, the whole world is represented by one tile. At storage level 1
 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme).
 The tiling process continues in this fashion until sufficient granularity has been
 achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds
 to the storage level.
 Depending on the available storage levels and the given camera zoom level, the
 appropriate z value of the tile key will be determined.</p></dd>
<dd><code>hasAlphaChannel</code> - <p>A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code>false</code>.</p></dd>
<dd><code>headers</code> - <p>The optional name-value pairs specifying HTTP headers that are passed with each tile request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List)">
<h3>Provider</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Provider</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>urlProvider</code> - <p>Provides a function that generates URLs based on tile coordinates and storage level.</p></dd>
<dd><code>tilingScheme</code> - <p>The tiling scheme used by this source.</p></dd>
<dd><code>storageLevels</code> - <p>The storage levels available for this data source. Supported range [0, 31].
 At least one level must be available for this provider to be used as a source of data.
 At storage level zero, the whole world is represented by one tile. At storage level 1
 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme).
 The tiling process continues in this fashion until sufficient granularity has been
 achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds
 to the storage level.
 Depending on the available storage levels and the given camera zoom level, the
 appropriate z value of the tile key will be determined.</p></dd>
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
