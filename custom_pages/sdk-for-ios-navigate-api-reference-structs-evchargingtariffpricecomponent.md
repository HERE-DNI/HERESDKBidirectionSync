---
title: "EVChargingTariffPriceComponent"
slug: "sdk-for-ios-navigate-api-reference-structs-evchargingtariffpricecomponent"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariffPriceComponent"></a>
<a title="EVChargingTariffPriceComponent Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-search">Search</a>

        EVChargingTariffPriceComponent Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingTariffPriceComponent</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTariffPriceComponent</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents the price component of an EV charging tariff.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingTariffPriceComponentV9dimensionAA0bC9DimensionOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dimension"></a>
<a class="token" href="#/s:7heresdk30EVChargingTariffPriceComponentV9dimensionAA0bC9DimensionOvp">dimension</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The dimension or type of the price component.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dimension</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-evchargingtariffdimension">EVChargingTariffDimension</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingTariffPriceComponentV5priceSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/price"></a>
<a class="token" href="#/s:7heresdk30EVChargingTariffPriceComponentV5priceSdvp">price</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The price per unit, excluding VAT. The units are defined by the <code><a href="../Structs/EVChargingTariffPriceComponent.html#/s:7heresdk30EVChargingTariffPriceComponentV9dimensionAA0bC9DimensionOvp">EVChargingTariffPriceComponent.dimension</a></code></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">price</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingTariffPriceComponentV3vatSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vat"></a>
<a class="token" href="#/s:7heresdk30EVChargingTariffPriceComponentV3vatSdSgvp">vat</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The VAT percentage of the price component. If not present, no VAT is applicable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vat</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingTariffPriceComponentV4stepSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/step"></a>
<a class="token" href="#/s:7heresdk30EVChargingTariffPriceComponentV4stepSdSgvp">step</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Dimension quantity used as a unit of billing. Present for all other dimensions except
<code><a href="../Enums/EVChargingTariffDimension.html#/s:7heresdk25EVChargingTariffDimensionO4flatyA2CmF">EVChargingTariffDimension.flat</a></code>. The customer is charged price for each full or partial
step of the dimension consumed. For <code><a href="../Enums/EVChargingTariffDimension.html#/s:7heresdk25EVChargingTariffDimensionO6energyyA2CmF">EVChargingTariffDimension.energy</a></code>, the step size unit
is 1 Wh, for <code><a href="../Enums/EVChargingTariffDimension.html#/s:7heresdk25EVChargingTariffDimensionO4timeyA2CmF">EVChargingTariffDimension.time</a></code> and <code><a href="../Enums/EVChargingTariffDimension.html#/s:7heresdk25EVChargingTariffDimensionO11parkingTimeyA2CmF">EVChargingTariffDimension.parkingTime</a></code>
it is 1 second. For example, if step is 300 for time, then time is billed in 5 minute steps, rounded upwards.
Similarly, if step is 100 for energy, then energy is billed in 100 Wh = 0.1 kWh steps.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">step</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingTariffPriceComponentV9dimension5price3vat4stepAcA0bC9DimensionO_S2dSgAJtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(dimension:price:vat:step:)"></a>
<a class="token" href="#/s:7heresdk30EVChargingTariffPriceComponentV9dimension5price3vat4stepAcA0bC9DimensionO_S2dSgAJtcfc">init(dimension:<wbr/>price:<wbr/>vat:<wbr/>step:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">dimension</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-evchargingtariffdimension">EVChargingTariffDimension</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-evchargingtariffdimension">EVChargingTariffDimension</a></span><span class="o">.</span><span class="n">flat</span><span class="p">,</span> <span class="nv">price</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">vat</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">step</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
