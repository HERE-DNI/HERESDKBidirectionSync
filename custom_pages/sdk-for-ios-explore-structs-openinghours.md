---
title: "OpeningHours"
slug: "sdk-for-ios-explore-structs-openinghours"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/OpeningHours"></a>
<a title="OpeningHours Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-search">Search</a>

        OpeningHours Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>OpeningHours</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">OpeningHours</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents opening hours information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12OpeningHoursV4textSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/text"></a>
<a class="token" href="#/s:7heresdk12OpeningHoursV4textSaySSGvp">text</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of opening hours presented as localized text.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">text</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12OpeningHoursV6isOpenSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isOpen"></a>
<a class="token" href="#/s:7heresdk12OpeningHoursV6isOpenSbvp">isOpen</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Boolean flag informing if the place is open or closed at the time when the search request was initiated.
For offline search, this is calculated using device’s time,
so it may give incorrect value if device and place are located in different time zones.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isOpen</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12OpeningHoursV19scheduleDetailsListSayAA08ScheduleE0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/scheduleDetailsList"></a>
<a class="token" href="#/s:7heresdk12OpeningHoursV19scheduleDetailsListSayAA08ScheduleE0VGvp">scheduleDetailsList</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of schedule details.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">scheduleDetailsList</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-structs-scheduledetails">ScheduleDetails</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12OpeningHoursV10categoriesSayAA13PlaceCategoryCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/categories"></a>
<a class="token" href="#/s:7heresdk12OpeningHoursV10categoriesSayAA13PlaceCategoryCGvp">categories</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of categories related to opening hours information.
This data is not available in offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">categories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-classes-placecategory">PlaceCategory</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12OpeningHoursV4text6isOpen19scheduleDetailsList10categoriesACSaySSG_SbSayAA08ScheduleH0VGSayAA13PlaceCategoryCGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(text:isOpen:scheduleDetailsList:categories:)"></a>
<a class="token" href="#/s:7heresdk12OpeningHoursV4text6isOpen19scheduleDetailsList10categoriesACSaySSG_SbSayAA08ScheduleH0VGSayAA13PlaceCategoryCGtcfc">init(text:<wbr/>isOpen:<wbr/>scheduleDetailsList:<wbr/>categories:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">text</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">],</span> <span class="nv">isOpen</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">scheduleDetailsList</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-structs-scheduledetails">ScheduleDetails</a></span><span class="p">],</span> <span class="nv">categories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-classes-placecategory">PlaceCategory</a></span><span class="p">])</span></code></pre>
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
