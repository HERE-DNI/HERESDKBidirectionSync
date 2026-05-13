---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-bordercrossingwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- BorderCrossingWarning.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BorderCrossingWarning"></a>
<a title="BorderCrossingWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        BorderCrossingWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>BorderCrossingWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BorderCrossingWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A border crossing. The main field describing the border crossing is <code><a href="../Structs/BorderCrossingWarning.html#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">BorderCrossingWarning.type</a></code> specifying whether the border crossing
is given for a country border or a state border. The <code><a href="../Structs/BorderCrossingWarning.html#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">BorderCrossingWarning.type</a></code> must be known.
The country and state codes are contained in <code><a href="../Structs/BorderCrossingWarning.html#/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp">BorderCrossingWarning.administrativeRules</a></code> along with other information such as speed
limits, u-turn regulations or pre-trip planning information contained by the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativerules">AdministrativeRules</a></code>.</p>
<p>Use <code>BorderCrossingWarningListener</code> to get notifications about upcoming country or state border crossings.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific border crossing warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV010distanceTobC8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToBorderCrossingInMeters"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV010distanceTobC8InMetersSdvp">distanceToBorderCrossingInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance to the border crossing in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToBorderCrossingInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of border crossing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-bordercrossingtype">BorderCrossingType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/administrativeRules"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp">administrativeRules</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The administrative rules for the country or state after the border crossing. It contains information regarding
rules such as driving side, speed limits, various sticker requirements, toll costs and others.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">administrativeRules</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativerules">AdministrativeRules</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance type for the warning, e.g. a warning for a new border crossing ahead or a warning for
passing a border crossing. Since the border crossing warning is given relative to a single position on
the route, <code><a href="../Enums/DistanceType.html#/s:7heresdk12DistanceTypeO7reachedyA2CmF">DistanceType.reached</a></code> will never be given for this warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV28commercialVehicleRegulationsAA024AdministrativeCommercialF5RulesVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/commercialVehicleRegulations"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV28commercialVehicleRegulationsAA024AdministrativeCommercialF5RulesVSgvp">commercialVehicleRegulations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Commercial vehicle regulations for the administrative region after the border crossing.
Contains access restrictions, speed limits, and drive/rest rules applicable to commercial vehicles.
This field is only populated when crossing into a region with specific commercial vehicle regulations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">commercialVehicleRegulations</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativecommercialvehiclerules">AdministrativeCommercialVehicleRules</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV2id010distanceTobC8InMeters4type19administrativeRules0F4Type28commercialVehicleRegulationsACs5Int32V_SdAA0bcM0OAA014AdministrativeL0VAA08DistanceM0OAA0r10CommercialoL0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceToBorderCrossingInMeters:type:administrativeRules:distanceType:commercialVehicleRegulations:)"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV2id010distanceTobC8InMeters4type19administrativeRules0F4Type28commercialVehicleRegulationsACs5Int32V_SdAA0bcM0OAA014AdministrativeL0VAA08DistanceM0OAA0r10CommercialoL0VSgtcfc">init(id:<wbr/>distanceToBorderCrossingInMeters:<wbr/>type:<wbr/>administrativeRules:<wbr/>distanceType:<wbr/>commercialVehicleRegulations:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceToBorderCrossingInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-bordercrossingtype">BorderCrossingType</a></span><span class="p">,</span> <span class="nv">administrativeRules</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativerules">AdministrativeRules</a></span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-distancetype">DistanceType</a></span><span class="p">,</span> <span class="nv">commercialVehicleRegulations</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativecommercialvehiclerules">AdministrativeCommercialVehicleRules</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

</div>
`
}</HTMLBlock>
