---
title: "ChargingStation constructor - ChargingStation - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-chargingstation-chargingstation"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ChargingStation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ChargingStation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ChargingStation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-id" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">id</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-name" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">name</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-connectorAttributes" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a>?</span> <span class="parameter-name">connectorAttributes</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `id` Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.
- `name` Human readable name of this charging station. It can be null when there is no name associated with the station.
- `connectorAttributes` Details of the connector suggested to be used.

</div>

## Implementation

``` dart
ChargingStation(this.id, this.name, this.connectorAttributes)
    : brand = null, chargePointOperator = null, matchingEMobilityServiceProviders = [];
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

