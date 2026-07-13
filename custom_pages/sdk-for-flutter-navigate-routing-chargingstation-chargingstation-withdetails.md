---
title: "ChargingStation.withDetails constructor - ChargingStation - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-chargingstation-chargingstation-withdetails"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStation.withDetails.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ChargingStation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ChargingStation.withDetails</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ChargingStation.withDetails</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withDetails-param-id" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">id</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withDetails-param-name" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">name</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withDetails-param-connectorAttributes" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a>?</span> <span class="parameter-name">connectorAttributes</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withDetails-param-brand" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a>?</span> <span class="parameter-name">brand</span>, </span>
5.  <span id="sdk-for-flutter-navigate-withDetails-param-chargePointOperator" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a>?</span> <span class="parameter-name">chargePointOperator</span>, </span>
6.  <span id="sdk-for-flutter-navigate-withDetails-param-matchingEMobilityServiceProviders" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a></span>\></span></span> <span class="parameter-name">matchingEMobilityServiceProviders</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `id` Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.
- `name` Human readable name of this charging station. It can be null when there is no name associated with the station.
- `connectorAttributes` Details of the connector suggested to be used.
- `brand` Charging station brand. <a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> reflect to charging station brand name. <a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> reflect to charging station brand unique ID.
- `chargePointOperator` Charging station charge-point-operator. <a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> reflect to charge-point-operator name. <a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> reflect to charge-point-operator ID.
- `matchingEMobilityServiceProviders` List of matched E-Mobility Service Providers. Populated only when <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a> was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a>. <a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> in each list item reflect to E-Mobility Service Provider name. <a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> in each list item reflect to E-Mobility Service Provider id.

</div>

## Implementation

``` dart
ChargingStation.withDetails(this.id, this.name, this.connectorAttributes, this.brand, this.chargePointOperator, this.matchingEMobilityServiceProviders);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
