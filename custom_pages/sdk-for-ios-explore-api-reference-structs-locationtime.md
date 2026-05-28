---
title: "Core / LocationTime"
slug: "sdk-for-ios-explore-api-reference-structs-locationtime"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocationTime"></a>
<a title="LocationTime Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LocationTime Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationTime</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LocationTime</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This struct presents all the time data tied to a location, like an arrival or departure time.
The time data is originally specified in RFC 3339, section 5.6 format. For example,
“2022-03-23T16:07:31+01:00” in Cracow, Poland, i.e. a Central European Time (CET) location.
Note that this struct doesn’t give any data on the tied location. The location should be derived
from the context.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LocationTimeV05localC010Foundation4DateVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localTime"></a>
<a class="token" href="#/s:7heresdk12LocationTimeV05localC010Foundation4DateVvp">localTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time as observed in the tied location. For example, if a route is requested in Cracow,
Poland, the local time is “2022-03-23T16:07:31” in CET, i.e. one hour ahead of the UTC time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">localTime</span><span class="p">:</span> <span class="kt">Date</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LocationTimeV03utcC010Foundation4DateVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/utcTime"></a>
<a class="token" href="#/s:7heresdk12LocationTimeV03utcC010Foundation4DateVvp">utcTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland,
the UTC time is “2022-03-23T15:07:31”, i.e. one hour behind the local time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">utcTime</span><span class="p">:</span> <span class="kt">Date</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LocationTimeV9utcOffsetSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/utcOffset"></a>
<a class="token" href="#/s:7heresdk12LocationTimeV9utcOffsetSdvp">utcOffset</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC)
in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is
UTC-05:00, it is -18000.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">utcOffset</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LocationTimeV05localC003utcC00E6OffsetAC10Foundation4DateV_AISdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(localTime:utcTime:utcOffset:)"></a>
<a class="token" href="#/s:7heresdk12LocationTimeV05localC003utcC00E6OffsetAC10Foundation4DateV_AISdtcfc">init(localTime:<wbr/>utcTime:<wbr/>utcOffset:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">localTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">,</span> <span class="nv">utcTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">,</span> <span class="nv">utcOffset</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span></code></pre>
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
