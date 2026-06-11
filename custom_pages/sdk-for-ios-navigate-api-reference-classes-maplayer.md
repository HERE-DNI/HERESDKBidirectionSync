---
title: "sdk-for-ios-navigate-api-reference-classes-maplayer"
slug: "sdk-for-ios-navigate-api-reference-classes-maplayer"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayer"></a>
<a title="MapLayer Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapLayer Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapLayer</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayer</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayer</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayer</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Interface for managing a map layer.
A map layer can be created by using the <code><a href="sdk-for-ios-navigate-api-reference-classes-maplayerbuilder">MapLayerBuilder</a></code>. At creation, the layer
gets added to a map. The layer gets removed from the map upon instance destruction.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapLayerC10setEnabledyySbF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setEnabled(_:)"></a>
<a class="token" href="#/s:7heresdk8MapLayerC10setEnabledyySbF">setEnabled(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets whether or not the layer is enabled to be drawn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setEnabled</span><span class="p">(</span><span class="n">_</span> <span class="nv">enable</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>enable</em>
</code>
</td>
<td>
<div>
<p><code>True</code> to enable the layer, <code>false</code> to disable it.</p>
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
<a name="/s:7heresdk8MapLayerC8setStyleyyAA0E0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setStyle(_:)"></a>
<a class="token" href="#/s:7heresdk8MapLayerC8setStyleyyAA0E0CF">setStyle(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the style to be used by the layer.
For more details see Custom Layer Style Reference in the documentation.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setStyle</span><span class="p">(</span><span class="n">_</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-style">Style</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>Style for the layer.</p>
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
<a name="/s:7heresdk8MapLayerC11setPriorityyyAA0bcE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setPriority(_:)"></a>
<a class="token" href="#/s:7heresdk8MapLayerC11setPriorityyyAA0bcE0CF">setPriority(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the render priority for the layer which replaces any previously defined priorities.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setPriority</span><span class="p">(</span><span class="n">_</span> <span class="nv">priority</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>priority</em>
</code>
</td>
<td>
<div>
<p>Priority for the layer.</p>
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
