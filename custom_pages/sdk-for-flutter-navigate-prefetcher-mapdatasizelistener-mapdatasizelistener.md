---
title: "MapDataSizeListener constructor - MapDataSizeListener - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-mapdatasizelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapDataSizeListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/MapDataSizeListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapDataSizeListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapDataSizeListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onSizeEstimatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onSizeEstimatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-mapdatasize-class">MapDataSize</a>?</span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class to get the result of map data size estimation.

</div>

## Implementation

``` dart
factory MapDataSizeListener(
  void Function(MapLoaderError?, MapDataSize?) onSizeEstimatedLambda,

) => MapDataSizeListener$Lambdas(
  onSizeEstimatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
