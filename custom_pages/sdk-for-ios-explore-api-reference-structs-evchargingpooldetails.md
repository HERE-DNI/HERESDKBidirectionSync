---
title: "Search / EVChargingPoolDetails"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingpooldetails"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingPoolDetails"></a>
<a title="EVChargingPoolDetails Structure Reference"></a>

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
<h1>EVChargingPoolDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingPoolDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evChargingOnSite</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evNetwork</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ownerInformation</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">reservable</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">totalNumberOfStations</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">evChargingOnSite</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">evNetwork</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">ownerInformation</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">reservable</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">totalNumberOfStations</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
