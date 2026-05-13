---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-protocols-offlinesearchindexlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- OfflineSearchIndexListener.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/OfflineSearchIndexListener"></a>
<a title="OfflineSearchIndexListener Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        OfflineSearchIndexListener Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>OfflineSearchIndexListener</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">OfflineSearchIndexListener</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Protocol to get updates about progress
of creating persistent map index.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26OfflineSearchIndexListenerP9onStarted9operationyAA0bcD0C9OperationO_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onStarted(operation:)"></a>
<a class="token" href="#/s:7heresdk26OfflineSearchIndexListenerP9onStarted9operationyAA0bcD0C9OperationO_tF">onStarted(operation:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called each time that the indexing has started. It is triggered by changes to persistent map
or by calling <code>OfflineSearchEngine.setIndexOptions</code>.
If a valid index was previously created for the installed regions, no additional indexing
is performed, so no notifications are sent. In this context, a valid index is the one
that contains data for the exact versions of the installed map regions. When any of them
is updated or new regions are downloaded or deleted, the index becomes invalid and is
automatically rebuilt, as long as indexing has been enabled previously.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onStarted</span><span class="p">(</span><span class="nv">operation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-offlinesearchindex">OfflineSearchIndex</a></span><span class="o">.</span><span class="kt">Operation</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>operation</em>
</code>
</td>
<td>
<div>
<p>Shows whether the index is being created or removed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26OfflineSearchIndexListenerP10onProgress10percentageys5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onProgress(percentage:)"></a>
<a class="token" href="#/s:7heresdk26OfflineSearchIndexListenerP10onProgress10percentageys5Int32V_tF">onProgress(percentage:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called multiple times to indicate the progress of index creation or deletion.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onProgress</span><span class="p">(</span><span class="nv">percentage</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>percentage</em>
</code>
</td>
<td>
<div>
<p>Represents a percentage of work done.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26OfflineSearchIndexListenerP10onComplete5erroryAA0bcD0C5ErrorOSg_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onComplete(error:)"></a>
<a class="token" href="#/s:7heresdk26OfflineSearchIndexListenerP10onComplete5erroryAA0bcD0C5ErrorOSg_tF">onComplete(error:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called after index creation or deletion has been completed.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onComplete</span><span class="p">(</span><span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-offlinesearchindex">OfflineSearchIndex</a></span><span class="o">.</span><span class="kt">Error</span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>error</em>
</code>
</td>
<td>
<div>
<p>Represents an error in case of a failure.
It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
</tbody>
</table>
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

</div>
`
}</HTMLBlock>
