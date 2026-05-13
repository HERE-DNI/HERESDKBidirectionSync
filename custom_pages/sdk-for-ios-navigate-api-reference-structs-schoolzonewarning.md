---
title: "Navigation / SchoolZoneWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-schoolzonewarning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SchoolZoneWarning"></a>
<a title="SchoolZoneWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SchoolZoneWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SchoolZoneWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SchoolZoneWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A school zone warning which notifies about a school zone presence on road with a speed limit
different than the default speed limit applicable for cars.
Use <code>SchoolZoneWarningListener</code> to get notifications about school zones.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SchoolZoneWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk17SchoolZoneWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific school zone warning instance.
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
<a name="/s:7heresdk17SchoolZoneWarningV010distanceTobC8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToSchoolZoneInMeters"></a>
<a class="token" href="#/s:7heresdk17SchoolZoneWarningV010distanceTobC8InMetersSdvp">distanceToSchoolZoneInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance from the current location to the school zone in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToSchoolZoneInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SchoolZoneWarningV27speedLimitInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk17SchoolZoneWarningV27speedLimitInMetersPerSecondSdvp">speedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Speed limit meters/second, which applies to current school zone.</p>
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
<a name="/s:7heresdk17SchoolZoneWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk17SchoolZoneWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance type for the warning, e.g. a warning for a new school zone ahead or a warning
for passing a school zone.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SchoolZoneWarningV8timeRuleAA04TimeF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeRule"></a>
<a class="token" href="#/s:7heresdk17SchoolZoneWarningV8timeRuleAA04TimeF0CSgvp">timeRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time rule indicating the time periods for which the warning applies.
If the field is ‘null’ then the warning is applicable at anytime.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-timerule">TimeRule</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SchoolZoneWarningV2id010distanceTobC8InMeters010speedLimithI9PerSecond0F4Type8timeRuleACs5Int32V_S2dAA08DistanceN0OAA04TimeP0CSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceToSchoolZoneInMeters:speedLimitInMetersPerSecond:distanceType:timeRule:)"></a>
<a class="token" href="#/s:7heresdk17SchoolZoneWarningV2id010distanceTobC8InMeters010speedLimithI9PerSecond0F4Type8timeRuleACs5Int32V_S2dAA08DistanceN0OAA04TimeP0CSgtcfc">init(id:<wbr/>distanceToSchoolZoneInMeters:<wbr/>speedLimitInMetersPerSecond:<wbr/>distanceType:<wbr/>timeRule:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceToSchoolZoneInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-distancetype">DistanceType</a></span><span class="p">,</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-timerule">TimeRule</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
