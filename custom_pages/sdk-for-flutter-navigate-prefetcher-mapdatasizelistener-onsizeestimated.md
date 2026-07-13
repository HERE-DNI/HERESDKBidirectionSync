---
title: "onSizeEstimated method - MapDataSizeListener class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-onsizeestimated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onSizeEstimated.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/MapDataSizeListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onSizeEstimated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onSizeEstimated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onSizeEstimated-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onSizeEstimated-param-dataSize" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-mapdatasize-class">MapDataSize</a>?</span> <span class="parameter-name">dataSize</span></span>

)

</div>

<div class="section desc markdown">

Called after map data size estimation has been completed either with success or with error.

Invoked on the main thread.

- `error` Represents an error in case of a failure. If the operation was successful, `null` is returned.

- `dataSize` Represents the map data size. In case of failure, `null` is returned.

</div>

## Implementation

``` dart
void onSizeEstimated(MapLoaderError? error, MapDataSize? dataSize);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
