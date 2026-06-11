---
title: "EVChargingTariffElement"
slug: "sdk-for-ios-navigate-api-reference-structs-evchargingtariffelement"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariffElement"></a>
<a title="EVChargingTariffElement Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-search">Search</a>

        EVChargingTariffElement Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingTariffElement</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTariffElement</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a tariff element, which defines how pricing is applied.
The associated condition assists the client in selecting the appropriate element for a charging session.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingTariffElementV10componentsSayAA0bC14PriceComponentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/components"></a>
<a class="token" href="#/s:7heresdk23EVChargingTariffElementV10componentsSayAA0bC14PriceComponentVGvp">components</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of price components that describe the tariff.
Each of the components should have a different <code><a href="sdk-for-ios-navigate-api-reference-enums-evchargingtariffdimension">EVChargingTariffDimension</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">components</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingTariffElementV9conditionAA0bcD9ConditionVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/condition"></a>
<a class="token" href="#/s:7heresdk23EVChargingTariffElementV9conditionAA0bcD9ConditionVSgvp">condition</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Condition that the charging session needs to meet to apply the tariff element. An element without any
condition is typically present for charging sessions that do not meet any of the conditions.</p>
<p>For example, a tariff element with a lower price can be valid only during nighttime, while a generic
tariff element without conditions applies for daytime charging sessions. The conditions are listed in
priority order. I.e., when <code><a href="../Structs/EVChargingTariffElementCondition.html#/s:7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp">EVChargingTariffElementCondition.date</a></code> is present, it should be matched first,
followed by <code><a href="../Structs/EVChargingTariffElementCondition.html#/s:7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp">EVChargingTariffElementCondition.days</a></code> and so on.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">condition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingtariffelementcondition">EVChargingTariffElementCondition</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingTariffElementV10components9conditionACSayAA0bC14PriceComponentVG_AA0bcD9ConditionVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(components:condition:)"></a>
<a class="token" href="#/s:7heresdk23EVChargingTariffElementV10components9conditionACSayAA0bC14PriceComponentVG_AA0bcD9ConditionVSgtcfc">init(components:<wbr/>condition:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>components: List of price components that describe the tariff.
Each of the components should have a different <code><a href="sdk-for-ios-navigate-api-reference-enums-evchargingtariffdimension">EVChargingTariffDimension</a></code>.</li>
<li>condition: Condition that the charging session needs to meet to apply the tariff element. An element without any
condition is typically present for charging sessions that do not meet any of the conditions.</li>
</ul>
<p>For example, a tariff element with a lower price can be valid only during nighttime, while a generic
  tariff element without conditions applies for daytime charging sessions. The conditions are listed in
  priority order. I.e., when <code><a href="../Structs/EVChargingTariffElementCondition.html#/s:7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp">EVChargingTariffElementCondition.date</a></code> is present, it should be matched first,
  followed by <code><a href="../Structs/EVChargingTariffElementCondition.html#/s:7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp">EVChargingTariffElementCondition.days</a></code> and so on.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">components</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">condition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingtariffelementcondition">EVChargingTariffElementCondition</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
