---
title: "frontalAreaInSquareMeters property - PhysicalConsumptionModel class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-physicalconsumptionmodel-frontalareainsquaremeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/PhysicalConsumptionModel-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">frontalAreaInSquareMeters</span> property

</div>

<div class="section multi-line-signature">

double <span class="name">frontalAreaInSquareMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters. Physical consumption model is using this value in combination with `airDragCoefficient` to calculate the consumption caused by air resistance. As fallback <a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a> are used.

This parameter is used to provide a more accurate consumption prediction for electric vehicles.

In the range from 0.5 to 50

</div>

## Implementation

``` dart
double frontalAreaInSquareMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

