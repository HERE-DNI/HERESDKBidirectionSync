---
title: "sdk-for-ios-navigate-api-reference-structs-vehiclerestriction"
slug: "sdk-for-ios-navigate-api-reference-structs-vehiclerestriction"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleRestriction"></a>
<a title="VehicleRestriction Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-transport">Transport</a>
<img alt="" id="carat" src="/carat.png"/>
        VehicleRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleRestriction</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a vehicle restriction.</p>
<p>Any non <code>nil</code> property adds more details to the restriction.
A general truck restriction is represented with <code>nil</code> values for
properties <code>restriction</code> and
<code>hazmatRestriction</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV11restrictionAA08SpecificC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restriction"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV11restrictionAA08SpecificC0VSgvp">restriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A <code><a href="sdk-for-ios-navigate-api-reference-structs-specificrestriction">SpecificRestriction</a></code> defines what type of restriction applies (weight, height, etc.)
and the range of allowed values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">restriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-specificrestriction">SpecificRestriction</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV06hazmatC0AA017HazardousMaterialC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazmatRestriction"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV06hazmatC0AA017HazardousMaterialC0VSgvp">hazmatRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restriction on transport of hazardous materials and max allowed tunnel category.
For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks
carrying flammable materials are not allowed to enter tunnels category D and E -
(TunnelCategory.B and TunnelCategory.C allowed).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazmatRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-hazardousmaterialrestriction">HazardousMaterialRestriction</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV04timeC0AA04TimeC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeRestriction"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV04timeC0AA04TimeC0VSgvp">timeRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restriction applies during specific time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-timerestriction">TimeRestriction</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV17appliesToDeliverySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/appliesToDelivery"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV17appliesToDeliverySbvp">appliesToDelivery</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Flag indicating whether this restriction applies to delivery vehicles.</p>
<ul>
<li><code>false</code> means delivery is allowed into this restricted street.</li>
<li><code>true</code> means delivery is NOT allowed into this restricted street.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">appliesToDelivery</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV7weatherAA11WeatherTypeOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weather"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV7weatherAA11WeatherTypeOSgvp">weather</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of weather in which restriction applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">weather</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-weathertype">WeatherType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV13truckCategoryAA05TruckE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckCategory"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV13truckCategoryAA05TruckE0OSgvp">truckCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restriction applies to a specific truck category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-truckcategory">TruckCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV12trailerCountAA12IntegerRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerCount"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV12trailerCountAA12IntegerRangeVSgvp">trailerCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of trailers for which the restriction applies.</p>
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
<a name="/s:7heresdk18VehicleRestrictionV9axleCountAA12IntegerRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/axleCount"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV9axleCountAA12IntegerRangeVSgvp">axleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The axle count for which the current restriction applies.
Can be used in conjunction with <code><a href="../Enums/RestrictionType.html#/s:7heresdk15RestrictionTypeO18weightPerAxleCountyA2CmF">RestrictionType.weightPerAxleCount</a></code>
to specify restriction based on weight per number of axles.
The <code>axleCount</code> considers total number of axles on the whole vehicle (truck + trailers).
This can be used to limit the weight per axle for the whole truck.
If <code>axleCount</code> is null, the restriction is general and applies regardless of axle count.
If the upper limit of the <code>axleCount</code> range is 0 or <code>nil</code> then it means the restriction applies
for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
When a user taps the icon, the allowed <code>axleCount</code> range can be retrieved directly
from <code>VehicleRestriction.axleCount</code>.
Examples:</p>
<ul>
<li>(2,2) → Restriction applies to vehicles with exactly 2 axles.</li>
<li>(2,4) → Restriction applies to vehicles with 2, 3, or 4 axles.</li>
<li>(2, 0) → Restriction applies to vehicles with 2 or more axles (equivalent to 2…∞)</li>
</ul>
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
<a name="/s:7heresdk18VehicleRestrictionV16axleCountInGroupAA12IntegerRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/axleCountInGroup"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV16axleCountInGroupAA12IntegerRangeVSgvp">axleCountInGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of axles in a group for which the current restriction applies.
<code>axleCountInGroup</code> is a set of axles close together: single, tandem (2), triple (3), etc.
Can be used in conjunction with <code><a href="../Enums/RestrictionType.html#/s:7heresdk15RestrictionTypeO18weightPerAxleGroupyA2CmF">RestrictionType.weightPerAxleGroup</a></code>
to specify restriction based on weight per axle group.
The <code>axleCountInGroup</code> considers number of axles in a specific axle group (usually rear axles on the truck or trailer).
This can be used to limit weight for a tandem/triple rear axle group.
If the upper limit of the <code>axleCountInGroup</code> range is 0 or <code>nil</code> then it means the restriction applies
for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
Examples:</p>
<ul>
<li>(1,1) → Restriction applies to single axle group.</li>
<li>(2,2) → Restriction applies to tandem axle group.</li>
<li>(2,4) → Restriction applies to any axle group from 2 to 4 axles.</li>
<li>(2,0) → Restriction applies to axle groups with 2 or more axles.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">axleCountInGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV11restriction06hazmatC004timeC017appliesToDelivery7weather13truckCategory12trailerCount04axleN00oN7InGroupAcA08SpecificC0VSg_AA017HazardousMaterialC0VSgAA04TimeC0VSgSbAA11WeatherTypeOSgAA05TruckL0OSgAA12IntegerRangeVSgA2_A2_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(restriction:hazmatRestriction:timeRestriction:appliesToDelivery:weather:truckCategory:trailerCount:axleCount:axleCountInGroup:)"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV11restriction06hazmatC004timeC017appliesToDelivery7weather13truckCategory12trailerCount04axleN00oN7InGroupAcA08SpecificC0VSg_AA017HazardousMaterialC0VSgAA04TimeC0VSgSbAA11WeatherTypeOSgAA05TruckL0OSgAA12IntegerRangeVSgA2_A2_tcfc">init(restriction:<wbr/>hazmatRestriction:<wbr/>timeRestriction:<wbr/>appliesToDelivery:<wbr/>weather:<wbr/>truckCategory:<wbr/>trailerCount:<wbr/>axleCount:<wbr/>axleCountInGroup:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">restriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-specificrestriction">SpecificRestriction</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">hazmatRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-hazardousmaterialrestriction">HazardousMaterialRestriction</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">timeRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-timerestriction">TimeRestriction</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">appliesToDelivery</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">true</span><span class="p">,</span> <span class="nv">weather</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-weathertype">WeatherType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">truckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-truckcategory">TruckCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCountInGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
