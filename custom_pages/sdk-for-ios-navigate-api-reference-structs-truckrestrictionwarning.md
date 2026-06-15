---
title: "TruckRestrictionWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-truckrestrictionwarning"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TruckRestrictionWarning"></a>
<a title="TruckRestrictionWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        TruckRestrictionWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TruckRestrictionWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckRestrictionWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck
or there can be a road ahead where the truck’s weight exceeds the permissible limit.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific truck restriction warning instance.
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
<a name="/s:7heresdk23TruckRestrictionWarningV16distanceInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceInMeters"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV16distanceInMetersSdvp">distanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance from the current location to the restriction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV06weightC0AA06WeightC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weightRestriction"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV06weightC0AA06WeightC0VSgvp">weightRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Weight restriction.
It is <code>nil</code> when there is no known weight restriction ahead.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">weightRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-weightrestriction">WeightRestriction</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV09dimensionC0AA09DimensionC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dimensionRestriction"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV09dimensionC0AA09DimensionC0VSgvp">dimensionRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle dimension restrictions.
It is <code>nil</code> when there is no known dimension restriction ahead.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dimensionRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-dimensionrestriction">DimensionRestriction</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <code><a href="../Structs/TruckRestrictionWarning.html#/s:7heresdk23TruckRestrictionWarningV16distanceInMetersSdvp">TruckRestrictionWarning.distanceInMeters</a></code> is greater than 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV12trailerCountAA12IntegerRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerCount"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV12trailerCountAA12IntegerRangeVSgvp">trailerCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The trailer count for which the current restriction applies.
If the field is ‘null’ then the current restriction does not have a condition based on trailers count.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV8timeRuleAA04TimeF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeRule"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV8timeRuleAA04TimeF0CSgvp">timeRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time rule indicating the time periods for which the restriction applies.
If the field is ‘null’ then the restriction is applicable at anytime.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-timerule">TimeRule</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV13truckRoadTypeAA0bfG0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRoadType"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV13truckRoadTypeAA0bfG0OSgvp">truckRoadType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck road type restriction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckRoadType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-truckroadtype">TruckRoadType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV18hazardousMaterialsSayAA17HazardousMaterialOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazardousMaterials"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV18hazardousMaterialsSayAA17HazardousMaterialOGvp">hazardousMaterials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of hazardous materials which are restricted on the road section for which the warning applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV14tunnelCategoryAA06TunnelF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tunnelCategory"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV14tunnelCategoryAA06TunnelF0OSgvp">tunnelCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tunnel category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV9axleCountAA12IntegerRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/axleCount"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV9axleCountAA12IntegerRangeVSgvp">axleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The axle count for which the current restriction applies.
If this field is <code>nil</code>, the restriction does not depend on axle count.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV2id16distanceInMeters06weightC009dimensionC00F4Type12trailerCount8timeRule09truckRoadK018hazardousMaterials14tunnelCategory04axleM0ACs5Int32V_SdAA06WeightC0VSgAA09DimensionC0VSgAA08DistanceK0OAA12IntegerRangeVSgAA04TimeO0CSgAA0bqK0OSgSayAA17HazardousMaterialOGAA06TunnelU0OSgA_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceInMeters:weightRestriction:dimensionRestriction:distanceType:trailerCount:timeRule:truckRoadType:hazardousMaterials:tunnelCategory:axleCount:)"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV2id16distanceInMeters06weightC009dimensionC00F4Type12trailerCount8timeRule09truckRoadK018hazardousMaterials14tunnelCategory04axleM0ACs5Int32V_SdAA06WeightC0VSgAA09DimensionC0VSgAA08DistanceK0OAA12IntegerRangeVSgAA04TimeO0CSgAA0bqK0OSgSayAA17HazardousMaterialOGAA06TunnelU0OSgA_tcfc">init(id:<wbr/>distanceInMeters:<wbr/>weightRestriction:<wbr/>dimensionRestriction:<wbr/>distanceType:<wbr/>trailerCount:<wbr/>timeRule:<wbr/>truckRoadType:<wbr/>hazardousMaterials:<wbr/>tunnelCategory:<wbr/>axleCount:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">weightRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-weightrestriction">WeightRestriction</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">dimensionRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-dimensionrestriction">DimensionRestriction</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span><span class="p">,</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-timerule">TimeRule</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">truckRoadType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-truckroadtype">TruckRoadType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV9isGeneralSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/isGeneral()"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV9isGeneralSbyF">isGeneral()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Checks if this truck restriction warning is general.
A general warning has no specific restriction conditions set.
Please note that time rule still might be set for a general warning, but it is not considered as a specific restriction condition.
This method only checks that no specific conditions are set for the warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">isGeneral</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>true</code> if all restriction fields are null or empty, <code>false</code> otherwise.</p>
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
} </HTMLBlock>
