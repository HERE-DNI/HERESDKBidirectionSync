---
title: "evChargingPool property - Details class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-details-evchargingpool"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/Details-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">evChargingPool</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-search-evchargingpool-class">EVChargingPool</a>? <span class="name">evChargingPool</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a> is enabled in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

For online search, this feature is only available if it is explicitly enabled. To do that, call

    SearchEngine.set_custom_option()

with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call

    SearchEngine.set_custom_option()

for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.
</p>

</div>

## Implementation

``` dart
EVChargingPool? evChargingPool;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

