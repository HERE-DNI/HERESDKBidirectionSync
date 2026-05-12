---
title: "EVChargingPool Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingpool"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingPool.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingPool"></a>
<a title="EVChargingPool Structure Reference"></a>
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
        EVChargingPool Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingPool : Hashable</code></pre>
</div>
</div>
<p>A charging pool for electric vehicles is an area equipped with one or more charging stations.</p>
<p>Use <code><a href="../Classes/PlaceCategory.html#/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ">PlaceCategory.businessAndServicesEvChargingStation</a></code> to find stations.
In the <code><a href="../Structs/Details.html">Details</a></code> of a <code><a href="../Classes/Place.html">Place</a></code> result you can find the list of found pools containing stations,
if any.</p>
<p>For offline EV rich attributes, also enable <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>
in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV16chargingStationsSayAA0B7StationVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingStations"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV16chargingStationsSayAA0B7StationVGvp">chargingStations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of charging stations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var chargingStations: [EVChargingStation]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV25eMobilityServiceProvidersSayAA09EMobilityE8ProviderVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eMobilityServiceProviders"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV25eMobilityServiceProvidersSayAA09EMobilityE8ProviderVGvp">eMobilityServiceProviders</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of e-Mobility Service Providers.
Only online search fills this field.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var eMobilityServiceProviders: [EMobilityServiceProvider]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV6accessAA12EVAccessTypeOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/access"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV6accessAA12EVAccessTypeOSgvp">access</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The accessibility level of the charging pool, or <code>nil</code> if unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var access: EVAccessType?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV24accessRestrictionReasonsSayAA08EVAccessE6ReasonOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/accessRestrictionReasons"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV24accessRestrictionReasonsSayAA08EVAccessE6ReasonOGvp">accessRestrictionReasons</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains the list of reasons for restriction.
Populated only for offline search and when access is <code><a href="../Enums/EVAccessType.html#/s:7heresdk12EVAccessTypeO16restrictedAccessyA2CmF">EVAccessType.restrictedAccess</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var accessRestrictionReasons: [EVAccessRestrictionReason]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV7detailsAA0bC7DetailsVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/details"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV7detailsAA0bC7DetailsVSgvp">details</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EV charging station attributes details. It is available only for a place that has charging station
for electric vehicles. Only offline search fills this field.</p>
<p><strong>Note:</strong> Not available as part of <code><a href="../Classes/Suggestion.html">Suggestion</a></code> results.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var details: EVChargingPoolDetails?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV2idSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV2idSSSgvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>HERE ID of the charging pool.
Only online search fills this field.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var id: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV5cpoIdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cpoId"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV5cpoIdSSSgvp">cpoId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>CPO (Charge Point Operator) id for charging pool.
Only online search fills this field.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var cpoId: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV8evseInfoSayAA4EvseVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evseInfo"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV8evseInfoSayAA4EvseVGvp">evseInfo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.
Only online search fills this field.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var evseInfo: [Evse]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVChargingPoolV16chargingStations25eMobilityServiceProviders6access0I18RestrictionReasons7details2id5cpoId8evseInfoACSayAA0B7StationVG_SayAA09EMobilityG8ProviderVGAA12EVAccessTypeOSgSayAA0uJ6ReasonOGAA0bC7DetailsVSgSSSgA_SayAA4EvseVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(chargingStations:eMobilityServiceProviders:access:accessRestrictionReasons:details:id:cpoId:evseInfo:)"></a>
<a class="token" href="#/s:7heresdk14EVChargingPoolV16chargingStations25eMobilityServiceProviders6access0I18RestrictionReasons7details2id5cpoId8evseInfoACSayAA0B7StationVG_SayAA09EMobilityG8ProviderVGAA12EVAccessTypeOSgSayAA0uJ6ReasonOGAA0bC7DetailsVSgSSSgA_SayAA4EvseVGtcfc">init(chargingStations:<wbr/>eMobilityServiceProviders:<wbr/>access:<wbr/>accessRestrictionReasons:<wbr/>details:<wbr/>id:<wbr/>cpoId:<wbr/>evseInfo:<wbr/>)</a>
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
<li>chargingStations: List of charging stations.</li>
<li>eMobilityServiceProviders: List of e-Mobility Service Providers.
Only online search fills this field.</li>
<li>access: The accessibility level of the charging pool, or <code>nil</code> if unknown.</li>
<li>accessRestrictionReasons: Contains the list of reasons for restriction.
Populated only for offline search and when access is <code><a href="../Enums/EVAccessType.html#/s:7heresdk12EVAccessTypeO16restrictedAccessyA2CmF">EVAccessType.restrictedAccess</a></code>.</li>
<li>details: EV charging station attributes details. It is available only for a place that has charging station
for electric vehicles. Only offline search fills this field.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <code><a href="../Classes/Suggestion.html">Suggestion</a></code> results.</p>
<ul>
<li>id: HERE ID of the charging pool.
Only online search fills this field.</li>
<li>cpoId: CPO (Charge Point Operator) id for charging pool.
Only online search fills this field.</li>
<li>evseInfo: Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.
Only online search fills this field.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(chargingStations: [EVChargingStation], eMobilityServiceProviders: [EMobilityServiceProvider], access: EVAccessType? = nil, accessRestrictionReasons: [EVAccessRestrictionReason], details: EVChargingPoolDetails? = nil, id: String? = nil, cpoId: String? = nil, evseInfo: [Evse] = [])</code></pre>
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
