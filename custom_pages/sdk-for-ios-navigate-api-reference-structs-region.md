---
title: "MapLoader / Region"
slug: "sdk-for-ios-navigate-api-reference-structs-region"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Region"></a>
<a title="Region Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Region Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Region</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Region</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Defines an area, especially part of a country or the world that can be downloaded.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV8regionIdAA0bD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/regionId"></a>
<a class="token" href="#/s:7heresdk6RegionV8regionIdAA0bD0Vvp">regionId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier specifying a region.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">regionId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-regionid">RegionId</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV4nameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk6RegionV4nameSSvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of region. Language is determined by the requested <code><a href="sdk-for-ios-navigate-api-reference-..-enums-languagecode">LanguageCode</a></code>. By default,
it is in <code><a href="../Enums/LanguageCode.html#/s:7heresdk12LanguageCodeO4enUsyA2CmF">LanguageCode.enUs</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV17sizeOnDiskInBytess5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sizeOnDiskInBytes"></a>
<a class="token" href="#/s:7heresdk6RegionV17sizeOnDiskInBytess5Int64Vvp">sizeOnDiskInBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk.
This value is a theoretical maximum for the region’s size allocation.
Note: If overlapping regions exist or data is already present on the disk,
the actual size occupied might be less than this value due to shared or reused map data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sizeOnDiskInBytes</span><span class="p">:</span> <span class="kt">Int64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV20sizeOnNetworkInBytess5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sizeOnNetworkInBytes"></a>
<a class="token" href="#/s:7heresdk6RegionV20sizeOnNetworkInBytess5Int64Vvp">sizeOnNetworkInBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Region size, for downloading/during network operations, in bytes. Regions are downloaded in
compressed form and hence they have reduced size on network.
Note: This value represents the theoretical maximum size required for the
region during transfer. If overlapping data already exists, the actual size
downloaded may be smaller due to map data reuse.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sizeOnNetworkInBytes</span><span class="p">:</span> <span class="kt">Int64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV12childRegionsSayACGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/childRegions"></a>
<a class="token" href="#/s:7heresdk6RegionV12childRegionsSayACGSgvp">childRegions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All child regions for current region.
Note that each child can again contain multiple children.
A downloadable region will contain the content of all children.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">childRegions</span><span class="p">:</span> <span class="p">[</span><span class="kt">Region</span><span class="p">]?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV12navigabilityAA16NavigabilityTypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/navigability"></a>
<a class="token" href="#/s:7heresdk6RegionV12navigabilityAA16NavigabilityTypeOvp">navigability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the navigability type of this region.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">navigability</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-navigabilitytype">NavigabilityType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV8regionId4name17sizeOnDiskInBytes0fg7NetworkiJ012childRegions12navigabilityAcA0bD0V_SSs5Int64VAMSayACGSgAA16NavigabilityTypeOtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(regionId:name:sizeOnDiskInBytes:sizeOnNetworkInBytes:childRegions:navigability:)"></a>
<a class="token" href="#/s:7heresdk6RegionV8regionId4name17sizeOnDiskInBytes0fg7NetworkiJ012childRegions12navigabilityAcA0bD0V_SSs5Int64VAMSayACGSgAA16NavigabilityTypeOtcfc">init(regionId:<wbr/>name:<wbr/>sizeOnDiskInBytes:<wbr/>sizeOnNetworkInBytes:<wbr/>childRegions:<wbr/>navigability:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">regionId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-regionid">RegionId</a></span><span class="p">,</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">sizeOnDiskInBytes</span><span class="p">:</span> <span class="kt">Int64</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">sizeOnNetworkInBytes</span><span class="p">:</span> <span class="kt">Int64</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">childRegions</span><span class="p">:</span> <span class="p">[</span><span class="kt">Region</span><span class="p">]?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">navigability</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-navigabilitytype">NavigabilityType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-navigabilitytype">NavigabilityType</a></span><span class="o">.</span><span class="n">navigable</span><span class="p">)</span></code></pre>
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
