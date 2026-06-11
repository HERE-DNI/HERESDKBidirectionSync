---
title: "Provider"
slug: "sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration-provider"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Provider"></a>
<a title="Provider Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

<a href="sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>

        Provider Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Provider</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Provider</span></code></pre>
</div>
</div>
<p>Configuration of a data provider.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV03urlF0ySSs5Int32V_A2Htcvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/urlProvider"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV03urlF0ySSs5Int32V_A2Htcvp">urlProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a function that generates URLs based on tile coordinates and storage level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">urlProvider</span><span class="p">:</span> <span class="kt"><a href="../../Maps.html#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV12tilingSchemeAA06TilingH0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tilingScheme"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV12tilingSchemeAA06TilingH0Ovp">tilingScheme</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The tiling scheme used by this source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tilingScheme</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tilingscheme">TilingScheme</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV13storageLevelsSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/storageLevels"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV13storageLevelsSays5Int32VGvp">storageLevels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The storage levels available for this data source. Supported range [0, 31].
At least one level must be available for this provider to be used as a source of data.
At storage level zero, the whole world is represented by one tile. At storage level 1
the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme).
The tiling process continues in this fashion until sufficient granularity has been
achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds
to the storage level.
Depending on the available storage levels and the given camera zoom level, the
appropriate z value of the tile key will be determined.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">storageLevels</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV15hasAlphaChannelSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hasAlphaChannel"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV15hasAlphaChannelSbvp">hasAlphaChannel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hasAlphaChannel</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV7headersSDyS2SGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/headers"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV7headersSDyS2SGSgvp">headers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The optional name-value pairs specifying HTTP headers that are passed with each tile request.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">headers</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">String</span><span class="p">]?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV03urlF012tilingScheme13storageLevels15hasAlphaChannel7headersAESSs5Int32V_A2Ltc_AA06TilingI0OSayALGSbSDyS2SGSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(urlProvider:tilingScheme:storageLevels:hasAlphaChannel:headers:)"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV03urlF012tilingScheme13storageLevels15hasAlphaChannel7headersAESSs5Int32V_A2Ltc_AA06TilingI0OSayALGSbSDyS2SGSgtcfc">init(urlProvider:<wbr/>tilingScheme:<wbr/>storageLevels:<wbr/>hasAlphaChannel:<wbr/>headers:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">urlProvider</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../../Maps.html#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a></span><span class="p">,</span> <span class="nv">tilingScheme</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tilingscheme">TilingScheme</a></span><span class="p">,</span> <span class="nv">storageLevels</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">],</span> <span class="nv">hasAlphaChannel</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">headers</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">String</span><span class="p">]?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
}</HTMLBlock>
