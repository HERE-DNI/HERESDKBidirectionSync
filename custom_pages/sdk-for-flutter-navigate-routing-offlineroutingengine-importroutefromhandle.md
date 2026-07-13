---
title: "importRouteFromHandle method - OfflineRoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-offlineroutingengine-importroutefromhandle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importRouteFromHandle.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/OfflineRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">importRouteFromHandle</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the \`import_route()\` method with RoutingOptions parameter instead.")

</div>

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name deprecated">importRouteFromHandle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-importRouteFromHandle-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span>
2.  <span id="sdk-for-flutter-navigate-importRouteFromHandle-param-refreshRouteOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-class" class="deprecated">RefreshRouteOptions</a></span> <span class="parameter-name">refreshRouteOptions</span>, </span>
3.  <span id="sdk-for-flutter-navigate-importRouteFromHandle-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously recreates a route from the <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> provided, i.e.

refreshes a previously calculated route, with the specified <a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-class" class="deprecated">RefreshRouteOptions</a>.

A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

- `routeHandle` The route handle holding the route to be refreshed.

- `refreshRouteOptions` Options to import the route from handle.

- `callback` Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the `import_route()` method with RoutingOptions parameter instead.")

TaskHandle importRouteFromHandle(RouteHandle routeHandle, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
