---
title: "EVChargingPoolDetails Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingpooldetails"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingPoolDetails.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingPoolDetails"></a>
<a title="EVChargingPoolDetails Structure Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingPoolDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingPoolDetails : Hashable</code></pre>
</div>
</div>
<p>Electric vehicle charging pool details.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21EVChargingPoolDetailsV16evChargingOnSiteSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evChargingOnSite"></a>
<a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV16evChargingOnSiteSbSgvp">evChargingOnSite</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the Place offers EV charging to customer or the general public.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var evChargingOnSite: Bool?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21EVChargingPoolDetailsV9evNetworkSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evNetwork"></a>
<a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV9evNetworkSSSgvp">evNetwork</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The name of the EV Network that operates the charging station.
Note: not all stations participate in a network.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var evNetwork: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21EVChargingPoolDetailsV16ownerInformationSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ownerInformation"></a>
<a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV16ownerInformationSSSgvp">ownerInformation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the party of ownership provided by some suppliers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var ownerInformation: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21EVChargingPoolDetailsV10reservableSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/reservable"></a>
<a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV10reservableSbSgvp">reservable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the charging stations can be reserved.
Note: Reservable charging stations operate on a first-come/first served basis.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var reservable: Bool?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21EVChargingPoolDetailsV21totalNumberOfStationss6UInt32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/totalNumberOfStations"></a>
<a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV21totalNumberOfStationss6UInt32VSgvp">totalNumberOfStations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the total number of stations available on the charging pool.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var totalNumberOfStations: UInt32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21EVChargingPoolDetailsV16evChargingOnSite0E7Network16ownerInformation10reservable21totalNumberOfStationsACSbSg_SSSgAjIs6UInt32VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(evChargingOnSite:evNetwork:ownerInformation:reservable:totalNumberOfStations:)"></a>
<a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV16evChargingOnSite0E7Network16ownerInformation10reservable21totalNumberOfStationsACSbSg_SSSgAjIs6UInt32VSgtcfc">init(evChargingOnSite:<wbr/>evNetwork:<wbr/>ownerInformation:<wbr/>reservable:<wbr/>totalNumberOfStations:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.
For offline EV rich attributes, also enable <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>
in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(evChargingOnSite: Bool? = nil, evNetwork: String? = nil, ownerInformation: String? = nil, reservable: Bool? = nil, totalNumberOfStations: UInt32? = nil)</code></pre>
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
