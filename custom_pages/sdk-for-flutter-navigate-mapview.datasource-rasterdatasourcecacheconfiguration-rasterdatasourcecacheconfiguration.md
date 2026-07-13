---
title: "RasterDataSourceCacheConfiguration constructor - RasterDataSourceCacheConfiguration - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceCacheConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSourceCacheConfiguration</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSourceCacheConfiguration</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-path" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">path</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-diskSize" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">diskSize</span></span>

)

</div>

<div class="section desc markdown">

Constructs a Cache object from the provided path and cache size.

- `path` The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.
- `diskSize` The maximum size to use on disk for the cache, in bytes. Default is 32 MiB. This cache is independent from the map cache as defined via `SDKOptions`. Its size is only limited by the total device storage capacity.

</div>

## Implementation

``` dart
RasterDataSourceCacheConfiguration(this.path, this.diskSize);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

