---
title: "sdk-for-ios-explore-api-reference-enums-evcharginglocationfeature"
slug: "sdk-for-ios-explore-api-reference-enums-evcharginglocationfeature"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVChargingLocationFeature"></a>
<a title="EVChargingLocationFeature Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-search">Search</a>
<img alt="" id="carat" src="/carat.png"/>
        EVChargingLocationFeature Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingLocationFeature</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVChargingLocationFeature</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Optional features that can be requested for EV charging locations.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO5evsesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/evses"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO5evsesyA2CmF">evses</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC5evsesSayAA8EVSEInfoVGvp">EVChargingLocation.evses</a></code> will be returned.
If <code><a href="../Enums/EVChargingLocationFeature.html#/s:7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF">EVChargingLocationFeature.connectorGroups</a></code> is also included, then
<code><a href="../Structs/EVChargingConnectorGroup.html#/s:7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp">EVChargingConnectorGroup.connectors</a></code> will also be returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">evses</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO17truckRestrictionsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truckRestrictions"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO17truckRestrictionsyA2CmF">truckRestrictions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC17truckRestrictionsAA0B16TruckRestrictionVSgvp">EVChargingLocation.truckRestrictions</a></code> will be returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">truckRestrictions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO12locationInfoyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/locationInfo"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO12locationInfoyA2CmF">locationInfo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC5cpoIDSSSgvp">EVChargingLocation.cpoID</a></code>, <code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp">EVChargingLocation.facilityTypes</a></code>,
<code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC11parkingTypeAA07ParkingE0OSgvp">EVChargingLocation.parkingType</a></code>, <code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC9energyMixAA06EnergyE0VSgvp">EVChargingLocation.energyMix</a></code>,
and <code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC12openingHoursAA0b7OpeningE0VSgvp">EVChargingLocation.openingHours</a></code> will be returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">locationInfo</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO5emspsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/emsps"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO5emspsyA2CmF">emsps</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC25eMobilityServiceProvidersSayAA0B8OperatorVGvp">EVChargingLocation.eMobilityServiceProviders</a></code> will be returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">emsps</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/connectorGroups"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF">connectorGroups</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC15connectorGroupsSayAA0B14ConnectorGroupVGvp">EVChargingLocation.connectorGroups</a></code> will be returned.
To ensure <code><a href="../Structs/EVChargingConnectorGroup.html#/s:7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp">EVChargingConnectorGroup.connectors</a></code> is available, also include
<code><a href="../Enums/EVChargingLocationFeature.html#/s:7heresdk25EVChargingLocationFeatureO5evsesyA2CmF">EVChargingLocationFeature.evses</a></code>.
To ensure <code><a href="../Structs/EVChargingConnectorGroup.html#/s:7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp">EVChargingConnectorGroup.tariffIndexes</a></code> is available, also include
<code><a href="../Enums/EVChargingLocationFeature.html#/s:7heresdk25EVChargingLocationFeatureO7tariffsyA2CmF">EVChargingLocationFeature.tariffs</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">connectorGroups</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO7tariffsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tariffs"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO7tariffsyA2CmF">tariffs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="../Structs/EVChargingConnectorGroup.html#/s:7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp">EVChargingConnectorGroup.tariffIndexes</a></code> will be returned.
Ignored if neither <code><a href="../Enums/EVChargingLocationFeature.html#/s:7heresdk25EVChargingLocationFeatureO5evsesyA2CmF">EVChargingLocationFeature.evses</a></code> nor
<code><a href="../Enums/EVChargingLocationFeature.html#/s:7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF">EVChargingLocationFeature.connectorGroups</a></code> are included.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tariffs</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO6nearbyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/nearby"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO6nearbyyA2CmF">nearby</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="../Classes/EVChargingLocation.html#/s:7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp">EVChargingLocation.facilityTypes</a></code> will be returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">nearby</span></code></pre>
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
