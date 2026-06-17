---
title: "ElectronicHorizonPath"
slug: "sdk-for-ios-navigate-structs-electronichorizonpath"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonPath"></a>
<a title="ElectronicHorizonPath Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-electronichorizon">ElectronicHorizon</a>

        ElectronicHorizonPath Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonPath</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonPath</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a single electronic horizon path.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ElectronicHorizonPathV06parentD5Indexs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parentPathIndex"></a>
<a class="token" href="#/s:7heresdk21ElectronicHorizonPathV06parentD5Indexs5Int32VSgvp">parentPathIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The index of the parent path. Index 0 marks the most-preferred path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parentPathIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ElectronicHorizonPathV18parentSegmentIndexs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parentSegmentIndex"></a>
<a class="token" href="#/s:7heresdk21ElectronicHorizonPathV18parentSegmentIndexs5Int32VSgvp">parentSegmentIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The index of the parent segment in the parent path.
This value is <code>nil</code> if the path is the most-preferred path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parentSegmentIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ElectronicHorizonPathV8segmentsSayAA0bC7SegmentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segments"></a>
<a class="token" href="#/s:7heresdk21ElectronicHorizonPathV8segmentsSayAA0bC7SegmentVGvp">segments</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The ordered list of segments in this path.
The list can be empty when no segments are available for the current path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-electronichorizonsegment">ElectronicHorizonSegment</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ElectronicHorizonPathV11probabilitySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/probability"></a>
<a class="token" href="#/s:7heresdk21ElectronicHorizonPathV11probabilitySdvp">probability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The probability of this electronic horizon path, where a value of 1 represents the most-preferred path and a value of 0 represents an unlikely path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">probability</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ElectronicHorizonPathV5levels5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/level"></a>
<a class="token" href="#/s:7heresdk21ElectronicHorizonPathV5levels5Int32Vvp">level</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The level of this path. A value of 0 represents the most-preferred path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">level</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ElectronicHorizonPathV06parentD5Index0e7SegmentF08segments11probability5levelACs5Int32VSg_AKSayAA0bcG0VGSdAJtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(parentPathIndex:parentSegmentIndex:segments:probability:level:)"></a>
<a class="token" href="#/s:7heresdk21ElectronicHorizonPathV06parentD5Index0e7SegmentF08segments11probability5levelACs5Int32VSg_AKSayAA0bcG0VGSdAJtcfc">init(parentPathIndex:<wbr/>parentSegmentIndex:<wbr/>segments:<wbr/>probability:<wbr/>level:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Offline availability: This property is available online and offline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">parentPathIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">parentSegmentIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">segments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-electronichorizonsegment">ElectronicHorizonSegment</a></span><span class="p">],</span> <span class="nv">probability</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">level</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
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
