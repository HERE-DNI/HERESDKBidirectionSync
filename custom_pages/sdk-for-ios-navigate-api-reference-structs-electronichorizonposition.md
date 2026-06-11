---
title: "sdk-for-ios-navigate-api-reference-structs-electronichorizonposition"
slug: "sdk-for-ios-navigate-api-reference-structs-electronichorizonposition"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonPosition"></a>
<a title="ElectronicHorizonPosition Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>
<img alt="" id="carat" src="/carat.png"/>
        ElectronicHorizonPosition Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonPosition</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonPosition</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides a position on an electronic horizon path with a reference to the current item in the <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizon">ElectronicHorizon</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25ElectronicHorizonPositionV9pathIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pathIndex"></a>
<a class="token" href="#/s:7heresdk25ElectronicHorizonPositionV9pathIndexs5Int32Vvp">pathIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The index of the current path in the list of <code><a href="../Structs/ElectronicHorizon.html#/s:7heresdk17ElectronicHorizonV5pathsSayAA0bC4PathVGvp">ElectronicHorizon.paths</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pathIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25ElectronicHorizonPositionV16pathSegmentIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pathSegmentIndex"></a>
<a class="token" href="#/s:7heresdk25ElectronicHorizonPositionV16pathSegmentIndexs5Int32Vvp">pathSegmentIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The index of the segment inside the <code><a href="../Structs/ElectronicHorizonPath.html#/s:7heresdk21ElectronicHorizonPathV8segmentsSayAA0bC7SegmentVGvp">ElectronicHorizonPath.segments</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pathSegmentIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25ElectronicHorizonPositionV25pathSegmentOffsetInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pathSegmentOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk25ElectronicHorizonPositionV25pathSegmentOffsetInMetersSdvp">pathSegmentOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The offset from the start of the segment in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pathSegmentOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25ElectronicHorizonPositionV9pathIndex0e7SegmentF00eG14OffsetInMetersACs5Int32V_AHSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(pathIndex:pathSegmentIndex:pathSegmentOffsetInMeters:)"></a>
<a class="token" href="#/s:7heresdk25ElectronicHorizonPositionV9pathIndex0e7SegmentF00eG14OffsetInMetersACs5Int32V_AHSdtcfc">init(pathIndex:<wbr/>pathSegmentIndex:<wbr/>pathSegmentOffsetInMeters:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">pathIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">pathSegmentIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">pathSegmentOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
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
