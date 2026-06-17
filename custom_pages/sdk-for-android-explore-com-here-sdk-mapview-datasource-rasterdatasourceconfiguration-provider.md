---
title: "RasterDataSourceConfiguration.Provider (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RasterDataSourceConfiguration.Provider.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">RasterDataSourceConfiguration.Provider</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Configuration of a data provider.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#hasAlphaChannel">hasAlphaChannel</a></code></div>
<div class="col-last even-row-color">
<div class="block">A flag indicating whether the image content contains an alpha channel for transparency.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#headers">headers</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The optional name-value pairs specifying HTTP headers that are passed with each tile request.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#storageLevels">storageLevels</a></code></div>
<div class="col-last even-row-color">
<div class="block">The storage levels available for this data source.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#tilingScheme">tilingScheme</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The tiling scheme used by this source.</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#urlProvider">urlProvider</a></code></div>
<div class="col-last even-row-color">
<div class="block">Provides a function that generates URLs based on tile coordinates and storage level.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List)">Provider</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List,boolean,java.util.Map)">Provider</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels,
 boolean hasAlphaChannel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; headers)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="urlProvider">
<h3>urlProvider</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a></span> <span class="element-name">urlProvider</span></div>
<div class="block"><p>Provides a function that generates URLs based on tile coordinates and storage level.</p></div>
</section>
</li>
<li>
<section class="detail" id="tilingScheme">
<h3>tilingScheme</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a></span> <span class="element-name">tilingScheme</span></div>
<div class="block"><p>The tiling scheme used by this source.</p></div>
</section>
</li>
<li>
<section class="detail" id="storageLevels">
<h3>storageLevels</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">storageLevels</span></div>
<div class="block"><p>The storage levels available for this data source. Supported range [0, 31].
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
<section class="detail" id="hasAlphaChannel">
<h3>hasAlphaChannel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAlphaChannel</span></div>
<div class="block"><p>A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="headers">
<h3>headers</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">headers</span></div>
<div class="block"><p>The optional name-value pairs specifying HTTP headers that are passed with each tile request.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List,boolean,java.util.Map)">
<h3>Provider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Provider</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels,
 boolean hasAlphaChannel,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; headers)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List)">
<h3>Provider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Provider</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tileurlprovidercallback" title="interface in com.here.sdk.mapview.datasource">TileUrlProviderCallback</a> urlProvider,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-tilingscheme" title="enum class in com.here.sdk.mapview.datasource">TilingScheme</a> tilingScheme,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; storageLevels)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
</main>





</div>
`
}</HTMLBlock>
