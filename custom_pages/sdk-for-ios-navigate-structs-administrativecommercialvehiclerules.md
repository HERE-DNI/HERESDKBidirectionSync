---
title: "AdministrativeCommercialVehicleRules"
slug: "sdk-for-ios-navigate-structs-administrativecommercialvehiclerules"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AdministrativeCommercialVehicleRules"></a>
<a title="AdministrativeCommercialVehicleRules Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-other%20structs">Other Structures</a>

        AdministrativeCommercialVehicleRules Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AdministrativeCommercialVehicleRules</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AdministrativeCommercialVehicleRules</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Commercial vehicle regulations for an administrative region (country or state).
Contains access restrictions, speed limits, and drive/rest rules applicable to
commercial vehicles on road segments within the region.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36AdministrativeCommercialVehicleRulesV2idAA14AdminContextIdVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk36AdministrativeCommercialVehicleRulesV2idAA14AdminContextIdVvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Administrative context identifier for this set of rules.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-admincontextid">AdminContextId</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36AdministrativeCommercialVehicleRulesV17accessRegulationsSayAA0D14SpecificAccessVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/accessRegulations"></a>
<a class="token" href="#/s:7heresdk36AdministrativeCommercialVehicleRulesV17accessRegulationsSayAA0D14SpecificAccessVGvp">accessRegulations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access restrictions for commercial vehicles (e.g. bridge/tunnel restrictions).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">accessRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-vehiclespecificaccess">VehicleSpecificAccess</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36AdministrativeCommercialVehicleRulesV21speedLimitRegulationsSayAA0d13SpecificSpeedG0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitRegulations"></a>
<a class="token" href="#/s:7heresdk36AdministrativeCommercialVehicleRulesV21speedLimitRegulationsSayAA0d13SpecificSpeedG0VGvp">speedLimitRegulations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle-specific speed limits for commercial vehicles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedLimitRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36AdministrativeCommercialVehicleRulesV19driveRestRegulationAA05DrivegH0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/driveRestRegulation"></a>
<a class="token" href="#/s:7heresdk36AdministrativeCommercialVehicleRulesV19driveRestRegulationAA05DrivegH0Vvp">driveRestRegulation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Drive and rest regulations for commercial drivers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">driveRestRegulation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-driverestregulation">DriveRestRegulation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36AdministrativeCommercialVehicleRulesV2id17accessRegulations010speedLimitH019driveRestRegulationAcA14AdminContextIdV_SayAA0D14SpecificAccessVGSayAA0dq5SpeedJ0VGAA05DrivelM0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:accessRegulations:speedLimitRegulations:driveRestRegulation:)"></a>
<a class="token" href="#/s:7heresdk36AdministrativeCommercialVehicleRulesV2id17accessRegulations010speedLimitH019driveRestRegulationAcA14AdminContextIdV_SayAA0D14SpecificAccessVGSayAA0dq5SpeedJ0VGAA05DrivelM0Vtcfc">init(id:<wbr/>accessRegulations:<wbr/>speedLimitRegulations:<wbr/>driveRestRegulation:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-admincontextid">AdminContextId</a></span><span class="p">,</span> <span class="nv">accessRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-vehiclespecificaccess">VehicleSpecificAccess</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">speedLimitRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">driveRestRegulation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-driverestregulation">DriveRestRegulation</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-driverestregulation">DriveRestRegulation</a></span><span class="p">())</span></code></pre>
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
