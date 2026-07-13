---
title: "CalculateIndoorRouteCallback typedef - venue.routing library - Dart API"
slug: "sdk-for-flutter-navigate-venue.routing-calculateindoorroutecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CalculateIndoorRouteCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.routing/venue.routing-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">CalculateIndoorRouteCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">CalculateIndoorRouteCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-indoorRoutingError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutingerror">IndoorRoutingError</a>?</span> <span class="parameter-name">indoorRoutingError</span>, </span><span id="sdk-for-flutter-navigate-param-routeList" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span>\></span>?</span> <span class="parameter-name">routeList</span></span>)</span></span>

</div>

<div class="section desc markdown">

A function which is called by the IndoorRoutingEngine after route calculation has completed.

It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument is the calculated routes. It is `null` in case of an error.

- `indoorRoutingError` The error in case of a failure. It is `null` for an operation that succeeds.

- `routeList` The calculated routes. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef CalculateIndoorRouteCallback = void Function(IndoorRoutingError? indoorRoutingError, List<Route>? routeList);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
