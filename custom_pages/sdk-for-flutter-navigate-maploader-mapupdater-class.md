---
title: "MapUpdater class abstract"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdater-class.html -->


<div>
<h1>MapUpdater class abstract</h1></div>

<p>A class for updating regions previously downloaded using the <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.</p>
<p>First, updates for the regions are downloaded. Once the download is complete, the update process begins,
installing the new content.
It is recommended to regularly call <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> to check for available updates
for any downloaded regions.</p>
<p>If updates are available, regions can be updated asynchronously using <a href="sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog">MapUpdater.updateCatalog</a>.
The <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class">MapUpdateProgressListener</a> provides update progress for each region.</p>
<p>Incremental map updates are supported, by default: Instead of downloading an entire region,
only the parts that have changed will be installed. This results in a faster update process.
MapUpdater also aligns previously downloaded content with <code>LayerConfiguration</code> changes made via <code>SDKOptions</code>.</p>
<p>Note that patching (also called "incremental updates") is only supported for up to 8 versions. For example, if an update started
with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9.
Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.</p>
<p>In case of an error, the previous map data remains available for use. It is only replaced
after new map data has been successfully downloaded. Regions that fail to update
must be retried in a new call. Paused updates can be resumed later.</p>
<p>During the update process, <a href="sdk-for-flutter-navigate-maploader-mapupdater-class">MapUpdater</a> internally retries failed downloads
until a timeout occurs. If this happens, it is reported via <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class">MapUpdateProgressListener</a>.</p>
<p>If the user cancels the update process during the update phase, it is ignored.
The update phase begins after all content has been downloaded, then the HERE SDK installs
and replaces the existing regions. Cancellation is only possible during the download phase,
and a successful cancellation is indicated via <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete">MapUpdateProgressListener.onComplete</a>.</p>
<p>Note that a <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.notReady</a> occurs when the <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a> is used in parallel.
In general, background updates are not supported explicitly, as the OS can abort background processes.
In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is
in progress and it will be indicated by a <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-mapupdater">MapUpdater</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-taskcount">taskCount</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-updatestatistics">updateStatistics</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-getcurrentmapversion">getCurrentMapVersion</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">retrieveCatalogsUpdateInfo</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-setversioncommitpolicy">setVersionCommitPolicy</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-tostring">toString</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog">updateCatalog</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-operator-equals">operator ==</a></li></ul>


<h2>Static Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync">fromSdkEngineAsync</a></li></ul>

 



</div>
`
}</HTMLBlock>
