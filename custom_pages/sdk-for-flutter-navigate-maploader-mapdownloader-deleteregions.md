---
title: "deleteRegions method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- deleteRegions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">deleteRegions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">deleteRegions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-deleteRegions-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span></span> <span class="parameter-name">regions</span>, </span>
2.  <span id="sdk-for-flutter-navigate-deleteRegions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-deletedregionscallback">DeletedRegionsCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous operation to delete map data for regions specified by a list of <a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>.

Note: Deleting a region when there is a pending download returns error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.internalError</a>. Also, deleting a region when there is an ongoing download returns error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.parallelRequest</a>.

If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then after the requested regions have been deleted, the index over remaining regions will be rebuilt, so that entries related to deleted regions are removed. The index is used by `OfflineSearchEngine` to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

- `regions` List of regions to be deleted.

- `callback` Callback which receives the result of deletion on the main thread.

</div>

## Implementation

``` dart
void deleteRegions(List<RegionId> regions, DeletedRegionsCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
