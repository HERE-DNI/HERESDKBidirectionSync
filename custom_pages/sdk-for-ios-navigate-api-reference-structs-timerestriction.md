---
title: "TimeRestriction"
slug: "sdk-for-ios-navigate-api-reference-structs-timerestriction"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TimeRestriction"></a>
<a title="TimeRestriction Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-transport">Transport</a>

        TimeRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TimeRestriction</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TimeRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents restriction based on time.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TimeRestrictionV8categoryAC8CategoryOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/category"></a>
<a class="token" href="#/s:7heresdk15TimeRestrictionV8categoryAC8CategoryOvp">category</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The category of the time restriction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">category</span><span class="p">:</span> <span class="kt">TimeRestriction</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-timerestriction-category">Category</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TimeRestrictionV13applicabilitySayAA13TransportTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/applicability"></a>
<a class="token" href="#/s:7heresdk15TimeRestrictionV13applicabilitySayAA13TransportTypeOGvp">applicability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies to which transportation types the time rules apply.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">applicability</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transporttype">TransportType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TimeRestrictionV8timeRuleAA0bE0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeRule"></a>
<a class="token" href="#/s:7heresdk15TimeRestrictionV8timeRuleAA0bE0CSgvp">timeRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time rule in TimeDomain format, which is part of the GDF specification.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-timerule">TimeRule</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TimeRestrictionV8category13applicability8timeRuleA2C8CategoryO_SayAA13TransportTypeOGAA0bG0CSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(category:applicability:timeRule:)"></a>
<a class="token" href="#/s:7heresdk15TimeRestrictionV8category13applicability8timeRuleA2C8CategoryO_SayAA13TransportTypeOGAA0bG0CSgtcfc">init(category:<wbr/>applicability:<wbr/>timeRule:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">category</span><span class="p">:</span> <span class="kt">TimeRestriction</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-timerestriction-category">Category</a></span> <span class="o">=</span> <span class="kt">TimeRestriction</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-timerestriction-category">Category</a></span><span class="o">.</span><span class="n">prohibited</span><span class="p">,</span> <span class="nv">applicability</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transporttype">TransportType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-timerule">TimeRule</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TimeRestrictionV8CategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Category"></a>
<a class="token" href="#/s:7heresdk15TimeRestrictionV8CategoryO">Category</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Category of time restriction.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-timerestriction-category">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">Category</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
