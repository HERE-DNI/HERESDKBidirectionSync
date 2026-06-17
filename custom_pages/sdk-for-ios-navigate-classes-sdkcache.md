---
title: "SDKCache"
slug: "sdk-for-ios-navigate-classes-sdkcache"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKCache"></a>
<a title="SDKCache Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-core">Core</a>

        SDKCache Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SDKCache</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SDKCache</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SDKCache</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SDKCache</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A class to manage SDK Cache. Path for SDKCache is specified via <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV9cachePathSSvp">SDKOptions.cachePath</a></code>.
SDKCache manages temporary downloaded map data during map interaction and follows LRU (least recently used) strategy to delete
map data when cache size exceeds the specified <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp">SDKOptions.cacheSizeInBytes</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8SDKCacheC10fromEngineyAcA09SDKNativeD0CFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromEngine(_:)"></a>
<a class="token" href="#/s:7heresdk8SDKCacheC10fromEngineyAcA09SDKNativeD0CFZ">fromEngine(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets a single instance of this class per provided <code><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromEngine</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">SDKCache</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>Instance of an existing SDKEngine.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>SDKCache instance for this engine.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8SDKCacheC10clearCache10completionyyAA14MapLoaderErrorOSgc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/clearCache(completion:)"></a>
<a class="token" href="#/s:7heresdk8SDKCacheC10clearCache10completionyyAA14MapLoaderErrorOSgc_tF">clearCache(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Clears all data that is currently stored in the SDK cache. Path for cache is specified by <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV9cachePathSSvp">SDKOptions.cachePath</a></code>.
The operation can have unexpected behaviour when it is called during a map interaction, during turn-by-turn navigation (only available for the Navigate license) or
during ongoing requests initiated by the OfflineSearchEngine or the OfflineRouteEngine (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">clearCache</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk30CacheCallbackCompletionHandlera">CacheCallbackCompletionHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
