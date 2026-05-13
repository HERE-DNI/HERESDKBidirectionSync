---
title: "MapData / SegmentDataLoader"
slug: "sdk-for-ios-navigate-api-reference-classes-segmentdataloader"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentDataLoader"></a>
<a title="SegmentDataLoader Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SegmentDataLoader Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SegmentDataLoader</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentDataLoader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentDataLoader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentDataLoader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides the protocol for the access to the
segments data available in the local OCM map. Please be aware that the methods within this class
load map data synchronously. In the event of absent data in the disk cache, the data will be
retrieved from the remote server. To mitigate the potential freezing of the calling thread,
it is advisable to proactively prefetch map data around the working area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SegmentDataLoaderCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk17SegmentDataLoaderCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SegmentDataLoaderC9sdkEngineAcA09SDKNativeF0C_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:)"></a>
<a class="token" href="#/s:7heresdk17SegmentDataLoaderC9sdkEngineAcA09SDKNativeF0C_tKcfc">init(sdkEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>A SDKEngine instance.</p>
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
<a name="/s:7heresdk17SegmentDataLoaderC28getSegmentsAroundCoordinates_14radiusInMetersSayAA12OCMSegmentIdVGAA03GeoH0V_SdtKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getSegmentsAroundCoordinates(_:radiusInMeters:)"></a>
<a class="token" href="#/s:7heresdk17SegmentDataLoaderC28getSegmentsAroundCoordinates_14radiusInMetersSayAA12OCMSegmentIdVGAA03GeoH0V_SdtKF">getSegmentsAroundCoordinates(_:<wbr/>radiusInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Loads the segments around a certain coordinates.
Returns an empty list in case no segments could be found around the coordinates.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapData.html#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a></code> Specifies reason, why list of a list of segments is not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getSegmentsAroundCoordinates</span><span class="p">(</span><span class="n">_</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">radiusInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-ocmsegmentid">OCMSegmentId</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The location to explore</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>radiusInMeters</em>
</code>
</td>
<td>
<div>
<p>The radius of the search. Only values between 1m and 5000m are accepted.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The list of segments around the given position. The segments are sorted by distance
from the point.
Throws if it’s not possible to return list of a list of segments.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadData(segment:options:)"></a>
<a class="token" href="#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">loadData(segment:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Synchronously load the data for the given map segment.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapData.html#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a></code> Specifies reason, why list of data of a segment is not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadData</span><span class="p">(</span><span class="nv">segment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-ocmsegmentid">OCMSegmentId</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-segmentdata">SegmentData</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>segment</em>
</code>
</td>
<td>
<div>
<p>The segment to load.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Request options</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Requested data of a segment.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadDirectedSegmentData(segment:options:)"></a>
<a class="token" href="#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">loadDirectedSegmentData(segment:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Synchronously load the data for the given map directed segment.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapData.html#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a></code> Specifies reason, why list of data of a segment is not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadDirectedSegmentData</span><span class="p">(</span><span class="nv">segment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-directedocmsegmentid">DirectedOCMSegmentId</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-segmentdata">SegmentData</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>segment</em>
</code>
</td>
<td>
<div>
<p>The directed segment to load.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Request options</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Requested data of a segment.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SegmentDataLoaderC12downloadFile14fileReferences18downloadingOptionsSay10Foundation0C0VGSayAA0F9ReferenceVG_AA011DownloadingfJ0VtKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/downloadFile(fileReferences:downloadingOptions:)"></a>
<a class="token" href="#/s:7heresdk17SegmentDataLoaderC12downloadFile14fileReferences18downloadingOptionsSay10Foundation0C0VGSayAA0F9ReferenceVG_AA011DownloadingfJ0VtKF">downloadFile(fileReferences:<wbr/>downloadingOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Synchronously load the optional image providing guidance of a directed or non directed segment.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapData.html#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a></code> Specifies reason, why list of data of a segment is not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">downloadFile</span><span class="p">(</span><span class="nv">fileReferences</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-filereference">FileReference</a></span><span class="p">],</span> <span class="nv">downloadingOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-downloadingfileoptions">DownloadingFileOptions</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">Data</span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>fileReferences</em>
</code>
</td>
<td>
<div>
<p>Provides information for a file reference.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>downloadingOptions</em>
</code>
</td>
<td>
<div>
<p>Provides information regarding downloading configuration.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Requested data of a segment.</p>
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
