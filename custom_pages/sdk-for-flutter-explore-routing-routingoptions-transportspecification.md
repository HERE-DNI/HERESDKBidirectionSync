---
title: "transportSpecification property - RoutingOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routingoptions-transportspecification"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">transportSpecification</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-transport-transportspecification-class">TransportSpecification</a> <span class="name">transportSpecification</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen. **Notes:**

- The transport mode <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.publicTransit</a> is not supported.
- By default all vehicle specifications from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> are set to `null` and the <a href="sdk-for-flutter-explore-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> is set to <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.car</a>.
- A route can be calculated with only the <a href="sdk-for-flutter-explore-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> set.
- It is highly recommended to define the <a href="sdk-for-flutter-explore-transport-truckcategory">TruckCategory</a> that is being used in <a href="sdk-for-flutter-explore-transport-vehiclespecification-truckcategory">VehicleSpecification.truckCategory</a> from <a href="sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a>, if the <a href="sdk-for-flutter-explore-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> is set to <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.truck</a>.
- The <a href="sdk-for-flutter-explore-transport-vehiclespecification-occupancy">VehicleSpecification.occupancy</a> from <a href="sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> won't have effect if HOV and/or HOT lane usage is not allowed using <a href="sdk-for-flutter-explore-routing-evtruckoptions-allowoptions">EVTruckOptions.allowOptions</a>.
- The <a href="sdk-for-flutter-explore-transport-pedestrianspecification-walkingspeedinmeterspersecond">PedestrianSpecification.walkingSpeedInMetersPerSecond</a> from <a href="sdk-for-flutter-explore-transport-transportspecification-pedestrianspecification">TransportSpecification.pedestrianSpecification</a> if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking along the route. The provided value must be in the range \[0.5, 2.0\]. When the value is outside this range, an invalid parameter error is raised. Refer to <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a> for details. The default speed is 1 meter per second.

</div>

## Implementation

``` dart
TransportSpecification transportSpecification;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

