---
title: "LaneMarkings"
slug: "sdk-for-ios-navigate-api-reference-structs-lanemarkings"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneMarkings"></a>
<a title="LaneMarkings Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        LaneMarkings Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LaneMarkings</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneMarkings</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides information for the lane markings.</p>
<p>Lane markings indicate the markings on the road.</p>
<p>Lane Divider Marker indicates the lane separator
on the right side of the specified lane in the lane driving direction for Right-side driving countries.
For left-sided driving countries the Lane Divider Marker is indicating the lane separator
on the left side of the specified lane in the lane driving direction.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LaneMarkingsV19centerDividerMarkerAA0eF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/centerDividerMarker"></a>
<a class="token" href="#/s:7heresdk12LaneMarkingsV19centerDividerMarkerAA0eF0OSgvp">centerDividerMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Center Divider Marker describes the type of lane separator for center dividers on bidirectional roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">centerDividerMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-dividermarker">DividerMarker</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LaneMarkingsV17laneDividerMarkerAA0eF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/laneDividerMarker"></a>
<a class="token" href="#/s:7heresdk12LaneMarkingsV17laneDividerMarkerAA0eF0OSgvp">laneDividerMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Lane Divider Marker describes the appearance and type of driving lane separators existing on a road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">laneDividerMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-dividermarker">DividerMarker</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LaneMarkingsV10directionsSayAA0B9DirectionOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/directions"></a>
<a class="token" href="#/s:7heresdk12LaneMarkingsV10directionsSayAA0B9DirectionOGvp">directions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of lane directions</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">directions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-lanedirection">LaneDirection</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LaneMarkingsV19centerDividerMarker04laneeF010directionsAcA0eF0OSg_AISayAA0B9DirectionOGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(centerDividerMarker:laneDividerMarker:directions:)"></a>
<a class="token" href="#/s:7heresdk12LaneMarkingsV19centerDividerMarker04laneeF010directionsAcA0eF0OSg_AISayAA0B9DirectionOGtcfc">init(centerDividerMarker:<wbr/>laneDividerMarker:<wbr/>directions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">centerDividerMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-dividermarker">DividerMarker</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">laneDividerMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-dividermarker">DividerMarker</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">directions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-lanedirection">LaneDirection</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
