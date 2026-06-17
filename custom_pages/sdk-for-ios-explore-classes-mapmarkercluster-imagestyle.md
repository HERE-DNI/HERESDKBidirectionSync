---
title: "ImageStyle"
slug: "sdk-for-ios-explore-classes-mapmarkercluster-imagestyle"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ImageStyle"></a>
<a title="ImageStyle Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-maps">Maps</a>

<a href="sdk-for-ios-explore-classes-mapmarkercluster">MapMarkerCluster</a>

        ImageStyle Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ImageStyle</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ImageStyle</span></code></pre>
</div>
</div>
<p>This class specifies the visual appearance of a cluster marker.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC10ImageStyleV5imageAA0bE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/image"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC10ImageStyleV5imageAA0bE0Cvp">image</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map image for the cluster marker.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-classes-mapimage">MapImage</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC10ImageStyleV6anchorAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/anchor"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC10ImageStyleV6anchorAA8Anchor2DVvp">anchor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The anchor point for the marker image which specifies the position offset relative
to the cluster’s position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">anchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC10ImageStyleV5image6anchorAeA0bE0C_AA8Anchor2DVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(image:anchor:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC10ImageStyleV5image6anchorAeA0bE0C_AA8Anchor2DVtcfc">init(image:<wbr/>anchor:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a cluster marker image style using a map image with anchor.</p>
<p>The anchor is a way of specifying position offset relative to image’s dimensions on the
screen. For example, (0, 0) places the top-left corner of the image at the cluster’s
position. (1, 1) would place the bottom-right corner of the image at the cluster’s
position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-classes-mapimage">MapImage</a></span><span class="p">,</span> <span class="nv">anchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>image</em>
</code>
</td>
<td>
<div>
<p>The map image for the cluster marker.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>anchor</em>
</code>
</td>
<td>
<div>
<p>The anchor point for the marker image which specifies the position offset relative
to the cluster’s position.</p>
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
<a name="/s:7heresdk16MapMarkerClusterC10ImageStyleV5imageAeA0bE0C_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(image:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC10ImageStyleV5imageAeA0bE0C_tcfc">init(image:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a marker cluster image representation with default anchor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-classes-mapimage">MapImage</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>image</em>
</code>
</td>
<td>
<div>
<p>The map image for the cluster marker.</p>
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
} </HTMLBlock>
