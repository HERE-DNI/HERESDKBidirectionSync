---
title: "latestWithIgnoringCachedData method - CatalogVersionHint class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-catalogversionhint-latestwithignoringcacheddata"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/CatalogVersionHint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">latestWithIgnoringCachedData</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a></span> <span class="name">latestWithIgnoringCachedData</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-latestWithIgnoringCachedData-param-ignoreCachedData" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">ignoreCachedData</span></span>

)

</div>

<div class="section desc markdown">

This static method can be called when you are interested in getting the most latest version of a catalog when initializing the HERE SDK with `SDKOptions` where you can specify the catalog(s) you want to use.

In effect, this will auto-update the cached map data on each start, if possible. Use this only when you have no installed `Regions`. Since this affects only the map data cache, calling this at initialization time has no or only a very limited effect on the start-up time.

In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the default HRN value: "hrn:here:data::olp-here:ocm" in your `DesiredCatalog`. Note that the HERE SDK (Explore) cannot be used with such settings and the initialization of the HERE SDK may fail - since it is based on a different map format.

- `ignoreCachedData` A flag to specify handling of any cached data present on a device when trying to update the map version. If set to true, the HERE SDK will auto-update to the latest catalog version when no installed `Regions` are present. If present, this call will have no effect - use

      updateCatalog()

  via `MapUpdater` instead to update all map data to the latest version. Note that cached data present on a device - for example, data in the map cache or data cached by `PrefetchAroundLocationWithRadius` or `PrefetchAroundRouteOnIntervals` - will be become obsolete if a newer map version is available. Such data will be evicted using a LRU strategy over time. If set to false, the HERE SDK will auto-update to use the latest version, only when there is no cached map data at all (for example, at first install or after clearing the cache) *and* no installed map data. Otherwise, this call will have no effect.

Returns <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a>. Instance of <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a>.

</div>

## Implementation

``` dart
static CatalogVersionHint latestWithIgnoringCachedData(bool ignoreCachedData) => $prototype.latestWithIgnoringCachedData(ignoreCachedData);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

