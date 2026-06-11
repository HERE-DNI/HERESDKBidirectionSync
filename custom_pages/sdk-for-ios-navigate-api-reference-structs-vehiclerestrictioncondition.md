---
title: "VehicleRestrictionCondition"
slug: "sdk-for-ios-navigate-api-reference-structs-vehiclerestrictioncondition"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleRestrictionCondition"></a>
<a title="VehicleRestrictionCondition Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-other%20structs">Other Structures</a>

        VehicleRestrictionCondition Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleRestrictionCondition</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleRestrictionCondition</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Combined set of conditions that must all be satisfied for a regulation to apply.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27VehicleRestrictionConditionV19requiredRoadProfileAA0fgD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredRoadProfile"></a>
<a class="token" href="#/s:7heresdk27VehicleRestrictionConditionV19requiredRoadProfileAA0fgD0VSgvp">requiredRoadProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road profile conditions that activate this restriction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredRoadProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-roadprofilecondition">RoadProfileCondition</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27VehicleRestrictionConditionV015requiredWeatherD0AA0F4TypeOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredWeatherCondition"></a>
<a class="token" href="#/s:7heresdk27VehicleRestrictionConditionV015requiredWeatherD0AA0F4TypeOSgvp">requiredWeatherCondition</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Weather condition that must be present for this restriction to apply.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredWeatherCondition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-weathertype">WeatherType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27VehicleRestrictionConditionV13appliesDuringSayAA8TimeRuleCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/appliesDuring"></a>
<a class="token" href="#/s:7heresdk27VehicleRestrictionConditionV13appliesDuringSayAA8TimeRuleCGvp">appliesDuring</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time rules during which this restriction is active.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">appliesDuring</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-timerule">TimeRule</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27VehicleRestrictionConditionV08requiredB7ProfileSayAA0bfC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requiredVehicleProfile"></a>
<a class="token" href="#/s:7heresdk27VehicleRestrictionConditionV08requiredB7ProfileSayAA0bfC0VGvp">requiredVehicleProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle profile that is subject to this restriction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requiredVehicleProfile</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehicleprofilerestriction">VehicleProfileRestriction</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27VehicleRestrictionConditionV19requiredRoadProfile0e7WeatherD013appliesDuring0ebG0AcA0fgD0VSg_AA0H4TypeOSgSayAA8TimeRuleCGSayAA0bgC0VGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(requiredRoadProfile:requiredWeatherCondition:appliesDuring:requiredVehicleProfile:)"></a>
<a class="token" href="#/s:7heresdk27VehicleRestrictionConditionV19requiredRoadProfile0e7WeatherD013appliesDuring0ebG0AcA0fgD0VSg_AA0H4TypeOSgSayAA8TimeRuleCGSayAA0bgC0VGtcfc">init(requiredRoadProfile:<wbr/>requiredWeatherCondition:<wbr/>appliesDuring:<wbr/>requiredVehicleProfile:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with default values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">requiredRoadProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-roadprofilecondition">RoadProfileCondition</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">requiredWeatherCondition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-weathertype">WeatherType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">appliesDuring</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-timerule">TimeRule</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">requiredVehicleProfile</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehicleprofilerestriction">VehicleProfileRestriction</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
