---
title: "ElectronicHorizonSegmentId"
slug: "sdk-for-ios-navigate-api-reference-structs-electronichorizonsegmentid"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonSegmentId"></a>
<a title="ElectronicHorizonSegmentId Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>

        ElectronicHorizonSegmentId Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonSegmentId</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonSegmentId</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Identifies a segment in an <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonSegmentIdV03ocmdE0AA018DirectedOCMSegmentE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ocmSegmentId"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonSegmentIdV03ocmdE0AA018DirectedOCMSegmentE0VSgvp">ocmSegmentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The directed OCM segment identifier.
This value can be <code>nil</code> if a route was built on a different version of the map and the route spans do not match any OCM segments.
In this case, only <code><a href="../Structs/ElectronicHorizonSegmentId.html#/s:7heresdk26ElectronicHorizonSegmentIdV16segmentReferenceAA0dG0VSgvp">ElectronicHorizonSegmentId.segmentReference</a></code> is provided.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ocmSegmentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-directedocmsegmentid">DirectedOCMSegmentId</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonSegmentIdV16segmentReferenceAA0dG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentReference"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonSegmentIdV16segmentReferenceAA0dG0VSgvp">segmentReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The segment reference, which is provided when a segment matches the route spans.
In other cases, this value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonSegmentIdV03ocmdE016segmentReferenceAcA018DirectedOCMSegmentE0VSg_AA0dH0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(ocmSegmentId:segmentReference:)"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonSegmentIdV03ocmdE016segmentReferenceAcA018DirectedOCMSegmentE0VSg_AA0dH0VSgtcfc">init(ocmSegmentId:<wbr/>segmentReference:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">ocmSegmentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-directedocmsegmentid">DirectedOCMSegmentId</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
