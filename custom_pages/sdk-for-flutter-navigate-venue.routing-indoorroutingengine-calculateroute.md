---
title: "calculateRoute method - IndoorRoutingEngine class - venue.routing library - Dart API"
slug: "sdk-for-flutter-navigate-venue.routing-indoorroutingengine-calculateroute"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.routing/IndoorRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculateRoute</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">calculateRoute</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-calculateRoute-param-from" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class">IndoorWaypoint</a></span> <span class="parameter-name">from</span>, </span>
2.  <span id="sdk-for-flutter-navigate-calculateRoute-param-to" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class">IndoorWaypoint</a></span> <span class="parameter-name">to</span>, </span>
3.  <span id="sdk-for-flutter-navigate-calculateRoute-param-routeOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-indoorrouteoptions-class">IndoorRouteOptions</a></span> <span class="parameter-name">routeOptions</span>, </span>
4.  <span id="sdk-for-flutter-navigate-calculateRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-routing-calculateindoorroutecallback">CalculateIndoorRouteCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates a route inside a venue.

- `from` A starting position of the route to calculate.

- `to` A destination position of the route to calculate.

- `routeOptions` Options specific for indoor route calculation, along with common route options.

- `callback` Callback object that will be invoked after route calculation. It is always invoked on the main thread.

</div>

## Implementation

``` dart
void calculateRoute(IndoorWaypoint from, IndoorWaypoint to, IndoorRouteOptions routeOptions, CalculateIndoorRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

