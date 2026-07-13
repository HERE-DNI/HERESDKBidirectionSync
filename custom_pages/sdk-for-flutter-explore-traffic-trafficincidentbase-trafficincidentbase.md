---
title: "TrafficIncidentBase constructor - TrafficIncidentBase - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficincidentbase-trafficincidentbase"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficIncidentBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TrafficIncidentBase</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TrafficIncidentBase</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-impactGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentimpact">TrafficIncidentImpact</a></span> <span class="parameter-name">impactGetLambda</span>(), </span>
2.  <span id="sdk-for-flutter-explore-param-typeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType</a></span> <span class="parameter-name">typeGetLambda</span>(), </span>
3.  <span id="sdk-for-flutter-explore-param-descriptionGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-localizedtext-class">LocalizedText</a></span> <span class="parameter-name">descriptionGetLambda</span>(), </span>
4.  <span id="sdk-for-flutter-explore-param-startTimeGetLambda" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">startTimeGetLambda</span>(), </span>
5.  <span id="sdk-for-flutter-explore-param-endTimeGetLambda" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">endTimeGetLambda</span>(), </span>

)

</div>

<div class="section desc markdown">

TrafficIncident provides details about a traffic incident.

</div>

## Implementation

``` dart
factory TrafficIncidentBase(
  TrafficIncidentImpact Function() impactGetLambda,
  TrafficIncidentType Function() typeGetLambda,
  LocalizedText Function() descriptionGetLambda,
  DateTime? Function() startTimeGetLambda,
  DateTime? Function() endTimeGetLambda
) => TrafficIncidentBase$Lambdas(
  impactGetLambda,
  typeGetLambda,
  descriptionGetLambda,
  startTimeGetLambda,
  endTimeGetLambda
);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

