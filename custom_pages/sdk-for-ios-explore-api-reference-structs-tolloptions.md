---
title: "Routing / TollOptions"
slug: "sdk-for-ios-explore-api-reference-structs-tolloptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollOptions"></a>
<a title="TollOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TollOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TollOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The option to specify how the tolls should be calculated.
<strong>Note</strong>
Not used for offline calculations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TollOptionsV12transpondersSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transponders"></a>
<a class="token" href="#/s:7heresdk11TollOptionsV12transpondersSaySSGvp">transponders</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the toll collection systems for which the user has valid transponders.
Note: currently, the only valid value is “all”. This means the user has a transponder that is accepted by all toll systems.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transponders</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TollOptionsV15vehicleCategoryAC07VehicleE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleCategory"></a>
<a class="token" href="#/s:7heresdk11TollOptionsV15vehicleCategoryAC07VehicleE0OSgvp">vehicleCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines special vehicle category for toll calculation. Usual types like car or truck
are determined from transport mode.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleCategory</span><span class="p">:</span> <span class="kt">TollOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-tolloptions-vehiclecategory">VehicleCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TollOptionsV12emissionTypeAC08EmissionE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/emissionType"></a>
<a class="token" href="#/s:7heresdk11TollOptionsV12emissionTypeAC08EmissionE0OSgvp">emissionType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the emission type as defined by the toll operator for toll calculation based on vehicle emissions class.
The emission type is based on the European emission standards (Euro 1 to Euro 6, and Euro EEV).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">emissionType</span><span class="p">:</span> <span class="kt">TollOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-tolloptions-emissiontype">EmissionType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TollOptionsV8co2Classs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/co2Class"></a>
<a class="token" href="#/s:7heresdk11TollOptionsV8co2Classs5Int32VSgvp">co2Class</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the CO2 class of the vehicle as defined by the toll operator.
CO2 class is used with <code><a href="../Structs/TollOptions.html#/s:7heresdk11TollOptionsV12emissionTypeAC08EmissionE0OSgvp">emissionType</a></code>.
Allowed values for CO2 class are 1, 2, 3, 4, or 5, where a lower value generally indicates lower CO2 emissions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">co2Class</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TollOptionsV12transponders15vehicleCategory12emissionType8co2ClassACSaySSG_AC07VehicleF0OSgAC08EmissionH0OSgs5Int32VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(transponders:vehicleCategory:emissionType:co2Class:)"></a>
<a class="token" href="#/s:7heresdk11TollOptionsV12transponders15vehicleCategory12emissionType8co2ClassACSaySSG_AC07VehicleF0OSgAC08EmissionH0OSgs5Int32VSgtcfc">init(transponders:<wbr/>vehicleCategory:<wbr/>emissionType:<wbr/>co2Class:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">transponders</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">vehicleCategory</span><span class="p">:</span> <span class="kt">TollOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-tolloptions-vehiclecategory">VehicleCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">emissionType</span><span class="p">:</span> <span class="kt">TollOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-tolloptions-emissiontype">EmissionType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">co2Class</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TollOptionsV15VehicleCategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VehicleCategory"></a>
<a class="token" href="#/s:7heresdk11TollOptionsV15VehicleCategoryO">VehicleCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Supported options of vehicle category for toll calculation.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-tolloptions-vehiclecategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VehicleCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TollOptionsV12EmissionTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EmissionType"></a>
<a class="token" href="#/s:7heresdk11TollOptionsV12EmissionTypeO">EmissionType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Supported options of emission type</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-tolloptions-emissiontype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EmissionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
