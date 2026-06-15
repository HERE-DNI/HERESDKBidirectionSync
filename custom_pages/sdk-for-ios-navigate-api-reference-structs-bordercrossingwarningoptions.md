---
title: "BorderCrossingWarningOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-bordercrossingwarningoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BorderCrossingWarningOptions"></a>
<a title="BorderCrossingWarningOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        BorderCrossingWarningOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>BorderCrossingWarningOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BorderCrossingWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Border crossing warning options.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28BorderCrossingWarningOptionsV014filterOutStateB8WarningsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/filterOutStateBorderWarnings"></a>
<a class="token" href="#/s:7heresdk28BorderCrossingWarningOptionsV014filterOutStateB8WarningsSbvp">filterOutStateBorderWarnings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If set to <code>true</code>, all the state border crossing notifications will not be given.
If the value is <code>false</code>, all border crossing notifications will be given for
both country borders and state borders. By default, the
<code>BorderCrossingWarningOptions.filterOutStateBorderWarnings</code> is set to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">filterOutStateBorderWarnings</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28BorderCrossingWarningOptionsV35includeCommercialVehicleRegulationsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/includeCommercialVehicleRegulations"></a>
<a class="token" href="#/s:7heresdk28BorderCrossingWarningOptionsV35includeCommercialVehicleRegulationsSbvp">includeCommercialVehicleRegulations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If set to <code>true</code>, commercial vehicle regulations data will be included in border crossing warnings
when available. If set to <code>false</code>, the commercial vehicle regulations field will be stripped from
warnings even if the data is available in the map. By default, this is set to <code>false</code>.
This is useful for commercial vehicles that need CVR information - they should explicitly enable it.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">includeCommercialVehicleRegulations</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28BorderCrossingWarningOptionsV014filterOutStateB8Warnings35includeCommercialVehicleRegulationsACSb_Sbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(filterOutStateBorderWarnings:includeCommercialVehicleRegulations:)"></a>
<a class="token" href="#/s:7heresdk28BorderCrossingWarningOptionsV014filterOutStateB8Warnings35includeCommercialVehicleRegulationsACSb_Sbtcfc">init(filterOutStateBorderWarnings:<wbr/>includeCommercialVehicleRegulations:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">filterOutStateBorderWarnings</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">true</span><span class="p">,</span> <span class="nv">includeCommercialVehicleRegulations</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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
