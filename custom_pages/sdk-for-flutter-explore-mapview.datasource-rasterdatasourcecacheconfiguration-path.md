---
title: "path property - RasterDataSourceCacheConfiguration class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-rasterdatasourcecacheconfiguration-path"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceCacheConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">path</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">path</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

</div>

## Implementation

``` dart
String path;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

