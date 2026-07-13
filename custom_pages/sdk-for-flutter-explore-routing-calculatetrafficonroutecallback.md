---
title: "CalculateTrafficOnRouteCallback typedef - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-calculatetrafficonroutecallback"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">CalculateTrafficOnRouteCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">CalculateTrafficOnRouteCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-routingError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a>?</span> <span class="parameter-name">routingError</span>, </span><span id="sdk-for-flutter-explore-param-trafficOnRoute" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-trafficonroute-class">TrafficOnRoute</a>?</span> <span class="parameter-name">trafficOnRoute</span></span>)</span></span>

</div>

<div class="section desc markdown">

A function which is called by the RoutingEngine after route traffic calculation has completed.

It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument is the calculated route traffic. It is `null` in case of an error.

- `routingError` The error in case of a failure. It is `null` for an operation that succeeds.

- `trafficOnRoute` The calculated route traffic. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef CalculateTrafficOnRouteCallback = void Function(RoutingError? routingError, TrafficOnRoute? trafficOnRoute);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

