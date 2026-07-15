---
title: "allowDownload property - CatalogConfiguration class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-catalogconfiguration-allowdownload"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/CatalogConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">allowDownload</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">allowDownload</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps. The storage path is specified in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>. If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see <a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-cacheexpirationperiod">CatalogConfiguration.cacheExpirationPeriod</a>). Defaults to `true`.

</div>

## Implementation

``` dart
bool allowDownload;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

