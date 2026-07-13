---
title: "PrefetchStatusListener constructor - PrefetchStatusListener - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-prefetchstatuslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/PrefetchStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PrefetchStatusListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PrefetchStatusListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onProgressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onProgressLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onCompleteLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onCompleteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class to get notified on status updates when prefetching map data.

</div>

## Implementation

``` dart
factory PrefetchStatusListener(
  void Function(int) onProgressLambda,
  void Function(MapLoaderError?) onCompleteLambda,

) => PrefetchStatusListener$Lambdas(
  onProgressLambda,
  onCompleteLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

