---
title: "getOfflineMapsStorageSizeInBytesAsync method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getOfflineMapsStorageSizeInBytesAsync</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">getOfflineMapsStorageSizeInBytesAsync</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getOfflineMapsStorageSizeInBytesAsync-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-offlinestoragesizecallback">OfflineStorageSizeCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Get the total size of all downloaded regions currently persisted on disk at the location that is specified via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.

This includes also data that is currently being downloaded.

- `callback` A callback which receives the value of offline map size or error on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

</div>

## Implementation

``` dart
TaskHandle getOfflineMapsStorageSizeInBytesAsync(OfflineStorageSizeCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

