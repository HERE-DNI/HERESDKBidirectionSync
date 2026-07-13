---
title: "weightPerAxleGroup property - VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">weightPerAxleGroup</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-transport-weightperaxlegroup-class">WeightPerAxleGroup</a>? <span class="name">weightPerAxleGroup</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms">VehicleSpecification.weightPerAxleInKilograms</a>. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set.

**Notes:**

- <a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms">VehicleSpecification.weightPerAxleInKilograms</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup">VehicleSpecification.weightPerAxleGroup</a> are incompatible. When available for your edition, if both attributes are set, during online `RoutingEngine` an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline `RoutingEngine` is in place, both parameters are evaluated and the maximum value between them will be used.
- Supported in <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.bus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.privateBus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a> (Beta), <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.

</div>

## Implementation

``` dart
WeightPerAxleGroup? weightPerAxleGroup;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

