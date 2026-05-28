---
title: "Search / EVChargingOpeningHoursSchedule"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingopeninghoursschedule"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHoursSchedule"></a>
<a title="EVChargingOpeningHoursSchedule Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingOpeningHoursSchedule Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingOpeningHoursSchedule</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingOpeningHoursSchedule</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Opening hours schedule for EV charging locations, represented by a list of days of the week
during which the location is open in the given time periods.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingOpeningHoursScheduleV4daysSayAA9DayOfWeekOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/days"></a>
<a class="token" href="#/s:7heresdk30EVChargingOpeningHoursScheduleV4daysSayAA9DayOfWeekOGvp">days</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Day(s) of the week.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">days</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-dayofweek">DayOfWeek</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingOpeningHoursScheduleV7periodsSayAA14TimeOfDayRangeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/periods"></a>
<a class="token" href="#/s:7heresdk30EVChargingOpeningHoursScheduleV7periodsSayAA14TimeOfDayRangeVGvp">periods</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of time periods.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">periods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-timeofdayrange">TimeOfDayRange</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingOpeningHoursScheduleV4days7periodsACSayAA9DayOfWeekOG_SayAA04TimeiH5RangeVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(days:periods:)"></a>
<a class="token" href="#/s:7heresdk30EVChargingOpeningHoursScheduleV4days7periodsACSayAA9DayOfWeekOG_SayAA04TimeiH5RangeVGtcfc">init(days:<wbr/>periods:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">days</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-dayofweek">DayOfWeek</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">periods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-timeofdayrange">TimeOfDayRange</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
