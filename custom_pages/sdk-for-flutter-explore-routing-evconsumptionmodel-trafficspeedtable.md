---
title: "trafficSpeedTable property - EVConsumptionModel class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/EVConsumptionModel-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trafficSpeedTable</span> property

</div>

<div class="section multi-line-signature">

Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter">double</span>\></span> <span class="name">trafficSpeedTable</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e. when the vehicle is expected to often change the travel speed. It defines a function curve specifying consumption rate at a given speed under traffic conditions on a flat stretch of road. Map keys represent traffic speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. If only one key/value pair is set, the consumption value is used for all possible traffic speed keys. If <a href="sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable">EVConsumptionModel.trafficSpeedTable</a> is empty then only <a href="sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable">EVConsumptionModel.freeFlowSpeedTable</a> is used for calculating speed-related energy consumption.

</div>

## Implementation

``` dart
Map<int, double> trafficSpeedTable;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

