---
title: "getOfflineMapsStorageSizeInBytes method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getOfflineMapsStorageSizeInBytes.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getOfflineMapsStorageSizeInBytes</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">getOfflineMapsStorageSizeInBytes</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Get the total size of all downloaded regions currently persisted on disk at the location that is specified via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.

This includes also data that is currently being downloaded.

Returns `int`. Value of offline map size.

Throws <a href="sdk-for-flutter-navigate-maploader-maploaderexceptionexception-class">MapLoaderExceptionException</a>. Specifies reason, why current map size is not returned.

</div>

## Implementation

``` dart
int getOfflineMapsStorageSizeInBytes();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
