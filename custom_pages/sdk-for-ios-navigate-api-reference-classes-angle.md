---
title: "Angle"
slug: "sdk-for-ios-navigate-api-reference-classes-angle"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Angle"></a>
<a title="Angle Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-core">Core</a>

        Angle Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Angle</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Angle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Angle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Angle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents an angle independent of the unit of measurement.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5AngleC7degreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/degrees"></a>
<a class="token" href="#/s:7heresdk5AngleC7degreesSdvp">degrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of this angle in degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">degrees</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5AngleC7radiansSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/radians"></a>
<a class="token" href="#/s:7heresdk5AngleC7radiansSdvp">radians</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of this angle in radians.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">radians</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5AngleC11fromDegrees5angleACSd_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromDegrees(angle:)"></a>
<a class="token" href="#/s:7heresdk5AngleC11fromDegrees5angleACSd_tFZ">fromDegrees(angle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new angle object based on the supplied angle value in degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromDegrees</span><span class="p">(</span><span class="nv">angle</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Angle</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>angle</em>
</code>
</td>
<td>
<div>
<p>Angle value in degrees.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The angle as specified by input in degrees.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5AngleC11fromRadians5angleACSd_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromRadians(angle:)"></a>
<a class="token" href="#/s:7heresdk5AngleC11fromRadians5angleACSd_tFZ">fromRadians(angle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new angle object based on the supplied angle value in radians.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromRadians</span><span class="p">(</span><span class="nv">angle</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Angle</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>angle</em>
</code>
</td>
<td>
<div>
<p>Angle value in radians.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The angle as specified by input in radians.</p>
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
