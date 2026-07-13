---
title: "grossWeightInKilograms property - VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">grossWeightInKilograms</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">grossWeightInKilograms</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a>. By default, it is not set.

**Notes:**

- Supported in <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.bus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.privateBus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a> (Beta), <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.
- Maximum weight for a car or taxi *without* a trailer is 4250 kg.
- Maximum weight for a car or taxi *with* a trailer is 7550 kg.

</div>

## Implementation

``` dart
int? grossWeightInKilograms;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

