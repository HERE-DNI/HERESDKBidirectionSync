---
title: "OfflineStorageSizeCallback typedef - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-offlinestoragesizecallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">OfflineStorageSizeCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">OfflineStorageSizeCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span>, </span><span id="sdk-for-flutter-navigate-param-size" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">size</span></span>)</span></span>

</div>

<div class="section desc markdown">

A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync">MapDownloader.getOfflineMapsStorageSizeInBytesAsync</a> has been completed.

The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.

- `error` Represents an error in case of a failure. It is `null` for an operation that succeeds.

- `size` The size of offline map. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef OfflineStorageSizeCallback = void Function(MapLoaderError? error, int? size);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

