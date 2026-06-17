---
title: "EnergyMix"
slug: "sdk-for-ios-navigate-structs-energymix"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EnergyMix"></a>
<a title="EnergyMix Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-search">Search</a>

        EnergyMix Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EnergyMix</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EnergyMix</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents details on the energy supplied at the charging location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EnergyMixV07isGreenB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isGreenEnergy"></a>
<a class="token" href="#/s:7heresdk9EnergyMixV07isGreenB0Sbvp">isGreenEnergy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Boolean flag indicating if the energy is 100% from regenerative sources.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isGreenEnergy</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EnergyMixV13energySourcesSayAA0B6SourceVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/energySources"></a>
<a class="token" href="#/s:7heresdk9EnergyMixV13energySourcesSayAA0B6SourceVGvp">energySources</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of energy sources.
The sum of the percentages over the energy sources should be 100%.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">energySources</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-energysource">EnergySource</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EnergyMixV8supplierSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supplier"></a>
<a class="token" href="#/s:7heresdk9EnergyMixV8supplierSSSgvp">supplier</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of the energy supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">supplier</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EnergyMixV13energyProductSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/energyProduct"></a>
<a class="token" href="#/s:7heresdk9EnergyMixV13energyProductSSSgvp">energyProduct</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of the energy suppliers product or plan.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">energyProduct</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EnergyMixV20environmentalImpactsSayAA19EnvironmentalImpactVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/environmentalImpacts"></a>
<a class="token" href="#/s:7heresdk9EnergyMixV20environmentalImpactsSayAA19EnvironmentalImpactVGvp">environmentalImpacts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of environmental impacts from this energy mix.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">environmentalImpacts</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-environmentalimpact">EnvironmentalImpact</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EnergyMixV07isGreenB013energySources8supplier0F7Product20environmentalImpactsACSb_SayAA0B6SourceVGSSSgALSayAA19EnvironmentalImpactVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(isGreenEnergy:energySources:supplier:energyProduct:environmentalImpacts:)"></a>
<a class="token" href="#/s:7heresdk9EnergyMixV07isGreenB013energySources8supplier0F7Product20environmentalImpactsACSb_SayAA0B6SourceVGSSSgALSayAA19EnvironmentalImpactVGtcfc">init(isGreenEnergy:<wbr/>energySources:<wbr/>supplier:<wbr/>energyProduct:<wbr/>environmentalImpacts:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">isGreenEnergy</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">energySources</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-energysource">EnergySource</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">supplier</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">energyProduct</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">environmentalImpacts</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-environmentalimpact">EnvironmentalImpact</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
