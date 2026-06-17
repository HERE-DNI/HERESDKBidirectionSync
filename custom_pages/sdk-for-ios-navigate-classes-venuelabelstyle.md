---
title: "VenueLabelStyle"
slug: "sdk-for-ios-navigate-classes-venuelabelstyle"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueLabelStyle"></a>
<a title="VenueLabelStyle Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-venues">Venues</a>

        VenueLabelStyle Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueLabelStyle</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueLabelStyle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueLabelStyle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueLabelStyle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a style of the label.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VenueLabelStyleC9fillColor07outlineF00G5Width7maxFontACSo7UIColorC_AISfs5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(fillColor:outlineColor:outlineWidth:maxFont:)"></a>
<a class="token" href="#/s:7heresdk15VenueLabelStyleC9fillColor07outlineF00G5Width7maxFontACSo7UIColorC_AISfs5Int32Vtcfc">init(fillColor:<wbr/>outlineColor:<wbr/>outlineWidth:<wbr/>maxFont:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a custom label style with specific parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">fillColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">outlineColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">outlineWidth</span><span class="p">:</span> <span class="kt">Float</span><span class="p">,</span> <span class="nv">maxFont</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>fillColor</em>
</code>
</td>
<td>
<div>
<p>The fill color.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>outlineColor</em>
</code>
</td>
<td>
<div>
<p>The outline color.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>outlineWidth</em>
</code>
</td>
<td>
<div>
<p>The width color.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>maxFont</em>
</code>
</td>
<td>
<div>
<p>The max font.</p>
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
<a name="/s:7heresdk15VenueLabelStyleC7maxFonts5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxFont"></a>
<a class="token" href="#/s:7heresdk15VenueLabelStyleC7maxFonts5Int32Vvp">maxFont</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum font size for this label style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxFont</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VenueLabelStyleC9fillColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fillColor"></a>
<a class="token" href="#/s:7heresdk15VenueLabelStyleC9fillColorSo7UIColorCvp">fillColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The fill color for this label style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fillColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VenueLabelStyleC12outlineColorSo7UIColorCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineColor"></a>
<a class="token" href="#/s:7heresdk15VenueLabelStyleC12outlineColorSo7UIColorCSgvp">outlineColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The outline color.
Defaults to <code>nil</code> if an outline color
has not been set for this label style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VenueLabelStyleC12outlineWidthSfvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineWidth"></a>
<a class="token" href="#/s:7heresdk15VenueLabelStyleC12outlineWidthSfvp">outlineWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The outline width for this label style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineWidth</span><span class="p">:</span> <span class="kt">Float</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
} </HTMLBlock>
