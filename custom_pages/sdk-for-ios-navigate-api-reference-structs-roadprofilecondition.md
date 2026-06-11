---
title: "RoadProfileCondition"
slug: "sdk-for-ios-navigate-api-reference-structs-roadprofilecondition"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadProfileCondition"></a>
<a title="RoadProfileCondition Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-other%20structs">Other Structures</a>

        RoadProfileCondition Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadProfileCondition</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadProfileCondition</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Road profile conditions that must be met for a regulation to apply.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV8roadTypeAA017CommercialVehiclebF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadType"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV8roadTypeAA017CommercialVehiclebF0Ovp">roadType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Required road type for the regulation to apply.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-commercialvehicleroadtype">CommercialVehicleRoadType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV25requiredFunctionalClassesSayAA0fB5ClassOSgGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredFunctionalClasses"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV25requiredFunctionalClassesSayAA0fB5ClassOSgGvp">requiredFunctionalClasses</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Functional road classes on which the regulation applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredFunctionalClasses</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></span><span class="p">?]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV19requiredRouteLevelsSayAA0F4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredRouteLevels"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV19requiredRouteLevelsSayAA0F4TypeOGvp">requiredRouteLevels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route levels on which the regulation applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredRouteLevels</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-routetype">RouteType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV21requiredNumberOfLanesAA12IntegerRangeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredNumberOfLanes"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV21requiredNumberOfLanesAA12IntegerRangeVvp">requiredNumberOfLanes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Range of lane counts for which the regulation applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredNumberOfLanes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV18isControlledAccessSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isControlledAccess"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV18isControlledAccessSbSgvp">isControlledAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to controlled access roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isControlledAccess</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV015isLimitedAccessB0SbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isLimitedAccessRoad"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV015isLimitedAccessB0SbSgvp">isLimitedAccessRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to limited access roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isLimitedAccessRoad</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV21isMultiplyDigitilizedSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isMultiplyDigitilized"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV21isMultiplyDigitilizedSbSgvp">isMultiplyDigitilized</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to multiply digitized roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isMultiplyDigitilized</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV02isB14LegallyDividedSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRoadLegallyDivided"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV02isB14LegallyDividedSbSgvp">isRoadLegallyDivided</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to legally divided roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRoadLegallyDivided</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV02isB17PhysicallyDividedSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRoadPhysicallyDivided"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV02isB17PhysicallyDividedSbSgvp">isRoadPhysicallyDivided</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to physically divided roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRoadPhysicallyDivided</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV010isPriorityB0SbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPriorityRoad"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV010isPriorityB0SbSgvp">isPriorityRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to priority roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPriorityRoad</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV9isUnpavedSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isUnpaved"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV9isUnpavedSbSgvp">isUnpaved</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to unpaved roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isUnpaved</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV23isMotorisedVehiclesOnlySbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isMotorisedVehiclesOnly"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV23isMotorisedVehiclesOnlySbSgvp">isMotorisedVehiclesOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to motorised vehicles only roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isMotorisedVehiclesOnly</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV7isUrbanSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isUrban"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV7isUrbanSbSgvp">isUrban</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to urban roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isUrban</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV7isRuralSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRural"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV7isRuralSbSgvp">isRural</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, applies only to rural roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRural</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RoadProfileConditionV8roadType25requiredFunctionalClasses0G11RouteLevels0G13NumberOfLanes18isControlledAccess0o7LimitedqB00O19MultiplyDigitilized0oB14LegallyDivided0ob10PhysicallyV00o8PriorityB00O7Unpaved0O21MotorisedVehiclesOnly0O5Urban0O5RuralAcA017CommercialVehiclebF0O_SayAA0hB5ClassOSgGSayAA0jF0OGAA12IntegerRangeVSbSgA1_A1_A1_A1_A1_A1_A1_A1_A1_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(roadType:requiredFunctionalClasses:requiredRouteLevels:requiredNumberOfLanes:isControlledAccess:isLimitedAccessRoad:isMultiplyDigitilized:isRoadLegallyDivided:isRoadPhysicallyDivided:isPriorityRoad:isUnpaved:isMotorisedVehiclesOnly:isUrban:isRural:)"></a>
<a class="token" href="#/s:7heresdk20RoadProfileConditionV8roadType25requiredFunctionalClasses0G11RouteLevels0G13NumberOfLanes18isControlledAccess0o7LimitedqB00O19MultiplyDigitilized0oB14LegallyDivided0ob10PhysicallyV00o8PriorityB00O7Unpaved0O21MotorisedVehiclesOnly0O5Urban0O5RuralAcA017CommercialVehiclebF0O_SayAA0hB5ClassOSgGSayAA0jF0OGAA12IntegerRangeVSbSgA1_A1_A1_A1_A1_A1_A1_A1_A1_tcfc">init(roadType:<wbr/>requiredFunctionalClasses:<wbr/>requiredRouteLevels:<wbr/>requiredNumberOfLanes:<wbr/>isControlledAccess:<wbr/>isLimitedAccessRoad:<wbr/>isMultiplyDigitilized:<wbr/>isRoadLegallyDivided:<wbr/>isRoadPhysicallyDivided:<wbr/>isPriorityRoad:<wbr/>isUnpaved:<wbr/>isMotorisedVehiclesOnly:<wbr/>isUrban:<wbr/>isRural:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">roadType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-commercialvehicleroadtype">CommercialVehicleRoadType</a></span><span class="p">,</span> <span class="nv">requiredFunctionalClasses</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></span><span class="p">?]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">requiredRouteLevels</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-routetype">RouteType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">requiredNumberOfLanes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">,</span> <span class="nv">isControlledAccess</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isLimitedAccessRoad</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isMultiplyDigitilized</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isRoadLegallyDivided</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isRoadPhysicallyDivided</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isPriorityRoad</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isUnpaved</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isMotorisedVehiclesOnly</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isUrban</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isRural</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
