---
title: "MapDownloader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapDownloader.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.maploader.MapDownloader</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapDownloader</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A class for downloading and managing map data for various regions worldwide.
 Downloaded map data is permanently stored on disk, enabling maps at all zoom levels,
 search, routing, and other features without an active data connection.
 Users can query available regions, download them to disk, or delete them.
 An instance of this class can be created using <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a>.
 </p><p>The storage path for downloaded maps can be specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 </p><p>To control the type of content included in a map download, use <code>LayerConfiguration</code>.
 Once applied, it affects both the map cache and offline maps.
 Satellite-based map schemes are not included in the downloaded region data.
 </p><p><strong>Note:</strong>
 During turn-by-turn navigation,
 while a map download or update is in progress, navigation may not function as expected,
 and the app may be blocked until the operation is completed.
 Ensure that all pending map operations are finished before starting navigation.
 This applies only to <code>MapDownloader</code> and <code>MapUpdater</code>. <code>RoutePrefetcher</code> operations are not affected.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#clearPersistentMapStorage(com.here.sdk.maploader.SDKCacheCallback)">clearPersistentMapStorage</a><wbr/>(<a href="sdk-for-android-navigate-sdkcachecallback" title="interface in com.here.sdk.maploader">SDKCacheCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous operation to clear the persistent map storage from all data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#deleteRegions(java.util.List,com.here.sdk.maploader.DeletedRegionsCallback)">deleteRegions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a>&gt; regions,
 <a href="sdk-for-android-navigate-deletedregionscallback" title="interface in com.here.sdk.maploader">DeletedRegionsCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous operation to delete map data for regions specified by a list of <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader"><code>RegionId</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#downloadArea(com.here.sdk.core.GeoPolygon,com.here.sdk.maploader.DownloadRegionsStatusListener)">downloadArea</a><wbr/>(<a href="sdk-for-android-navigate-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> area,
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to download map data for area specified by a GeoPolygon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#downloadRegions(java.util.List,com.here.sdk.maploader.DownloadRegionsStatusListener)">downloadRegions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a>&gt; regions,
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to download map data for regions specified
 by a list of <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader"><code>RegionId</code></a> instances.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)">fromEngineAsync</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-mapdownloaderconstructioncallback" title="interface in com.here.sdk.maploader">MapDownloaderConstructionCallback</a> mapDownloaderConstructionCallback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets a single instance of this class per provided <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)">getDownloadableRegions</a><wbr/>(<a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="sdk-for-android-navigate-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to fetch a list of <a href="sdk-for-android-navigate-region" title="class in com.here.sdk.maploader"><code>Region</code></a> objects with <a href="sdk-for-android-navigate-region#name"><code>Region.name</code></a>
 in given <code>languageCode</code>, that can be used to download the actual map data in a separate request.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getDownloadableRegions(com.here.sdk.maploader.DownloadableRegionsCallback)">getDownloadableRegions</a><wbr/>(<a href="sdk-for-android-navigate-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs an asynchronous request to fetch a list of <a href="sdk-for-android-navigate-region" title="class in com.here.sdk.maploader"><code>Region</code></a> objects
 for downloading map data in a separate request.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getInitialPersistentMapStatus()">getInitialPersistentMapStatus</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the initial status of the already downloaded regions at start-up time of the app.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-installedregion" title="class in com.here.sdk.maploader">InstalledRegion</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getInstalledRegions()">getInstalledRegions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method to get a list of map regions that are currently installed on the device.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getOfflineMapsStorageSizeInBytes()">getOfflineMapsStorageSizeInBytes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the total size of all downloaded regions currently persisted on disk at the location that
 is specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getOfflineMapsStorageSizeInBytes(com.here.sdk.maploader.OfflineStorageSizeCallback)">getOfflineMapsStorageSizeInBytes</a><wbr/>(<a href="sdk-for-android-navigate-offlinestoragesizecallback" title="interface in com.here.sdk.maploader">OfflineStorageSizeCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the total size of all downloaded regions currently persisted on disk at the location that
 is specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getTaskCount()">getTaskCount</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the number of concurrent tasks for downloading a map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#onEnterForeground()">onEnterForeground</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Only part of Internal variant.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback)">repairPersistentMap</a><wbr/>(<a href="sdk-for-android-navigate-repairpersistentmapcallback" title="interface in com.here.sdk.maploader">RepairPersistentMapCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tries to repair already downloaded regions that are in a corrupted state (see <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getInitialPersistentMapStatus()"><code>getInitialPersistentMapStatus()</code></a>).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#setTaskCount(long)">setTaskCount</a><wbr/>(long value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the number of concurrent tasks for downloading a map.</div>
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
<section class="detail" id="fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)">
<h3>fromEngineAsync</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">fromEngineAsync</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-mapdownloaderconstructioncallback" title="interface in com.here.sdk.maploader">MapDownloaderConstructionCallback</a> mapDownloaderConstructionCallback)</span></div>
<div class="block"><p>Gets a single instance of this class per provided <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An instance of the SDKNativeEngine</p></dd>
<dd><code>mapDownloaderConstructionCallback</code> - <p>A callback that will receive the result of construction</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDownloadableRegions(com.here.sdk.maploader.DownloadableRegionsCallback)">
<h3>getDownloadableRegions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">getDownloadableRegions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to fetch a list of <a href="sdk-for-android-navigate-region" title="class in com.here.sdk.maploader"><code>Region</code></a> objects
 for downloading map data in a separate request.
 </p><p>The default language for <a href="sdk-for-android-navigate-region#name"><code>Region.name</code></a> is <a href="sdk-for-android-navigate-languagecode#EN_US"><code>LanguageCode.EN_US</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)">
