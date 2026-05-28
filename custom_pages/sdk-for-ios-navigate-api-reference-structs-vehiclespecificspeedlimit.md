---
title: "Other Structures / VehicleSpecificSpeedLimit"
slug: "sdk-for-ios-navigate-api-reference-structs-vehiclespecificspeedlimit"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleSpecificSpeedLimit"></a>
<a title="VehicleSpecificSpeedLimit Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-other%20structs">Other Structures</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VehicleSpecificSpeedLimit Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleSpecificSpeedLimit</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleSpecificSpeedLimit</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Speed limit regulation specific to a vehicle type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecondSdvp">speedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum permitted speed in meters per second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleSpecificSpeedLimitV10isAdvisorySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isAdvisory"></a>
<a class="token" href="#/s:7heresdk25VehicleSpecificSpeedLimitV10isAdvisorySbvp">isAdvisory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, this speed limit is advisory rather than legally enforced.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isAdvisory</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleSpecificSpeedLimitV022builtUpAreaMaxOverrideD17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/builtUpAreaMaxOverrideSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk25VehicleSpecificSpeedLimitV022builtUpAreaMaxOverrideD17InMetersPerSecondSdSgvp">builtUpAreaMaxOverrideSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max Override Speed indicates the maximum speed a commercial vehicle may travel within a BUA.
Could be 0 if unlimited.
A <code>nil</code> value means the speed limit is not affected by the BUA override or not present.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">builtUpAreaMaxOverrideSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleSpecificSpeedLimitV9conditionAA0B20RestrictionConditionVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/condition"></a>
<a class="token" href="#/s:7heresdk25VehicleSpecificSpeedLimitV9conditionAA0B20RestrictionConditionVvp">condition</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Conditions under which this speed limit is active.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">condition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecond10isAdvisory022builtUpAreaMaxOverridedghiJ09conditionACSd_SbSdSgAA0B20RestrictionConditionVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(speedLimitInMetersPerSecond:isAdvisory:builtUpAreaMaxOverrideSpeedInMetersPerSecond:condition:)"></a>
<a class="token" href="#/s:7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecond10isAdvisory022builtUpAreaMaxOverridedghiJ09conditionACSd_SbSdSgAA0B20RestrictionConditionVtcfc">init(speedLimitInMetersPerSecond:<wbr/>isAdvisory:<wbr/>builtUpAreaMaxOverrideSpeedInMetersPerSecond:<wbr/>condition:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">isAdvisory</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">builtUpAreaMaxOverrideSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">condition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a></span><span class="p">)</span></code></pre>
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
