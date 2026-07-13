---
title: "clearPersistentMapStorage method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-clearpersistentmapstorage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- clearPersistentMapStorage.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">clearPersistentMapStorage</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">clearPersistentMapStorage</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-clearPersistentMapStorage-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-sdkcachecallback">SDKCacheCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous operation to clear the persistent map storage from all data.

All downloaded regions will be removed. Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.

Any previously built index will also be deleted. See <a href="sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions">MapDownloader.downloadRegions</a> to learn more about index.

- `callback` Callback which receives the result of clearing on the main thread.

</div>

## Implementation

``` dart
void clearPersistentMapStorage(SDKCacheCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
