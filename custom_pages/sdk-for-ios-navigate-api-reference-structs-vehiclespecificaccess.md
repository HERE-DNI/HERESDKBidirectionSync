---
title: "VehicleSpecificAccess"
slug: "sdk-for-ios-navigate-api-reference-structs-vehiclespecificaccess"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleSpecificAccess"></a>
<a title="VehicleSpecificAccess Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-other%20structs">Other Structures</a>

        VehicleSpecificAccess Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleSpecificAccess</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleSpecificAccess</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Access regulation for a specific vehicle type on a road segment.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VehicleSpecificAccessV13isPermitBasedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPermitBased"></a>
<a class="token" href="#/s:7heresdk21VehicleSpecificAccessV13isPermitBasedSbvp">isPermitBased</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, access is only permitted with a special permit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPermitBased</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VehicleSpecificAccessV17physicalStructureAA08PhysicalF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/physicalStructure"></a>
<a class="token" href="#/s:7heresdk21VehicleSpecificAccessV17physicalStructureAA08PhysicalF0Ovp">physicalStructure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Physical structure (e.g. bridge or tunnel) to which this access regulation applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">physicalStructure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-physicalstructure">PhysicalStructure</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VehicleSpecificAccessV20noTruckInnermostLanes5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/noTruckInnermostLane"></a>
<a class="token" href="#/s:7heresdk21VehicleSpecificAccessV20noTruckInnermostLanes5Int32VSgvp">noTruckInnermostLane</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If true, trucks are prohibited from using the innermost lane.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">noTruckInnermostLane</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VehicleSpecificAccessV9conditionAA0B20RestrictionConditionVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/condition"></a>
<a class="token" href="#/s:7heresdk21VehicleSpecificAccessV9conditionAA0B20RestrictionConditionVvp">condition</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Conditions under which this access regulation is active.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">condition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VehicleSpecificAccessV13isPermitBased17physicalStructure20noTruckInnermostLane9conditionACSb_AA08PhysicalI0Os5Int32VSgAA0B20RestrictionConditionVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(isPermitBased:physicalStructure:noTruckInnermostLane:condition:)"></a>
<a class="token" href="#/s:7heresdk21VehicleSpecificAccessV13isPermitBased17physicalStructure20noTruckInnermostLane9conditionACSb_AA08PhysicalI0Os5Int32VSgAA0B20RestrictionConditionVtcfc">init(isPermitBased:<wbr/>physicalStructure:<wbr/>noTruckInnermostLane:<wbr/>condition:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">isPermitBased</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">physicalStructure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-physicalstructure">PhysicalStructure</a></span><span class="p">,</span> <span class="nv">noTruckInnermostLane</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">condition</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a></span><span class="p">)</span></code></pre>
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
} </HTMLBlock>
