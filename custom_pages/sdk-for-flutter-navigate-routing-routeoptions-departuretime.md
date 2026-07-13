---
title: "departureTime property - RouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routeoptions-departuretime"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- departureTime.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">departureTime</span> property

</div>

<div class="section multi-line-signature">

DateTime? <span class="name">departureTime</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode">RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

**Note**:

- Both departure time and <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a> cannot be set at the same time.
- This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

</div>

## Implementation

``` dart
DateTime? departureTime;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
