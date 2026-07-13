---
title: "prefetchGeoCorridor method - RoutePrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/RoutePrefetcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">prefetchGeoCorridor</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">prefetchGeoCorridor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-prefetchGeoCorridor-param-corridor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridor</span>, </span>
2.  <span id="sdk-for-flutter-navigate-prefetchGeoCorridor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class">PrefetchStatusListener</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Prefetch tiles for a given geo-corridor.

A geo-corridor can easily be created from a route with <a href="sdk-for-flutter-navigate-routing-route-geometry">Route.geometry</a> so navigation on this route is possible in offline cases. Please note, tiles will be saved in mutable cache so when there is not enough space to accommodate new prefetched tiles <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.notEnoughSpace</a> is returned. When updating mutable cache, all tiles will be unusable. Please re-download the geoCorridor again. Please also note, any route calculation may not possible on prefetched tiles.

To control list of map content features for corridor prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.

- `corridor` indicates `GeoCorridor` that can be constructed from the route.

- `callback` is invoked to report progress and the result of prefetch. After operation is finished, <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete">PrefetchStatusListener.onComplete</a> is invoked on the main thread. Progress is reported by invocation of <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress">PrefetchStatusListener.onProgress</a> on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle prefetchGeoCorridor(GeoCorridor corridor, PrefetchStatusListener callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

