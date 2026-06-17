---
title: "PlaceFilter"
slug: "sdk-for-ios-navigate-structs-placefilter"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PlaceFilter"></a>
<a title="PlaceFilter Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-search">Search</a>

        PlaceFilter Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PlaceFilter</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PlaceFilter</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The filter options to specify a place.
Consists of fuel, truck and EV options.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV9fuelTypesSayAA8FuelTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fuelTypes"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV9fuelTypesSayAA8FuelTypeOGvp">fuelTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-enums-fueltype">FuelType</a></code> elements that should be used to find only
the <code><a href="sdk-for-ios-navigate-structs-fuelstation">FuelStation</a></code> search results that support all of them.
This filter is available to use with the <code><a href="sdk-for-ios-navigate-classes-searchengine">SearchEngine</a></code> and
<code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> (only available for the Navigate license), however <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code>
supports it only for <code>searchByText</code> and <code>searchByCategory</code> with allowed fuel types <code>DIESEL</code>, <code>LPG</code>,
<code>BIO_DIESEL</code>, <code>CNG</code>, <code>DIESEL_WITH_ADDITIVES</code>, <code>E10</code>, <code>E85</code>, <code>ETHANOL</code>, <code>ETHANOL_WITH_ADDITIVES</code>,
<code>GASOLINE</code>, <code>HYDROGEN</code>, <code>LNG</code>, <code>MIDGRADE</code>, <code>PREMIUM</code> and <code>REGULAR</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fuelTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-fueltype">FuelType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV14truckFuelTypesSayAA05TruckE4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckFuelTypes"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV14truckFuelTypesSayAA05TruckE4TypeOGvp">truckFuelTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-enums-truckfueltype">TruckFuelType</a></code> elements that should be used to find only
the <code><a href="sdk-for-ios-navigate-structs-fuelstation">FuelStation</a></code> search results that support all of them.
Not supported for <code>suggestByText</code> in <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> (only available for the Navigate license).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckFuelTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-truckfueltype">TruckFuelType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV10truckClassAA05TruckE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckClass"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV10truckClassAA05TruckE0OSgvp">truckClass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Should be used to find only the <code><a href="sdk-for-ios-navigate-structs-fuelstation">FuelStation</a></code> search results with minimum supported <code><a href="sdk-for-ios-navigate-enums-truckclass">TruckClass</a></code>.
This filter is only available to use with the <code><a href="sdk-for-ios-navigate-classes-searchengine">SearchEngine</a></code>.
The <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> (only available for the Navigate license) does not apply this filter.
<code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05lightC0yA2CmF">TruckClass.lightClass</a></code> is not accepted in the filter.
Otherwise will result in <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO17invalidTruckClassyA2CmF">SearchError.invalidTruckClass</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckClass</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-truckclass">TruckClass</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2evAC2EvVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ev"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2evAC2EvVvp">ev</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constraints that are applicable on the places of category EV station.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ev</span><span class="p">:</span> <span class="kt">PlaceFilter</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-structs-placefilter-ev">Ev</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV9fuelTypes09truckFuelE00F5Class2evACSayAA0G4TypeOG_SayAA05TruckgJ0OGAA0kH0OSgAC2EvVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(fuelTypes:truckFuelTypes:truckClass:ev:)"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV9fuelTypes09truckFuelE00F5Class2evACSayAA0G4TypeOG_SayAA05TruckgJ0OGAA0kH0OSgAC2EvVtcfc">init(fuelTypes:<wbr/>truckFuelTypes:<wbr/>truckClass:<wbr/>ev:<wbr/>)</a>
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
<li>fuelTypes: The list of <code><a href="sdk-for-ios-navigate-enums-fueltype">FuelType</a></code> elements that should be used to find only
the <code><a href="sdk-for-ios-navigate-structs-fuelstation">FuelStation</a></code> search results that support all of them.
This filter is available to use with the <code><a href="sdk-for-ios-navigate-classes-searchengine">SearchEngine</a></code> and
<code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> (only available for the Navigate license), however <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code>
supports it only for <code>searchByText</code> and <code>searchByCategory</code> with allowed fuel types <code>DIESEL</code>, <code>LPG</code>,
<code>BIO_DIESEL</code>, <code>CNG</code>, <code>DIESEL_WITH_ADDITIVES</code>, <code>E10</code>, <code>E85</code>, <code>ETHANOL</code>, <code>ETHANOL_WITH_ADDITIVES</code>,
<code>GASOLINE</code>, <code>HYDROGEN</code>, <code>LNG</code>, <code>MIDGRADE</code>, <code>PREMIUM</code> and <code>REGULAR</code>.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>truckFuelTypes: The list of <code><a href="sdk-for-ios-navigate-enums-truckfueltype">TruckFuelType</a></code> elements that should be used to find only
the <code><a href="sdk-for-ios-navigate-structs-fuelstation">FuelStation</a></code> search results that support all of them.
Not supported for <code>suggestByText</code> in <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> (only available for the Navigate license).</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>truckClass: Should be used to find only the <code><a href="sdk-for-ios-navigate-structs-fuelstation">FuelStation</a></code> search results with minimum supported <code><a href="sdk-for-ios-navigate-enums-truckclass">TruckClass</a></code>.
This filter is only available to use with the <code><a href="sdk-for-ios-navigate-classes-searchengine">SearchEngine</a></code>.
The <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> (only available for the Navigate license) does not apply this filter.
<code><a href="../Enums/TruckClass.html#/s:7heresdk10TruckClassO05lightC0yA2CmF">TruckClass.lightClass</a></code> is not accepted in the filter.
Otherwise will result in <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO17invalidTruckClassyA2CmF">SearchError.invalidTruckClass</a></code>.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>ev: Constraints that are applicable on the places of category EV station.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">fuelTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-fueltype">FuelType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">truckFuelTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-truckfueltype">TruckFuelType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">truckClass</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-truckclass">TruckClass</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">ev</span><span class="p">:</span> <span class="kt">PlaceFilter</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-structs-placefilter-ev">Ev</a></span> <span class="o">=</span> <span class="kt">PlaceFilter</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-structs-placefilter-ev">Ev</a></span><span class="p">())</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2EvV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Ev"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2EvV">Ev</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constraints that are applicable on the places of category EV station.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-placefilter-ev">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Ev</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
