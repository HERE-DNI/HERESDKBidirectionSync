---
title: "VehicleRestrictionResult"
slug: "sdk-for-ios-navigate-api-reference-classes-pickmapcontentresult-vehiclerestrictionresult"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleRestrictionResult"></a>
<a title="VehicleRestrictionResult Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

<a href="sdk-for-ios-navigate-api-reference-classes-pickmapcontentresult">PickMapContentResult</a>

        VehicleRestrictionResult Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleRestrictionResult</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleRestrictionResult</span></code></pre>
</div>
</div>
<p>Carries the result of picking a vehicle restriction object.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the vehicle restriction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V11countryCodeAA07CountryI0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V11countryCodeAA07CountryI0OSgvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Country code.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-countrycode">CountryCode</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V07vehicleG0AA0fG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleRestriction"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V07vehicleG0AA0fG0Vvp">vehicleRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The vehicle restriction details.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclerestriction">VehicleRestriction</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V11coordinates11countryCode07vehicleG0AeA14GeoCoordinatesV_AA07CountryJ0OSgAA0fG0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coordinates:countryCode:vehicleRestriction:)"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V11coordinates11countryCode07vehicleG0AeA14GeoCoordinatesV_AA07CountryJ0OSgAA0fG0Vtcfc">init(coordinates:<wbr/>countryCode:<wbr/>vehicleRestriction:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-countrycode">CountryCode</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">vehicleRestriction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclerestriction">VehicleRestriction</a></span><span class="p">)</span></code></pre>
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
