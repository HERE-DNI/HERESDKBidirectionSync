---
title: "sdk-for-ios-navigate-api-reference-structs-catalogconfiguration"
slug: "sdk-for-ios-navigate-api-reference-structs-catalogconfiguration"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CatalogConfiguration"></a>
<a title="CatalogConfiguration Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-core">Core</a>
<img alt="" id="carat" src="/carat.png"/>
        CatalogConfiguration Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CatalogConfiguration</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CatalogConfiguration</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Using this class you can configure in the <code><a href="sdk-for-ios-navigate-api-reference-structs-sdkoptions">SDKOptions</a></code>,
how the <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> should access, use and store the data for the desired catalog.</p>
<p>Using this class, you can access default catalogs on the HERE platform and also custom catalogs
such as for self-hosted or BYOD (bring your own data) use cases.</p>
<p>For information on how the user can identify a catalog on the HERE platform, see <code><a href="sdk-for-ios-navigate-api-reference-structs-desiredcatalog">DesiredCatalog</a></code>
For further information about catalogs and related concepts see <code><a href="sdk-for-ios-navigate-api-reference-structs-catalogidentifier">CatalogIdentifier</a></code>.</p>
<p><strong>Note:</strong>
This API is only applicable for the Navigate license.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20CatalogConfigurationV7catalogAA07DesiredB0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/catalog"></a>
<a class="token" href="#/s:7heresdk20CatalogConfigurationV7catalogAA07DesiredB0Vvp">catalog</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The identifier for the desired catalog to be accessed on the HERE platform.
See <code><a href="sdk-for-ios-navigate-api-reference-structs-desiredcatalog">DesiredCatalog</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">catalog</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-desiredcatalog">DesiredCatalog</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20CatalogConfigurationV8patchHrnSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/patchHrn"></a>
<a class="token" href="#/s:7heresdk20CatalogConfigurationV8patchHrnSSSgvp">patchHrn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Some catalogs may have additional modifications to their data
contained in an entirely separate catalog, called the patch catalog.
This field indicates the HERE Resource Name (HRN) for the patch catalog.
When this field is present, the catalog’s data as referenced by
<code><a href="../Structs/CatalogConfiguration.html#/s:7heresdk20CatalogConfigurationV7catalogAA07DesiredB0Vvp">CatalogConfiguration.catalog</a></code> is merged with data from the patch catalog.
If this field is <code>nil</code>, then incremental updates are disabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">patchHrn</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20CatalogConfigurationV21cacheExpirationPeriodSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cacheExpirationPeriod"></a>
<a class="token" href="#/s:7heresdk20CatalogConfigurationV21cacheExpirationPeriodSdSgvp">cacheExpirationPeriod</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Expiration time in seconds for how long the catalog data is retained in the
map cache before it is removed. Cache path is specified by <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV9cachePathSSvp">SDKOptions.cachePath</a></code>.
If not set, the cache will be deleted on a Least Recently Used (LRU) basis.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cacheExpirationPeriod</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20CatalogConfigurationV13allowDownloadSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowDownload"></a>
<a class="token" href="#/s:7heresdk20CatalogConfigurationV13allowDownloadSbvp">allowDownload</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.
The storage path is specified in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>.
If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see <code><a href="../Structs/CatalogConfiguration.html#/s:7heresdk20CatalogConfigurationV21cacheExpirationPeriodSdSgvp">CatalogConfiguration.cacheExpirationPeriod</a></code>).
Defaults to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowDownload</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20CatalogConfigurationV7catalog8patchHrn21cacheExpirationPeriod13allowDownloadAcA07DesiredB0V_SSSgSdSgSbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(catalog:patchHrn:cacheExpirationPeriod:allowDownload:)"></a>
<a class="token" href="#/s:7heresdk20CatalogConfigurationV7catalog8patchHrn21cacheExpirationPeriod13allowDownloadAcA07DesiredB0V_SSSgSdSgSbtcfc">init(catalog:<wbr/>patchHrn:<wbr/>cacheExpirationPeriod:<wbr/>allowDownload:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">catalog</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-desiredcatalog">DesiredCatalog</a></span><span class="p">,</span> <span class="nv">patchHrn</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">cacheExpirationPeriod</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">allowDownload</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">true</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20CatalogConfigurationV10getDefault11catalogTypeAcA0bG0O_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDefault(catalogType:)"></a>
<a class="token" href="#/s:7heresdk20CatalogConfigurationV10getDefault11catalogTypeAcA0bG0O_tFZ">getDefault(catalogType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the default catalog configuration for the specified catalog type.
It uses the catalog version that was the latest at the time when the HERE SDK was built.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">getDefault</span><span class="p">(</span><span class="nv">catalogType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-catalogtype">CatalogType</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">CatalogConfiguration</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>catalogType</em>
</code>
</td>
<td>
<div>
<p>Catalog type</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code>CatalogConfiguration</code>.</p>
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
