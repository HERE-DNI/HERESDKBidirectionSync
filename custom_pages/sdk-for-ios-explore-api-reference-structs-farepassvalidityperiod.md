---
title: "FarePassValidityPeriod"
slug: "sdk-for-ios-explore-api-reference-structs-farepassvalidityperiod"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FarePassValidityPeriod"></a>
<a title="FarePassValidityPeriod Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        FarePassValidityPeriod Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>FarePassValidityPeriod</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FarePassValidityPeriod</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Specifies a temporal validity period for a pass</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22FarePassValidityPeriodV10periodTypeAA0bcdeG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/periodType"></a>
<a class="token" href="#/s:7heresdk22FarePassValidityPeriodV10periodTypeAA0bcdeG0Ovp">periodType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies one of the <code><a href="sdk-for-ios-explore-api-reference-enums-farepassvalidityperiodtype">FarePassValidityPeriodType</a></code> periods.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">periodType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-farepassvalidityperiodtype">FarePassValidityPeriodType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22FarePassValidityPeriodV5counts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/count"></a>
<a class="token" href="#/s:7heresdk22FarePassValidityPeriodV5counts5Int32VSgvp">count</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies how many <code><a href="../Structs/FarePassValidityPeriod.html#/s:7heresdk22FarePassValidityPeriodV10periodTypeAA0bcdeG0Ovp">FarePassValidityPeriod.periodType</a></code>s are covered by the pass. Present if <code><a href="../Structs/FarePassValidityPeriod.html#/s:7heresdk22FarePassValidityPeriodV10periodTypeAA0bcdeG0Ovp">FarePassValidityPeriod.periodType</a></code> is
<code><a href="../Enums/FarePassValidityPeriodType.html#/s:7heresdk26FarePassValidityPeriodTypeO7minutesyA2CmF">FarePassValidityPeriodType.minutes</a></code>, <code><a href="../Enums/FarePassValidityPeriodType.html#/s:7heresdk26FarePassValidityPeriodTypeO4daysyA2CmF">FarePassValidityPeriodType.days</a></code> or <code><a href="../Enums/FarePassValidityPeriodType.html#/s:7heresdk26FarePassValidityPeriodTypeO6monthsyA2CmF">FarePassValidityPeriodType.months</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">count</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22FarePassValidityPeriodV10periodType5countAcA0bcdeG0O_s5Int32VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(periodType:count:)"></a>
<a class="token" href="#/s:7heresdk22FarePassValidityPeriodV10periodType5countAcA0bcdeG0O_s5Int32VSgtcfc">init(periodType:<wbr/>count:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">periodType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-farepassvalidityperiodtype">FarePassValidityPeriodType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-farepassvalidityperiodtype">FarePassValidityPeriodType</a></span><span class="o">.</span><span class="n">annual</span><span class="p">,</span> <span class="nv">count</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
