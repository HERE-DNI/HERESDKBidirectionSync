---
title: "ImageStyle Structure Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapmarkercluster-imagestyle"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ImageStyle.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/ImageStyle"></a>
<a title="ImageStyle Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Maps.html">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Classes/MapMarkerCluster.html">MapMarkerCluster</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        ImageStyle Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct ImageStyle</code></pre>
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
<pre><code>public let image: MapImage</code></pre>
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
<pre><code>public let anchor: Anchor2D</code></pre>
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
<pre><code>public init(image: MapImage, anchor: Anchor2D)</code></pre>
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
<pre><code>public init(image: MapImage)</code></pre>
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



</div>
`
}</HTMLBlock>
