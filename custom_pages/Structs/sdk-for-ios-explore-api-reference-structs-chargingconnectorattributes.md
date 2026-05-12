---
title: "ChargingConnectorAttributes Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-chargingconnectorattributes"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ChargingConnectorAttributes.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/ChargingConnectorAttributes"></a>
<a title="ChargingConnectorAttributes Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ChargingConnectorAttributes Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct ChargingConnectorAttributes : Hashable</code></pre>
</div>
</div>
<p>Details of the connector that is suggested to be used in the section’s
<code><a href="../Structs/PostAction.html">PostAction</a></code>‘s for charging.</p>
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
<pre><code>public var powerInKilowatts: Double</code></pre>
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
<pre><code>public var currentInAmperes: Double?</code></pre>
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
<pre><code>public var voltageInVolts: Double?</code></pre>
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
<pre><code>public var supplyType: ChargingSupplyType?</code></pre>
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
<pre><code>public var connectorType: ChargingConnectorType?</code></pre>
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
<pre><code>public init(powerInKilowatts: Double, currentInAmperes: Double? = nil, voltageInVolts: Double? = nil, supplyType: ChargingSupplyType? = nil, connectorType: ChargingConnectorType? = nil)</code></pre>
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



</div>
`
}</HTMLBlock>
