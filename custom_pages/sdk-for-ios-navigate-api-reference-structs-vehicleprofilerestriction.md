---
title: "sdk-for-ios-navigate-api-reference-structs-vehicleprofilerestriction"
slug: "sdk-for-ios-navigate-api-reference-structs-vehicleprofilerestriction"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleProfileRestriction"></a>
<a title="VehicleProfileRestriction Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-other%20structs">Other Structures</a>
<img alt="" id="carat" src="/carat.png"/>
        VehicleProfileRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleProfileRestriction</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleProfileRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Physical and cargo profile of a vehicle that triggers a regulation.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleProfileRestrictionV09requestedB4TypeAA0bF9ConditionOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requestedVehicleType"></a>
<a class="token" href="#/s:7heresdk25VehicleProfileRestrictionV09requestedB4TypeAA0bF9ConditionOSgvp">requestedVehicleType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle type to which this restriction applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requestedVehicleType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-vehicletypecondition">VehicleTypeCondition</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleProfileRestrictionV25requiredWeightInKilogramsAA12IntegerRangeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk25VehicleProfileRestrictionV25requiredWeightInKilogramsAA12IntegerRangeVvp">requiredWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Weight limits in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredWeightInKilograms</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleProfileRestrictionV30requiredGrossWeightInKilogramsAA12IntegerRangeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredGrossWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk25VehicleProfileRestrictionV30requiredGrossWeightInKilogramsAA12IntegerRangeVvp">requiredGrossWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gross weight limits in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredGrossWeightInKilograms</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleProfileRestrictionV24requiredAmountOfTrailersAA12IntegerRangeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredAmountOfTrailers"></a>
<a class="token" href="#/s:7heresdk25VehicleProfileRestrictionV24requiredAmountOfTrailersAA12IntegerRangeVvp">requiredAmountOfTrailers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Trailer count limits.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredAmountOfTrailers</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleProfileRestrictionV17hazardousMaterialAA09HazardousF4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazardousMaterial"></a>
<a class="token" href="#/s:7heresdk25VehicleProfileRestrictionV17hazardousMaterialAA09HazardousF4TypeOvp">hazardousMaterial</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Hazardous material condition associated with this profile.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazardousMaterial</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-hazardousmaterialtype">HazardousMaterialType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleProfileRestrictionV09requestedB4Type25requiredWeightInKilograms0g5GrosshiJ00G16AmountOfTrailers17hazardousMaterialAcA0bF9ConditionOSg_AA12IntegerRangeVA2mA09HazardouspF0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(requestedVehicleType:requiredWeightInKilograms:requiredGrossWeightInKilograms:requiredAmountOfTrailers:hazardousMaterial:)"></a>
<a class="token" href="#/s:7heresdk25VehicleProfileRestrictionV09requestedB4Type25requiredWeightInKilograms0g5GrosshiJ00G16AmountOfTrailers17hazardousMaterialAcA0bF9ConditionOSg_AA12IntegerRangeVA2mA09HazardouspF0Otcfc">init(requestedVehicleType:<wbr/>requiredWeightInKilograms:<wbr/>requiredGrossWeightInKilograms:<wbr/>requiredAmountOfTrailers:<wbr/>hazardousMaterial:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with specified parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">requestedVehicleType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-vehicletypecondition">VehicleTypeCondition</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">requiredWeightInKilograms</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">,</span> <span class="nv">requiredGrossWeightInKilograms</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">,</span> <span class="nv">requiredAmountOfTrailers</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">,</span> <span class="nv">hazardousMaterial</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-hazardousmaterialtype">HazardousMaterialType</a></span><span class="p">)</span></code></pre>
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
