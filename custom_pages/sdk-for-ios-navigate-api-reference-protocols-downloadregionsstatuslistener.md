---
title: "MapLoader / DownloadRegionsStatusListener"
slug: "sdk-for-ios-navigate-api-reference-protocols-downloadregionsstatuslistener"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DownloadRegionsStatusListener"></a>
<a title="DownloadRegionsStatusListener Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        DownloadRegionsStatusListener Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DownloadRegionsStatusListener</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DownloadRegionsStatusListener</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Protocol to get notified on
status updates when downloading map regions.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29DownloadRegionsStatusListenerP02onbC8Complete5error7regionsyAA14MapLoaderErrorOSg_SayAA8RegionIdVGSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onDownloadRegionsComplete(error:regions:)"></a>
<a class="token" href="#/s:7heresdk29DownloadRegionsStatusListenerP02onbC8Complete5error7regionsyAA14MapLoaderErrorOSg_SayAA8RegionIdVGSgtF">onDownloadRegionsComplete(error:<wbr/>regions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called after the download for all requested regions has been completed with success or
failure. In this callback, failure represents non-retryable error (eg. authentication failure
because of invalid credentials and similars). Temporary failures (eg. network errors) are
notified through <code><a href="../Protocols/DownloadRegionsStatusListener.html#/s:7heresdk29DownloadRegionsStatusListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF">onPause(...)</a></code> and downloads will be
in paused state so they can be resumed later.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onDownloadRegionsComplete</span><span class="p">(</span><span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-maploadererror">MapLoaderError</a></span><span class="p">?,</span> <span class="nv">regions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-regionid">RegionId</a></span><span class="p">]?)</span></code></pre>
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
<p>Represents an error in case of a failure. It is <code>nil</code> for an operation that
succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>regions</em>
</code>
</td>
<td>
<div>
<p>Represents a list of regions which has been downloaded. It is <code>nil</code> in case
of an error.</p>
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
<a name="/s:7heresdk29DownloadRegionsStatusListenerP10onProgress6region10percentageyAA8RegionIdV_s5Int32VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onProgress(region:percentage:)"></a>
<a class="token" href="#/s:7heresdk29DownloadRegionsStatusListenerP10onProgress6region10percentageyAA8RegionIdV_s5Int32VtF">onProgress(region:<wbr/>percentage:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called multiple times to indicate the download progress for each requested region
individually.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onProgress</span><span class="p">(</span><span class="nv">region</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-regionid">RegionId</a></span><span class="p">,</span> <span class="nv">percentage</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
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
<p>Represents a percentage of data which has been downloaded for particular
region.</p>
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
<a name="/s:7heresdk29DownloadRegionsStatusListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onPause(error:)"></a>
<a class="token" href="#/s:7heresdk29DownloadRegionsStatusListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF">onPause(error:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when download is paused.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onPause</span><span class="p">(</span><span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-maploadererror">MapLoaderError</a></span><span class="p">?)</span></code></pre>
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
<p>Populated when retryable error is a reason of a pause. It is ‘null’ when pause
is called by the user.</p>
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
<a name="/s:7heresdk29DownloadRegionsStatusListenerP8onResumeyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onResume()"></a>
<a class="token" href="#/s:7heresdk29DownloadRegionsStatusListenerP8onResumeyyF">onResume()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when paused download is resumed.</p>
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
