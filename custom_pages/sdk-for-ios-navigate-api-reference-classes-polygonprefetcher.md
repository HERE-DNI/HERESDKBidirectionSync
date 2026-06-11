---
title: "PolygonPrefetcher"
slug: "sdk-for-ios-navigate-api-reference-classes-polygonprefetcher"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonPrefetcher"></a>
<a title="PolygonPrefetcher Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        PolygonPrefetcher Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PolygonPrefetcher</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonPrefetcher</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonPrefetcher</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonPrefetcher</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Supports downloading of map data - in advance - into the cache to optimize temporary offline
use cases that rely on cached map data.
Please note, this class puts data in the map cache, which has its own size constraints,
and extensive usage may start evicting old cached data.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PolygonPrefetcherCyAcA15SDKNativeEngineCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk17PolygonPrefetcherCyAcA15SDKNativeEngineCcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a PolygonPrefetcher instance for a given <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span></code></pre>
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
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PolygonPrefetcherC8prefetch03geoB08callbackAA10TaskHandle_pAA03GeoB0V_AA22PrefetchStatusListener_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/prefetch(geoPolygon:callback:)"></a>
<a class="token" href="#/s:7heresdk17PolygonPrefetcherC8prefetch03geoB08callbackAA10TaskHandle_pAA03GeoB0V_AA22PrefetchStatusListener_ptF">prefetch(geoPolygon:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Prefetches map data for an area bounded by geo polygon.
After the operation is finished <code>onComplete(...)</code> is
invoked on the main thread. Progress is reported by invocation
of <code>onProgress(...)</code> on the main thread.
If there is not enough space left in the cache to store needed tiles, operation will
fail with <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF">MapLoaderError.notEnoughSpace</a></code>. To increase cache size, use
<code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp">SDKOptions.cacheSizeInBytes</a></code> API.</p>
<p>To control list of map content features for area prefetch, use <code><a href="../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>.</p>
<p>To prefetch map data within user-defined circular area around a given location:</p>
<ol>
<li>Create a GeoCircle using the given location and radius.</li>
<li>Create a GeoPolygon using the GeoCircle.</li>
<li>Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API.
Usage:
GeoCircle geoCircle = GeoCircle(location, radius);
GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);</li>
</ol>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">prefetch</span><span class="p">(</span><span class="nv">geoPolygon</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolygon">GeoPolygon</a></span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-prefetchstatuslistener">PrefetchStatusListener</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoPolygon</em>
</code>
</td>
<td>
<div>
<p>Area to prefetch map data for.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>Callback that is triggered to report progress and the result of prefetch.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PolygonPrefetcherC19estimateMapDataSize03geoB08callbackAA10TaskHandle_pAA03GeoB0V_AA0efG8Listener_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/estimateMapDataSize(geoPolygon:callback:)"></a>
<a class="token" href="#/s:7heresdk17PolygonPrefetcherC19estimateMapDataSize03geoB08callbackAA10TaskHandle_pAA03GeoB0V_AA0efG8Listener_ptF">estimateMapDataSize(geoPolygon:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimates map data size for the area bounded by geo polygon. Size for tiles that are already
in the cache will not be included in the final result.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">estimateMapDataSize</span><span class="p">(</span><span class="nv">geoPolygon</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolygon">GeoPolygon</a></span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-mapdatasizelistener">MapDataSizeListener</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoPolygon</em>
</code>
</td>
<td>
<div>
<p>Area to estimate map data size for.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>Callback that is triggered to report the result of map data size estimation.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate execution of the task.</p>
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
