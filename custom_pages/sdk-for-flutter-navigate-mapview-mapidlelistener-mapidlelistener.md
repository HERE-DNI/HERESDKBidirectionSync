---
title: "MapIdleListener constructor - MapIdleListener - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapidlelistener-mapidlelistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapIdleListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapIdleListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapIdleListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onMapBusyLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onMapBusyLambda</span>(), </span>
2.  <span id="sdk-for-flutter-navigate-param-onMapIdleLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onMapIdleLambda</span>()</span>

)

</div>

<div class="section desc markdown">

Used to detect when the map becomes idle or busy.

Map is considered busy when its state changes (for example as a result of camera manipulation) and/or when it requires a redraw (for example, as a result of map data being downloaded).

Map is considered idle when current state is fully rendered and no further redraws are necessary.

</div>

## Implementation

``` dart
factory MapIdleListener(
  void Function() onMapBusyLambda,
  void Function() onMapIdleLambda,

) => MapIdleListener$Lambdas(
  onMapBusyLambda,
  onMapIdleLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

