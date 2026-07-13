---
title: "prefetchAroundRouteOnIntervals method - RoutePrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundrouteonintervals"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/RoutePrefetcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">prefetchAroundRouteOnIntervals</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">prefetchAroundRouteOnIntervals</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-prefetchAroundRouteOnIntervals-param-navigator" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a></span> <span class="parameter-name">navigator</span></span>

)

</div>

<div class="section desc markdown">

Prefetches map data within a corridor along the route, that is currently set for the provided <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> instance.

If no route is set, no data will be prefetched. The route corridor defaults to a length of 10 km and a width of 5 km. To prefetch the whole route before navigation has been started see <a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor">RoutePrefetcher.prefetchGeoCorridor</a>. Map data is prefetched only in discrete intervals. Prefetching starts 1 km before reaching the end of the current corridor. Prefetching happens based on the current map-matched location - as indicated by the <a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a> event. This method should be called right after navigation has started. In case of default prefetch length first prefetching will start after traveling a distance of 9 km along the route.

To control list of map content features for prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.

- `navigator` The <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> to listen for Route Progress to prefetch data ahead.

</div>

## Implementation

``` dart
void prefetchAroundRouteOnIntervals(NavigatorInterface navigator);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

