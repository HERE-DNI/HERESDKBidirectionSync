---
title: "MapUpdater (API Reference)"
slug: "sdk-for-android-navigate-mapupdater"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapUpdater.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.maploader.MapUpdater</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapUpdater</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A class for updating regions previously downloaded using the <a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a>.
 First, updates for the regions are downloaded. Once the download is complete, the update process begins,
 installing the new content.
 It is recommended to regularly call <a href="#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> to check for available updates
 for any downloaded regions.
 <p>If updates are available, regions can be updated asynchronously using <a href="#updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo,com.here.sdk.maploader.CatalogUpdateProgressListener)"><code>updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo, com.here.sdk.maploader.CatalogUpdateProgressListener)</code></a>.
 The <a href="sdk-for-android-navigate-mapupdateprogresslistener" title="interface in com.here.sdk.maploader"><code>MapUpdateProgressListener</code></a> provides update progress for each region.
 <p>Incremental map updates are supported, by default: Instead of downloading an entire region,
 only the parts that have changed will be installed. This results in a faster update process.
 MapUpdater also aligns previously downloaded content with <code>LayerConfiguration</code> changes made via <code>SDKOptions</code>.
 <p>Note that patching (also called "incremental updates") is only supported for up to 8 versions. For example, if an update started
 with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9.
 Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.
 <p>In case of an error, the previous map data remains available for use. It is only replaced
 after new map data has been successfully downloaded. Regions that fail to update
 must be retried in a new call. Paused updates can be resumed later.
 <p>During the update process, <a href="sdk-for-android-navigate-mapupdater" title="class in com.here.sdk.maploader"><code>MapUpdater</code></a> internally retries failed downloads
 until a timeout occurs. If this happens, it is reported via <a href="sdk-for-android-navigate-mapupdateprogresslistener" title="interface in com.here.sdk.maploader"><code>MapUpdateProgressListener</code></a>.
 <p>If the user cancels the update process during the update phase, it is ignored.
 The update phase begins after all content has been downloaded, then the HERE SDK installs
 and replaces the existing regions. Cancellation is only possible during the download phase,
 and a successful cancellation is indicated via <a href="sdk-for-android-navigate-mapupdateprogresslistener#onComplete(com.here.sdk.maploader.MapLoaderError)"><code>MapUpdateProgressListener.onComplete(com.here.sdk.maploader.MapLoaderError)</code></a>.
 <p>Note that a <a href="sdk-for-android-navigate-maploadererror#NOT_READY"><code>MapLoaderError.NOT_READY</code></a> occurs when the <a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a> is used in parallel.
 In general, background updates are not supported explicitly, as the OS can abort background processes.
 In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is
 in progress and it will be indicated by a <a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader"><code>MapLoaderError</code></a>.</p></p></p></p></p></p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines if installed regions and subregions are updated one-by-one or if all regions are
 updated only once the updates for all installed regions have been downloaded entirely.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)">fromEngineAsync</a><wbr/>(<a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-mapupdaterconstructioncallback" title="interface in com.here.sdk.maploader">MapUpdaterConstructionCallback</a> mapUpdaterConstructionCallback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets a single instance of this class per provided <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapversionhandle" title="class in com.here.sdk.maploader">MapVersionHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentMapVersion()">getCurrentMapVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a handle that contains the map version of the already downloaded and installed regions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTaskCount()">getTaskCount</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the number of concurrent tasks for downloading a map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-updatestatistics" title="class in com.here.sdk.maploader">UpdateStatistics</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUpdateStatistics()">getUpdateStatistics</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Map update statistics for the ongoing session of the current application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)">retrieveCatalogsUpdateInfo</a><wbr/>(<a href="sdk-for-android-navigate-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader">CatalogsUpdateInfoCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves information of all catalogs that have newer version available.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTaskCount(long)">setTaskCount</a><wbr/>(long value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the number of concurrent tasks for downloading a map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVersionCommitPolicy(com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy)">setVersionCommitPolicy</a><wbr/>(<a href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a> versionCommitPolicy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the map update version policy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-catalogupdatetask" title="class in com.here.sdk.maploader">CatalogUpdateTask</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo,com.here.sdk.maploader.CatalogUpdateProgressListener)">updateCatalog</a><wbr/>(<a href="sdk-for-android-navigate-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a> catalogInfo,
 <a href="sdk-for-android-navigate-catalogupdateprogresslistener" title="interface in com.here.sdk.maploader">CatalogUpdateProgressListener</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request for each catalog to update map data to the latest available version.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)">
<h3>fromEngineAsync</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">fromEngineAsync</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-mapupdaterconstructioncallback" title="interface in com.here.sdk.maploader">MapUpdaterConstructionCallback</a> mapUpdaterConstructionCallback)</span></div>
<div class="block"><p>Gets a single instance of this class per provided <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An instance of the SDKNativeEngine</p></dd>
<dd><code>mapUpdaterConstructionCallback</code> - <p>A callback that will receive the result of construction</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentMapVersion()">
<h3>getCurrentMapVersion</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapversionhandle" title="class in com.here.sdk.maploader">MapVersionHandle</a></span> <span class="element-name">getCurrentMapVersion</span>()
                                      throws <span class="exceptions"><a href="sdk-for-android-navigate-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span></div>
<div class="block"><p>Returns a handle that contains the map version of the already downloaded and installed regions.
 This information is only needed for debugging purposes.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A handle to get the map version.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></code> - <p>Specifies reason, why current map version is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo,com.here.sdk.maploader.CatalogUpdateProgressListener)">
