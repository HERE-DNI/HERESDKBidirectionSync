---
title: "sdk-for-ios-navigate-api-reference-classes-tilegeoboundscalculator"
slug: "sdk-for-ios-navigate-api-reference-classes-tilegeoboundscalculator"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TileGeoBoundsCalculator"></a>
<a title="TileGeoBoundsCalculator Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        TileGeoBoundsCalculator Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TileGeoBoundsCalculator</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TileGeoBoundsCalculator</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TileGeoBoundsCalculator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TileGeoBoundsCalculator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A calculator of geodetic bounds for tiles identified by keys generated
in a particular tiling scheme (<code><a href="sdk-for-ios-navigate-api-reference-enums-tilingscheme">TilingScheme</a></code>).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TileGeoBoundsCalculatorCyAcA12TilingSchemeOcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk23TileGeoBoundsCalculatorCyAcA12TilingSchemeOcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of <code>TileGeoBoundsCalculator</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">tilingScheme</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tilingscheme">TilingScheme</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tilingScheme</em>
</code>
</td>
<td>
<div>
<p>The tiling scheme used for generating the tile keys that are to be supported by this instance.</p>
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
<a name="/s:7heresdk23TileGeoBoundsCalculatorC8boundsOfyAA0C3BoxVAA0B3KeyVF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/boundsOf(_:)"></a>
<a class="token" href="#/s:7heresdk23TileGeoBoundsCalculatorC8boundsOfyAA0C3BoxVAA0B3KeyVF">boundsOf(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Computes the geodetic bounds (as <code><a href="sdk-for-ios-navigate-api-reference-structs-geobox">GeoBox</a></code>) for a tile identified by <code><a href="sdk-for-ios-navigate-api-reference-structs-tilekey">TileKey</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">boundsOf</span><span class="p">(</span><span class="n">_</span> <span class="nv">tileKey</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tilekey">TileKey</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geobox">GeoBox</a></span></code></pre>
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
<p><code><a href="sdk-for-ios-navigate-api-reference-structs-tilekey">TileKey</a></code> to compute geodetic bounds for.
The geodetic bounds would be calculated relative to the tiling scheme
provided at this <code>TileGeoBoundsCalculator</code> instance creation.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The geodetic bounds of tile identified by given <code><a href="sdk-for-ios-navigate-api-reference-structs-tilekey">TileKey</a></code>.</p>
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
