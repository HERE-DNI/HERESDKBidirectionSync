---
title: "sdk-for-ios-navigate-api-reference-classes-offlinesearchindex-error"
slug: "sdk-for-ios-navigate-api-reference-classes-offlinesearchindex-error"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Error"></a>
<a title="Error Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-search">Search</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchindex">OfflineSearchIndex</a>
<img alt="" id="carat" src="/carat.png"/>
        Error Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Error</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">Error</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Error corresponding to the offline search operation.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18OfflineSearchIndexC5ErrorO21invalidPersistentPathyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidPersistentPath"></a>
<a class="token" href="#/s:7heresdk18OfflineSearchIndexC5ErrorO21invalidPersistentPathyA2EmF">invalidPersistentPath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unreachable <code><a href="../../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code> or lacking required permission
to generate index inside.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidPersistentPath</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18OfflineSearchIndexC5ErrorO03mapE0yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapError"></a>
<a class="token" href="#/s:7heresdk18OfflineSearchIndexC5ErrorO03mapE0yA2EmF">mapError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Failed to get installed regions in protected cache.
Any previous available index would be deleted when this error occurs.
Use method <code>MapDownloader.getInitialPersistentMapStatus</code> to get the status of the
map and check <code>maploader.PersistentMapStatus</code> for exact healing procedure for specific status.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">mapError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18OfflineSearchIndexC5ErrorO08databaseE0yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/databaseError"></a>
<a class="token" href="#/s:7heresdk18OfflineSearchIndexC5ErrorO08databaseE0yA2EmF">databaseError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unable to generate index due to failed database operation.
Any previous available index would be deleted when this error occurs.
Call <code>MapDownloader.repairPersistentMap</code> to retry index generation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">databaseError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18OfflineSearchIndexC5ErrorO18operationCancelledyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationCancelled"></a>
<a class="token" href="#/s:7heresdk18OfflineSearchIndexC5ErrorO18operationCancelledyA2EmF">operationCancelled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indexing operation cancelled due to OS killing the application or when a new indexing operation is invoked by SDK
after finishing a map operation while the previous indexing operation was in progress.
Any previous available index would be deleted when this error occurs.
In later case, SDK would finish the latest indexing operation successfully and it can be tracked through
<code><a href="sdk-for-ios-navigate-api-reference-protocols-offlinesearchindexlistener">OfflineSearchIndexListener</a></code>, otherwise call <code>MapDownloader.repairPersistentMap</code> to retry index generation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">operationCancelled</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18OfflineSearchIndexC5ErrorO08internalE0yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/internalError"></a>
<a class="token" href="#/s:7heresdk18OfflineSearchIndexC5ErrorO08internalE0yA2EmF">internalError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Internal error occurred.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">internalError</span></code></pre>
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
