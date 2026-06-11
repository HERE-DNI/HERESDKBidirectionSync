---
title: "sdk-for-ios-navigate-api-reference-structs-installedregion"
slug: "sdk-for-ios-navigate-api-reference-structs-installedregion"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/InstalledRegion"></a>
<a title="InstalledRegion Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maploader">MapLoader</a>
<img alt="" id="carat" src="/carat.png"/>
        InstalledRegion Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>InstalledRegion</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">InstalledRegion</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a region, from persistent map storage.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15InstalledRegionV8regionIdAA0cE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/regionId"></a>
<a class="token" href="#/s:7heresdk15InstalledRegionV8regionIdAA0cE0Vvp">regionId</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">regionId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-regionid">RegionId</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15InstalledRegionV8parentIdAA0cE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parentId"></a>
<a class="token" href="#/s:7heresdk15InstalledRegionV8parentIdAA0cE0Vvp">parentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parent region identifier. Continents have a parent_id of 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-regionid">RegionId</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15InstalledRegionV17sizeOnDiskInBytess5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sizeOnDiskInBytes"></a>
<a class="token" href="#/s:7heresdk15InstalledRegionV17sizeOnDiskInBytess5Int64Vvp">sizeOnDiskInBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Region size on disk in bytes.</p>
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
<a name="/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/status"></a>
<a class="token" href="#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">status</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Status of the region in the persistent map storage.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">status</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-installedregionstatus">InstalledRegionStatus</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15InstalledRegionV14lastUpdateTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastUpdateTime"></a>
<a class="token" href="#/s:7heresdk15InstalledRegionV14lastUpdateTime10Foundation4DateVSgvp">lastUpdateTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The last update time of the region in the persistent map storage.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lastUpdateTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15InstalledRegionV8regionId06parentE017sizeOnDiskInBytes6status14lastUpdateTimeAcA0cE0V_AJs5Int64VAA0bC6StatusO10Foundation4DateVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(regionId:parentId:sizeOnDiskInBytes:status:lastUpdateTime:)"></a>
<a class="token" href="#/s:7heresdk15InstalledRegionV8regionId06parentE017sizeOnDiskInBytes6status14lastUpdateTimeAcA0cE0V_AJs5Int64VAA0bC6StatusO10Foundation4DateVSgtcfc">init(regionId:<wbr/>parentId:<wbr/>sizeOnDiskInBytes:<wbr/>status:<wbr/>lastUpdateTime:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">regionId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-regionid">RegionId</a></span><span class="p">,</span> <span class="nv">parentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-regionid">RegionId</a></span><span class="p">,</span> <span class="nv">sizeOnDiskInBytes</span><span class="p">:</span> <span class="kt">Int64</span><span class="p">,</span> <span class="nv">status</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-installedregionstatus">InstalledRegionStatus</a></span><span class="p">,</span> <span class="nv">lastUpdateTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
