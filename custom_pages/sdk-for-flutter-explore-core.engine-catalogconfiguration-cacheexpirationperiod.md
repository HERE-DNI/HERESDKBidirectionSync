---
title: "cacheExpirationPeriod property - CatalogConfiguration class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-catalogconfiguration-cacheexpirationperiod"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/CatalogConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">cacheExpirationPeriod</span> property

</div>

<div class="section multi-line-signature">

Duration? <span class="name">cacheExpirationPeriod</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Expiration time in seconds for how long the catalog data is retained in the map cache before it is removed. Cache path is specified by <a href="sdk-for-flutter-explore-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a>. If not set, the cache will be deleted on a Least Recently Used (LRU) basis.

</div>

## Implementation

``` dart
Duration? cacheExpirationPeriod;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

