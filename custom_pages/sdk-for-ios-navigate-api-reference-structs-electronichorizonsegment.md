---
title: "ElectronicHorizonSegment"
slug: "sdk-for-ios-navigate-api-reference-structs-electronichorizonsegment"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonSegment"></a>
<a title="ElectronicHorizonSegment Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>

        ElectronicHorizonSegment Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonSegment</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonSegment</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a segment in an <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonSegmentV9segmentIdAA0bcdF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentId"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonSegmentV9segmentIdAA0bcdF0Vvp">segmentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique identifier of the segment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonSegmentV15parentPathIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parentPathIndex"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonSegmentV15parentPathIndexs5Int32Vvp">parentPathIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The index of the parent path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parentPathIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonSegmentV19startOffsetInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonSegmentV19startOffsetInMetersSdvp">startOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The start offset from the beginning of the most preferred path in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonSegmentV17endOffsetInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/endOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonSegmentV17endOffsetInMetersSdvp">endOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The end offset from the beginning of the most preferred path in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">endOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonSegmentV15sidePathIndexesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sidePathIndexes"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonSegmentV15sidePathIndexesSays5Int32VGvp">sidePathIndexes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of indexes of the paths that branch off at the end of this segment.
The list can be empty when no side paths branch off at this segment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sidePathIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonSegmentV9segmentId15parentPathIndex19startOffsetInMeters03endklM004sideH7IndexesAcA0bcdF0V_s5Int32VS2dSayALGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(segmentId:parentPathIndex:startOffsetInMeters:endOffsetInMeters:sidePathIndexes:)"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonSegmentV9segmentId15parentPathIndex19startOffsetInMeters03endklM004sideH7IndexesAcA0bcdF0V_s5Int32VS2dSayALGtcfc">init(segmentId:<wbr/>parentPathIndex:<wbr/>startOffsetInMeters:<wbr/>endOffsetInMeters:<wbr/>sidePathIndexes:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">segmentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a></span><span class="p">,</span> <span class="nv">parentPathIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">endOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">sidePathIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
