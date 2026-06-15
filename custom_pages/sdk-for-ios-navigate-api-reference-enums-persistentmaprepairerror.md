---
title: "PersistentMapRepairError"
slug: "sdk-for-ios-navigate-api-reference-enums-persistentmaprepairerror"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PersistentMapRepairError"></a>
<a title="PersistentMapRepairError Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maploader">MapLoader</a>

        PersistentMapRepairError Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PersistentMapRepairError</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PersistentMapRepairError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Specifies possible errors that may result after a map repair operation has been completed.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PersistentMapRepairErrorO17partiallyRestoredyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/partiallyRestored"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO17partiallyRestoredyA2CmF">partiallyRestored</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Persistent map is repaired, but some map data is lost. Lost regions marked with a PENDING status.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">partiallyRestored</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PersistentMapRepairErrorO11invalidPathyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidPath"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO11invalidPathyA2CmF">invalidPath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Invalid persistent map path. The provided path to store the persistent map data doesn’t own the required Read/Write (RW) permissions.
Try to choose a different path with RW permissions.</p>
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
<a name="/s:7heresdk24PersistentMapRepairErrorO8brokenDbyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/brokenDb"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO8brokenDbyA2CmF">brokenDb</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The persisted map data can’t be recovered and all map data was fully deleted. It is recommended, to ask
the user if they want to try to download the lost regions again.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">brokenDb</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PersistentMapRepairErrorO16noOfflineVersionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noOfflineVersion"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO16noOfflineVersionyA2CmF">noOfflineVersion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map data version was not cached. The region list data will be cleared from the persisted storage.
It is recommended to download the list of downloadable regions again.
After this it is recommended to try to repair the corrupted map data again.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noOfflineVersion</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PersistentMapRepairErrorO9noJournalyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noJournal"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO9noJournalyA2CmF">noJournal</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>It is not possible to retrieve the list of downloaded regions. The region list data will be cleared from the persisted storage.
It is recommended to download the list of downloadable regions again.
After this it is recommended to try to repair the corrupted map data again.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noJournal</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PersistentMapRepairErrorO12brokenUpdateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/brokenUpdate"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO12brokenUpdateyA2CmF">brokenUpdate</a>
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
<a name="/s:7heresdk24PersistentMapRepairErrorO21operationAfterDisposeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationAfterDispose"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO21operationAfterDisposeyA2CmF">operationAfterDispose</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Repair is invoked on object connected to the disposed <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">operationAfterDispose</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PersistentMapRepairErrorO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An unknown error occurred. Try to clear the persisted storage by calling <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.
It is recommended, to ask the user if they want to try to download the lost regions again.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unknown</span></code></pre>
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
