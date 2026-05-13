---
title: "MapData / SegmentSpecialSpeedSituation"
slug: "sdk-for-ios-navigate-api-reference-structs-segmentspecialspeedsituation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentSpecialSpeedSituation"></a>
<a title="SegmentSpecialSpeedSituation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SegmentSpecialSpeedSituation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SegmentSpecialSpeedSituation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentSpecialSpeedSituation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A special speed situation indicates a speed that exists under special circumstances. It can be used to further refine
the estimation of traversal times, route calculation and calculation of route guidance timing.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28SegmentSpecialSpeedSituationV07specialD4TypeAA0cdG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/specialSpeedType"></a>
<a class="token" href="#/s:7heresdk28SegmentSpecialSpeedSituationV07specialD4TypeAA0cdG0Ovp">specialSpeedType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the speed situation type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">specialSpeedType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-specialspeedtype">SpecialSpeedType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28SegmentSpecialSpeedSituationV27speedLimitInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk28SegmentSpecialSpeedSituationV27speedLimitInMetersPerSecondSdvp">speedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Overrides normal speed limit for this situation.</p>
<p>May be 0 to indicate no special speed limit in the case of special_speed_type = SPEED_BUMPS_PRESENT
and special_speed_type = LANE_DEPENDENT.
Speed limit in meter per seconds.</p>
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
<a name="/s:7heresdk28SegmentSpecialSpeedSituationV13appliesDuringSayAA8TimeRuleCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/appliesDuring"></a>
<a class="token" href="#/s:7heresdk28SegmentSpecialSpeedSituationV13appliesDuringSayAA8TimeRuleCGvp">appliesDuring</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The times during which the condition applies.
May be empty for all special_speed_type values except <code>TIME_DEPENDENT</code> and <code>APPROXIMATE_SEASONAL_TIME</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">appliesDuring</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-timerule">TimeRule</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28SegmentSpecialSpeedSituationV07specialD4Type27speedLimitInMetersPerSecond13appliesDuringAcA0cdG0O_SdSayAA8TimeRuleCGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(specialSpeedType:speedLimitInMetersPerSecond:appliesDuring:)"></a>
<a class="token" href="#/s:7heresdk28SegmentSpecialSpeedSituationV07specialD4Type27speedLimitInMetersPerSecond13appliesDuringAcA0cdG0O_SdSayAA8TimeRuleCGtcfc">init(specialSpeedType:<wbr/>speedLimitInMetersPerSecond:<wbr/>appliesDuring:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with default values.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>specialSpeedType: Represents the speed situation type.</li>
<li>speedLimitInMetersPerSecond: Overrides normal speed limit for this situation.</li>
</ul>
<p>May be 0 to indicate no special speed limit in the case of special_speed_type = SPEED_BUMPS_PRESENT
  and special_speed_type = LANE_DEPENDENT.
  Speed limit in meter per seconds.</p>
<ul>
<li>appliesDuring: The times during which the condition applies.
May be empty for all special_speed_type values except <code>TIME_DEPENDENT</code> and <code>APPROXIMATE_SEASONAL_TIME</code>.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">specialSpeedType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-specialspeedtype">SpecialSpeedType</a></span><span class="p">,</span> <span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">appliesDuring</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-timerule">TimeRule</a></span><span class="p">])</span></code></pre>
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
