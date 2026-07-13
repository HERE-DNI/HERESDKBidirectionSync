---
title: "refreshRouteWithRouteHandleAndRefreshRouteParameters method - RoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routingengine-refreshroutewithroutehandleandrefreshrouteparameters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">refreshRouteWithRouteHandleAndRefreshRouteParameters</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">refreshRouteWithRouteHandleAndRefreshRouteParameters</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-refreshRouteWithRouteHandleAndRefreshRouteParameters-param-refreshRouteParameters" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-refreshrouteparameters-class">RefreshRouteParameters</a></span> <span class="parameter-name">refreshRouteParameters</span>, </span>
2.  <span id="sdk-for-flutter-navigate-refreshRouteWithRouteHandleAndRefreshRouteParameters-param-routingOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">routingOptions</span>, </span>
3.  <span id="sdk-for-flutter-navigate-refreshRouteWithRouteHandleAndRefreshRouteParameters-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>, updating the starting point and route metadata based on <a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a>.

The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated.

- `refreshRouteParameters` The parameters used to refresh the route

- `routingOptions` The options define the vehicle and route options used to calculate the route.

- `callback` Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle refreshRouteWithRouteHandleAndRefreshRouteParameters(RefreshRouteParameters refreshRouteParameters, RoutingOptions routingOptions, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

