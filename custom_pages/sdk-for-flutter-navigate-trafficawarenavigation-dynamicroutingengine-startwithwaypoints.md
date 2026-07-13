---
title: "startWithWaypoints method - DynamicRoutingEngine class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithWaypoints.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startWithWaypoints</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the \`start()\` method with RoutingOptions parameter instead.")

</div>

<span class="returntype">void</span> <span class="name deprecated">startWithWaypoints</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startWithWaypoints-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span>
2.  <span id="sdk-for-flutter-navigate-startWithWaypoints-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span>
3.  <span id="sdk-for-flutter-navigate-startWithWaypoints-param-refreshRouteOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-class" class="deprecated">RefreshRouteOptions</a></span> <span class="parameter-name">refreshRouteOptions</span>, </span>
4.  <span id="sdk-for-flutter-navigate-startWithWaypoints-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a></span> <span class="parameter-name">listener</span>, </span>

)

</div>

<div class="section desc markdown">

Starts polling the HERE backend services to find a better route, as defined by the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>.

**Note:** The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

- `routeHandle` The route handle from the HERE routing backend.

- `waypoints` Allows to specify detailed information on the waypoints of the route. This parameter can be useful, when additional information needs to be specified besides the coordinates - as the coordinates can be retrieved from the contained <a href="sdk-for-flutter-navigate-routing-routeplace-class">RoutePlace</a> that are already contained in the <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> parameter.

- `refreshRouteOptions` The options for the route calculation.

- `listener` The listener to receive the events.

Throws <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class">DynamicRoutingEngineStartException</a>. when the passed parameter are invalid.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the `start()` method with RoutingOptions parameter instead.")

void startWithWaypoints(RouteHandle routeHandle, List<Waypoint> waypoints, RefreshRouteOptions refreshRouteOptions, DynamicRoutingListener listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
