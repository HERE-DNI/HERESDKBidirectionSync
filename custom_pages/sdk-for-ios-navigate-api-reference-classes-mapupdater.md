---
title: "sdk-for-ios-navigate-api-reference-classes-mapupdater"
slug: "sdk-for-ios-navigate-api-reference-classes-mapupdater"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapUpdater"></a>
<a title="MapUpdater Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maploader">MapLoader</a>
<img alt="" id="carat" src="/carat.png"/>
        MapUpdater Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapUpdater</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapUpdater</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapUpdater</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapUpdater</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A class for updating regions previously downloaded using the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code>.
First, updates for the regions are downloaded. Once the download is complete, the update process begins,
installing the new content.
It is recommended to regularly call <code><a href="../Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">MapUpdater.retrieveCatalogsUpdateInfo(...)</a></code> to check for available updates
for any downloaded regions.</p>
<p>If updates are available, regions can be updated asynchronously using <code><a href="../Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF">MapUpdater.updateCatalog(...)</a></code>.
The <code><a href="sdk-for-ios-navigate-api-reference-protocols-mapupdateprogresslistener">MapUpdateProgressListener</a></code> provides update progress for each region.</p>
<p>Incremental map updates are supported, by default: Instead of downloading an entire region,
only the parts that have changed will be installed. This results in a faster update process.
MapUpdater also aligns previously downloaded content with <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> changes made via <code><a href="sdk-for-ios-navigate-api-reference-structs-sdkoptions">SDKOptions</a></code>.</p>
<p>Note that patching (also called “incremental updates”) is only supported for up to 8 versions. For example, if an update started
with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9.
Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.</p>
<p>In case of an error, the previous map data remains available for use. It is only replaced
after new map data has been successfully downloaded. Regions that fail to update
must be retried in a new call. Paused updates can be resumed later.</p>
<p>During the update process, <code>MapUpdater</code> internally retries failed downloads
until a timeout occurs. If this happens, it is reported via <code><a href="sdk-for-ios-navigate-api-reference-protocols-mapupdateprogresslistener">MapUpdateProgressListener</a></code>.</p>
<p>If the user cancels the update process during the update phase, it is ignored.
The update phase begins after all content has been downloaded, then the HERE SDK installs
and replaces the existing regions. Cancellation is only possible during the download phase,
and a successful cancellation is indicated via <code>onComplete(...)</code>.</p>
<p>Note that a <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO8notReadyyA2CmF">MapLoaderError.notReady</a></code> occurs when the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> is used in parallel.
In general, background updates are not supported explicitly, as the OS can abort background processes.
In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is
in progress and it will be indicated by a <code><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC9taskCounts6UInt32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/taskCount"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC9taskCounts6UInt32Vvp">taskCount</a>
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
<a name="/s:7heresdk10MapUpdaterC16updateStatisticsAA06UpdateE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/updateStatistics"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC16updateStatisticsAA06UpdateE0Vvp">updateStatistics</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map update statistics for the current application session.
In the event of binary updates, patches are downloaded and applied. This
property helps to  determine the success or failure rate of applied patches.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">updateStatistics</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-updatestatistics">UpdateStatistics</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapUpdateVersionCommitPolicy"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO">MapUpdateVersionCommitPolicy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines if installed regions and subregions are updated one-by-one or if all regions are
updated only once the updates for all installed regions have been downloaded entirely.
This influences the required size of the storage during an update.
Regardless of the set policy, during an update, the previous region data is kept
until the new region data is committed successfully to the persisted storage.
This allows to revert to the previous version in case the update fails.
With <code><a href="../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onComplete</a></code>, more data has to be kept until
the update process finishes, while <code><a href="../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion</a></code>
allows to make faster use of the downloaded region and requires less disk space as only the
currently updated region is kept until the process completes.
However, with an <code><a href="../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion</a></code> policy the overall
process can be less reliable and bears a higher risk of errors.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapupdater-mapupdateversioncommitpolicy">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapUpdateVersionCommitPolicy</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromEngineAsync(_:_:)"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">fromEngineAsync(_:<wbr/>_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets a single instance of this class per provided <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromEngineAsync</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="n">_</span> <span class="nv">mapUpdaterConstructionCallback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk29MapUpdaterConstructionHandlera">MapUpdaterConstructionHandler</a></span><span class="p">)</span></code></pre>
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
<em>mapUpdaterConstructionCallback</em>
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
<a name="/s:7heresdk10MapUpdaterC010getCurrentB7VersionAA0bF6HandleCyKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getCurrentMapVersion()"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC010getCurrentB7VersionAA0bF6HandleCyKF">getCurrentMapVersion()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a handle that contains the map version of the already downloaded and installed regions.
This information is only needed for debugging purposes.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapLoader.html#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a></code> Specifies reason, why current map version is not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getCurrentMapVersion</span><span class="p">()</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapversionhandle">MapVersionHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>A handle to get the map version.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/updateCatalog(catalogInfo:completion:)"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF">updateCatalog(catalogInfo:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request for each catalog to update map data to the latest available version.
This applies to all previously installed <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code> map data and any incomplete downloads in a pending state.</p>
<p>If no regions are downloaded, this method updates only the map version.
The map cache and persisted regions are always bound to the same map version.</p>
<p>If no updates are available, <code><a href="../MapLoader.html#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a></code> from
<code><a href="../Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">MapUpdater.retrieveCatalogsUpdateInfo(...)</a></code> returns an empty list.
In this case, <code>onComplete(...)</code> is called immediately.</p>
<p>To check for available updates, use <code><a href="../Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">MapUpdater.retrieveCatalogsUpdateInfo(...)</a></code> to retrieve catalogs with newer versions.
Individual catalogs can then be updated using this method.
Ensure that the device has enough free disk space to perform a catalog update.
Information about the required disk space is available in <code><a href="../Structs/CatalogUpdateInfo.html#/s:7heresdk17CatalogUpdateInfoV15diskSizeInBytess5Int64Vvp">CatalogUpdateInfo.diskSizeInBytes</a></code>.</p>
<p>If there is not enough space to perform the catalog update with the default
<code><a href="../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onComplete</a></code>, try using <code><a href="../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion</a></code>.
This option requires less space but follows a different strategy for handling errors during the map update.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, the index is rebuilt after the map is updated.
The index helps <code><a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchengine">OfflineSearchEngine</a></code> provide better search results.</p>
<p>Note: Indexing is a beta feature and may have bugs or unexpected behavior.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">updateCatalog</span><span class="p">(</span><span class="nv">catalogInfo</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-catalogupdateinfo">CatalogUpdateInfo</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-catalogupdateprogresslistener">CatalogUpdateProgressListener</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-catalogupdatetask">CatalogUpdateTask</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>catalogInfo</em>
</code>
</td>
<td>
<div>
<p>catalog to update. CatalogUpdateInfo should be get from <code><a href="../Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">MapUpdater.retrieveCatalogsUpdateInfo(...)</a></code></p>
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
<p>A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/retrieveCatalogsUpdateInfo(callback:)"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">retrieveCatalogsUpdateInfo(callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves information of all catalogs that have newer version available. This method can also be used to query
catalog information like HRN, current installed version and newer available version on server.
An empty list in <code><a href="../MapLoader.html#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a></code> represent no map updates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">retrieveCatalogsUpdateInfo</span><span class="p">(</span><span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>callback</em>
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
<p>A handle to cancel a pending operation.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC22setVersionCommitPolicy07versionfG0yAC0b6UpdateefG0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setVersionCommitPolicy(versionCommitPolicy:)"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC22setVersionCommitPolicy07versionfG0yAC0b6UpdateefG0O_tF">setVersionCommitPolicy(versionCommitPolicy:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the map update version policy. Defaults to <code><a href="../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onComplete</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setVersionCommitPolicy</span><span class="p">(</span><span class="nv">versionCommitPolicy</span><span class="p">:</span> <span class="kt">MapUpdater</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapupdater-mapupdateversioncommitpolicy">MapUpdateVersionCommitPolicy</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>versionCommitPolicy</em>
</code>
</td>
<td>
<div>
<p>to choose from <code><a href="sdk-for-ios-navigate-api-reference-classes-mapupdater-mapupdateversioncommitpolicy">MapUpdater.MapUpdateVersionCommitPolicy</a></code></p>
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