<h3>getDownloadableRegions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">getDownloadableRegions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to fetch a list of <a href="sdk-for-android-navigate-region" title="class in com.here.sdk.maploader"><code>Region</code></a> objects with <a href="sdk-for-android-navigate-region#name"><code>Region.name</code></a>
 in given <code>languageCode</code>, that can be used to download the actual map data in a separate request.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>languageCode</code> - <p>The language code determines the language of <a href="sdk-for-android-navigate-region#name"><code>Region.name</code></a>.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="downloadRegions(java.util.List,com.here.sdk.maploader.DownloadRegionsStatusListener)">
<h3>downloadRegions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></span> <span class="element-name">downloadRegions</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a>&gt; regions,
 @NonNull
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</span></div>
<div class="block"><p>Performs an asynchronous request to download map data for regions specified
 by a list of <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader"><code>RegionId</code></a> instances.
 <code>statusListener</code> receives notifications until
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a> is called.
 The returned <a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> can be used to pause or resume the download
 using <code>MapDownloaderTask.pause(boolean)</code> or <a href="sdk-for-android-navigate-mapdownloadertask#resume()"><code>MapDownloaderTask.resume()</code></a>.
 </p><p>To cancel the request, call <a href="sdk-for-android-navigate-mapdownloadertask#cancel()"><code>MapDownloaderTask.cancel()</code></a> on the returned
 <a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> object. After cancellation,
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a> is called
 with the error <a href="sdk-for-android-navigate-maploadererror#OPERATION_CANCELLED"><code>MapLoaderError.OPERATION_CANCELLED</code></a>.
 </p><p><a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> remains operational until <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a> is called.
 </p><p>To get list of downloadable regions use <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)"><code>getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)</code></a> API.
 </p><p>Simultaneous downloads of the same region are not supported.
 If this occurs, <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a>
 is called with <a href="sdk-for-android-navigate-maploadererror#SERVICE_ACCESS_FAILED"><code>MapLoaderError.SERVICE_ACCESS_FAILED</code></a> for the new request,
 while the previous one continues uninterrupted.
 </p><p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
 the requested regions have been downloaded, the corresponding index will be created.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.
 </p><p>To control list of map content features for region download, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.
 <br/>
 Note: If an application is forcefully closed or crashes during a map download operation, then this
 method can be called again to resume the download. For example, if a download was interrupted at 60%,
 then the next call to download the same region will load the remaining 40%.
 <br/>
 Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
 region three times before giving up. A connection will be timed out after one minute.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>regions</code> - <p>List of regions to download. Can be fetched using <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)"><code>getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)</code></a> API.</p></dd>
