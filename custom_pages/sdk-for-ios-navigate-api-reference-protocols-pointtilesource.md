---
title: "PointTileSource"
slug: "sdk-for-ios-navigate-api-reference-protocols-pointtilesource"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PointTileSource"></a>
<a title="PointTileSource Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        PointTileSource Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PointTileSource</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PointTileSource</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-tilesource">TileSource</a></span></code></pre>
</div>
</div>
<p>A source of geodetic point tiles.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PointTileSourceP12tilingSchemeAA06TilingF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tilingScheme"></a>
<a class="token" href="#/s:7heresdk15PointTileSourceP12tilingSchemeAA06TilingF0Ovp">tilingScheme</a>
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
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">tilingScheme</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tilingscheme">TilingScheme</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PointTileSourceP13storageLevelsSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/storageLevels"></a>
<a class="token" href="#/s:7heresdk15PointTileSourceP13storageLevelsSays5Int32VGvp">storageLevels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The storage levels available for this data source. Supported range [0, 31].</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">storageLevels</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PointTileSourceP14getDataVersion7tileKeyAA0cdfG0VAA0cI0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDataVersion(tileKey:)"></a>
<a class="token" href="#/s:7heresdk15PointTileSourceP14getDataVersion7tileKeyAA0cdfG0VAA0cI0V_tF">getDataVersion(tileKey:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the current data version of a tile.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getDataVersion</span><span class="p">(</span><span class="nv">tileKey</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tilekey">TileKey</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tilesourcedataversion">TileSourceDataVersion</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tileKey</em>
</code>
</td>
<td>
<div>
<p>Key of the tile for which to retrieve the version.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Data version for a tile.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PointTileSourceP11addDelegateyyAA0cdF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk15PointTileSourceP11addDelegateyyAA0cdF0_pF">addDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a delegate for receiving state notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">addDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-tilesourcedelegate">TileSourceDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The delegate</p>
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
<a name="/s:7heresdk15PointTileSourceP14removeDelegateyyAA0cdF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk15PointTileSourceP14removeDelegateyyAA0cdF0_pF">removeDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a delegate from receiving state notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">removeDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-tilesourcedelegate">TileSourceDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>Delegate to be removed from receiving state notifications.</p>
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
<a name="/s:7heresdk15PointTileSourceP04loadC07tileKey17completionHandlerAA0cd4LoadC13RequestHandle_pSgAA0cG0V_AA0bcdj6ResultI0_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadTile(tileKey:completionHandler:)"></a>
<a class="token" href="#/s:7heresdk15PointTileSourceP04loadC07tileKey17completionHandlerAA0cd4LoadC13RequestHandle_pSgAA0cG0V_AA0bcdj6ResultI0_ptF">loadTile(tileKey:<wbr/>completionHandler:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Load data of a tile.
Upon completion, the handler gets informed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">loadTile</span><span class="p">(</span><span class="nv">tileKey</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tilekey">TileKey</a></span><span class="p">,</span> <span class="nv">completionHandler</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-pointtilesourceloadresulthandler">PointTileSourceLoadResultHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-tilesourceloadtilerequesthandle">TileSourceLoadTileRequestHandle</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tileKey</em>
</code>
</td>
<td>
<div>
<p>Key of the tile to load data for.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completionHandler</em>
</code>
</td>
<td>
<div>
<p>Load result handler.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A handle to the created load request.</p>
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
