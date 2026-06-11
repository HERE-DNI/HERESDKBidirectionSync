---
title: "TimeRule"
slug: "sdk-for-ios-navigate-api-reference-classes-timerule"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TimeRule"></a>
<a title="TimeRule Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-core">Core</a>

        TimeRule Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TimeRule</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TimeRule</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TimeRule</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TimeRule</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification.
For example:
-*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents:
March 2nd Sunday 02h:00m for 9 months
ONLY DURING November 1st Sunday 02h:00m from 9 months ago
BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00</p>
<p>The operator * represents reccuring occurrence, <code>+</code> represents a logical OR operation and <code>-</code> represents exclusion meaning, BUT NOT operations.</p>
<p>This example string represents a time period that meets the following criteria:</p>
<ul>
<li><code>M3f21h2</code>: M3 denotes third month of the year, i.e. March,
f2 stands for the second Sunday of the month (as “f” might indicate “first”, “second”, “third”, etc.),
1 stands for the day of the week (1…7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li><code>{M9}</code>: This denotes “for 9 months”, with “M9” standing for nine months. The brackets {} indicate a duration.</li>
<li><code>M11f12h2</code>: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month,
2 stands for the day of the week (1…7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li>{-M9}: This denotes “9 months ago from the current stated time”, with “-M9” standing for nine months in the past.</li>
<li><code>(h15){h2}(h20){h2}</code>: 15:00 to 17:00 OR 20:00 to 22:00
The brackets {} denotes duration, and the negative sign - represents a past duration.</li>
</ul>
<p>Note: The time period is a logical AND (&amp;&amp;) combination of two components or points in time and it only applies if a point in time is in both components.</p>
<p>For more advanced examples of <code>TimeRule</code> see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TimeRuleC04timeC00D17ZoneOffsetSeconds7dstSpecACSS_s5Int32VSStcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(timeRule:timeZoneOffsetSeconds:dstSpec:)"></a>
<a class="token" href="#/s:7heresdk8TimeRuleC04timeC00D17ZoneOffsetSeconds7dstSpecACSS_s5Int32VSStcfc">init(timeRule:<wbr/>timeZoneOffsetSeconds:<wbr/>dstSpec:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">timeRule</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">timeZoneOffsetSeconds</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">dstSpec</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>timeRule</em>
</code>
</td>
<td>
<div>
<p>The time rule as a string in ISO 14825 format.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>timeZoneOffsetSeconds</em>
</code>
</td>
<td>
<div>
<p>The time zone offset in seconds for the location where the time rule applies.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>dstSpec</em>
</code>
</td>
<td>
<div>
<p>Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TimeRuleC04timeC6StringSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeRuleString"></a>
<a class="token" href="#/s:7heresdk8TimeRuleC04timeC6StringSSvp">timeRuleString</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time rule as a string in ISO 14825 format.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeRuleString</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TimeRuleC21timeZoneOffsetSecondss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeZoneOffsetSeconds"></a>
<a class="token" href="#/s:7heresdk8TimeRuleC21timeZoneOffsetSecondss5Int32Vvp">timeZoneOffsetSeconds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time zone offset in seconds for the location where the time rule applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeZoneOffsetSeconds</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TimeRuleC7dstSpecSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dstSpec"></a>
<a class="token" href="#/s:7heresdk8TimeRuleC7dstSpecSSvp">dstSpec</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dstSpec</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TimeRuleC9appliesTo04dateB0Sb10Foundation4DateV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/appliesTo(dateTime:)"></a>
<a class="token" href="#/s:7heresdk8TimeRuleC9appliesTo04dateB0Sb10Foundation4DateV_tF">appliesTo(dateTime:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">appliesTo</span><span class="p">(</span><span class="nv">dateTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>dateTime</em>
</code>
</td>
<td>
<div>
<p>date and time that should be used for rule verification.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>true</code> if the time domain rules applies to the given date and time., <code>false</code> - otherwise.</p>
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
