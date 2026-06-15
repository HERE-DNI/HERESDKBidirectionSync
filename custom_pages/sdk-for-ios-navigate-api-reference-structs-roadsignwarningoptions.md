---
title: "RoadSignWarningOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-roadsignwarningoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadSignWarningOptions"></a>
<a title="RoadSignWarningOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        RoadSignWarningOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadSignWarningOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadSignWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides road sign warning options. Set the options for filtering of road sign notifications.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RoadSignWarningOptionsV11typesFilterSayAA0bC4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/typesFilter"></a>
<a class="token" href="#/s:7heresdk22RoadSignWarningOptionsV11typesFilterSayAA0bC4TypeOGvp">typesFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of road sign types for which a warning will be given. If the list is empty, road
signs are not filtered by type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">typesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigntype">RoadSignType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RoadSignWarningOptionsV16categoriesFilterSayAA0bC8CategoryOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/categoriesFilter"></a>
<a class="token" href="#/s:7heresdk22RoadSignWarningOptionsV16categoriesFilterSayAA0bC8CategoryOGvp">categoriesFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of road sign categories for which a warning will be given. If the list is empty,
road signs are not filtered by category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">categoriesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigncategory">RoadSignCategory</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RoadSignWarningOptionsV07generalD11TypesFilterSayAA07GeneraldbC4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/generalWarningTypesFilter"></a>
<a class="token" href="#/s:7heresdk22RoadSignWarningOptionsV07generalD11TypesFilterSayAA07GeneraldbC4TypeOGvp">generalWarningTypesFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of road sign general warning types for which a warning will be given. If the list is
empty, road signs are not filtered by general warning type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">generalWarningTypesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RoadSignWarningOptionsV18vehicleTypesFilterSayAA0bC11VehicleTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleTypesFilter"></a>
<a class="token" href="#/s:7heresdk22RoadSignWarningOptionsV18vehicleTypesFilterSayAA0bC11VehicleTypeOGvp">vehicleTypesFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of road sign vehicle types for which a warning will be given. If the list is empty,
road signs are not filtered by vehicle type, which means that you get road sign warnings for all vehicle types.</p>
<p><strong>Example:</strong> For a filter that contains only bus and trucks you will only receive specific road sign warnings for
bus and trucks - you will not get signs for the other types, such as heavy trucks or motorhomes.
Furthermore, you will <em>not</em> get any signs that are generally applicable for all vehicles. For example,
you cannot set a filter that allows to get signs for trucks <em>and</em> cars. If you want to get signs for standard vehicles
like cars, then the only option is to set an empty list as filter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleTypesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsignvehicletype">RoadSignVehicleType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RoadSignWarningOptionsV11typesFilter010categoriesG007generald5TypesG007vehiclejG0ACSayAA0bC4TypeOG_SayAA0bC8CategoryOGSayAA07GeneraldbcL0OGSayAA0bc7VehicleL0OGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(typesFilter:categoriesFilter:generalWarningTypesFilter:vehicleTypesFilter:)"></a>
<a class="token" href="#/s:7heresdk22RoadSignWarningOptionsV11typesFilter010categoriesG007generald5TypesG007vehiclejG0ACSayAA0bC4TypeOG_SayAA0bC8CategoryOGSayAA07GeneraldbcL0OGSayAA0bc7VehicleL0OGtcfc">init(typesFilter:<wbr/>categoriesFilter:<wbr/>generalWarningTypesFilter:<wbr/>vehicleTypesFilter:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>typesFilter: The list of road sign types for which a warning will be given. If the list is empty, road
signs are not filtered by type.</li>
<li>categoriesFilter: The list of road sign categories for which a warning will be given. If the list is empty,
road signs are not filtered by category.</li>
<li>generalWarningTypesFilter: The list of road sign general warning types for which a warning will be given. If the list is
empty, road signs are not filtered by general warning type.</li>
<li>vehicleTypesFilter: The list of road sign vehicle types for which a warning will be given. If the list is empty,
road signs are not filtered by vehicle type, which means that you get road sign warnings for all vehicle types.</li>
</ul>
<p><strong>Example:</strong> For a filter that contains only bus and trucks you will only receive specific road sign warnings for
  bus and trucks - you will not get signs for the other types, such as heavy trucks or motorhomes.
  Furthermore, you will <em>not</em> get any signs that are generally applicable for all vehicles. For example,
  you cannot set a filter that allows to get signs for trucks <em>and</em> cars. If you want to get signs for standard vehicles
  like cars, then the only option is to set an empty list as filter.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">typesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigntype">RoadSignType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">categoriesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigncategory">RoadSignCategory</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">generalWarningTypesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">vehicleTypesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsignvehicletype">RoadSignVehicleType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
