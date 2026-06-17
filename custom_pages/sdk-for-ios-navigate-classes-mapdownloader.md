---
title: "MapDownloader"
slug: "sdk-for-ios-navigate-classes-mapdownloader"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapDownloader"></a>
<a title="MapDownloader Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-maploader">MapLoader</a>

        MapDownloader Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapDownloader</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapDownloader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapDownloader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapDownloader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A class for downloading and managing map data for various regions worldwide.
Downloaded map data is permanently stored on disk, enabling maps at all zoom levels,
search, routing, and other features without an active data connection.
Users can query available regions, download them to disk, or delete them.
An instance of this class can be created using <code><a href="../Classes/MapDownloader.html#/s:7heresdk13MapDownloaderC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">MapDownloader.fromEngineAsync(...)</a></code>.</p>
<p>The storage path for downloaded maps can be specified via <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>.</p>
<p>To control the type of content included in a map download, use <code><a href="sdk-for-ios-navigate-structs-layerconfiguration">LayerConfiguration</a></code>.
Once applied, it affects both the map cache and offline maps.
Satellite-based map schemes are not included in the downloaded region data.</p>
<p><strong>Note:</strong>
During turn-by-turn navigation,
while a map download or update is in progress, navigation may not function as expected,
and the app may be blocked until the operation is completed.
Ensure that all pending map operations are finished before starting navigation.
This applies only to <code>MapDownloader</code> and <code><a href="sdk-for-ios-navigate-classes-mapupdater">MapUpdater</a></code>. <code><a href="sdk-for-ios-navigate-classes-routeprefetcher">RoutePrefetcher</a></code> operations are not affected.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC9taskCounts6UInt32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/taskCount"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC9taskCounts6UInt32Vvp">taskCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The number of concurrent tasks for downloading a map.
A valid task count is between 1 to 64. When the value set is outside the valid range,
then it is clamped to a valid range:</p>
<ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">taskCount</span><span class="p">:</span> <span class="kt">UInt32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromEngineAsync(_:_:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">fromEngineAsync(_:<wbr/>_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets a single instance of this class per provided <code><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromEngineAsync</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="n">_</span> <span class="nv">mapDownloaderConstructionCallback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk31MapDownloaderConstructionHandlea">MapDownloaderConstructionHandle</a></span><span class="p">)</span></code></pre>
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
<p>An instance of the SDKNativeEngine</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>mapDownloaderConstructionCallback</em>
</code>
</td>
<td>
<div>
<p>A callback that will receive the result of construction</p>
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
<a name="/s:7heresdk13MapDownloaderC22getDownloadableRegions10completionAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA6RegionVGSgtc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDownloadableRegions(completion:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC22getDownloadableRegions10completionAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA6RegionVGSgtc_tF">getDownloadableRegions(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to fetch a list of <code><a href="sdk-for-ios-navigate-structs-region">Region</a></code> objects
for downloading map data in a separate request.</p>
<p>The default language for <code><a href="../Structs/Region.html#/s:7heresdk6RegionV4nameSSvp">Region.name</a></code> is <code><a href="../Enums/LanguageCode.html#/s:7heresdk12LanguageCodeO4enUsyA2CmF">LanguageCode.enUs</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">getDownloadableRegions</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk17CompletionHandlera">CompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC22getDownloadableRegions12languageCode10completionAA10TaskHandle_pAA08LanguageH0O_yAA0B11LoaderErrorOSg_SayAA6RegionVGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDownloadableRegions(languageCode:completion:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC22getDownloadableRegions12languageCode10completionAA10TaskHandle_pAA08LanguageH0O_yAA0B11LoaderErrorOSg_SayAA6RegionVGSgtctF">getDownloadableRegions(languageCode:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to fetch a list of <code><a href="sdk-for-ios-navigate-structs-region">Region</a></code> objects with <code><a href="../Structs/Region.html#/s:7heresdk6RegionV4nameSSvp">Region.name</a></code>
in given <code>MapDownloader.getDownloadableRegions(LanguageCode, CompletionHandler).languageCode</code>, that can be used to download the actual map data in a separate request.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">getDownloadableRegions</span><span class="p">(</span><span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk17CompletionHandlera">CompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>languageCode</em>
</code>
</td>
<td>
<div>
<p>The language code determines the language of <code><a href="../Structs/Region.html#/s:7heresdk6RegionV4nameSSvp">Region.name</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC15downloadRegions7regions14statusListenerAA0bC4TaskCSayAA8RegionIdVG_AA08Downloade6StatusH0_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/downloadRegions(regions:statusListener:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC15downloadRegions7regions14statusListenerAA0bC4TaskCSayAA8RegionIdVG_AA08Downloade6StatusH0_ptF">downloadRegions(regions:<wbr/>statusListener:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to download map data for regions specified
by a list of <code><a href="sdk-for-ios-navigate-structs-regionid">RegionId</a></code> instances.
<code>MapDownloader.downloadRegions(...).statusListener</code> receives notifications until
<code>onDownloadRegionsComplete(...)</code> is called.
The returned <code><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></code> can be used to pause or resume the download
using <code>MapDownloaderTask.pause(Bool)</code> or <code><a href="../Classes/MapDownloaderTask.html#/s:7heresdk17MapDownloaderTaskC6resumeyyF">MapDownloaderTask.resume(...)</a></code>.</p>
<p>To cancel the request, call <code><a href="../Classes/MapDownloaderTask.html#/s:7heresdk17MapDownloaderTaskC6cancelyyF">MapDownloaderTask.cancel(...)</a></code> on the returned
<code><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></code> object. After cancellation,
<code>onDownloadRegionsComplete(...)</code> is called
with the error <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO18operationCancelledyA2CmF">MapLoaderError.operationCancelled</a></code>.</p>
<p><code><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></code> remains operational until <code>onDownloadRegionsComplete(...)</code> is called.</p>
<p>To get list of downloadable regions use <code>MapDownloader.getDownloadableRegions(LanguageCode, CompletionHandler)</code> API.</p>
<p>Simultaneous downloads of the same region are not supported.
If this occurs, <code>onDownloadRegionsComplete(...)</code>
is called with <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF">MapLoaderError.serviceAccessFailed</a></code> for the new request,
while the previous one continues uninterrupted.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been downloaded, the corresponding index will be created.
The index is used by <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<p>To control list of map content features for region download, use <code><a href="../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>.</p>
<p><br/>
Note: If an application is forcefully closed or crashes during a map download operation, then this
method can be called again to resume the download. For example, if a download was interrupted at 60%,
then the next call to download the same region will load the remaining 40%.
<br/>
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
region three times before giving up. A connection will be timed out after one minute.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">downloadRegions</span><span class="p">(</span><span class="nv">regions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-regionid">RegionId</a></span><span class="p">],</span> <span class="nv">statusListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-downloadregionsstatuslistener">DownloadRegionsStatusListener</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC12downloadArea4area14statusListenerAA0bC4TaskCAA10GeoPolygonV_AA021DownloadRegionsStatusH0_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/downloadArea(area:statusListener:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC12downloadArea4area14statusListenerAA0bC4TaskCAA10GeoPolygonV_AA021DownloadRegionsStatusH0_ptF">downloadArea(area:<wbr/>statusListener:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to download map data for area specified by a GeoPolygon.
<code>MapDownloader.downloadArea(...).statusListener</code> is receiving notifications until <code>onDownloadRegionsComplete(...)</code> is called.
Returned <code><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></code> should be used to pause or resume started download, by invoking
<code>MapDownloaderTask.pause(Bool)</code> or <code><a href="../Classes/MapDownloaderTask.html#/s:7heresdk17MapDownloaderTaskC6resumeyyF">MapDownloaderTask.resume(...)</a></code>.
Request can be cancelled by calling <code><a href="../Classes/MapDownloaderTask.html#/s:7heresdk17MapDownloaderTaskC6cancelyyF">MapDownloaderTask.cancel(...)</a></code> on returned <code><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></code> object, afterwards
<code>onDownloadRegionsComplete(...)</code> is called with error <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO18operationCancelledyA2CmF">MapLoaderError.operationCancelled</a></code>.</p>
<p><code><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></code> remains operational until <code>onDownloadRegionsComplete(...)</code> is called.</p>
<p>Downloaded area will be associated to a unique id that will be reported via <code><a href="sdk-for-ios-navigate-protocols-downloadregionsstatuslistener">DownloadRegionsStatusListener</a></code>.</p>
<p>Simultaneous download of the same region twice is not supported. When such condition occurs then
<code>onDownloadRegionsComplete(...)</code> is called with error <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF">MapLoaderError.serviceAccessFailed</a></code>
for a new request, while previous one continues uninterrupted.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been downloaded, the corresponding index will be created.
The index is used by <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<p>To control list of map content features for area download, use <code><a href="../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>.</p>
<p><br/>
Note: If an application is forcefully closed or crashes during a map download operation, then this
method can be called again to resume the download. For example, if a download was interrupted at 60%,
then the next call to download the same region will load the remaining 40%.
<br/>
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
region three times before giving up. A connection will be timed out after one minute.
<br/>
Note: If user try to re-download same GeoPolygon the status will be reported as per the
state of previous download operation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">downloadArea</span><span class="p">(</span><span class="nv">area</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geopolygon">GeoPolygon</a></span><span class="p">,</span> <span class="nv">statusListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-downloadregionsstatuslistener">DownloadRegionsStatusListener</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-mapdownloadertask">MapDownloaderTask</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC13deleteRegions7regions10completionySayAA8RegionIdVG_yAA0B11LoaderErrorOSg_AISgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/deleteRegions(regions:completion:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC13deleteRegions7regions10completionySayAA8RegionIdVG_yAA0B11LoaderErrorOSg_AISgtctF">deleteRegions(regions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous operation to delete map data for regions specified by a list of <code><a href="sdk-for-ios-navigate-structs-regionid">RegionId</a></code>.
Note: Deleting a region when there is a pending download returns error
<code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO08internalD0yA2CmF">MapLoaderError.internalError</a></code>. Also, deleting a region when there is an ongoing download returns
error <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO15parallelRequestyA2CmF">MapLoaderError.parallelRequest</a></code>.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been deleted, the index over remaining regions will be rebuilt,
so that entries related to deleted regions are removed.
The index is used by <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">deleteRegions</span><span class="p">(</span><span class="nv">regions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-regionid">RegionId</a></span><span class="p">],</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk30DeleteRegionsCompletionHandlera">DeleteRegionsCompletionHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>regions</em>
</code>
</td>
<td>
<div>
<p>List of regions to be deleted.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result of deletion on the main thread.</p>
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
<a name="/s:7heresdk13MapDownloaderC015clearPersistentB7Storage10completionyyAA0B11LoaderErrorOSgc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/clearPersistentMapStorage(completion:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC015clearPersistentB7Storage10completionyyAA0B11LoaderErrorOSgc_tF">clearPersistentMapStorage(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous operation to clear the persistent map storage from all data. All downloaded regions will be removed.
Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.</p>
<p>Any previously built index will also be deleted.
See <code><a href="../Classes/MapDownloader.html#/s:7heresdk13MapDownloaderC15downloadRegions7regions14statusListenerAA0bC4TaskCSayAA8RegionIdVG_AA08Downloade6StatusH0_ptF">MapDownloader.downloadRegions(...)</a></code> to learn more about index.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">clearPersistentMapStorage</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk30CacheCallbackCompletionHandlera">CacheCallbackCompletionHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result of clearing on the main thread.</p>
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
<a name="/s:7heresdk13MapDownloaderC19getInstalledRegionsSayAA0E6RegionVGyKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getInstalledRegions()"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC19getInstalledRegionsSayAA0E6RegionVGyKF">getInstalledRegions()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Method to get a list of map regions that are currently installed on the device.
Throws if it’s not possible to return list of installed regions.
Returned list contains:</p>
<ul>
<li>successfully downloaded regions, indicated by <code><a href="../Enums/InstalledRegionStatus.html#/s:7heresdk21InstalledRegionStatusO9installedyA2CmF">InstalledRegionStatus.installed</a></code> in <code><a href="../Structs/InstalledRegion.html#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">InstalledRegion.status</a></code>;</li>
<li>regions, that are in the download process, indicated by <code><a href="../Enums/InstalledRegionStatus.html#/s:7heresdk21InstalledRegionStatusO7pendingyA2CmF">InstalledRegionStatus.pending</a></code> in <code><a href="../Structs/InstalledRegion.html#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">InstalledRegion.status</a></code>;</li>
<li>regions, which were failed to be downloaded, indicated by <code><a href="../Enums/InstalledRegionStatus.html#/s:7heresdk21InstalledRegionStatusO7pendingyA2CmF">InstalledRegionStatus.pending</a></code> in <code><a href="../Structs/InstalledRegion.html#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">InstalledRegion.status</a></code>.
Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is
set to the <code><a href="../Enums/InstalledRegionStatus.html#/s:7heresdk21InstalledRegionStatusO7pendingyA2CmF">InstalledRegionStatus.pending</a></code> in <code><a href="../Structs/InstalledRegion.html#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">InstalledRegion.status</a></code>. Precise Japan content is available as an additional offering, please contact sales team for more information.</li>
</ul><div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapLoader.html#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a></code> Specifies reason, why list of installed regions is not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getInstalledRegions</span><span class="p">()</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-installedregion">InstalledRegion</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>List of IDs of regions that are installed on the device</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC020getInitialPersistentB6StatusAA0fbG0OyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getInitialPersistentMapStatus()"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC020getInitialPersistentB6StatusAA0fbG0OyF">getInitialPersistentMapStatus()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the initial status of the already downloaded regions at start-up time of the app.
It is not recommended to download or to upload map data while an app is running in
background. However, it can happen, that an app gets shut down during an ongoing
operation, for example, due to a crash. In such a case, some or all of the downloaded map data
may be in a corrupted state.
Refer to the <code><a href="sdk-for-ios-navigate-enums-persistentmapstatus">PersistentMapStatus</a></code> for exact healing procedure for specific
status.
Note: This value will not change during the lifetime of an app.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getInitialPersistentMapStatus</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-persistentmapstatus">PersistentMapStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Initial status of the persistent map.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC016repairPersistentB010completionyyAA0eB11RepairErrorOSgc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/repairPersistentMap(completion:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC016repairPersistentB010completionyyAA0eB11RepairErrorOSgc_tF">repairPersistentMap(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tries to repair already downloaded regions that are in a corrupted state (see <code><a href="../Classes/MapDownloader.html#/s:7heresdk13MapDownloaderC020getInitialPersistentB6StatusAA0fbG0OyF">MapDownloader.getInitialPersistentMapStatus(...)</a></code>).</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then index will be
rebuilt if existing index does not match with the installed map regions after this operation.
The index is used by <code><a href="sdk-for-ios-navigate-classes-offlinesearchengine">OfflineSearchEngine</a></code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">repairPersistentMap</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk23RepairCompletionHandlera">RepairCompletionHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>A callback which receives the result of the repair operation on the main thread.</p>
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
<a name="/s:7heresdk13MapDownloaderC32getOfflineMapsStorageSizeInBytess6UInt64VyKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getOfflineMapsStorageSizeInBytes()"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC32getOfflineMapsStorageSizeInBytess6UInt64VyKF">getOfflineMapsStorageSizeInBytes()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Get the total size of all downloaded regions currently persisted on disk at the location that
is specified via <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>.
This includes also data that is currently being downloaded.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapLoader.html#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a></code> Specifies reason, why current map size is not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getOfflineMapsStorageSizeInBytes</span><span class="p">()</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">UInt64</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Value of offline map size.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC32getOfflineMapsStorageSizeInBytes10completionAA10TaskHandle_pyAA0B11LoaderErrorOSg_s6UInt64VSgtc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getOfflineMapsStorageSizeInBytes(completion:)"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC32getOfflineMapsStorageSizeInBytes10completionAA10TaskHandle_pyAA0B11LoaderErrorOSg_s6UInt64VSgtc_tF">getOfflineMapsStorageSizeInBytes(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Get the total size of all downloaded regions currently persisted on disk at the location that
is specified via <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>.
This includes also data that is currently being downloaded.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getOfflineMapsStorageSizeInBytes</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk25OfflineStorageSizeHandlera">OfflineStorageSizeHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>A callback which receives the value of offline map size or error on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
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
