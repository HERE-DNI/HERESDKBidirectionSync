---
title: "queryForFlowInCircle method - TrafficEngine class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForFlowInCircle.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">queryForFlowInCircle</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">queryForFlowInCircle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-queryForFlowInCircle-param-circleArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circleArea</span>, </span>
2.  <span id="sdk-for-flutter-explore-queryForFlowInCircle-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span>
3.  <span id="sdk-for-flutter-explore-queryForFlowInCircle-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously queries for traffic flow using a circle as a filter.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `circleArea` The circle area to search for traffic flow. The maximum radius of the circle filter is 50000 meters.

- `queryOptions` The options which are specific for flow query.

- `callback` It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle queryForFlowInCircle(GeoCircle circleArea, TrafficFlowQueryOptions queryOptions, TrafficFlowQueryCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
