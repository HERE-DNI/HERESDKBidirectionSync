---
title: "MapUpdater (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdater"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapUpdater.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.maploader.MapUpdater</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapUpdater</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A class for updating regions previously downloaded using the <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a>.
 First, updates for the regions are downloaded. Once the download is complete, the update process begins,
 installing the new content.
 It is recommended to regularly call <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> to check for available updates
 for any downloaded regions.
 If updates are available, regions can be updated asynchronously using <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater#updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo,com.here.sdk.maploader.CatalogUpdateProgressListener)"><code>updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo, com.here.sdk.maploader.CatalogUpdateProgressListener)</code></a>.
 The <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdateprogresslistener" title="interface in com.here.sdk.maploader"><code>MapUpdateProgressListener</code></a> provides update progress for each region.
 Incremental map updates are supported, by default: Instead of downloading an entire region,
 only the parts that have changed will be installed. This results in a faster update process.
 MapUpdater also aligns previously downloaded content with <code>LayerConfiguration</code> changes made via <code>SDKOptions</code>.
 Note that patching (also called "incremental updates") is only supported for up to 8 versions. For example, if an update started
 with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9.
 Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.
 In case of an error, the previous map data remains available for use. It is only replaced
 after new map data has been successfully downloaded. Regions that fail to update
 must be retried in a new call. Paused updates can be resumed later.
 During the update process, <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater" title="class in com.here.sdk.maploader"><code>MapUpdater</code></a> internally retries failed downloads
 until a timeout occurs. If this happens, it is reported via <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdateprogresslistener" title="interface in com.here.sdk.maploader"><code>MapUpdateProgressListener</code></a>.
 If the user cancels the update process during the update phase, it is ignored.
 The update phase begins after all content has been downloaded, then the HERE SDK installs
 and replaces the existing regions. Cancellation is only possible during the download phase,
 and a successful cancellation is indicated via <a href="sdk-for-android-navigate-mapupdateprogresslistener#onComplete(com.here.sdk.maploader.MapLoaderError)"><code>MapUpdateProgressListener.onComplete(com.here.sdk.maploader.MapLoaderError)</code></a>.
 Note that a <a href="sdk-for-android-navigate-maploadererror#NOT_READY"><code>MapLoaderError.NOT_READY</code></a> occurs when the <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a> is used in parallel.
 In general, background updates are not supported explicitly, as the OS can abort background processes.
 In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is
 in progress and it will be indicated by a <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader"><code>MapLoaderError</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines if installed regions and subregions are updated one-by-one or if all regions are
 updated only once the updates for all installed regions have been downloaded entirely.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)">
<h3>fromEngineAsync</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">fromEngineAsync</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdaterconstructioncallback" title="interface in com.here.sdk.maploader">MapUpdaterConstructionCallback</a> mapUpdaterConstructionCallback)</span></div>
<div className="block"><p>Gets a single instance of this class per provided <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An instance of the SDKNativeEngine</p></dd>
<dd><code>mapUpdaterConstructionCallback</code> - <p>A callback that will receive the result of construction</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCurrentMapVersion()">
<h3>getCurrentMapVersion</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapversionhandle" title="class in com.here.sdk.maploader">MapVersionHandle</a></span> <span className="element-name">getCurrentMapVersion</span>()
                                      throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span></div>
<div className="block"><p>Returns a handle that contains the map version of the already downloaded and installed regions.
 This information is only needed for debugging purposes.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A handle to get the map version.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></code> - <p>Specifies reason, why current map version is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo,com.here.sdk.maploader.CatalogUpdateProgressListener)">
