---
title: "weightPerAxleInKilograms property - TruckSpecifications class - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-truckspecifications-weightperaxleinkilograms"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/TruckSpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">weightPerAxleInKilograms</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">weightPerAxleInKilograms</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

</div>

## Implementation

``` dart
int? weightPerAxleInKilograms;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

