---
title: "downloadArea method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-downloadarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadArea.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">downloadArea</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a></span> <span class="name">downloadArea</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-downloadArea-param-area" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">area</span>, </span>
2.  <span id="sdk-for-flutter-navigate-downloadArea-param-statusListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a></span> <span class="parameter-name">statusListener</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to download map data for area specified by a GeoPolygon.

`MapDownloader.downloadArea.statusListener` is receiving notifications until <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called. Returned <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> should be used to pause or resume started download, by invoking `MapDownloaderTask.pauseWithCompaction` or <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-resume">MapDownloaderTask.resume</a>. Request can be cancelled by calling <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-cancel">MapDownloaderTask.cancel</a> on returned <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> object, afterwards <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.operationCancelled</a>.

<a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a> remains operational until <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called.

Downloaded area will be associated to a unique id that will be reported via <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a>.

Simultaneous download of the same region twice is not supported. When such condition occurs then <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.serviceAccessFailed</a> for a new request, while previous one continues uninterrupted.

If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then after the requested regions have been downloaded, the corresponding index will be created. The index is used by `OfflineSearchEngine` to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

To control list of map content features for area download, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.

\
Note: If an application is forcefully closed or crashes during a map download operation, then this method can be called again to resume the download. For example, if a download was interrupted at 60%, then the next call to download the same region will load the remaining 40%.\
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected region three times before giving up. A connection will be timed out after one minute.\
Note: If user try to re-download same GeoPolygon the status will be reported as per the state of previous download operation.

- `area` Area to download.

- `statusListener` Notifies on the download progress.

Returns <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

</div>

## Implementation

``` dart
MapDownloaderTask downloadArea(GeoPolygon area, DownloadRegionsStatusListener statusListener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
