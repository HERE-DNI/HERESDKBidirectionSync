---
title: "MapDownloader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapDownloader.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.maploader.MapDownloader</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapDownloader</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A class for downloading and managing map data for various regions worldwide.
 Downloaded map data is permanently stored on disk, enabling maps at all zoom levels,
 search, routing, and other features without an active data connection.
 Users can query available regions, download them to disk, or delete them.
 An instance of this class can be created using <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a>.
 The storage path for downloaded maps can be specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 To control the type of content included in a map download, use <code>LayerConfiguration</code>.
 Once applied, it affects both the map cache and offline maps.
 Satellite-based map schemes are not included in the downloaded region data.
 <strong>Note:</strong>
 During turn-by-turn navigation,
 while a map download or update is in progress, navigation may not function as expected,
 and the app may be blocked until the operation is completed.
 Ensure that all pending map operations are finished before starting navigation.
 This applies only to <code>MapDownloader</code> and <code>MapUpdater</code>. <code>RoutePrefetcher</code> operations are not affected.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<section className="detail" id="fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)">
<h3>fromEngineAsync</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">fromEngineAsync</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloaderconstructioncallback" title="interface in com.here.sdk.maploader">MapDownloaderConstructionCallback</a> mapDownloaderConstructionCallback)</span></div>
<div className="block"><p>Gets a single instance of this class per provided <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An instance of the SDKNativeEngine</p></dd>
<dd><code>mapDownloaderConstructionCallback</code> - <p>A callback that will receive the result of construction</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDownloadableRegions(com.here.sdk.maploader.DownloadableRegionsCallback)">
<h3>getDownloadableRegions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">getDownloadableRegions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous request to fetch a list of <a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader"><code>Region</code></a> objects
 for downloading map data in a separate request.
 The default language for <a href="sdk-for-android-navigate-region#name"><code>Region.name</code></a> is <a href="sdk-for-android-navigate-languagecode#EN_US"><code>LanguageCode.EN_US</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)">
<h3>getDownloadableRegions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">getDownloadableRegions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous request to fetch a list of <a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader"><code>Region</code></a> objects with <a href="sdk-for-android-navigate-region#name"><code>Region.name</code></a>
 in given <code>languageCode</code>, that can be used to download the actual map data in a separate request.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>languageCode</code> - <p>The language code determines the language of <a href="sdk-for-android-navigate-region#name"><code>Region.name</code></a>.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="downloadRegions(java.util.List,com.here.sdk.maploader.DownloadRegionsStatusListener)">
<h3>downloadRegions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></span> <span className="element-name">downloadRegions</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a>&gt; regions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</span></div>
<div className="block"><p>Performs an asynchronous request to download map data for regions specified
 by a list of <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader"><code>RegionId</code></a> instances.
 <code>statusListener</code> receives notifications until
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a> is called.
 The returned <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> can be used to pause or resume the download
 using <code>MapDownloaderTask.pause(boolean)</code> or <a href="sdk-for-android-navigate-mapdownloadertask#resume()"><code>MapDownloaderTask.resume()</code></a>.
 To cancel the request, call <a href="sdk-for-android-navigate-mapdownloadertask#cancel()"><code>MapDownloaderTask.cancel()</code></a> on the returned
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> object. After cancellation,
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a> is called
 with the error <a href="sdk-for-android-navigate-maploadererror#OPERATION_CANCELLED"><code>MapLoaderError.OPERATION_CANCELLED</code></a>.
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> remains operational until <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a> is called.
 To get list of downloadable regions use <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)"><code>getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)</code></a> API.
 Simultaneous downloads of the same region are not supported.
 If this occurs, <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a>
 is called with <a href="sdk-for-android-navigate-maploadererror#SERVICE_ACCESS_FAILED"><code>MapLoaderError.SERVICE_ACCESS_FAILED</code></a> for the new request,
 while the previous one continues uninterrupted.
 If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
 the requested regions have been downloaded, the corresponding index will be created.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.
 To control list of map content features for region download, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.
 <br/>
 Note: If an application is forcefully closed or crashes during a map download operation, then this
 method can be called again to resume the download. For example, if a download was interrupted at 60%,
 then the next call to download the same region will load the remaining 40%.
 <br/>
 Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
 region three times before giving up. A connection will be timed out after one minute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>regions</code> - <p>List of regions to download. Can be fetched using <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)"><code>getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)</code></a> API.</p></dd>
