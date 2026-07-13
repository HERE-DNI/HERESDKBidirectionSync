---
title: "repairPersistentMap method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- repairPersistentMap.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">repairPersistentMap</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">repairPersistentMap</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-repairPersistentMap-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-repairpersistentmapcallback">RepairPersistentMapCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Tries to repair already downloaded regions that are in a corrupted state (see <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus">MapDownloader.getInitialPersistentMapStatus</a>).

If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then index will be rebuilt if existing index does not match with the installed map regions after this operation. The index is used by `OfflineSearchEngine` to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

- `callback` A callback which receives the result of the repair operation on the main thread.

</div>

## Implementation

``` dart
void repairPersistentMap(RepairPersistentMapCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
