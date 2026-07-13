---
title: "lookupIncident method - TrafficEngine class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficengine-lookupincident"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookupIncident</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">lookupIncident</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookupIncident-param-originalId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">originalId</span>, </span>
2.  <span id="sdk-for-flutter-explore-lookupIncident-param-lookupOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-class">TrafficIncidentLookupOptions</a></span> <span class="parameter-name">lookupOptions</span>, </span>
3.  <span id="sdk-for-flutter-explore-lookupIncident-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentlookupcallback">TrafficIncidentLookupCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously queries for traffic incident by the original id.

See <a href="sdk-for-flutter-explore-traffic-trafficincident-originalid">TrafficIncident.originalId</a> for more information.

- `originalId` The requested incident original id.

- `lookupOptions` The options which are specific for the incident lookup query.

- `callback` The callback object that will be invoked after the incident lookup query. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle lookupIncident(String originalId, TrafficIncidentLookupOptions lookupOptions, TrafficIncidentLookupCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

