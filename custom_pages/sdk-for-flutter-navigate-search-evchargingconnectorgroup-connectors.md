---
title: "connectors property - EVChargingConnectorGroup class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evchargingconnectorgroup-connectors"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVChargingConnectorGroup-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">connectors</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingconnectorreference-class">EVChargingConnectorReference</a></span>\></span> <span class="name">connectors</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Array of EVSE + connector(s) pairs that belong to the group. Provides access to EVSE statuses and more detailed connector characteristics. Available only if `EVChargingLocationFeature.EVSES` is included in `EVSearchOptions.additional_features`, otherwise empty.

</div>

## Implementation

``` dart
List<EVChargingConnectorReference> connectors;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

