---
title: "ElectronicHorizonDataLoader"
slug: "sdk-for-ios-navigate-api-reference-classes-electronichorizondataloader"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/ElectronicHorizonDataLoader"></a>
<a title="ElectronicHorizonDataLoader Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>

        ElectronicHorizonDataLoader Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonDataLoader</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ElectronicHorizonDataLoader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonDataLoader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonDataLoader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Loads map data for segments that belong to the <code><a href="sdk-for-ios-navigate-api-reference-classes-electronichorizonengine">ElectronicHorizonEngine</a></code> paths.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ElectronicHorizonDataLoaderC9sdkEngine7options07segmentD9CacheSizeAcA09SDKNativeG0C_AA07SegmentdE7OptionsVs5Int32VtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:options:segmentDataCacheSize:)"></a>
<a class="token" href="#/s:7heresdk27ElectronicHorizonDataLoaderC9sdkEngine7options07segmentD9CacheSizeAcA09SDKNativeG0C_AA07SegmentdE7OptionsVs5Int32VtKcfc">init(sdkEngine:<wbr/>options:<wbr/>segmentDataCacheSize:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of <code>ElectronicHorizonDataLoader</code>.
The constructor accepts options to configure the data loader. For more information, see <code><a href="sdk-for-ios-navigate-api-reference-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a></code>.
The cache size limits the number of segments that the loader can keep in memory at the same time.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> <code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> If the data loader cannot be created.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a></span><span class="p">,</span> <span class="nv">segmentDataCacheSize</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> instance that provides shared services, such as networking and map data.</p>
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
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a></code> instance that configures how segment data is requested.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>segmentDataCacheSize</em>
</code>
</td>
<td>
<div>
<p>The maximum number of segments that the loader can cache.</p>
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
<a name="/s:7heresdk27ElectronicHorizonDataLoaderC04loadD0010electronicC6UpdateyAA0bcH0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadData(electronicHorizonUpdate:)"></a>
<a class="token" href="#/s:7heresdk27ElectronicHorizonDataLoaderC04loadD0010electronicC6UpdateyAA0bcH0V_tF">loadData(electronicHorizonUpdate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadData</span><span class="p">(</span><span class="nv">electronicHorizonUpdate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonupdate">ElectronicHorizonUpdate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>electronicHorizonUpdate</em>
</code>
</td>
<td>
<div>
<p>The update that contains the segments to add to the cache and the segments to remove from the cache.</p>
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
<a name="/s:7heresdk27ElectronicHorizonDataLoaderC10getSegment9segmentIdAA0bcdE6ResultVAA018DirectedOCMSegmentI0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getSegment(segmentId:)"></a>
<a class="token" href="#/s:7heresdk27ElectronicHorizonDataLoaderC10getSegment9segmentIdAA0bcdE6ResultVAA018DirectedOCMSegmentI0V_tF">getSegment(segmentId:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns loaded data for the given segment identifier.
The result contains either the loaded data or an error code.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getSegment</span><span class="p">(</span><span class="nv">segmentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-directedocmsegmentid">DirectedOCMSegmentId</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizondataloaderresult">ElectronicHorizonDataLoaderResult</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>segmentId</em>
</code>
</td>
<td>
<div>
<p>The segment identifier for which to return the loaded data from the cache.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The result object that contains either the loaded segment data or an error code.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ElectronicHorizonDataLoaderC03addbcdE14StatusDelegateyyAA0bcdegH0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addElectronicHorizonDataLoaderStatusDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk27ElectronicHorizonDataLoaderC03addbcdE14StatusDelegateyyAA0bcdegH0_pF">addElectronicHorizonDataLoaderStatusDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds an <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a></code> to the subscription list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addElectronicHorizonDataLoaderStatusDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">electronicHorizonListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>electronicHorizonListener</em>
</code>
</td>
<td>
<div>
<p>The listener that receives data loader status updates.</p>
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
<a name="/s:7heresdk27ElectronicHorizonDataLoaderC06removebcdE14StatusDelegateyyAA0bcdegH0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeElectronicHorizonDataLoaderStatusDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk27ElectronicHorizonDataLoaderC06removebcdE14StatusDelegateyyAA0bcdegH0_pF">removeElectronicHorizonDataLoaderStatusDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes an <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a></code> from the subscription list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeElectronicHorizonDataLoaderStatusDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">electronicHorizonListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>electronicHorizonListener</em>
</code>
</td>
<td>
<div>
<p>The listener that should no longer receive data loader status updates.</p>
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

`
}</HTMLBlock>
