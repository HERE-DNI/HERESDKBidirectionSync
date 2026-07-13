---
title: "freeFlowSpeedTable property - EVConsumptionModel class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-evconsumptionmodel-freeflowspeedtable"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- freeFlowSpeedTable.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/EVConsumptionModel-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">freeFlowSpeedTable</span> property

</div>

<div class="section multi-line-signature">

Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter">double</span>\></span> <span class="name">freeFlowSpeedTable</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Free flow speed table describes energy consumption when traveling at constant speed. It defines a function curve specifying consumption rate at a given free flow speed on a flat stretch of road. Map keys represent speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. At minimum, one key/value pair must be set. In this case the consumption value is used for all possible speed keys.

</div>

## Implementation

``` dart
Map<int, double> freeFlowSpeedTable;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
