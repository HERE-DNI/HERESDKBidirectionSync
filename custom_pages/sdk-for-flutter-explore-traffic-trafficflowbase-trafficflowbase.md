---
title: "TrafficFlowBase constructor - TrafficFlowBase - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficflowbase-trafficflowbase"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficFlowBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TrafficFlowBase</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TrafficFlowBase</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-freeFlowSpeedInMetersPerSecondGetLambda" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">freeFlowSpeedInMetersPerSecondGetLambda</span>(), </span>
2.  <span id="sdk-for-flutter-explore-param-jamFactorGetLambda" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">jamFactorGetLambda</span>()</span>

)

</div>

<div class="section desc markdown">

This interface provides details about a traffic flow.\
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
factory TrafficFlowBase(
  double Function() freeFlowSpeedInMetersPerSecondGetLambda,
  double Function() jamFactorGetLambda
) => TrafficFlowBase$Lambdas(
  freeFlowSpeedInMetersPerSecondGetLambda,
  jamFactorGetLambda
);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

