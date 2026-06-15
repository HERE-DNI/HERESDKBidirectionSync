---
title: "downloadRegions abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadRegions.html -->


<div>
<h1>downloadRegions abstract method</h1></div>

<a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a>
downloadRegions(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>&gt; regions, </li>
<li><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a> statusListener</li>
</ol>)

      

    

<p>Performs an asynchronous request to download map data for regions specified
by a list of <a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a> instances.</p>
<p><code>MapDownloader.downloadRegions.statusListener</code> receives notifications until
<a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called.
The returned <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> can be used to pause or resume the download
using <code>MapDownloaderTask.pauseWithCompaction</code> or <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-resume">MapDownloaderTask.resume</a>.</p>
<p>To cancel the request, call <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-cancel">MapDownloaderTask.cancel</a> on the returned
<a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> object. After cancellation,
<a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called
with the error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.operationCancelled</a>.</p>
<p><a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> remains operational until <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called.</p>
<p>To get list of downloadable regions use <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">MapDownloader.getDownloadableRegionsWithLanguageCode</a> API.</p>
<p>Simultaneous downloads of the same region are not supported.
If this occurs, <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a>
is called with <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.serviceAccessFailed</a> for the new request,
while the previous one continues uninterrupted.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been downloaded, the corresponding index will be created.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<p>To control list of map content features for region download, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.</p>
<br/>
Note: If an application is forcefully closed or crashes during a map download operation, then this
method can be called again to resume the download. For example, if a download was interrupted at 60%,
then the next call to download the same region will load the remaining 40%.
<br/>
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
region three times before giving up. A connection will be timed out after one minute.
<ul>
<li>
<p><code>regions</code> List of regions to download. Can be fetched using <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">MapDownloader.getDownloadableRegionsWithLanguageCode</a> API.</p>
</li>
<li>
<p><code>statusListener</code> Notifies on the download progress.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapDownloaderTask downloadRegions(List&lt;RegionId&gt; regions, DownloadRegionsStatusListener statusListener);</code></pre>

 



</div>
`
}</HTMLBlock>
