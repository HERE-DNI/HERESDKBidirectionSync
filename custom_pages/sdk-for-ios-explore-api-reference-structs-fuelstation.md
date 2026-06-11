---
title: "FuelStation"
slug: "sdk-for-ios-explore-api-reference-structs-fuelstation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FuelStation"></a>
<a title="FuelStation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        FuelStation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>FuelStation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FuelStation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains information about a specific fuel station.</p>
<p>Use <code><a href="../Classes/PlaceCategory.html#/s:7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ">PlaceCategory.businessAndServicesPetrolGasolineStation</a></code> to find fuel stations.
In the <code><a href="sdk-for-ios-explore-api-reference-structs-details">Details</a></code> of a <code><a href="sdk-for-ios-explore-api-reference-classes-place">Place</a></code> result you can find the associated fuel station information,
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fuels</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-genericfuel">GenericFuel</a></span><span class="p">]</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckFuels</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckfuel">TruckFuel</a></span><span class="p">]</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">payAtThePump</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">highVolumePumps</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">fuels</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-genericfuel">GenericFuel</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">truckFuels</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckfuel">TruckFuel</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">payAtThePump</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">highVolumePumps</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
