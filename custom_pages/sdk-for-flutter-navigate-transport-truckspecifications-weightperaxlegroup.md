---
title: "weightPerAxleGroup property - TruckSpecifications class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-truckspecifications-weightperaxlegroup"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/TruckSpecifications-class-sidebar.html" data-below-sidebar="">

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

Allows specification of axle weights in a more fine-grained way than `weight_per_axle_in_kilograms`. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

</div>

## Implementation

``` dart
WeightPerAxleGroup? weightPerAxleGroup;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

