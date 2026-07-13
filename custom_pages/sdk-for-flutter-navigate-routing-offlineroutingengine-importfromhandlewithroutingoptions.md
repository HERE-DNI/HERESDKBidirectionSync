---
title: "importFromHandleWithRoutingOptions method - OfflineRoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-offlineroutingengine-importfromhandlewithroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importFromHandleWithRoutingOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/OfflineRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">importFromHandleWithRoutingOptions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">importFromHandleWithRoutingOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-importFromHandleWithRoutingOptions-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span>
2.  <span id="sdk-for-flutter-navigate-importFromHandleWithRoutingOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-importFromHandleWithRoutingOptions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously recreates a route from the <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> provided, i.e.

refreshes a previously calculated route, with the specified <a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-class" class="deprecated">RefreshRouteOptions</a>.

A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

- `routeHandle` The route handle holding the route to be refreshed.

- `options` Options to import the route from handle.

- `callback` Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle importFromHandleWithRoutingOptions(RouteHandle routeHandle, RoutingOptions options, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
