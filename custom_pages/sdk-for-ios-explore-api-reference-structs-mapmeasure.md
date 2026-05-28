---
title: "Maps / MapMeasure"
slug: "sdk-for-ios-explore-api-reference-structs-mapmeasure"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMeasure"></a>
<a title="MapMeasure Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapMeasure Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMeasure</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMeasure</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A map measure.
Check <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcamera">MapCamera</a></code> for more details on each supported measure.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapMeasureV4kindAC4KindOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/kind"></a>
<a class="token" href="#/s:7heresdk10MapMeasureV4kindAC4KindOvp">kind</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The kind of measure represented by value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">kind</span><span class="p">:</span> <span class="kt">MapMeasure</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-mapmeasure-kind">Kind</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapMeasureV5valueSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/value"></a>
<a class="token" href="#/s:7heresdk10MapMeasureV5valueSdvp">value</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The measure value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapMeasureV4kind5valueA2C4KindO_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(kind:value:)"></a>
<a class="token" href="#/s:7heresdk10MapMeasureV4kind5valueA2C4KindO_Sdtcfc">init(kind:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a MapMeasure from the kind and value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">kind</span><span class="p">:</span> <span class="kt">MapMeasure</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-mapmeasure-kind">Kind</a></span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>kind</em>
</code>
</td>
<td>
<div>
<p>The measure kind.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>The measure value.</p>
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
<a name="/s:7heresdk10MapMeasureV4KindO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Kind"></a>
<a class="token" href="#/s:7heresdk10MapMeasureV4KindO">Kind</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Kinds of measures.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-mapmeasure-kind">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">Kind</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
