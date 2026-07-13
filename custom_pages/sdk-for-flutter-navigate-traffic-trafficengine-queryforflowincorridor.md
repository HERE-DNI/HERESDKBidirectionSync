---
title: "queryForFlowInCorridor method - TrafficEngine class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincorridor"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">queryForFlowInCorridor</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">queryForFlowInCorridor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-queryForFlowInCorridor-param-corridorArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridorArea</span>, </span>
2.  <span id="sdk-for-flutter-navigate-queryForFlowInCorridor-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span>
3.  <span id="sdk-for-flutter-navigate-queryForFlowInCorridor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously queries for traffic flow by a corridor as a filter.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `corridorArea` The corridor box to search for traffic flow. The maximum length for the corridor is 500000 meters and the maximum `GeoCorridor.half_width_in_meters` is 5000 meters.

Maximum number of points in the corridor is 300.

To reduce number of points in the corridor use <a href="sdk-for-flutter-navigate-core-polylinesimplifier-class">PolylineSimplifier</a>.

If no `GeoCorridor.half_width_in_meters` is specified, the default value is used. The default value is 30 meters.

- `queryOptions` The options which are specific for flow query.

- `callback` It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle queryForFlowInCorridor(GeoCorridor corridorArea, TrafficFlowQueryOptions queryOptions, TrafficFlowQueryCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

