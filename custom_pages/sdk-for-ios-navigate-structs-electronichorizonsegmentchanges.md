---
title: "ElectronicHorizonSegmentChanges"
slug: "sdk-for-ios-navigate-structs-electronichorizonsegmentchanges"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonSegmentChanges"></a>
<a title="ElectronicHorizonSegmentChanges Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-electronichorizon">ElectronicHorizon</a>

        ElectronicHorizonSegmentChanges Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonSegmentChanges</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonSegmentChanges</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct describing the set of changes in horizon segments
between two consecutive updates.
Includes lists of both newly added and removed segments.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31ElectronicHorizonSegmentChangesV5addedSayAA0bcD0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/added"></a>
<a class="token" href="#/s:7heresdk31ElectronicHorizonSegmentChangesV5addedSayAA0bcD0VGvp">added</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of segments that were added since the previous update.
May be empty if no segments were added.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">added</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-electronichorizonsegment">ElectronicHorizonSegment</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31ElectronicHorizonSegmentChangesV10removedIdsSayAA0bcD2IdVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/removedIds"></a>
<a class="token" href="#/s:7heresdk31ElectronicHorizonSegmentChangesV10removedIdsSayAA0bcD2IdVGvp">removedIds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifiers of segments that were removed since the previous update.
May be empty if no segments were removed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">removedIds</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31ElectronicHorizonSegmentChangesV5added10removedIdsACSayAA0bcD0VG_SayAA0bcD2IdVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(added:removedIds:)"></a>
<a class="token" href="#/s:7heresdk31ElectronicHorizonSegmentChangesV5added10removedIdsACSayAA0bcD0VG_SayAA0bcD2IdVGtcfc">init(added:<wbr/>removedIds:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">added</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-electronichorizonsegment">ElectronicHorizonSegment</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">removedIds</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
