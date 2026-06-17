---
title: "CatalogVersionHint"
slug: "sdk-for-ios-navigate-classes-catalogversionhint"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/CatalogVersionHint"></a>
<a title="CatalogVersionHint Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-core">Core</a>

        CatalogVersionHint Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CatalogVersionHint</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">CatalogVersionHint</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">CatalogVersionHint</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">CatalogVersionHint</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This is a class for capturing user’s intent for the
desired catalog version to use in <code><a href="sdk-for-ios-navigate-structs-desiredcatalog">DesiredCatalog</a></code> class.</p>
<p>You can request a specific or latest version of a catalog by calling the
static functions <code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">CatalogVersionHint.specific(...)</a></code> and
<code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">CatalogVersionHint.latest(...)</a></code> respectively. The HERE platform will make the
best effort to provide an appropriate version for the catalog based on this
version hint.
Please take note that for the API <code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">CatalogVersionHint.specific(...)</a></code> to function properly,
it is essential that the mutable and persistent storage should be cleaned.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/specific(version:)"></a>
<a class="token" href="#/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">specific(version:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This static method is used when you are interested in a
specific version of a catalog, that you want to specify manually.
To ensure proper functioning of this API, it is essential to clean the mutable and persistent storage.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">specific</span><span class="p">(</span><span class="nv">version</span><span class="p">:</span> <span class="kt">Int64</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">CatalogVersionHint</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>version</em>
</code>
</td>
<td>
<div>
<p>An integer value indicating the version of catalog desired.
If the desired version does not exist, the HERE platform will make the
best effort to provide an appropriate version or result in error logs
about invalid version.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code>CatalogVersionHint</code> with specified version.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/latest(ignoreCachedData:)"></a>
<a class="token" href="#/s:7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">latest(ignoreCachedData:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This static method can be called when you are interested in getting the most latest version of
a catalog when initializing the HERE SDK with <code><a href="sdk-for-ios-navigate-structs-sdkoptions">SDKOptions</a></code> where you can specify the
catalog(s) you want to use. In effect, this will auto-update the cached map data on each
start, if possible. Use this only when you have no installed <code>Regions</code>. Since this affects
only the map data cache, calling this at initialization time has no or only a very limited
effect on the start-up time.</p>
<p>In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the
default HRN value: “hrn:here:data::olp-here:ocm” in your <code><a href="sdk-for-ios-navigate-structs-desiredcatalog">DesiredCatalog</a></code>. Note that the
HERE SDK (Explore) cannot be used with such settings and the
initialization of the HERE SDK may fail - since it is based on a different map
format.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">latest</span><span class="p">(</span><span class="nv">ignoreCachedData</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">CatalogVersionHint</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>ignoreCachedData</em>
</code>
</td>
<td>
<div>
<p>A flag to specify handling of any cached data present on a device when
trying to update the map version.
If set to true, the HERE SDK will auto-update to the latest catalog version when no installed
<code>Regions</code> are present. If present, this call will have no effect - use <code>updateCatalog()</code>
via <code><a href="sdk-for-ios-navigate-classes-mapupdater">MapUpdater</a></code> instead to update all map data to the latest version.
Note that cached data present on a device - for example, data in the map cache or data cached
by <code>PrefetchAroundLocationWithRadius</code> or <code>PrefetchAroundRouteOnIntervals</code> - will be become obsolete if
a newer map version is available. Such data will be evicted using a LRU strategy over time.
If set to false, the HERE SDK will auto-update to use the latest version, only
when there is no cached map data at all (for example, at first install or after
clearing the cache) <em>and</em> no installed map data. Otherwise, this call will have no effect.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code>CatalogVersionHint</code>.</p>
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
} </HTMLBlock>
