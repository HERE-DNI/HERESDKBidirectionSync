---
title: "Search / TextQuery"
slug: "sdk-for-ios-navigate-api-reference-structs-textquery"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TextQuery"></a>
<a title="TextQuery Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TextQuery Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TextQuery</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TextQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify a text query.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TextQueryV5querySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/query"></a>
<a class="token" href="#/s:7heresdk9TextQueryV5querySSvp">query</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Desired query to search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">query</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TextQueryV4areaAC4AreaVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/area"></a>
<a class="token" href="#/s:7heresdk9TextQueryV4areaAC4AreaVvp">area</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Area which to provide the most relevant places.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">area</span><span class="p">:</span> <span class="kt">TextQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-textquery-area">Area</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TextQueryV11placeFilterAA05PlaceE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/placeFilter"></a>
<a class="token" href="#/s:7heresdk9TextQueryV11placeFilterAA05PlaceE0Vvp">placeFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The filter options to specify a place in query.
Consists of fuel and truck options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">placeFilter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-placefilter">PlaceFilter</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TextQueryV_4areaACSS_AC4AreaVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:area:)"></a>
<a class="token" href="#/s:7heresdk9TextQueryV_4areaACSS_AC4AreaVtcfc">init(_:<wbr/>area:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a TextQuery from the provided text query and geographic area.
For Offline Search, search in a given <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></code>, <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geocircle">GeoCircle</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geocorridor">GeoCorridor</a></code>
restricts the results to only POIs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">area</span><span class="p">:</span> <span class="kt">TextQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-textquery-area">Area</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired query to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>area</em>
</code>
</td>
<td>
<div>
<p>Area which to provide the most relevant places.</p>
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
<a name="/s:7heresdk9TextQueryV4AreaV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Area"></a>
<a class="token" href="#/s:7heresdk9TextQueryV4AreaV">Area</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Area to perform search on.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-structs-textquery-area">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Area</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