<dd><code>statusListener</code> - <p>Notifies on the download progress.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="downloadArea(com.here.sdk.core.GeoPolygon,com.here.sdk.maploader.DownloadRegionsStatusListener)">
<h3>downloadArea</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></span> <span className="element-name">downloadArea</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> area,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</span></div>
<div className="block"><p>Performs an asynchronous request to download map data for area specified by a GeoPolygon.
 <code>statusListener</code> is receiving notifications until <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a> is called.
 Returned <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> should be used to pause or resume started download, by invoking
 <code>MapDownloaderTask.pause(boolean)</code> or <a href="sdk-for-android-navigate-mapdownloadertask#resume()"><code>MapDownloaderTask.resume()</code></a>.
 Request can be cancelled by calling <a href="sdk-for-android-navigate-mapdownloadertask#cancel()"><code>MapDownloaderTask.cancel()</code></a> on returned <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> object, afterwards
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a> is called with error <a href="sdk-for-android-navigate-maploadererror#OPERATION_CANCELLED"><code>MapLoaderError.OPERATION_CANCELLED</code></a>.
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> remains operational until <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a> is called.
 Downloaded area will be associated to a unique id that will be reported via <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader"><code>DownloadRegionsStatusListener</code></a>.
 Simultaneous download of the same region twice is not supported. When such condition occurs then
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List<com.here.sdk.maploader.regionid>)</com.here.sdk.maploader.regionid></code></a> is called with error <a href="sdk-for-android-navigate-maploadererror#SERVICE_ACCESS_FAILED"><code>MapLoaderError.SERVICE_ACCESS_FAILED</code></a>
 for a new request, while previous one continues uninterrupted.
 If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
 the requested regions have been downloaded, the corresponding index will be created.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.
 To control list of map content features for area download, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.
 <br/>
 Note: If an application is forcefully closed or crashes during a map download operation, then this
 method can be called again to resume the download. For example, if a download was interrupted at 60%,
 then the next call to download the same region will load the remaining 40%.
 <br/>
 Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
 region three times before giving up. A connection will be timed out after one minute.
 <br/>
 Note: If user try to re-download same GeoPolygon the status will be reported as per the
 state of previous download operation.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>area</code> - <p>Area to download.</p></dd>
<dd><code>statusListener</code> - <p>Notifies on the download progress.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="deleteRegions(java.util.List,com.here.sdk.maploader.DeletedRegionsCallback)">
<h3>deleteRegions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">deleteRegions</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a>&gt; regions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-deletedregionscallback" title="interface in com.here.sdk.maploader">DeletedRegionsCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous operation to delete map data for regions specified by a list of <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader"><code>RegionId</code></a>.
 Note: Deleting a region when there is a pending download returns error
 <a href="sdk-for-android-navigate-maploadererror#INTERNAL_ERROR"><code>MapLoaderError.INTERNAL_ERROR</code></a>. Also, deleting a region when there is an ongoing download returns
 error <a href="sdk-for-android-navigate-maploadererror#PARALLEL_REQUEST"><code>MapLoaderError.PARALLEL_REQUEST</code></a>.
 If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
 the requested regions have been deleted, the index over remaining regions will be rebuilt,
 so that entries related to deleted regions are removed.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>regions</code> - <p>List of regions to be deleted.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result of deletion on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="clearPersistentMapStorage(com.here.sdk.maploader.SDKCacheCallback)">
<h3>clearPersistentMapStorage</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">clearPersistentMapStorage</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-sdkcachecallback" title="interface in com.here.sdk.maploader">SDKCacheCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous operation to clear the persistent map storage from all data. All downloaded regions will be removed.
 Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.
 Any previously built index will also be deleted.
 See <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#downloadRegions(java.util.List,com.here.sdk.maploader.DownloadRegionsStatusListener)"><code>downloadRegions(java.util.List<com.here.sdk.maploader.regionid>, com.here.sdk.maploader.DownloadRegionsStatusListener)</com.here.sdk.maploader.regionid></code></a> to learn more about index.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result of clearing on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInstalledRegions()">