<h3>updateCatalog</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-catalogupdatetask" title="class in com.here.sdk.maploader">CatalogUpdateTask</a></span> <span class="element-name">updateCatalog</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a> catalogInfo,
 @NonNull
 <a href="sdk-for-android-navigate-catalogupdateprogresslistener" title="interface in com.here.sdk.maploader">CatalogUpdateProgressListener</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request for each catalog to update map data to the latest available version.
 This applies to all previously installed <a href="sdk-for-android-navigate-region" title="class in com.here.sdk.maploader"><code>Region</code></a> map data and any incomplete downloads in a pending state.
 <p>If no regions are downloaded, this method updates only the map version.
 The map cache and persisted regions are always bound to the same map version.
 <p>If no updates are available, <a href="sdk-for-android-navigate-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader"><code>CatalogsUpdateInfoCallback</code></a> from
 <a href="#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> returns an empty list.
 In this case, <a href="sdk-for-android-navigate-mapupdateprogresslistener#onComplete(com.here.sdk.maploader.MapLoaderError)"><code>MapUpdateProgressListener.onComplete(com.here.sdk.maploader.MapLoaderError)</code></a> is called immediately.
 <p>To check for available updates, use <a href="#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> to retrieve catalogs with newer versions.
 Individual catalogs can then be updated using this method.
 Ensure that the device has enough free disk space to perform a catalog update.
 Information about the required disk space is available in <a href="sdk-for-android-navigate-catalogupdateinfo#diskSizeInBytes"><code>CatalogUpdateInfo.diskSizeInBytes</code></a>.
 <p>If there is not enough space to perform the catalog update with the default
 <a href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy#ON_COMPLETE"><code>MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE</code></a>, try using <a href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy#ON_FIRST_REGION"><code>MapUpdater.MapUpdateVersionCommitPolicy.ON_FIRST_REGION</code></a>.
 This option requires less space but follows a different strategy for handling errors during the map update.
 <p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, the index is rebuilt after the map is updated.
 The index helps <code>OfflineSearchEngine</code> provide better search results.
 <p>Note: Indexing is a beta feature and may have bugs or unexpected behavior.</p></p></p></p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>catalogInfo</code> - <p>catalog to update. CatalogUpdateInfo should be get from <a href="#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a></p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)">
<h3>retrieveCatalogsUpdateInfo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">retrieveCatalogsUpdateInfo</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader">CatalogsUpdateInfoCallback</a> callback)</span></div>
<div class="block"><p>Retrieves information of all catalogs that have newer version available. This method can also be used to query
 catalog information like HRN, current installed version and newer available version on server.
 An empty list in <a href="sdk-for-android-navigate-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader"><code>CatalogsUpdateInfoCallback</code></a> represent no map updates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>A handle to cancel a pending operation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVersionCommitPolicy(com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy)">
<h3>setVersionCommitPolicy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVersionCommitPolicy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a> versionCommitPolicy)</span></div>
<div class="block"><p>Sets the map update version policy. Defaults to <a href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy#ON_COMPLETE"><code>MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>versionCommitPolicy</code> - <p>to choose from <a href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader"><code>MapUpdater.MapUpdateVersionCommitPolicy</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTaskCount()">
<h3>getTaskCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getTaskCount</span>()</div>
<div class="block"><p>Gets the number of concurrent tasks for downloading a map.
 <p>A valid task count is between 1 to 64. When the value set is outside the valid range,
 then it is clamped to a valid range:
 <ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.</li>
</ul></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The number of concurrent tasks for downloading a map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTaskCount(long)">
<h3>setTaskCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTaskCount</span><wbr/><span class="parameters">(long value)</span></div>
<div class="block"><p>Sets the number of concurrent tasks for downloading a map.
 <p>A valid task count is between 1 to 64. When the value set is outside the valid range,
 then it is clamped to a valid range:
 <ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.</li>
</ul></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The number of concurrent tasks for downloading a map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUpdateStatistics()">
<h3>getUpdateStatistics</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-updatestatistics" title="class in com.here.sdk.maploader">UpdateStatistics</a></span> <span class="element-name">getUpdateStatistics</span>()</div>
<div class="block"><p>Map update statistics for the ongoing session of the current application.
 <p>In the event of binary updates, patches are downloaded and applied. This
 property helps to  determine the success or failure rate of applied patches.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Map update statistics for the current application session.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
