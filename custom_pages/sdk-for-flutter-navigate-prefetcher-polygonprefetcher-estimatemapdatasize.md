---
title: "estimateMapDataSize method - PolygonPrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-estimatemapdatasize"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- estimateMapDataSize.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/PolygonPrefetcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">estimateMapDataSize</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">estimateMapDataSize</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-estimateMapDataSize-param-geoPolygon" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geoPolygon</span>, </span>
2.  <span id="sdk-for-flutter-navigate-estimateMapDataSize-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-class">MapDataSizeListener</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Estimates map data size for the area bounded by geo polygon.

Size for tiles that are already in the cache will not be included in the final result.

- `geoPolygon` Area to estimate map data size for.

- `callback` Callback that is triggered to report the result of map data size estimation.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.

</div>

## Implementation

``` dart
TaskHandle estimateMapDataSize(GeoPolygon geoPolygon, MapDataSizeListener callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
