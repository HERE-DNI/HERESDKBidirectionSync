---
title: "importScooterRouteWithStops method - RoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routingengine-importscooterroutewithstops"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">importScooterRouteWithStops</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the \`import_route()\` methods with RoutingOptions parameter instead.")

</div>

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name deprecated">importScooterRouteWithStops</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-importScooterRouteWithStops-param-locations" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span>\></span></span> <span class="parameter-name">locations</span>, </span>
2.  <span id="sdk-for-flutter-navigate-importScooterRouteWithStops-param-routeStops" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-routestop-class">RouteStop</a></span>\></span></span> <span class="parameter-name">routeStops</span>, </span>
3.  <span id="sdk-for-flutter-navigate-importScooterRouteWithStops-param-scooterOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-scooteroptions-class" class="deprecated">ScooterOptions</a></span> <span class="parameter-name">scooterOptions</span>, </span>
4.  <span id="sdk-for-flutter-navigate-importScooterRouteWithStops-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other.

The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

**Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-flutter-navigate-routing-section-sectionnotices">Section.sectionNotices</a> .

- `locations` The list of locations used to calculate the route. Note that only the <a href="sdk-for-flutter-navigate-core-location-coordinates">Location.coordinates</a> of a location are used to import the route.

An <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the location list size is not in the range \[2,50000\].

- `routeStops` The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

An <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

- `scooterOptions` Options specific for scooter route calculation, along with common route options. Note that <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode.shortest</a> is not supported for scooters and converted to <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode.fastest</a> automatically.

- `callback` Callback object that will be invoked after route calculation. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.")

TaskHandle importScooterRouteWithStops(List<Location> locations, List<RouteStop> routeStops, ScooterOptions scooterOptions, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

