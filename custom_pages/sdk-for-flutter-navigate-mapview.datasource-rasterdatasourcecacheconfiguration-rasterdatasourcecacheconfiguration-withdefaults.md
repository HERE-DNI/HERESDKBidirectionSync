---
title: "RasterDataSourceCacheConfiguration.withDefaults constructor - RasterDataSourceCacheConfiguration - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration-withdefaults"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceCacheConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSourceCacheConfiguration.withDefaults</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSourceCacheConfiguration.withDefaults</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withDefaults-param-path" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">path</span></span>

)

</div>

<div class="section desc markdown">

Constructs a Cache object from the provided path and a default cache size of 32 MiB.

- `path` The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

</div>

## Implementation

``` dart
RasterDataSourceCacheConfiguration.withDefaults(this.path)
    : diskSize = 33554432;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

