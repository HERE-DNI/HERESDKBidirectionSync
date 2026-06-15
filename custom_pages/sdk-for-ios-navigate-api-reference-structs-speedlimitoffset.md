---
title: "SpeedLimitOffset"
slug: "sdk-for-ios-navigate-api-reference-structs-speedlimitoffset"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedLimitOffset"></a>
<a title="SpeedLimitOffset Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        SpeedLimitOffset Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpeedLimitOffset</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedLimitOffset</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that represents two separate speed limit offsets for higher and lower speed limits.
A driver will be notified when the current driving speed is above the speed limit + offset.
Only one of the two offsets is used depending on the current speed limit.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lowSpeedOffsetInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecondSdvp">lowSpeedOffsetInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A speed limit offset for speed limits below the <code><a href="../Structs/SpeedLimitOffset.html#/s:7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp">SpeedLimitOffset.highSpeedBoundaryInMetersPerSecond</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lowSpeedOffsetInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpeedLimitOffsetV04highbD17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/highSpeedOffsetInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk16SpeedLimitOffsetV04highbD17InMetersPerSecondSdvp">highSpeedOffsetInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A speed limit offset for speed limits above the <code><a href="../Structs/SpeedLimitOffset.html#/s:7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp">SpeedLimitOffset.highSpeedBoundaryInMetersPerSecond</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">highSpeedOffsetInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/highSpeedBoundaryInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp">highSpeedBoundaryInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The boundary that defines higher and lower speed limits.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">highSpeedBoundaryInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecond04highbdfghI00jb8BoundaryfghI0ACSd_S2dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lowSpeedOffsetInMetersPerSecond:highSpeedOffsetInMetersPerSecond:highSpeedBoundaryInMetersPerSecond:)"></a>
<a class="token" href="#/s:7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecond04highbdfghI00jb8BoundaryfghI0ACSd_S2dtcfc">init(lowSpeedOffsetInMetersPerSecond:<wbr/>highSpeedOffsetInMetersPerSecond:<wbr/>highSpeedBoundaryInMetersPerSecond:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lowSpeedOffsetInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">highSpeedOffsetInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">highSpeedBoundaryInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">)</span></code></pre>
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
