---
title: "elements property - EVChargingTariff class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingtariff-elements"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVChargingTariff-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">elements</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-class">EVChargingTariffElement</a></span>\></span> <span class="name">elements</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Elements composing the tariff. Each element can have multiple components. When multiple elements are present, the associated condition helps the client to select the element that matches the charging session. If no condition matches, the element without any condition applies.

Please note that tariff elements or conditions requiring access to vehicle APIs are not present in this API. The provided elements can only be used to derive a price estimate, which in most cases is reasonably close to the final price.

</div>

## Implementation

``` dart
List<EVChargingTariffElement> elements;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