<h3>updateCatalog</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatetask" title="class in com.here.sdk.maploader">CatalogUpdateTask</a></span> <span className="element-name">updateCatalog</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a> catalogInfo,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateprogresslistener" title="interface in com.here.sdk.maploader">CatalogUpdateProgressListener</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous request for each catalog to update map data to the latest available version.
 This applies to all previously installed <a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader"><code>Region</code></a> map data and any incomplete downloads in a pending state.
 If no regions are downloaded, this method updates only the map version.
 The map cache and persisted regions are always bound to the same map version.
 If no updates are available, <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader"><code>CatalogsUpdateInfoCallback</code></a> from
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> returns an empty list.
 In this case, <a href="sdk-for-android-navigate-mapupdateprogresslistener#onComplete(com.here.sdk.maploader.MapLoaderError)"><code>MapUpdateProgressListener.onComplete(com.here.sdk.maploader.MapLoaderError)</code></a> is called immediately.
 To check for available updates, use <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> to retrieve catalogs with newer versions.
 Individual catalogs can then be updated using this method.
 Ensure that the device has enough free disk space to perform a catalog update.
 Information about the required disk space is available in <a href="sdk-for-android-navigate-catalogupdateinfo#diskSizeInBytes"><code>CatalogUpdateInfo.diskSizeInBytes</code></a>.
 If there is not enough space to perform the catalog update with the default
 <a href="sdk-for-android-navigate-mapupdater-mapupdateversioncommitpolicy#ON_COMPLETE"><code>MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE</code></a>, try using <a href="sdk-for-android-navigate-mapupdater-mapupdateversioncommitpolicy#ON_FIRST_REGION"><code>MapUpdater.MapUpdateVersionCommitPolicy.ON_FIRST_REGION</code></a>.
 This option requires less space but follows a different strategy for handling errors during the map update.
 If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, the index is rebuilt after the map is updated.
 The index helps <code>OfflineSearchEngine</code> provide better search results.
 Note: Indexing is a beta feature and may have bugs or unexpected behavior.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>catalogInfo</code> - <p>catalog to update. CatalogUpdateInfo should be get from <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a></p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)">
<h3>retrieveCatalogsUpdateInfo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">retrieveCatalogsUpdateInfo</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader">CatalogsUpdateInfoCallback</a> callback)</span></div>
<div className="block"><p>Retrieves information of all catalogs that have newer version available. This method can also be used to query
 catalog information like HRN, current installed version and newer available version on server.
 An empty list in <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader"><code>CatalogsUpdateInfoCallback</code></a> represent no map updates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>A handle to cancel a pending operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setVersionCommitPolicy(com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy)">
<h3>setVersionCommitPolicy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setVersionCommitPolicy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a> versionCommitPolicy)</span></div>
<div className="block"><p>Sets the map update version policy. Defaults to <a href="sdk-for-android-navigate-mapupdater-mapupdateversioncommitpolicy#ON_COMPLETE"><code>MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>versionCommitPolicy</code> - <p>to choose from <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader"><code>MapUpdater.MapUpdateVersionCommitPolicy</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTaskCount()">
<h3>getTaskCount</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">getTaskCount</span>()</div>
<div className="block"><p>Gets the number of concurrent tasks for downloading a map.
 A valid task count is between 1 to 64. When the value set is outside the valid range,
 then it is clamped to a valid range:
 <ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.</li>
</ul></p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The number of concurrent tasks for downloading a map.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTaskCount(long)">
<h3>setTaskCount</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTaskCount</span><wbr/><span className="parameters">(long value)</span></div>
<div className="block"><p>Sets the number of concurrent tasks for downloading a map.
 A valid task count is between 1 to 64. When the value set is outside the valid range,
 then it is clamped to a valid range:
 <ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.</li>
</ul></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The number of concurrent tasks for downloading a map.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getUpdateStatistics()">
<h3>getUpdateStatistics</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-updatestatistics" title="class in com.here.sdk.maploader">UpdateStatistics</a></span> <span className="element-name">getUpdateStatistics</span>()</div>
<div className="block"><p>Map update statistics for the ongoing session of the current application.
 In the event of binary updates, patches are downloaded and applied. This
 property helps to  determine the success or failure rate of applied patches.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
