---
title: "MapDownloaderConstructionCallback typedef - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloaderconstructioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapDownloaderConstructionCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">MapDownloaderConstructionCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">MapDownloaderConstructionCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-mapDownloader" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a></span> <span class="parameter-name">mapDownloader</span></span>)</span></span>

</div>

<div class="section desc markdown">

A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync">MapDownloader.fromSdkEngineAsync</a> has been completed.

The `MapDownloader` instance is created on a background thread to not block the calling thread.

During construction an online connection is established to fetch configuration data for internal use. If no online connection is available, cached or default values will be used. This is only for internal reasons and has no effect on the operability of the resulting instance. When configuration data is available from the cache, construction can still take a reasonable amount of time. Applications should consider to show a loading indicator.

- `mapDownloader` Represents a constructed MapDownloader object.

</div>

## Implementation

``` dart
typedef MapDownloaderConstructionCallback = void Function(MapDownloader mapDownloader);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
