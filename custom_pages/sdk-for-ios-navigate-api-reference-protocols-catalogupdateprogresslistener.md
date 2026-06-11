---
title: "sdk-for-ios-navigate-api-reference-protocols-catalogupdateprogresslistener"
slug: "sdk-for-ios-navigate-api-reference-protocols-catalogupdateprogresslistener"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/CatalogUpdateProgressListener"></a>
<a title="CatalogUpdateProgressListener Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maploader">MapLoader</a>
<img alt="" id="carat" src="/carat.png"/>
        CatalogUpdateProgressListener Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CatalogUpdateProgressListener</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">CatalogUpdateProgressListener</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Protocol to get notified on status updates
when updating catalog, previously downloaded by <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29CatalogUpdateProgressListenerP02onD06region10percentageyAA8RegionIdV_s5Int32VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onProgress(region:percentage:)"></a>
<a class="token" href="#/s:7heresdk29CatalogUpdateProgressListenerP02onD06region10percentageyAA8RegionIdV_s5Int32VtF">onProgress(region:<wbr/>percentage:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called multiple times to indicate the update progress.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onProgress</span><span class="p">(</span><span class="nv">region</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-regionid">RegionId</a></span><span class="p">,</span> <span class="nv">percentage</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>region</em>
</code>
</td>
<td>
<div>
<p>Represents an id of region status update is related to.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>percentage</em>
</code>
</td>
<td>
<div>
<p>Represents a percentage of catalog data which has been updated.</p>
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
<a name="/s:7heresdk29CatalogUpdateProgressListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onPause(error:)"></a>
<a class="token" href="#/s:7heresdk29CatalogUpdateProgressListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF">onPause(error:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when update is paused.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onPause</span><span class="p">(</span><span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></span><span class="p">?)</span></code></pre>
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
<p>Populated when a retryable error is the reason for a pause. A retryable error can happen,
when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection.
In general, the HERE SDK will try a few times, before the update is paused.
This error value gives a hint on the reason for the necessary retry operation.
A paused download can be resumed by the user at a later time.
It is ‘null’ when <code>CatalogUpdateTask.pause(Bool)</code> was called by the user.</p>
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
<a name="/s:7heresdk29CatalogUpdateProgressListenerP10onComplete5erroryAA14MapLoaderErrorOSg_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onComplete(error:)"></a>
<a class="token" href="#/s:7heresdk29CatalogUpdateProgressListenerP10onComplete5erroryAA14MapLoaderErrorOSg_tF">onComplete(error:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called after the update process for all regions has been completed.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onComplete</span><span class="p">(</span><span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></span><span class="p">?)</span></code></pre>
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
If an error occurs, the operation cannot be resumed later.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk29CatalogUpdateProgressListenerP8onResumeyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onResume()"></a>
<a class="token" href="#/s:7heresdk29CatalogUpdateProgressListenerP8onResumeyyF">onResume()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when a paused map update is resumed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onResume</span><span class="p">()</span></code></pre>
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
