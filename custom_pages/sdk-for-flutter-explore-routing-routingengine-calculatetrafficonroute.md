---
title: "calculateTrafficOnRoute method - RoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTrafficOnRoute.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculateTrafficOnRoute</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">calculateTrafficOnRoute</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-calculateTrafficOnRoute-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-route-class">Route</a></span> <span class="parameter-name">route</span>, </span>
2.  <span id="sdk-for-flutter-explore-calculateTrafficOnRoute-param-lastTraveledSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">lastTraveledSectionIndex</span>, </span>
3.  <span id="sdk-for-flutter-explore-calculateTrafficOnRoute-param-traveledDistanceOnLastSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnLastSectionInMeters</span>, </span>
4.  <span id="sdk-for-flutter-explore-calculateTrafficOnRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-calculatetrafficonroutecallback">CalculateTrafficOnRouteCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates the traffic along a route starting from the index of the last traveled route section and an offset (in meters) from the last visited position on the section.

Call this when only the contained traffic information or the latest ETA duration is needed. This can be called periodically to retrieve updated ETA values during navigation.

**Note:** Calling this method will trigger a new "HERE Traffic" transaction, for example, if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.

- `route` A <a href="sdk-for-flutter-explore-routing-route-class">Route</a> calculated using the online routing engine. Its <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> and the original route calculation options will be used to compute the traffic on the route. The original route remains untouched.

- `lastTraveledSectionIndex` Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

- `traveledDistanceOnLastSectionInMeters` Offset, in meters, to the last visited position on the route section defined by the last traveled section index.

- `callback` Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle calculateTrafficOnRoute(Route route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, CalculateTrafficOnRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
