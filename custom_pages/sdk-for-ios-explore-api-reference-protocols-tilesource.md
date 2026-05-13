---
title: "TileSource Protocol Reference"
slug: "sdk-for-ios-explore-api-reference-protocols-tilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TileSource.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Protocol/TileSource"></a>
<a title="TileSource Protocol Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TileSource Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public protocol TileSource : AnyObject</code></pre>
</div>
</div>
<p>A source of tiles.
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
<a name="/s:7heresdk10TileSourceP12tilingSchemeAA06TilingE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tilingScheme"></a>
<a class="token" href="#/s:7heresdk10TileSourceP12tilingSchemeAA06TilingE0Ovp">tilingScheme</a>
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
<pre><code>var tilingScheme: TilingScheme { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10TileSourceP13storageLevelsSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/storageLevels"></a>
<a class="token" href="#/s:7heresdk10TileSourceP13storageLevelsSays5Int32VGvp">storageLevels</a>
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
<pre><code>var storageLevels: [Int32] { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10TileSourceP14getDataVersion7tileKeyAA0bceF0VAA0bH0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDataVersion(tileKey:)"></a>
<a class="token" href="#/s:7heresdk10TileSourceP14getDataVersion7tileKeyAA0bceF0VAA0bH0V_tF">getDataVersion(tileKey:<wbr/>)</a>
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
<pre><code>func getDataVersion(tileKey: TileKey) -&gt; TileSourceDataVersion</code></pre>
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
<a name="/s:7heresdk10TileSourceP11addDelegateyyAA0bcE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk10TileSourceP11addDelegateyyAA0bcE0_pF">addDelegate(_:<wbr/>)</a>
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
<pre><code>func addDelegate(_ delegate: TileSourceDelegate)</code></pre>
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
<a name="/s:7heresdk10TileSourceP14removeDelegateyyAA0bcE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk10TileSourceP14removeDelegateyyAA0bcE0_pF">removeDelegate(_:<wbr/>)</a>
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
<pre><code>func removeDelegate(_ delegate: TileSourceDelegate)</code></pre>
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



</div>
`
}</HTMLBlock>
