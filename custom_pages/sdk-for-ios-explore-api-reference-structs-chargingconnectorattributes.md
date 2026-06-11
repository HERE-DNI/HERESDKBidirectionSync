---
title: "sdk-for-ios-explore-api-reference-structs-chargingconnectorattributes"
slug: "sdk-for-ios-explore-api-reference-structs-chargingconnectorattributes"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ChargingConnectorAttributes"></a>
<a title="ChargingConnectorAttributes Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        ChargingConnectorAttributes Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ChargingConnectorAttributes</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ChargingConnectorAttributes</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Details of the connector that is suggested to be used in the section’s
<code><a href="sdk-for-ios-explore-api-reference-structs-postaction">PostAction</a></code>‘s for charging.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ChargingConnectorAttributesV16powerInKilowattsSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/powerInKilowatts"></a>
<a class="token" href="#/s:7heresdk27ChargingConnectorAttributesV16powerInKilowattsSdvp">powerInKilowatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Power supplied by the suggested connector in kW.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">powerInKilowatts</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ChargingConnectorAttributesV16currentInAmperesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentInAmperes"></a>
<a class="token" href="#/s:7heresdk27ChargingConnectorAttributesV16currentInAmperesSdSgvp">currentInAmperes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current of the suggested connector in Amperes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currentInAmperes</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ChargingConnectorAttributesV14voltageInVoltsSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/voltageInVolts"></a>
<a class="token" href="#/s:7heresdk27ChargingConnectorAttributesV14voltageInVoltsSdSgvp">voltageInVolts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Voltage of the suggested connector in Volts.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">voltageInVolts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ChargingConnectorAttributesV10supplyTypeAA0b6SupplyF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supplyType"></a>
<a class="token" href="#/s:7heresdk27ChargingConnectorAttributesV10supplyTypeAA0b6SupplyF0OSgvp">supplyType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Supply type of the suggested connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">supplyType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingsupplytype">ChargingSupplyType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ChargingConnectorAttributesV13connectorTypeAA0bcF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorType"></a>
<a class="token" href="#/s:7heresdk27ChargingConnectorAttributesV13connectorTypeAA0bcF0OSgvp">connectorType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Suggested connector for charging at this station.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectorType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingconnectortype">ChargingConnectorType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ChargingConnectorAttributesV16powerInKilowatts07currentF7Amperes07voltageF5Volts10supplyType09connectorM0ACSd_SdSgAiA0b6SupplyM0OSgAA0bcM0OSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(powerInKilowatts:currentInAmperes:voltageInVolts:supplyType:connectorType:)"></a>
<a class="token" href="#/s:7heresdk27ChargingConnectorAttributesV16powerInKilowatts07currentF7Amperes07voltageF5Volts10supplyType09connectorM0ACSd_SdSgAiA0b6SupplyM0OSgAA0bcM0OSgtcfc">init(powerInKilowatts:<wbr/>currentInAmperes:<wbr/>voltageInVolts:<wbr/>supplyType:<wbr/>connectorType:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">powerInKilowatts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">currentInAmperes</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">voltageInVolts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">supplyType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingsupplytype">ChargingSupplyType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">connectorType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingconnectortype">ChargingConnectorType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