<h3>getInstalledRegions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion" title="class in com.here.sdk.maploader">InstalledRegion</a>&gt;</span> <span className="element-name">getInstalledRegions</span>()
                                          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span></div>
<div className="block"><p>Method to get a list of map regions that are currently installed on the device.
 Throws if it's not possible to return list of installed regions.
 Returned list contains:
 <ul>
<li>successfully downloaded regions, indicated by <a href="sdk-for-android-navigate-installedregionstatus#INSTALLED"><code>InstalledRegionStatus.INSTALLED</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>;</li>
<li>regions, that are in the download process, indicated by <a href="sdk-for-android-navigate-installedregionstatus#PENDING"><code>InstalledRegionStatus.PENDING</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>;</li>
<li>regions, which were failed to be downloaded, indicated by <a href="sdk-for-android-navigate-installedregionstatus#PENDING"><code>InstalledRegionStatus.PENDING</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>.
 Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is
 set to the <a href="sdk-for-android-navigate-installedregionstatus#PENDING"><code>InstalledRegionStatus.PENDING</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>. Precise Japan content is available as an additional offering, please contact sales team for more information.</li>
</ul></p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>List of IDs of regions that are installed on the device</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></code> - <p>Specifies reason, why list of installed regions is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInitialPersistentMapStatus()">
<h3>getInitialPersistentMapStatus</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">getInitialPersistentMapStatus</span>()</div>
<div className="block"><p>Gets the initial status of the already downloaded regions at start-up time of the app.
 It is not recommended to download or to upload map data while an app is running in
 background. However, it can happen, that an app gets shut down during an ongoing
 operation, for example, due to a crash. In such a case, some or all of the downloaded map data
 may be in a corrupted state.
 Refer to the <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader"><code>PersistentMapStatus</code></a> for exact healing procedure for specific
 status.
 Note: This value will not change during the lifetime of an app.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Initial status of the persistent map.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback)">
<h3>repairPersistentMap</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">repairPersistentMap</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-repairpersistentmapcallback" title="interface in com.here.sdk.maploader">RepairPersistentMapCallback</a> callback)</span></div>
<div className="block"><p>Tries to repair already downloaded regions that are in a corrupted state (see <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getInitialPersistentMapStatus()"><code>getInitialPersistentMapStatus()</code></a>).
 If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then index will be
 rebuilt if existing index does not match with the installed map regions after this operation.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>A callback which receives the result of the repair operation on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOfflineMapsStorageSizeInBytes()">
<h3>getOfflineMapsStorageSizeInBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">getOfflineMapsStorageSizeInBytes</span>()
                                      throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span></div>
<div className="block"><p>Get the total size of all downloaded regions currently persisted on disk at the location that
 is specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 This includes also data that is currently being downloaded.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Value of offline map size.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></code> - <p>Specifies reason, why current map size is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOfflineMapsStorageSizeInBytes(com.here.sdk.maploader.OfflineStorageSizeCallback)">
<h3>getOfflineMapsStorageSizeInBytes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">getOfflineMapsStorageSizeInBytes</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-offlinestoragesizecallback" title="interface in com.here.sdk.maploader">OfflineStorageSizeCallback</a> callback)</span></div>
<div className="block"><p>Get the total size of all downloaded regions currently persisted on disk at the location that
 is specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 This includes also data that is currently being downloaded.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>A callback which receives the value of offline map size or error on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onEnterForeground()">
<h3>onEnterForeground</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onEnterForeground</span>()</div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Only part of Internal variant. Please use <code>sdk.maploader.BackgroundMapOperationContext.onEnterForeground</code> instead.</p></div>
</div>
<div className="block"><p>To enable background map downloads for iOS, this method must be invoked when the application
 moves from the foreground to the background, usually triggered when the user switches
 to another application or when the device's screen is turned off.
 Please note that this method is only relevant to the iOS platform.
 Robust handling of online requests finished while in the background
 depends on the integration with AppDelegate. How to integrate it
 see <code>sdk.maploader.BackgroundMapOperationContext</code>.</p></div>
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
