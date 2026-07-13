---
title: "downloadRegions method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadRegions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">downloadRegions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a></span> <span class="name">downloadRegions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-downloadRegions-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span></span> <span class="parameter-name">regions</span>, </span>
2.  <span id="sdk-for-flutter-navigate-downloadRegions-param-statusListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a></span> <span class="parameter-name">statusListener</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to download map data for regions specified by a list of <a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a> instances.

`MapDownloader.downloadRegions.statusListener` receives notifications until <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called. The returned <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> can be used to pause or resume the download using `MapDownloaderTask.pauseWithCompaction` or <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-resume">MapDownloaderTask.resume</a>.

To cancel the request, call <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-cancel">MapDownloaderTask.cancel</a> on the returned <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> object. After cancellation, <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with the error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.operationCancelled</a>.

<a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> remains operational until <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called.

To get list of downloadable regions use <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">MapDownloader.getDownloadableRegionsWithLanguageCode</a> API.

Simultaneous downloads of the same region are not supported. If this occurs, <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.serviceAccessFailed</a> for the new request, while the previous one continues uninterrupted.

If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then after the requested regions have been downloaded, the corresponding index will be created. The index is used by `OfflineSearchEngine` to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

To control list of map content features for region download, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.

\
Note: If an application is forcefully closed or crashes during a map download operation, then this method can be called again to resume the download. For example, if a download was interrupted at 60%, then the next call to download the same region will load the remaining 40%.\
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected region three times before giving up. A connection will be timed out after one minute.

- `regions` List of regions to download. Can be fetched using <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">MapDownloader.getDownloadableRegionsWithLanguageCode</a> API.

- `statusListener` Notifies on the download progress.

Returns <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

</div>

## Implementation

``` dart
MapDownloaderTask downloadRegions(List<RegionId> regions, DownloadRegionsStatusListener statusListener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
