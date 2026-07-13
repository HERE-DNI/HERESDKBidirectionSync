---
title: "CalculateRouteCallback typedef - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-calculateroutecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CalculateRouteCallback.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">CalculateRouteCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">CalculateRouteCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-routingError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a>?</span> <span class="parameter-name">routingError</span>, </span><span id="sdk-for-flutter-explore-param-routeList" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-route-class">Route</a></span>\></span>?</span> <span class="parameter-name">routeList</span></span>)</span></span>

</div>

<div class="section desc markdown">

A function which is called by the RoutingEngine after route calculation has completed.

It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument is the calculated routes. It is `null` in case of an error.

- `routingError` The error in case of a failure. It is `null` for an operation that succeeds.

- `routeList` The calculated routes. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef CalculateRouteCallback = void Function(RoutingError? routingError, List<Route>? routeList);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
