---
title: "CatalogUpdateInfo"
slug: "sdk-for-ios-navigate-structs-catalogupdateinfo"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CatalogUpdateInfo"></a>
<a title="CatalogUpdateInfo Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-maploader">MapLoader</a>

        CatalogUpdateInfo Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CatalogUpdateInfo</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CatalogUpdateInfo</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Holds information for the catalog update intent. Provides information regarding installed catalog
and its latest available version.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogUpdateInfoV09installedB0AA09InstalledB0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/installedCatalog"></a>
<a class="token" href="#/s:7heresdk17CatalogUpdateInfoV09installedB0AA09InstalledB0Vvp">installedCatalog</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Installed catalog.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">installedCatalog</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-installedcatalog">InstalledCatalog</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogUpdateInfoV13latestVersions5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/latestVersion"></a>
<a class="token" href="#/s:7heresdk17CatalogUpdateInfoV13latestVersions5Int64Vvp">latestVersion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Latest version available for a catalog.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">latestVersion</span><span class="p">:</span> <span class="kt">Int64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogUpdateInfoV5stateAA0bC5StateOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/state"></a>
<a class="token" href="#/s:7heresdk17CatalogUpdateInfoV5stateAA0bC5StateOvp">state</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>State of current catalog update.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">state</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-catalogupdatestate">CatalogUpdateState</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogUpdateInfoV18networkSizeInBytess5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/networkSizeInBytes"></a>
<a class="token" href="#/s:7heresdk17CatalogUpdateInfoV18networkSizeInBytess5Int64Vvp">networkSizeInBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Total size in bytes that needs to be downloaded over the network to update the installed catalog.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">networkSizeInBytes</span><span class="p">:</span> <span class="kt">Int64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogUpdateInfoV15diskSizeInBytess5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/diskSizeInBytes"></a>
<a class="token" href="#/s:7heresdk17CatalogUpdateInfoV15diskSizeInBytess5Int64Vvp">diskSizeInBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimates the size of the offline maps after an update.
<strong>Note</strong>
In order to estimate, if catalog update is feasible, given the amount of free space on the disk,
application can compare amount of the free space on the disk with <code>disk_size_in_bytes + temporary_disk_requirement_in_bytes</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">diskSizeInBytes</span><span class="p">:</span> <span class="kt">Int64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogUpdateInfoV31temporaryDiskRequirementInBytess5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/temporaryDiskRequirementInBytes"></a>
<a class="token" href="#/s:7heresdk17CatalogUpdateInfoV31temporaryDiskRequirementInBytess5Int64Vvp">temporaryDiskRequirementInBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performing an update requires additional storage on top of existing offline maps.
This space is used to store intermittent copy of map content according to
the specified <code><a href="sdk-for-ios-navigate-classes-mapupdater-mapupdateversioncommitpolicy">MapUpdater.MapUpdateVersionCommitPolicy</a></code>.
<strong>Note</strong>
In order to estimate, if catalog update is feasible, given the amount of free space on the disk,
application can compare amount of the free space on the disk with <code>disk_size_in_bytes + temporary_disk_requirement_in_bytes</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">temporaryDiskRequirementInBytes</span><span class="p">:</span> <span class="kt">Int64</span></code></pre>
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