<dd><code>statusListener</code> - <p>Notifies on the download progress.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="downloadArea(com.here.sdk.core.GeoPolygon,com.here.sdk.maploader.DownloadRegionsStatusListener)">
<h3>downloadArea</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></span> <span class="element-name">downloadArea</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> area,
 @NonNull
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</span></div>
<div class="block"><p>Performs an asynchronous request to download map data for area specified by a GeoPolygon.
 <code>statusListener</code> is receiving notifications until <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a> is called.
 Returned <a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> should be used to pause or resume started download, by invoking
 <code>MapDownloaderTask.pause(boolean)</code> or <a href="sdk-for-android-navigate-mapdownloadertask#resume()"><code>MapDownloaderTask.resume()</code></a>.
 Request can be cancelled by calling <a href="sdk-for-android-navigate-mapdownloadertask#cancel()"><code>MapDownloaderTask.cancel()</code></a> on returned <a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> object, afterwards
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a> is called with error <a href="sdk-for-android-navigate-maploadererror#OPERATION_CANCELLED"><code>MapLoaderError.OPERATION_CANCELLED</code></a>.
 </p><p><a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader"><code>MapDownloaderTask</code></a> remains operational until <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a> is called.
 </p><p>Downloaded area will be associated to a unique id that will be reported via <a href="sdk-for-android-navigate-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader"><code>DownloadRegionsStatusListener</code></a>.
 </p><p>Simultaneous download of the same region twice is not supported. When such condition occurs then
 <a href="sdk-for-android-navigate-downloadregionsstatuslistener#onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError,java.util.List)"><code>DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List&lt;com.here.sdk.maploader.RegionId&gt;)</code></a> is called with error <a href="sdk-for-android-navigate-maploadererror#SERVICE_ACCESS_FAILED"><code>MapLoaderError.SERVICE_ACCESS_FAILED</code></a>
 for a new request, while previous one continues uninterrupted.
 </p><p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
 the requested regions have been downloaded, the corresponding index will be created.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.
 </p><p>To control list of map content features for area download, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.
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
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>area</code> - <p>Area to download.</p></dd>
<dd><code>statusListener</code> - <p>Notifies on the download progress.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deleteRegions(java.util.List,com.here.sdk.maploader.DeletedRegionsCallback)">
<h3>deleteRegions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deleteRegions</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a>&gt; regions,
 @NonNull
 <a href="sdk-for-android-navigate-deletedregionscallback" title="interface in com.here.sdk.maploader">DeletedRegionsCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous operation to delete map data for regions specified by a list of <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader"><code>RegionId</code></a>.
 Note: Deleting a region when there is a pending download returns error
 <a href="sdk-for-android-navigate-maploadererror#INTERNAL_ERROR"><code>MapLoaderError.INTERNAL_ERROR</code></a>. Also, deleting a region when there is an ongoing download returns
 error <a href="sdk-for-android-navigate-maploadererror#PARALLEL_REQUEST"><code>MapLoaderError.PARALLEL_REQUEST</code></a>.
 </p><p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
 the requested regions have been deleted, the index over remaining regions will be rebuilt,
 so that entries related to deleted regions are removed.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>regions</code> - <p>List of regions to be deleted.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result of deletion on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearPersistentMapStorage(com.here.sdk.maploader.SDKCacheCallback)">
<h3>clearPersistentMapStorage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearPersistentMapStorage</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdkcachecallback" title="interface in com.here.sdk.maploader">SDKCacheCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous operation to clear the persistent map storage from all data. All downloaded regions will be removed.
 Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.
 </p><p>Any previously built index will also be deleted.
 See <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#downloadRegions(java.util.List,com.here.sdk.maploader.DownloadRegionsStatusListener)"><code>downloadRegions(java.util.List&lt;com.here.sdk.maploader.RegionId&gt;, com.here.sdk.maploader.DownloadRegionsStatusListener)</code></a> to learn more about index.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback which receives the result of clearing on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstalledRegions()">
<h3>getInstalledRegions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-installedregion" title="class in com.here.sdk.maploader">InstalledRegion</a>&gt;</span> <span class="element-name">getInstalledRegions</span>()
                                          throws <span class="exceptions"><a href="sdk-for-android-navigate-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span></div>
<div class="block"><p>Method to get a list of map regions that are currently installed on the device.
 Throws if it's not possible to return list of installed regions.
 Returned list contains:
 <ul>
