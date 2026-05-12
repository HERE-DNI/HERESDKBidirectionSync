---
title: "GeoOrientationUpdate Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-geoorientationupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- GeoOrientationUpdate.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoOrientationUpdate"></a>
<a title="GeoOrientationUpdate Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Core.html">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        GeoOrientationUpdate Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct GeoOrientationUpdate : Hashable</code></pre>
</div>
</div>
<p>Describes geodetic orientation update with bearing and tilt.
Updating an orientation value can be skipped by setting <code>nil</code> in an appriopriate field.
For example, if one wants bearing not to be updated set it to <code>nil</code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoOrientationUpdateV7bearingSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearing"></a>
<a class="token" href="#/s:7heresdk20GeoOrientationUpdateV7bearingSdSgvp">bearing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bearing in degrees. 0 is north up, positive is clockwise.
A <code>nil</code> value means that bearing is not updated and the current value is kept.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let bearing: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoOrientationUpdateV4tiltSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tilt"></a>
<a class="token" href="#/s:7heresdk20GeoOrientationUpdateV4tiltSdSgvp">tilt</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tilt in degrees. 0 is perpendicular to earth surface, a positive value turns the camera’s nose up
and changes the camera’s location to ensure that the camera target is not changed.
A <code>nil</code> value means that tilt is not updated and the current value is kept.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let tilt: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoOrientationUpdateV7bearing4tiltACSdSg_AFtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(bearing:tilt:)"></a>
<a class="token" href="#/s:7heresdk20GeoOrientationUpdateV7bearing4tiltACSdSg_AFtcfc">init(bearing:<wbr/>tilt:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(bearing: Double?, tilt: Double?)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>bearing</em>
</code>
</td>
<td>
<div>
<p>Bearing in degrees. When the passed value is <code>nil</code> bearing is not updated and the current value is kept.
NaN value is converted to <code>nil</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>tilt</em>
</code>
</td>
<td>
<div>
<p>Tilt in degrees. When the passed value is <code>nil</code> tilt is not updated and the current value is kept.
NaN value is converted to <code>nil</code>.</p>
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
<a name="/s:7heresdk20GeoOrientationUpdateVyAcA0bC0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk20GeoOrientationUpdateVyAcA0bC0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new GeoOrientationUpdate instance from a GeoOrientation instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ orientation: GeoOrientation)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>A GeoOrientation instance used as a source for a GeoOrientationUpdate instance’s values.</p>
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
