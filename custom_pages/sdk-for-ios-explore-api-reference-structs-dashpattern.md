---
title: "DashPattern"
slug: "sdk-for-ios-explore-api-reference-structs-dashpattern"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DashPattern"></a>
<a title="DashPattern Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        DashPattern Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DashPattern</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DashPattern</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a dash pattern for map polyline.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11DashPatternV14firstGapLengthSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/firstGapLength"></a>
<a class="token" href="#/s:7heresdk11DashPatternV14firstGapLengthSdvp">firstGapLength</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Length of first gap in pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">firstGapLength</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11DashPatternV05firstB6LengthSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/firstDashLength"></a>
<a class="token" href="#/s:7heresdk11DashPatternV05firstB6LengthSdvp">firstDashLength</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Length of first dash in pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">firstDashLength</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11DashPatternV10dashLengthACSd_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(dashLength:)"></a>
<a class="token" href="#/s:7heresdk11DashPatternV10dashLengthACSd_tcfc">init(dashLength:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a uniform dash pattern in which the length of a gap is the same
as the length of a dash.
This allows for patterns like <code>' — — — —'</code> or <code>'   ———   ———   ———'</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">dashLength</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>dashLength</em>
</code>
</td>
<td>
<div>
<p>The length of a dash in pixels. The gap will have the same length.
Clamped to the range of [1, 500].</p>
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
<a name="/s:7heresdk11DashPatternV9gapLength04dashE0ACSd_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(gapLength:dashLength:)"></a>
<a class="token" href="#/s:7heresdk11DashPatternV9gapLength04dashE0ACSd_Sdtcfc">init(gapLength:<wbr/>dashLength:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.
This allows for patterns like <code>'  —  —  —  —'</code> or <code>' ——— ——— ———'</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">gapLength</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">dashLength</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>gapLength</em>
</code>
</td>
<td>
<div>
<p>The length of a gap in pixels. Clamped to the range of [1, 500].</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>dashLength</em>
</code>
</td>
<td>
<div>
<p>The length of a dash in pixels. Clamped to the range of [1, 500].</p>
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
