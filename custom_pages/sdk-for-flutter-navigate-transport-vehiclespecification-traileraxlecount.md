---
title: "trailerAxleCount property - VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trailerAxleCount</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">trailerAxleCount</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a>, hence <a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a> must be less than <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> and greater than or equal to 1. <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-trailercount">VehicleSpecification.trailerCount</a> are required to specify <a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a>. By default, it is not set.

**Note:**: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

</div>

## Implementation

``` dart
int? trailerAxleCount;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

