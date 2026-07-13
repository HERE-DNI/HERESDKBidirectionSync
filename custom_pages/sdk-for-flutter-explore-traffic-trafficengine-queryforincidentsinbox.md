---
title: "queryForIncidentsInBox method - TrafficEngine class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsinbox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForIncidentsInBox.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">queryForIncidentsInBox</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">queryForIncidentsInBox</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-queryForIncidentsInBox-param-boxArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">boxArea</span>, </span>
2.  <span id="sdk-for-flutter-explore-queryForIncidentsInBox-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span>
3.  <span id="sdk-for-flutter-explore-queryForIncidentsInBox-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously queries for traffic incidents using a bounding box as a filter.

- `boxArea` The bounding box area to search for traffic incidents. The maximum width and height for a bounding box filter is 1 degree.

- `queryOptions` The options which are specific for incidents query.

- `callback` It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle queryForIncidentsInBox(GeoBox boxArea, TrafficIncidentsQueryOptions queryOptions, TrafficIncidentsQueryCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
