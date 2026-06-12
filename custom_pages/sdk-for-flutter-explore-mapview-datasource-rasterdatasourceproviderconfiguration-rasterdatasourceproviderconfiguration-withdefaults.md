---
title: "RasterDataSourceProviderConfiguration.withDefaults constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-withdefaults"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceProviderConfiguration.withDefaults.html -->


<div>
<h1>RasterDataSourceProviderConfiguration.withDefaults constructor</h1></div>

RasterDataSourceProviderConfiguration.withDefaults(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a> urlProvider, </li>
<li><a href="/sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a> tilingScheme, </li>
<li>List&lt;int&gt; storageLevels</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>urlProvider</code> Provides a function that generates URLs based on tile coordinates and storage level.</li>
<li><code>tilingScheme</code> The tiling scheme used by this source.</li>
<li><code>storageLevels</code> The storage levels available for this data source. Supported range [0, 31].
At least one level must be available for this provider to be used as a source of data.
At storage level zero, the whole world is represented by one tile. At storage level 1
the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme).
The tiling process continues in this fashion until sufficient granularity has been
achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds
to the storage level.
Depending on the available storage levels and the given camera zoom level, the
appropriate z value of the tile key will be determined.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RasterDataSourceProviderConfiguration.withDefaults(this.urlProvider, this.tilingScheme, this.storageLevels)
    : hasAlphaChannel = false, headers = null;</code></pre>

 



</div>
`
}</HTMLBlock>
