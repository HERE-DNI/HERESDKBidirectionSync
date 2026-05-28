---
title: "Maps / RasterDataSourceConfigurationUpdate"
slug: "sdk-for-ios-navigate-api-reference-structs-rasterdatasourceconfigurationupdate"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RasterDataSourceConfigurationUpdate"></a>
<a title="RasterDataSourceConfigurationUpdate Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RasterDataSourceConfigurationUpdate Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RasterDataSourceConfigurationUpdate</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RasterDataSourceConfigurationUpdate</span></code></pre>
</div>
</div>
<p>Configuration update for a RasterDataSource.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk35RasterDataSourceConfigurationUpdateV15providerHeadersSDyS2SGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/providerHeaders"></a>
<a class="token" href="#/s:7heresdk35RasterDataSourceConfigurationUpdateV15providerHeadersSDyS2SGSgvp">providerHeaders</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional update of the provider headers. The new list replaces the current one.
When not set, no change is made to the current list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">providerHeaders</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">String</span><span class="p">]?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk35RasterDataSourceConfigurationUpdateV013ignoreExpiredC0SbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ignoreExpiredData"></a>
<a class="token" href="#/s:7heresdk35RasterDataSourceConfigurationUpdateV013ignoreExpiredC0SbSgvp">ignoreExpiredData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional update of the flag indicating whether expired data should be ignored until refreshed.
When not set, no change is made to the current flag state.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ignoreExpiredData</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk35RasterDataSourceConfigurationUpdateV13cacheDiskSizes5Int64VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cacheDiskSize"></a>
<a class="token" href="#/s:7heresdk35RasterDataSourceConfigurationUpdateV13cacheDiskSizes5Int64VSgvp">cacheDiskSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional update of the cache disk size, in bytes.
When not set, no change is made to the current value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cacheDiskSize</span><span class="p">:</span> <span class="kt">Int64</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk35RasterDataSourceConfigurationUpdateV15providerHeaders013ignoreExpiredC013cacheDiskSizeACSDyS2SGSg_SbSgs5Int64VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(providerHeaders:ignoreExpiredData:cacheDiskSize:)"></a>
<a class="token" href="#/s:7heresdk35RasterDataSourceConfigurationUpdateV15providerHeaders013ignoreExpiredC013cacheDiskSizeACSDyS2SGSg_SbSgs5Int64VSgtcfc">init(providerHeaders:<wbr/>ignoreExpiredData:<wbr/>cacheDiskSize:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">providerHeaders</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">String</span><span class="p">]?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">ignoreExpiredData</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">cacheDiskSize</span><span class="p">:</span> <span class="kt">Int64</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
