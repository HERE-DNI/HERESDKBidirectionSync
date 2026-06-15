---
title: "LowSpeedZoneWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-lowspeedzonewarning"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LowSpeedZoneWarning"></a>
<a title="LowSpeedZoneWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        LowSpeedZoneWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LowSpeedZoneWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LowSpeedZoneWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides low speed zone. The main field describing the low speed zone is <code>LowSpeedZoneWarning.speed_limit_in_meters_per_second</code>
specifying the speed limit of the low speed zone.
Use <code>LowSpeedZoneWarningListener</code> to get notifications about upcoming low speed zones.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LowSpeedZoneWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk19LowSpeedZoneWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific low speed zone warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LowSpeedZoneWarningV010distanceTobcD8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToLowSpeedZoneInMeters"></a>
<a class="token" href="#/s:7heresdk19LowSpeedZoneWarningV010distanceTobcD8InMetersSdvp">distanceToLowSpeedZoneInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance to the low speed warning in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToLowSpeedZoneInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LowSpeedZoneWarningV27speedLimitInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk19LowSpeedZoneWarningV27speedLimitInMetersPerSecondSdvp">speedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Speed limit of the low speed zone.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LowSpeedZoneWarningV12distanceTypeAA08DistanceG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk19LowSpeedZoneWarningV12distanceTypeAA08DistanceG0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance type for the warning, e.g. a warning for a new low speed zone ahead or a warning
for passing a low speed zone.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LowSpeedZoneWarningV16segmentReferenceAA07SegmentG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentReference"></a>
<a class="token" href="#/s:7heresdk19LowSpeedZoneWarningV16segmentReferenceAA07SegmentG0Vvp">segmentReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The reference to the segment where the low speed zone is located. It can be used to identify the
location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LowSpeedZoneWarningV2id010distanceTobcD8InMeters010speedLimitiJ9PerSecond0G4Type16segmentReferenceACs5Int32V_S2dAA08DistanceO0OAA07SegmentQ0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceToLowSpeedZoneInMeters:speedLimitInMetersPerSecond:distanceType:segmentReference:)"></a>
<a class="token" href="#/s:7heresdk19LowSpeedZoneWarningV2id010distanceTobcD8InMeters010speedLimitiJ9PerSecond0G4Type16segmentReferenceACs5Int32V_S2dAA08DistanceO0OAA07SegmentQ0Vtcfc">init(id:<wbr/>distanceToLowSpeedZoneInMeters:<wbr/>speedLimitInMetersPerSecond:<wbr/>distanceType:<wbr/>segmentReference:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceToLowSpeedZoneInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span><span class="p">,</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">)</span></code></pre>
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
