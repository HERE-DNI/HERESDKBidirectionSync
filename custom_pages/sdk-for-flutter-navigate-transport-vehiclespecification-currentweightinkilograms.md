---
title: "currentWeightInKilograms property - VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- currentWeightInKilograms.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">currentWeightInKilograms</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">currentWeightInKilograms</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>. By default, it is not set.

**Notes:**

- Supported in <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.bus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.privateBus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a> (Beta), <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.
- Maximum weight for a car or taxi *without* a trailer is 5000 kg.
- Maximum weight for a car or taxi *with* a trailer is 8500 kg.
- A route request with <a href="sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a> above <a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a> may result in non-compliant or invalid routes.

</div>

## Implementation

``` dart
int? currentWeightInKilograms;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
