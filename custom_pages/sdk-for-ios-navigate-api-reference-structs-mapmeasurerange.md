---
title: "MapMeasureRange"
slug: "sdk-for-ios-navigate-api-reference-structs-mapmeasurerange"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMeasureRange"></a>
<a title="MapMeasureRange Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        MapMeasureRange Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMeasureRange</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMeasureRange</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A map measure range.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapMeasureRangeV4kindAA0bC0V4KindOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/kind"></a>
<a class="token" href="#/s:7heresdk15MapMeasureRangeV4kindAA0bC0V4KindOvp">kind</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">kind</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="o">.</span><span class="kt">Kind</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapMeasureRangeV12minimumValueSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minimumValue"></a>
<a class="token" href="#/s:7heresdk15MapMeasureRangeV12minimumValueSdvp">minimumValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The minimum measure value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">minimumValue</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapMeasureRangeV12maximumValueSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maximumValue"></a>
<a class="token" href="#/s:7heresdk15MapMeasureRangeV12maximumValueSdvp">maximumValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum measure value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">maximumValue</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapMeasureRangeV4kind12minimumValue07maximumG0AcA0bC0V4KindO_S2dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(kind:minimumValue:maximumValue:)"></a>
<a class="token" href="#/s:7heresdk15MapMeasureRangeV4kind12minimumValue07maximumG0AcA0bC0V4KindO_S2dtcfc">init(kind:<wbr/>minimumValue:<wbr/>maximumValue:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a MapMeasureRange from the kind and range values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">kind</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="o">.</span><span class="kt">Kind</span><span class="p">,</span> <span class="nv">minimumValue</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">maximumValue</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
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
<em>minimumValue</em>
</code>
</td>
<td>
<div>
<p>The minimum measure value.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>maximumValue</em>
</code>
</td>
<td>
<div>
<p>The maximum measure value.</p>
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
}</HTMLBlock>
