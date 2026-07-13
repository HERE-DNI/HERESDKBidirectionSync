---
title: "queryForIncidentsInCorridor method - TrafficEngine class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForIncidentsInCorridor.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">queryForIncidentsInCorridor</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">queryForIncidentsInCorridor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-queryForIncidentsInCorridor-param-corridorArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridorArea</span>, </span>
2.  <span id="sdk-for-flutter-explore-queryForIncidentsInCorridor-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span>
3.  <span id="sdk-for-flutter-explore-queryForIncidentsInCorridor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously queries for traffic incidents by a corridor as a filter.

- `corridorArea` The corridor box to search for traffic incidents. The maximum length for the corridor is 500000 meters and the maximum `GeoCorridor.half_width_in_meters` is 5000 meters. If the number of points in corridor is greater than 300 then request is split into smaller ones and results are aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.

To reduce number of points in the corridor use <a href="sdk-for-flutter-explore-core-polylinesimplifier-class">PolylineSimplifier</a>.

If no `GeoCorridor.half_width_in_meters` is specified, the default value is used. The default value is 30 meters.

- `queryOptions` The options which are specific for incidents query.

- `callback` It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle queryForIncidentsInCorridor(GeoCorridor corridorArea, TrafficIncidentsQueryOptions queryOptions, TrafficIncidentsQueryCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
