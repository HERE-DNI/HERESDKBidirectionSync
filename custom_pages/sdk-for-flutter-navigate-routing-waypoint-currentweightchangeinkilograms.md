---
title: "currentWeightChangeInKilograms property - Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-waypoint-currentweightchangeinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- currentWeightChangeInKilograms.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">currentWeightChangeInKilograms</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">currentWeightChangeInKilograms</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Changes the value of `vehicle[currentWeight]` by this value. Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route. Changes to the configuration of the vehicle, such as adding a trailer, aren't supported. Relative value in kilograms. Available range: from -40000 to 40000 (inclusive). **Note:**

- A route request with this parameter requires to set <a href="sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>.
- This feature is supported in transport modes of <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a>, or <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
int? currentWeightChangeInKilograms;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
