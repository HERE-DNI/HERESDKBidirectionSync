---
title: "DynamicRoutingListener constructor - DynamicRoutingListener - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-dynamicroutinglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DynamicRoutingListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DynamicRoutingListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onBetterRouteFoundLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onBetterRouteFoundLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onRoutingErrorLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRoutingErrorLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about the new route via the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>.

</div>

## Implementation

``` dart
factory DynamicRoutingListener(
  void Function(Route, int, int) onBetterRouteFoundLambda,
  void Function(RoutingError) onRoutingErrorLambda,

) => DynamicRoutingListener$Lambdas(
  onBetterRouteFoundLambda,
  onRoutingErrorLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