<li>successfully downloaded regions, indicated by <a href="sdk-for-android-navigate-installedregionstatus#INSTALLED"><code>InstalledRegionStatus.INSTALLED</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>;</li>
<li>regions, that are in the download process, indicated by <a href="sdk-for-android-navigate-installedregionstatus#PENDING"><code>InstalledRegionStatus.PENDING</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>;</li>
<li>regions, which were failed to be downloaded, indicated by <a href="sdk-for-android-navigate-installedregionstatus#PENDING"><code>InstalledRegionStatus.PENDING</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>.
 Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is
 set to the <a href="sdk-for-android-navigate-installedregionstatus#PENDING"><code>InstalledRegionStatus.PENDING</code></a> in <a href="sdk-for-android-navigate-installedregion#status"><code>InstalledRegion.status</code></a>. Precise Japan content is available as an additional offering, please contact sales team for more information.</li>
</ul></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>List of IDs of regions that are installed on the device</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></code> - <p>Specifies reason, why list of installed regions is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInitialPersistentMapStatus()">
<h3>getInitialPersistentMapStatus</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">getInitialPersistentMapStatus</span>()</div>
<div class="block"><p>Gets the initial status of the already downloaded regions at start-up time of the app.
 It is not recommended to download or to upload map data while an app is running in
 background. However, it can happen, that an app gets shut down during an ongoing
 operation, for example, due to a crash. In such a case, some or all of the downloaded map data
 may be in a corrupted state.
 Refer to the <a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader"><code>PersistentMapStatus</code></a> for exact healing procedure for specific
 status.
 Note: This value will not change during the lifetime of an app.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Initial status of the persistent map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback)">
<h3>repairPersistentMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">repairPersistentMap</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-repairpersistentmapcallback" title="interface in com.here.sdk.maploader">RepairPersistentMapCallback</a> callback)</span></div>
<div class="block"><p>Tries to repair already downloaded regions that are in a corrupted state (see <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getInitialPersistentMapStatus()"><code>getInitialPersistentMapStatus()</code></a>).
 </p><p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then index will be
 rebuilt if existing index does not match with the installed map regions after this operation.
 The index is used by <code>OfflineSearchEngine</code> to find better results.
 Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>A callback which receives the result of the repair operation on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOfflineMapsStorageSizeInBytes()">
<h3>getOfflineMapsStorageSizeInBytes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getOfflineMapsStorageSizeInBytes</span>()
                                      throws <span class="exceptions"><a href="sdk-for-android-navigate-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span></div>
<div class="block"><p>Get the total size of all downloaded regions currently persisted on disk at the location that
 is specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 This includes also data that is currently being downloaded.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Value of offline map size.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></code> - <p>Specifies reason, why current map size is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOfflineMapsStorageSizeInBytes(com.here.sdk.maploader.OfflineStorageSizeCallback)">
<h3>getOfflineMapsStorageSizeInBytes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">getOfflineMapsStorageSizeInBytes</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-offlinestoragesizecallback" title="interface in com.here.sdk.maploader">OfflineStorageSizeCallback</a> callback)</span></div>
<div class="block"><p>Get the total size of all downloaded regions currently persisted on disk at the location that
 is specified via <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 This includes also data that is currently being downloaded.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>A callback which receives the value of offline map size or error on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onEnterForeground()">
<h3>onEnterForeground</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onEnterForeground</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Only part of Internal variant. Please use <code>sdk.maploader.BackgroundMapOperationContext.onEnterForeground</code> instead.</p></div>
</div>
<div class="block"><p>To enable background map downloads for iOS, this method must be invoked when the application
 moves from the foreground to the background, usually triggered when the user switches
 to another application or when the device's screen is turned off.
 Please note that this method is only relevant to the iOS platform.
 Robust handling of online requests finished while in the background
 depends on the integration with AppDelegate. How to integrate it
 see <code>sdk.maploader.BackgroundMapOperationContext</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="getTaskCount()">
<h3>getTaskCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getTaskCount</span>()</div>
<div class="block"><p>Gets the number of concurrent tasks for downloading a map.
 </p><p>A valid task count is between 1 to 64. When the value set is outside the valid range,
 then it is clamped to a valid range:
 <ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.</li>
</ul></p></div>
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
 </p><p>A valid task count is between 1 to 64. When the value set is outside the valid range,
 then it is clamped to a valid range:
 <ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.</li>
</ul></p></div>
<dl class="notes">
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
`
}</HTMLBlock>
