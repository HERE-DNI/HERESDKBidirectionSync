---
title: "tariffs property - EVChargingLocation class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evcharginglocation-tariffs"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVChargingLocation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">tariffs</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evchargingtariff-class">EVChargingTariff</a></span>\></span></span> <span class="name">tariffs</span>

</div>

<div class="section desc markdown">

List of tariffs or price plans for the connectors of the charging station. Tariffs are typically connector-type specific. Hence, they are always linked with connectors and/or connector groups, by indexes to this list.

This property is set only when data is available and when `EVSearchOptions.additional_features` include either `EVChargingLocationFeature.EVSES` or `EVChargingLocationFeature.CONNECTOR_GROUPS`.

By default, the list includes tariffs for ad-hoc charging, per connector type, for EVSEs that accept payment without registering. Gets the list of tariffs or price plans for the connectors of the charging station.

</div>

## Implementation

``` dart
List<EVChargingTariff> get tariffs;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

