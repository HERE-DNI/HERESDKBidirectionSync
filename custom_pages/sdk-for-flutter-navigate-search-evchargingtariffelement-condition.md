---
title: "condition property - EVChargingTariffElement class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evchargingtariffelement-condition"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- condition.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVChargingTariffElement-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">condition</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-class">EVChargingTariffElementCondition</a>? <span class="name">condition</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Condition that the charging session needs to meet to apply the tariff element. An element without any condition is typically present for charging sessions that do not meet any of the conditions.

For example, a tariff element with a lower price can be valid only during nighttime, while a generic tariff element without conditions applies for daytime charging sessions. The conditions are listed in priority order. I.e., when <a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-date">EVChargingTariffElementCondition.date</a> is present, it should be matched first, followed by <a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-days">EVChargingTariffElementCondition.days</a> and so on.

</div>

## Implementation

``` dart
EVChargingTariffElementCondition? condition;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
