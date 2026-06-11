---
title: "ScheduleDetails"
slug: "sdk-for-ios-explore-api-reference-structs-scheduledetails"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ScheduleDetails"></a>
<a title="ScheduleDetails Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        ScheduleDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ScheduleDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ScheduleDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Encapsulates schedule details complying with the iCalendar specification: <a href="https://tools.ietf.org/html/rfc5545">https://tools.ietf.org/html/rfc5545</a>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ScheduleDetailsV5startSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/start"></a>
<a class="token" href="#/s:7heresdk15ScheduleDetailsV5startSSvp">start</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies when the iCalendar component begins, for example “T000000” (starts at midnight).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">start</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ScheduleDetailsV8durationSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk15ScheduleDetailsV8durationSSvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a positive duration of time for the iCalendar component, for example “PT24H00M” (lasts 24h).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ScheduleDetailsV10recurrenceSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/recurrence"></a>
<a class="token" href="#/s:7heresdk15ScheduleDetailsV10recurrenceSSvp">recurrence</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The recurrence information for a iCalendar component, for example “FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR,SA”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">recurrence</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ScheduleDetailsV5start8duration10recurrenceACSS_S2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(start:duration:recurrence:)"></a>
<a class="token" href="#/s:7heresdk15ScheduleDetailsV5start8duration10recurrenceACSS_S2Stcfc">init(start:<wbr/>duration:<wbr/>recurrence:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">start</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">recurrence</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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
