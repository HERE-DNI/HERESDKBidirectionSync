---
title: "Search / EVChargingTruckRestriction"
slug: "sdk-for-ios-navigate-api-reference-structs-evchargingtruckrestriction"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTruckRestriction"></a>
<a title="EVChargingTruckRestriction Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingTruckRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingTruckRestriction</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingTruckRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents access restrictions for trucks and light commercial vehicles.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26EVChargingTruckRestrictionV11truckAccessSayAA0C5ClassOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckAccess"></a>
<a class="token" href="#/s:7heresdk26EVChargingTruckRestrictionV11truckAccessSayAA0C5ClassOGvp">truckAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access categories for trucks and light commercial vehicles that the
EV charging location is designed to serve.</p>
<p>While the classifications used as basis for the categories are solely based on vehicle mass,
in EV charging context they can be interpreted to give an idea of the dimensional class too,
as well as possible other restrictions set by the operator. If there are true dimensional or
weight limits at the EV charging location, they are specified separately in vehicleLimitations.</p>
<p>The classification is available only to a subset of EV charging locations, depending on the
information available from the operators. Hence, at least vehicles belonging to the
<code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05lightC0yA2CmF">TruckClass.lightClass</a></code> category can be charged also in many EV charging locations not having
explicit signaling for the <code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05lightC0yA2CmF">TruckClass.lightClass</a></code> category.</p>
<p>Furthermore, although the classification is based on mass/weight ranges in growing order,
an upper class does not automatically mean that also all lower class vehicles are welcome to charge.
For example, a location marked only with category <code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05heavyC0yA2CmF">TruckClass.heavyClass</a></code>
is reserved for long-haul trucks only.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckAccess</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-truckclass">TruckClass</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26EVChargingTruckRestrictionV24hazardousGoodsRestrictedSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazardousGoodsRestricted"></a>
<a class="token" href="#/s:7heresdk26EVChargingTruckRestrictionV24hazardousGoodsRestrictedSbSgvp">hazardousGoodsRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indication if vehicles carrying hazardous / dangerous goods (ADR) can enter the EV Charging Location.</p>
<ul>
<li>True means the access is restricted. The client should assume the restriction covers all ADR classes.</li>
<li>False means there are no restrictions.</li>
<li>Absence means the information is not known.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazardousGoodsRestricted</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26EVChargingTruckRestrictionV11truckAccess24hazardousGoodsRestrictedACSayAA0C5ClassOG_SbSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(truckAccess:hazardousGoodsRestricted:)"></a>
<a class="token" href="#/s:7heresdk26EVChargingTruckRestrictionV11truckAccess24hazardousGoodsRestrictedACSayAA0C5ClassOG_SbSgtcfc">init(truckAccess:<wbr/>hazardousGoodsRestricted:<wbr/>)</a>
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
<li>truckAccess: Access categories for trucks and light commercial vehicles that the
EV charging location is designed to serve.</li>
</ul>
<p>While the classifications used as basis for the categories are solely based on vehicle mass,
  in EV charging context they can be interpreted to give an idea of the dimensional class too,
  as well as possible other restrictions set by the operator. If there are true dimensional or
  weight limits at the EV charging location, they are specified separately in vehicleLimitations.</p>
<p>The classification is available only to a subset of EV charging locations, depending on the
  information available from the operators. Hence, at least vehicles belonging to the
  <code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05lightC0yA2CmF">TruckClass.lightClass</a></code> category can be charged also in many EV charging locations not having
  explicit signaling for the <code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05lightC0yA2CmF">TruckClass.lightClass</a></code> category.</p>
<p>Furthermore, although the classification is based on mass/weight ranges in growing order,
  an upper class does not automatically mean that also all lower class vehicles are welcome to charge.
  For example, a location marked only with category <code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05heavyC0yA2CmF">TruckClass.heavyClass</a></code>
  is reserved for long-haul trucks only.</p>
<ul>
<li>hazardousGoodsRestricted: Indication if vehicles carrying hazardous / dangerous goods (ADR) can enter the EV Charging Location.

<ul>
<li>True means the access is restricted. The client should assume the restriction covers all ADR classes.</li>
<li>False means there are no restrictions.</li>
<li>Absence means the information is not known.</li>
</ul></li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">truckAccess</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-truckclass">TruckClass</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">hazardousGoodsRestricted</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
