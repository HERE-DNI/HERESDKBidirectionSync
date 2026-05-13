---
title: "ChargingActionDetails Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-chargingactiondetails"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ChargingActionDetails.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/ChargingActionDetails"></a>
<a title="ChargingActionDetails Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ChargingActionDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct ChargingActionDetails : Hashable</code></pre>
</div>
</div>
<p>Parameters related to the electric vehicle’s charging action.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ChargingActionDetailsV26consumablePowerInKilowattsSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/consumablePowerInKilowatts"></a>
<a class="token" href="#/s:7heresdk21ChargingActionDetailsV26consumablePowerInKilowattsSdvp">consumablePowerInKilowatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum charging power (in kW) available to the vehicle, based on the properties of the charging station and the vehicle.
A valid <code>ChargingActionDetails</code> object will have positive <code>ChargingActionDetails.consumablePowerInKilowatts</code>.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var consumablePowerInKilowatts: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ChargingActionDetailsV28arrivalChargeInKilowattHoursSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/arrivalChargeInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21ChargingActionDetailsV28arrivalChargeInKilowattHoursSdvp">arrivalChargeInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimated vehicle battery charge before this action (in kWh).
A valid <code>ChargingActionDetails</code> object will have positive <code>ChargingActionDetails.arrivalChargeInKilowattHours</code>.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var arrivalChargeInKilowattHours: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ChargingActionDetailsV27targetChargeInKilowattHoursSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/targetChargeInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21ChargingActionDetailsV27targetChargeInKilowattHoursSdvp">targetChargeInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Level to which vehicle battery should be charged by this action (in kWh).
A valid <code>ChargingActionDetails</code> object will have positive <code>ChargingActionDetails.targetChargeInKilowattHours</code>.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var targetChargeInKilowattHours: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ChargingActionDetailsV26consumablePowerInKilowatts013arrivalChargeG13KilowattHours06targetjgkL0ACSd_S2dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(consumablePowerInKilowatts:arrivalChargeInKilowattHours:targetChargeInKilowattHours:)"></a>
<a class="token" href="#/s:7heresdk21ChargingActionDetailsV26consumablePowerInKilowatts013arrivalChargeG13KilowattHours06targetjgkL0ACSd_S2dtcfc">init(consumablePowerInKilowatts:<wbr/>arrivalChargeInKilowattHours:<wbr/>targetChargeInKilowattHours:<wbr/>)</a>
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
<pre><code>public init(consumablePowerInKilowatts: Double = 0.0, arrivalChargeInKilowattHours: Double = 0.0, targetChargeInKilowattHours: Double = 0.0)</code></pre>
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
