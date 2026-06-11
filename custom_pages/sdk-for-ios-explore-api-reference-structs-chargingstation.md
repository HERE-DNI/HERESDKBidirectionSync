---
title: "ChargingStation"
slug: "sdk-for-ios-explore-api-reference-structs-chargingstation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ChargingStation"></a>
<a title="ChargingStation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        ChargingStation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ChargingStation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ChargingStation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Data for an electric vehicle charging station.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ChargingStationV2idSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk15ChargingStationV2idSSSgvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of this charging station. It can only be null when custom charging
stations from non-HERE datasets have been injected on the HERE platform.
By default, with HERE datasets it is guranteed to be not null.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ChargingStationV4nameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk15ChargingStationV4nameSSSgvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Human readable name of this charging station. It can be null when there is no
name associated with the station.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ChargingStationV19connectorAttributesAA0b9ConnectorE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorAttributes"></a>
<a class="token" href="#/s:7heresdk15ChargingStationV19connectorAttributesAA0b9ConnectorE0VSgvp">connectorAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Details of the connector suggested to be used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectorAttributes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-chargingconnectorattributes">ChargingConnectorAttributes</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ChargingStationV5brandAA6NameIDVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/brand"></a>
<a class="token" href="#/s:7heresdk15ChargingStationV5brandAA6NameIDVSgvp">brand</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging station brand.
<code><a href="../Structs/NameID.html#/s:7heresdk6NameIDV4nameSSSgvp">NameID.name</a></code> reflect to charging station brand name.
<code><a href="../Structs/NameID.html#/s:7heresdk6NameIDV2idSSSgvp">NameID.id</a></code> reflect to charging station brand unique ID.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">brand</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-nameid">NameID</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ChargingStationV19chargePointOperatorAA6NameIDVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargePointOperator"></a>
<a class="token" href="#/s:7heresdk15ChargingStationV19chargePointOperatorAA6NameIDVSgvp">chargePointOperator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging station charge-point-operator.
<code><a href="../Structs/NameID.html#/s:7heresdk6NameIDV4nameSSSgvp">NameID.name</a></code> reflect to charge-point-operator name.
<code><a href="../Structs/NameID.html#/s:7heresdk6NameIDV2idSSSgvp">NameID.id</a></code> reflect to charge-point-operator ID.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">chargePointOperator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-nameid">NameID</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ChargingStationV33matchingEMobilityServiceProvidersSayAA6NameIDVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/matchingEMobilityServiceProviders"></a>
<a class="token" href="#/s:7heresdk15ChargingStationV33matchingEMobilityServiceProvidersSayAA6NameIDVGvp">matchingEMobilityServiceProviders</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of matched E-Mobility Service Providers.
Populated only when <code><a href="../Structs/ElectricVehicleOptions.html#/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a></code> was set.
This list reflects the subset of E-Mobility Service Providers supported by the charging station,
from the list specified in the request parameter <code><a href="../Structs/ElectricVehicleOptions.html#/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a></code>.
<code><a href="../Structs/NameID.html#/s:7heresdk6NameIDV4nameSSSgvp">NameID.name</a></code> in each list item reflect to E-Mobility Service Provider name.
<code><a href="../Structs/NameID.html#/s:7heresdk6NameIDV2idSSSgvp">NameID.id</a></code> in each list item reflect to E-Mobility Service Provider id.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">matchingEMobilityServiceProviders</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-nameid">NameID</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ChargingStationV2id4name19connectorAttributes5brand19chargePointOperator33matchingEMobilityServiceProvidersACSSSg_AjA0b9ConnectorG0VSgAA6NameIDVSgAPSayAOGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:name:connectorAttributes:brand:chargePointOperator:matchingEMobilityServiceProviders:)"></a>
<a class="token" href="#/s:7heresdk15ChargingStationV2id4name19connectorAttributes5brand19chargePointOperator33matchingEMobilityServiceProvidersACSSSg_AjA0b9ConnectorG0VSgAA6NameIDVSgAPSayAOGtcfc">init(id:<wbr/>name:<wbr/>connectorAttributes:<wbr/>brand:<wbr/>chargePointOperator:<wbr/>matchingEMobilityServiceProviders:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">connectorAttributes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-chargingconnectorattributes">ChargingConnectorAttributes</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">brand</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-nameid">NameID</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">chargePointOperator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-nameid">NameID</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">matchingEMobilityServiceProviders</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-nameid">NameID</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
