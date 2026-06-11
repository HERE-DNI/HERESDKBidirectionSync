---
title: "sdk-for-ios-navigate-api-reference-enums-persistentmapstatus"
slug: "sdk-for-ios-navigate-api-reference-enums-persistentmapstatus"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PersistentMapStatus"></a>
<a title="PersistentMapStatus Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maploader">MapLoader</a>
<img alt="" id="carat" src="/carat.png"/>
        PersistentMapStatus Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PersistentMapStatus</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PersistentMapStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Specifies possible statuses of the already downloaded map regions as a whole.
Note: This can be valid only for a single region in case of a <code><a href="../Enums/PersistentMapStatus.html#/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF">PersistentMapStatus.corrupted</a></code> state.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO2okyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ok"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO2okyA2CmF">ok</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All downloaded regions are in a workable state, no issues found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">ok</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/corrupted"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF">corrupted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>One or more downloaded regions failed to open and a repair action should be performed to mitigate this
issue. All map download and map update operations (except for
<code>sdk.maploader.MapDownloader.repair_persistent_map</code>) will return <code>sdk.maploader.MapLoaderError.NOT_READY</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">corrupted</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO12brokenUpdateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/brokenUpdate"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO12brokenUpdateyA2CmF">brokenUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unrecoverable error during construction of pending update parameters.
Operations such as catalog updates or region downloads will fail.
The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">brokenUpdate</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO15migrationNeededyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/migrationNeeded"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO15migrationNeededyA2CmF">migrationNeeded</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates that the downloaded regions need to be migrated to a new internal format by calling
<code>sdk.maploader.MapDownloader.repair_persistent_map</code>. This error is not a result of a data loss,
nor any data will be lost when performing the repair operation and the map version will stay
unchanged afterwards.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">migrationNeeded</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO13pendingUpdateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pendingUpdate"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO13pendingUpdateyA2CmF">pendingUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A map update operation initiated by a user has been interrupted.
Calls to <code>sdk.maploader.MapDownloader.download_regions</code> and
<code>sdk.maploader.MapDownloader.delete_regions</code> will fail with <code>sdk.maploader.MapLoaderError.INTERNAL_ERROR</code>.
To repair a map, call again <code>sdk.maploader.MapUpdater.update_catalog</code> for the affected catalog.
<code>sdk.maploader.MapUpdater.retrieve_catalogs_update_info</code> returns a list of <code>sdk.maploader.CatalogUpdateInfo</code> items:
The affected catalog can be identified by the state, which is set to <code>sdk.maploader.CatalogUpdateState.PENDING_UPDATE</code>.
To know if a map needs to be repaired, check if <code>sdk.maploader.MapLoaderError.PENDING_UPDATE</code> has occurred.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pendingUpdate</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO11invalidPathyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidPath"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO11invalidPathyA2CmF">invalidPath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unreachable <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV9cachePathSSvp">SDKOptions.cachePath</a></code> or <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>.
Make sure that <code><a href="sdk-for-ios-navigate-api-reference-structs-sdkoptions">SDKOptions</a></code> has accessible <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV9cachePathSSvp">SDKOptions.cachePath</a></code>
and <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidPath</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO12invalidStateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidState"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO12invalidStateyA2CmF">invalidState</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unrecoverable error during construction of internal map access object.
The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidState</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO13storageClosedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/storageClosed"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO13storageClosedyA2CmF">storageClosed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">storageClosed</span></code></pre>
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
