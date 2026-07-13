---
title: "prefetch method - PolygonPrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-prefetch"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/PolygonPrefetcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">prefetch</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">prefetch</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-prefetch-param-geoPolygon" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geoPolygon</span>, </span>
2.  <span id="sdk-for-flutter-navigate-prefetch-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class">PrefetchStatusListener</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Prefetches map data for an area bounded by geo polygon.

After the operation is finished <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete">PrefetchStatusListener.onComplete</a> is invoked on the main thread. Progress is reported by invocation of <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress">PrefetchStatusListener.onProgress</a> on the main thread. If there is not enough space left in the cache to store needed tiles, operation will fail with <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.notEnoughSpace</a>. To increase cache size, use <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachesizeinbytes">SDKOptions.cacheSizeInBytes</a> API.

To control list of map content features for area prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.

To prefetch map data within user-defined circular area around a given location:

1.  Create a GeoCircle using the given location and radius.
2.  Create a GeoPolygon using the GeoCircle.
3.  Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API. Usage: GeoCircle geoCircle = GeoCircle(location, radius); GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);

- `geoPolygon` Area to prefetch map data for.

- `callback` Callback that is triggered to report progress and the result of prefetch.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.

</div>

## Implementation

``` dart
TaskHandle prefetch(GeoPolygon geoPolygon, PrefetchStatusListener callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

