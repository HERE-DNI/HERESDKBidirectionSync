---
title: "FuelStation Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-fuelstation"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- FuelStation.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/FuelStation"></a>
<a title="FuelStation Structure Reference"></a>
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
<a href="../Search.html">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        FuelStation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct FuelStation : Hashable</code></pre>
</div>
</div>
<p>Contains information about a specific fuel station.</p>
<p>Use <code><a href="../Classes/PlaceCategory.html#/s:7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ">PlaceCategory.businessAndServicesPetrolGasolineStation</a></code> to find fuel stations.
In the <code><a href="../Structs/Details.html">Details</a></code> of a <code><a href="../Classes/Place.html">Place</a></code> result you can find the associated fuel station information,
if any.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11FuelStationV5fuelsSayAA07GenericB0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fuels"></a>
<a class="token" href="#/s:7heresdk11FuelStationV5fuelsSayAA07GenericB0VGvp">fuels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of car fuel types associated with the fuel station.
The list can be empty when no generic fuels are offered or when the information is unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var fuels: [GenericFuel]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11FuelStationV10truckFuelsSayAA05TruckB0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckFuels"></a>
<a class="token" href="#/s:7heresdk11FuelStationV10truckFuelsSayAA05TruckB0VGvp">truckFuels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of truck fuel types associated with the fuel station.
The list can be empty when no truck fuels are offered or when the information is unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var truckFuels: [TruckFuel]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11FuelStationV12payAtThePumpSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/payAtThePump"></a>
<a class="token" href="#/s:7heresdk11FuelStationV12payAtThePumpSbSgvp">payAtThePump</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if paying at the pump is supported or not. <code>nil</code> means information is unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var payAtThePump: Bool?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11FuelStationV15highVolumePumpsSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/highVolumePumps"></a>
<a class="token" href="#/s:7heresdk11FuelStationV15highVolumePumpsSbSgvp">highVolumePumps</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if high volume pumps are available or not. <code>nil</code> means information is unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var highVolumePumps: Bool?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11FuelStationV5fuels10truckFuels12payAtThePump15highVolumePumpsACSayAA07GenericB0VG_SayAA05TruckB0VGSbSgANtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(fuels:truckFuels:payAtThePump:highVolumePumps:)"></a>
<a class="token" href="#/s:7heresdk11FuelStationV5fuels10truckFuels12payAtThePump15highVolumePumpsACSayAA07GenericB0VG_SayAA05TruckB0VGSbSgANtcfc">init(fuels:<wbr/>truckFuels:<wbr/>payAtThePump:<wbr/>highVolumePumps:<wbr/>)</a>
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
<pre><code>public init(fuels: [GenericFuel] = [], truckFuels: [TruckFuel] = [], payAtThePump: Bool? = nil, highVolumePumps: Bool? = nil)</code></pre>
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
