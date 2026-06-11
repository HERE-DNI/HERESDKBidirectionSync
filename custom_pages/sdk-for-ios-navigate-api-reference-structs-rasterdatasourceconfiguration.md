---
title: "RasterDataSourceConfiguration"
slug: "sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RasterDataSourceConfiguration"></a>
<a title="RasterDataSourceConfiguration Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        RasterDataSourceConfiguration Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RasterDataSourceConfiguration</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RasterDataSourceConfiguration</span></code></pre>
</div>
</div>
<p>Called on the main thread after <code>fromJsonFile()</code> method finishes loading
the configuration.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV4nameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV4nameSSvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique name of the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8providerAC8ProviderVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/provider"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8providerAC8ProviderVvp">provider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Data provider configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">provider</span><span class="p">:</span> <span class="kt">RasterDataSourceConfiguration</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration-provider">Provider</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV5cacheAC5CacheVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cache"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV5cacheAC5CacheVvp">cache</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Local cache configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cache</span><span class="p">:</span> <span class="kt">RasterDataSourceConfiguration</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration-cache">Cache</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV013ignoreExpiredC0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ignoreExpiredData"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV013ignoreExpiredC0Sbvp">ignoreExpiredData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag indicating whether expired data should be ignored until refreshed. Default value is <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ignoreExpiredData</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV4name8provider5cache013ignoreExpiredC0ACSS_AC8ProviderVAC5CacheVSbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(name:provider:cache:ignoreExpiredData:)"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV4name8provider5cache013ignoreExpiredC0ACSS_AC8ProviderVAC5CacheVSbtcfc">init(name:<wbr/>provider:<wbr/>cache:<wbr/>ignoreExpiredData:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">provider</span><span class="p">:</span> <span class="kt">RasterDataSourceConfiguration</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration-provider">Provider</a></span><span class="p">,</span> <span class="nv">cache</span><span class="p">:</span> <span class="kt">RasterDataSourceConfiguration</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration-cache">Cache</a></span><span class="p">,</span> <span class="nv">ignoreExpiredData</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Provider"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV">Provider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configuration of a data provider.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration-provider">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Provider</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV5CacheV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Cache"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV5CacheV">Cache</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configuration of a local data cache.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfiguration-cache">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Cache</span></code></pre>
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
