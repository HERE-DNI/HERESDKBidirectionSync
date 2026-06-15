---
title: "MapDownloader class abstract"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapDownloader-class.html -->


<div>
<h1>MapDownloader class abstract</h1></div>

<p>A class for downloading and managing map data for various regions worldwide.</p>
<p>Downloaded map data is permanently stored on disk, enabling maps at all zoom levels,
search, routing, and other features without an active data connection.
Users can query available regions, download them to disk, or delete them.
An instance of this class can be created using <a href="sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync">MapDownloader.fromSdkEngineAsync</a>.</p>
<p>The storage path for downloaded maps can be specified via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.</p>
<p>To control the type of content included in a map download, use <code>LayerConfiguration</code>.
Once applied, it affects both the map cache and offline maps.
Satellite-based map schemes are not included in the downloaded region data.</p>
<p><strong>Note:</strong>
During turn-by-turn navigation,
while a map download or update is in progress, navigation may not function as expected,
and the app may be blocked until the operation is completed.
Ensure that all pending map operations are finished before starting navigation.
This applies only to <code>MapDownloader</code> and <code>MapUpdater</code>. <code>RoutePrefetcher</code> operations are not affected.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-mapdownloader">MapDownloader</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-taskcount">taskCount</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-clearpersistentmapstorage">clearPersistentMapStorage</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions">deleteRegions</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-downloadarea">downloadArea</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions">downloadRegions</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregions">getDownloadableRegions</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">getDownloadableRegionsWithLanguageCode</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus">getInitialPersistentMapStatus</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getinstalledregions">getInstalledRegions</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytes">getOfflineMapsStorageSizeInBytes</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync">getOfflineMapsStorageSizeInBytesAsync</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap">repairPersistentMap</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-operator-equals">operator ==</a></li></ul>


<h2>Static Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync">fromSdkEngineAsync</a></li></ul>

 



</div>
`
}</HTMLBlock>
