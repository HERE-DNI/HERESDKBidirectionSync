---
title: "SectionProgress"
slug: "sdk-for-ios-navigate-api-reference-structs-sectionprogress"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SectionProgress"></a>
<a title="SectionProgress Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        SectionProgress Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SectionProgress</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SectionProgress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Indicates a user’s progress along a <code><a href="sdk-for-ios-navigate-api-reference-classes-section">Section</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SectionProgressV25remainingDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/remainingDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk15SectionProgressV25remainingDistanceInMeterss5Int32Vvp">remainingDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance in meters from current location until the end of the <code><a href="sdk-for-ios-navigate-api-reference-classes-section">Section</a></code>.
Note that the value is accumulated per section, and that the last section contains the overall
distance to the destination.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">remainingDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SectionProgressV17remainingDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/remainingDuration"></a>
<a class="token" href="#/s:7heresdk15SectionProgressV17remainingDurationSdvp">remainingDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated time in seconds from current location until the end of the <code><a href="sdk-for-ios-navigate-api-reference-classes-section">Section</a></code>
is reached, including traffic delays if available.
Note that the value is accumulated per section, and that the last section contains the overall
duration until the destination is reached.
Defaults to 0 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">remainingDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SectionProgressV12trafficDelaySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficDelay"></a>
<a class="token" href="#/s:7heresdk15SectionProgressV12trafficDelaySdvp">trafficDelay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated traffic delay in seconds from current location until the end of the
<code><a href="sdk-for-ios-navigate-api-reference-classes-section">Section</a></code> is reached.
Note that the value is accumulated per section, and that the last section contains the overall
traffic delay until the destination is reached. The delay might be a negative value:
Negative values indicate that the part of this section can be traversed faster than usual.
Note that this is based on a delay value received at the moment of route calculation.
Defaults to 0 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficDelay</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SectionProgressV25remainingDistanceInMeters0D8Duration12trafficDelayACs5Int32V_S2dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(remainingDistanceInMeters:remainingDuration:trafficDelay:)"></a>
<a class="token" href="#/s:7heresdk15SectionProgressV25remainingDistanceInMeters0D8Duration12trafficDelayACs5Int32V_S2dtcfc">init(remainingDistanceInMeters:<wbr/>remainingDuration:<wbr/>trafficDelay:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">remainingDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">remainingDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">trafficDelay</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span></code></pre>
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
