---
title: "EVChargingOpeningHours"
slug: "sdk-for-ios-navigate-api-reference-structs-evchargingopeninghours"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHours"></a>
<a title="EVChargingOpeningHours Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-search">Search</a>

        EVChargingOpeningHours Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingOpeningHours</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingOpeningHours</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents the times when the EVSEs at the charging location can be accessed for charging.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV8open24x7Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/open24x7"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV8open24x7Sbvp">open24x7</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the charging location is open 24 hours a day, 7 days per week.
If true, <code><a href="../Structs/EVChargingOpeningHours.html#/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp">EVChargingOpeningHours.regularSchedule</a></code> and <code><a href="../Structs/EVChargingOpeningHours.html#/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp">EVChargingOpeningHours.exceptions</a></code> will be empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">open24x7</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV18chargingWhenClosedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingWhenClosed"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV18chargingWhenClosedSbvp">chargingWhenClosed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if it is allowed to leave vehicles in the charging location to continue
charging outside opening hours.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">chargingWhenClosed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/regularSchedule"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp">regularSchedule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of regular opening hours schedule for EV charging locations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">regularSchedule</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingopeninghoursschedule">EVChargingOpeningHoursSchedule</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/exceptions"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp">exceptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of opening hours exceptions for EV charging locations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">exceptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingopeninghoursexception">EVChargingOpeningHoursException</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV8open24x718chargingWhenClosed15regularSchedule10exceptionsACSb_SbSayAA0bcdJ0VGSayAA0bcD9ExceptionVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(open24x7:chargingWhenClosed:regularSchedule:exceptions:)"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV8open24x718chargingWhenClosed15regularSchedule10exceptionsACSb_SbSayAA0bcdJ0VGSayAA0bcD9ExceptionVGtcfc">init(open24x7:<wbr/>chargingWhenClosed:<wbr/>regularSchedule:<wbr/>exceptions:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">open24x7</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">chargingWhenClosed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">true</span><span class="p">,</span> <span class="nv">regularSchedule</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingopeninghoursschedule">EVChargingOpeningHoursSchedule</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">exceptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingopeninghoursexception">EVChargingOpeningHoursException</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
