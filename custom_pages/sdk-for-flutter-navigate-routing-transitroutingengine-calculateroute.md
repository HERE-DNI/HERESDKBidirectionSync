---
title: "calculateRoute method - TransitRoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-transitroutingengine-calculateroute"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/TransitRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculateRoute</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">calculateRoute</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-calculateRoute-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-transitwaypoint-class">TransitWaypoint</a></span> <span class="parameter-name">startingPoint</span>, </span>
2.  <span id="sdk-for-flutter-navigate-calculateRoute-param-destination" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-transitwaypoint-class">TransitWaypoint</a></span> <span class="parameter-name">destination</span>, </span>
3.  <span id="sdk-for-flutter-navigate-calculateRoute-param-routeOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-class">TransitRouteOptions</a></span> <span class="parameter-name">routeOptions</span>, </span>
4.  <span id="sdk-for-flutter-navigate-calculateRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates a public transit route from the origin to the destination.

- `startingPoint` Position of starting point.

- `destination` Position of destination.

- `routeOptions` Options for public transit route calculation.

- `callback` Callback object that will be invoked after route calculation. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle calculateRoute(TransitWaypoint startingPoint, TransitWaypoint destination, TransitRouteOptions routeOptions, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

