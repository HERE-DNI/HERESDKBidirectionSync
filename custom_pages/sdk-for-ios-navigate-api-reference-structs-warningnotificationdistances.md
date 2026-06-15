---
title: "WarningNotificationDistances"
slug: "sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WarningNotificationDistances"></a>
<a title="WarningNotificationDistances Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        WarningNotificationDistances Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>WarningNotificationDistances</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WarningNotificationDistances</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Distances for emitting warnings according to the timing profile.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/slowSpeedDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeterss5Int32Vvp">slowSpeedDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance in meters for emitting warnings when the speed limit or current speed is slow.
The conditions for a speed to be considered slow are the same ones as for <code>TimingProfile.SLOW_SPEED</code>.
The distance should be greater than 0.
Defaults to 500 meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">slowSpeedDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28WarningNotificationDistancesV28regularSpeedDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/regularSpeedDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk28WarningNotificationDistancesV28regularSpeedDistanceInMeterss5Int32Vvp">regularSpeedDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance in meters for emitting warnings when the speed limit or current speed is regular.
The conditions for a speed to be considered regular are the same ones as for <code>TimingProfile.REGULAR_SPEED</code>.
The distance should be greater than 0.
Defaults to 750 meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">regularSpeedDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28WarningNotificationDistancesV25fastSpeedDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fastSpeedDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk28WarningNotificationDistancesV25fastSpeedDistanceInMeterss5Int32Vvp">fastSpeedDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance in meters for emitting warnings when the speed limit or current speed is fast.
The conditions for a speed to be considered fast are the same ones as for <code>TimingProfile.FAST_SPEED</code>.
The distance should be greater than 0.
Defaults to 1500 meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fastSpeedDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeters07regularfghI004fastfghI0ACs5Int32V_A2Htcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(slowSpeedDistanceInMeters:regularSpeedDistanceInMeters:fastSpeedDistanceInMeters:)"></a>
<a class="token" href="#/s:7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeters07regularfghI004fastfghI0ACs5Int32V_A2Htcfc">init(slowSpeedDistanceInMeters:<wbr/>regularSpeedDistanceInMeters:<wbr/>fastSpeedDistanceInMeters:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">slowSpeedDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">500</span><span class="p">,</span> <span class="nv">regularSpeedDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">750</span><span class="p">,</span> <span class="nv">fastSpeedDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1500</span><span class="p">)</span></code></pre>
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
