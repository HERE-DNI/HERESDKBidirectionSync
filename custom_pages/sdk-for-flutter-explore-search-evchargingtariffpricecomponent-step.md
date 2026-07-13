---
title: "step property - EVChargingTariffPriceComponent class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingtariffpricecomponent-step"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- step.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVChargingTariffPriceComponent-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">step</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">step</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Dimension quantity used as a unit of billing. Present for all other dimensions except <a href="sdk-for-flutter-explore-search-evchargingtariffdimension">EVChargingTariffDimension.flat</a>. The customer is charged price for each full or partial step of the dimension consumed. For <a href="sdk-for-flutter-explore-search-evchargingtariffdimension">EVChargingTariffDimension.energy</a>, the step size unit is 1 Wh, for <a href="sdk-for-flutter-explore-search-evchargingtariffdimension">EVChargingTariffDimension.time</a> and <a href="sdk-for-flutter-explore-search-evchargingtariffdimension">EVChargingTariffDimension.parkingTime</a> it is 1 second. For example, if step is 300 for time, then time is billed in 5 minute steps, rounded upwards. Similarly, if step is 100 for energy, then energy is billed in 100 Wh = 0.1 kWh steps.

</div>

## Implementation

``` dart
double? step;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
