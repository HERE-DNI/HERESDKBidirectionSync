---
title: "downloadArea abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-downloadarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadArea.html -->


<div>
<h1>downloadArea abstract method</h1></div>

<a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a>
downloadArea(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a> area, </li>
<li><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a> statusListener</li>
</ol>)

      

    

<p>Performs an asynchronous request to download map data for area specified by a GeoPolygon.</p>
<p><code>MapDownloader.downloadArea.statusListener</code> is receiving notifications until <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called.
Returned <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> should be used to pause or resume started download, by invoking
<code>MapDownloaderTask.pauseWithCompaction</code> or <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-resume">MapDownloaderTask.resume</a>.
Request can be cancelled by calling <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-cancel">MapDownloaderTask.cancel</a> on returned <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> object, afterwards
<a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.operationCancelled</a>.</p>
<p><a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> remains operational until <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called.</p>
<p>Downloaded area will be associated to a unique id that will be reported via <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a>.</p>
<p>Simultaneous download of the same region twice is not supported. When such condition occurs then
<a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.serviceAccessFailed</a>
for a new request, while previous one continues uninterrupted.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been downloaded, the corresponding index will be created.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<p>To control list of map content features for area download, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.</p>
<br/>
Note: If an application is forcefully closed or crashes during a map download operation, then this
method can be called again to resume the download. For example, if a download was interrupted at 60%,
then the next call to download the same region will load the remaining 40%.
<br/>
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
region three times before giving up. A connection will be timed out after one minute.
<br/>
Note: If user try to re-download same GeoPolygon the status will be reported as per the
state of previous download operation.
<ul>
<li>
<p><code>area</code> Area to download.</p>
</li>
<li>
<p><code>statusListener</code> Notifies on the download progress.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapDownloaderTask downloadArea(GeoPolygon area, DownloadRegionsStatusListener statusListener);</code></pre>

 



</div>
`
}</HTMLBlock>
